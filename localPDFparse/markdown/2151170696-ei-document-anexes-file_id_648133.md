---
title: Sin título
author: Usuario
date: D:20210316151455-03'00'
language: es
type: report
pages: 20
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
  - 4 CARACTERISTICAS Y ANÁLISIS HIDROLÓGICO QUEBRADA
  - 5 CONCLUSIONES
-->

|Rev.|Fecha|Realizado|Revisado|Aprobado|Descripción|
|---|---|---|---|---|---|
|A|16-03-21|RRR, CAD|AGL|AGL|Para revisión|
|||||||
|<br>||||||

|Rev.|Fecha|Revisión/aprobación cliente|Descripción|
|---|---|---|---|
|||||
|<br>||<br>||

|PROYECTO:|PARQUE FOTOVOLTAICO SANTA BARBARA|
|---|---|
|**MATERIA:**|**CARACTERIZACIÓN HIDROLÓGICA**|
|**CLIENTE:**|**SOLEK CHILE**|
|**CODIGO:**|**013-2102.032 D**|

página ii

# RESUMEN

El objetivo del presente informe es definir las características hidrológicas y áreas de
inundación de la red hídrica asociada al proyecto Parque Fotovoltaico Santa Barbara, que se
proyecta al este de la comuna de Ninhue, región de Ñuble.

Para lo anterior, se realizó un levantamiento de información en terreno, se hizo una revisión

de antecedentes, se realizaron labores de topografía y se definieron las principales
características hidrológicas del área. Con ello se identificó la red hídrica de la zona, asociada
solo a quebradas naturales intermitentes, para las cuales se generó un modelo hidráulico para
definir el área de inundación para un período de retorno de 100 años.

Para estas quebradas se estimó un caudal total, asociado a un periodo de retorno de 100 años,
de 8.85 m [3] /s, y se determinó que existen desbordes localizados, de la cual, en un sector, la
crecida ingresa al área del proyecto, pero no se intercepta con ninguna obra, por lo que se
descarta que existe interacción entre la crecida de la quebrada y las obras del parque

fotovoltaico.

Considerando lo anterior, la Dirección General de Aguas a través de la Resolución DGA
N°135/20 y el Memo DGA N°118/20, ha definido que los cauces naturales que deberán
someterse al permiso de modificación de cauce deberán identificarse según las bases de datos
oficiales asociadas a la cartografía IGM, documentación técnica generada por la DGA, los
planes maestros de aguas lluvias y los demás antecedentes oficiales de gestión territorial,
evaluados para un periodo de retorno de 100 años, por lo que, dado que las obras del proyecto
se encuentran fuera del área de inundación de la quebrada no aplicaría el permiso de
modificación de cauce, ni los permisos ambientales sectoriales 156 y 157 de competencia de

la DGA.

página iii

**ÍNDICE**

RESUMEN ............................................................................................................................. ii

1 INTRODUCCIÓN .......................................................................................................... 4

2 TOPOGRAFÍA................................................................................................................ 5

3 ZONA DE ESTUDIO Y RED HÍDRICA ....................................................................... 6

4 CARACTERISTICAS Y ANÁLISIS HIDROLÓGICO QUEBRADA ......................... 8

4.1 Hidrología ................................................................................................................ 8

4.1.1 Análisis de Precipitaciones ............................................................................... 8

4.1.2 Análisis de Caudales ......................................................................................... 9

4.2 Modelación Hidráulica .......................................................................................... 14

4.2.1 Caudales ......................................................................................................... 14

4.2.2 Perfiles Transversales ..................................................................................... 14

4.2.3 Rugosidad del Lecho ...................................................................................... 15

4.2.4 Condiciones de Borde ..................................................................................... 17

4.2.5 Resultados ....................................................................................................... 17

5 CONCLUSIONES ........................................................................................................ 20



# 1 INTRODUCCIÓN

El presente informe se desarrolla en el contexto del levantamiento de información hidrológica
del área donde se emplazará el proyecto “Parque Fotovoltaico Santa Bárbara”, ubicado en la
cuenca del río Itata, subcuenca del río Lonquén, al este de la comuna de Ninhue, provincia
de Itata, región de Ñuble. La Figura 1-1 presenta la ubicación del proyecto.

El proyecto Parque Fotovoltaico Santa Barbara es un proyecto energético que se emplazará
en un predio donde actualmente se realizan labores de postero de animales y donde existe
una red de cauces naturales que forman parte de la red hídrica del río Lonquen, por lo que se
hace necesario efectuar un análisis hidráulico para caracterizas estos cauces y, en caso de
requerirse, determinar los alcances de sus crecidas.

Figura 1-1. Ubicación del proyecto.

El objetivo del presente informe consiste en determinar las principales características
hidrológicas y definir las zonas de inundación de la red hídrica del área donde se emplaza el
proyecto. Para lo anterior, se realizó un levantamiento de información en terreno, se hizo una
revisión de antecedentes, se realizaron labores de topografía y se definieron las principales
características hidrológicas del área. Con ello, se generó un modelo hidráulico para definir el
área de inundación para el cauce natural que circula por el área del proyecto, para un periodo

de retorno de 100 años.



# 2 TOPOGRAFÍA

La campaña de levantamiento topográfico del área de interés fue realizada el día 5 de marzo
de 2021 mediante GPS geodésico en modo RTK, utilizando un GPS fijo en tierra, y otro en
estado móvil para la captura de los datos de terreno en los cauces de interés (Figura 2-1).

Figura 2-1. Levantamiento Topográfico mediante GPS RTK.

Con el fin de complementar la información de terreno obtenida del levantamiento topográfico
con GPS geodésico, se realizó un levantamiento aerofotogramétrico con dron DJI Phantom
4 RTK (Figura 2-2). Este dron cuenta con una cámara fotográfica de 20 MP y un estabilizador
Gimbal con rango de vibración angular de + 0.02°. El levantamiento abarca toda el área de
estudio, y es ligado con algunos puntos de control en tierra, los que son identificados,
individualizados y georreferenciados durante el levantamiento topográfico mediante GPS.
Con ello se generó, a través de un proceso fotogramétrico, un ortomosaico georreferenciado,

mediante el software Pix4D.

Figura 2-2. Dron Phantom 4 RTK.



# 3 ZONA DE ESTUDIO Y RED HÍDRICA

La zona de estudio se ubica referencialmente en las coordenadas UTM (m) N: 5.965.334 y

E: 734.910, datum WGS84, Huso 18 sur, al sureste de la localidad de Ninhue, comuna de

Ninhue (Figura 3-1).

El proyecto se encuentra específicamente en la subsubcuenca Río Lonquen hasta Estero El
Tiuque, código BNA:08142. El estero Tiuque que se encuentra a 1.5 km aguas abajo del área
del proyecto; mientras que, el cuerpo de agua principal, el río Lonquen, se encuentra a 490
metros del polígono del proyecto.

Figura 3-1. Área de estudio del proyecto y red hídrica.



Considerando lo anterior, la red hídrica que eventualmente interactúa con las obras del
proyecto, son una serie de quebradas sin nombre, intermitentes, que presentan dirección
norponiente a surporiente, y que al acercarse al proyecto cambian de dirección hacia el
nororiente para descargar finalmente al río Lonquen (Figura 3-1).

Considerando lo anterior, la Dirección General de Aguas a través de la Resolución DGA
N°135/20 y el Memo DGA N°118/20, ha definido qué obras serán sometidas a permisos de
modificación de cauce en virtud del artículo 41 y 171 del Código de Aguas, y, por lo tanto,
sometidos al permiso ambiental sectorial 156 o 157 de competencia de dicho servicio. De los
citados documentos se desprende que los cauces naturales que deberán someterse al permiso
de modificación de cauce deberán identificarse según la base de datos oficiales asociada a la
cartografía IGM, documentación técnica generada por la DGA, los planes maestros de aguas
lluvias y los demás antecedentes oficiales de gestión territorial, evaluados para un periodo de

retorno de 100 años.

Por lo tanto, si las obras del parque fotovoltaico requiriesen de alguna modificación de los
cauces naturales que se identificaron en el área del proyecto, se deberá evaluar con los
criterios antes descritos para ver la aplicabilidad del permiso de modificación de cauce, así
como la respectiva presentación de un PAS 156 o PAS 157.



# 4 CARACTERISTICAS Y ANÁLISIS HIDROLÓGICO QUEBRADA

A continuación, se describe el desarrollo de la correspondiente caracterización y análisis
hidrológico de la quebrada sin nombre con el fin de describir sus principales características
y los alcances de una crecida de la quebrada para un periodo de retorno de 100 años.

## 4.1 Hidrología

### 4.1.1 Análisis de Precipitaciones

Para efectuar el análisis de precipitaciones, se utilizó información registrada en la estación
pluviométrica San Agustín de Puñual, la que se emplaza aproximadamente a 8 km al norte
de la zona de estudio, por lo que se considera representativa del área del proyecto (Tabla
4-1).

Tabla 4-1. Estación San Agustín de Puñual.

|Estación|Código BNA|Periodo de registro|
|---|---|---|
|~~San Agustín de Puñual~~<br>|~~08118004-0~~|~~1993-2020~~|

Para el análisis de precipitaciones se efectuó un análisis de Máximos Anuales, en donde se
considera la precipitación máxima diaria registrada en cada año. Adicionalmente, se calculó
la precipitación máxima horaria, como P 24 = 1.1 P D . En la Tabla 4-2 se presentan los valores
de precipitación.

Tabla 4-2. Precipitaciones Máximas Anuales en 24 h.

|Año|P (mm)<br>D|P (mm)<br>24|Año|P (mm)<br>D|P (mm)<br>24|
|---|---|---|---|---|---|
|~~1993~~<br>|~~72~~<br>|~~79.2~~<br>|~~2007~~<br>|~~52~~<br>|~~57.2~~<br>|
|~~1994~~<br>|~~44~~<br>|~~48.4~~<br>|~~2008~~<br>|~~109~~<br>|~~119.9~~<br>|
|~~1995~~<br>|~~76~~<br>|~~83.6~~<br>|~~2009~~<br>|~~164~~<br>|~~180.4~~<br>|
|~~1996~~<br>|~~66.6~~<br>|~~73.26~~<br>|~~2010~~<br>|~~58~~<br>|~~63.8~~<br>|
|~~1997~~<br>|~~95.8~~<br>|~~105.38~~<br>|~~2011~~<br>|~~47.5~~<br>|~~52.25~~<br>|
|~~1998~~<br>|~~30.5~~<br>|~~33.55~~<br>|~~2012~~<br>|~~72.7~~<br>|~~79.97~~<br>|
|~~1999~~<br>|~~63~~<br>|~~69.3~~<br>|~~2013~~<br>|~~52~~<br>|~~57.2~~<br>|
|~~2000~~<br>|~~59~~<br>|~~64.9~~<br>|~~2014~~<br>|~~55~~<br>|~~60.5~~<br>|
|~~2001~~<br>|~~92.4~~<br>|~~101.64~~<br>|~~2015~~<br>|~~102~~<br>|~~112.2~~<br>|
|~~2002~~<br>|~~106~~<br>|~~116.6~~<br>|~~2016~~<br>|~~58.5~~<br>|~~64.35~~<br>|
|~~2003~~<br>|~~69~~<br>|~~75.9~~<br>|~~2017~~<br>|~~57.7~~<br>|~~63.47~~<br>|
|~~2004~~<br>|~~46~~<br>|~~50.6~~<br>|~~2018~~<br>|~~39.5~~<br>|~~43.45~~<br>|
|~~2005~~<br>|~~106~~<br>|~~116.6~~<br>|~~2019~~<br>|~~108~~<br>|~~118.8~~<br>|
|~~2006~~<br>|~~76.4~~|~~84.04~~|~~2020~~|~~56.5~~|~~62.15~~|



A partir de los datos de precipitación, se efectuó un análisis estadístico para conocer las
precipitaciones en 24 h asociadas a distintos periodos de retorno. En la Tabla 4-3 se presentan
los resultados obtenidos. A partir de estos datos se adopta los valores asociados a la
distribución Pearson 5, debido a la mejor bondad de ajuste y buen ajuste gráfico.

Tabla 4-3. Resultados del Análisis Estadístico de Precipitaciones.

|T (años)|P (mm)<br>24|Col3|Col4|Col5|Col6|Col7|Valor-p|Col9|
|---|---|---|---|---|---|---|---|---|
|T (años)<br>|~~2 ~~<br>|~~5 ~~<br>|~~10~~<br>|~~25~~<br>|~~50~~<br>|~~100~~<br>|~~K - S~~<br>|~~Chi 2~~<br>|
|~~**Pearson 5**~~<br>|~~**73.0**~~<br>|~~**100.8**~~<br>|~~**121.0**~~<br>|~~**148.7**~~<br>|~~**171.1**~~<br>|~~**195.0**~~<br>|~~0.946~~<br>|~~0.332~~<br>|
|~~Log-Pearson 3~~<br>|~~73.6~~<br>|~~101.7~~<br>|~~121.3~~<br>|~~147.4~~<br>|~~167.6~~<br>|~~188.7~~<br>|~~0.922~~<br>|~~0.691~~<br>|
|~~Lognormal (3P)~~<br>|~~73.6~~<br>|~~101.4~~<br>|~~120.6~~<br>|~~145.6~~<br>|~~164.7~~<br>|~~184.3~~<br>|~~0.916~~<br>|~~0.698~~<br>|
|~~Gamma (3P)~~<br>|~~74.2~~<br>|~~102.6~~<br>|~~121.1~~<br>|~~143.7~~<br>|~~159.9~~<br>|~~175.6~~<br>|~~0.913~~<br>|~~0.706~~<br>|
|~~Pearson 5 (3P)~~<br>|~~73.5~~|~~100.9~~|~~120.2~~|~~146.2~~|~~166.8~~|~~188.5~~|~~0.911~~|~~0.694~~|

### 4.1.2 Análisis de Caudales

A partir de los resultados del análisis de precipitaciones, se calcula la serie de caudales para
las quebradas del área de estudio. El cálculo de caudales se efectuó con la Fórmula Racional,
de acuerdo con el Manual de Carreteras Volumen 3 (MOP, 2020).

La delimitación de la cuenca hidrográfica se realizó mediante el software ArcGIS, a partir de
un Modelo de Elevación Digital ALOS PALSAR, de 30 m de resolución. En la Figura 4-1
se presenta la cuenca hidrográfica de los cauces en estudio, y en la Tabla 4-4 se presentan las

características morfométricas de las cuencas.

Cuenca

Quebrada 2

Cuenca

Quebrada1

Figura 4-1. Cuenca quebrada 1 y quebrada 2.



Tabla 4-4. Características Morfométricas de las Cuencas.

|Característica|Símbolo (unidad)|Cuenca "Quebrada 1"|Cuenca "Quebrada 2"|
|---|---|---|---|
|Característica<br>|Símbolo (unidad)<br>|~~Valor~~<br>|~~Valor~~<br>|
|~~Área~~<br>|~~A (km2) ~~<br>|~~0.24~~<br>|~~2.19~~<br>|
|~~Desnivel~~<br>|~~H (m)~~|~~21~~|~~64~~|
|~~Desnivel entre cota~~<br>media y salida<br>|Hm (m)<br>|6 <br>|22<br>|
|~~Pendiente Media~~<br>|~~S ~~<br>|~~0.0291~~<br>|~~0.0714~~<br>|
|~~Longitud de cauce~~<br>|~~L (km)~~|~~0.70~~|~~1.94~~|

De acuerdo con la Fórmula Racional, el caudal asociado a distintos periodos de retorno está
dado por la ecuación:

QQ [TT] = [CC ii] [TT] [ AA]
3.6

Donde:
_Q_ : Caudal para un período de retorno T (m [3] /s).

_C_ : Coeficiente de escorrentía.
_i_ _[T]_ : intensidad de precipitación para un periodo de retorno T (mm/h).
_A_ : : Área de la cuenca (km [2] ).

El empleo de la Fórmula Racional requiere del cálculo del coeficiente de escorrentía, de la
intensidad de precipitación y el área de la cuenca, los cuales se presentan a continuación.

Para el cálculo del coeficiente de escorrentía de la cuenca se utilizan los términos C 1, C 2, C 3

y C 4 recomendados en el Manual de Carreteras (Tabla 3.702.503.B). En la Tabla 4-5 y Tabla
4-6 se indican los valores adoptados, junto con la descripción correspondiente.

El valor del coeficiente de escorrentía para períodos de retorno bajos es C = 0.35, en ambas
cuencas. Para períodos de retorno mayores se amplifica, como se indica en la Tabla 4-7.



Tabla 4-5. Factores de Coeficiente de Escorrentía, Cuenca "Cauce 1"

|Factor|Col2|Valor|Descripción|
|---|---|---|---|
|C1|Relieve|0.11|~~Relativamente plano, con pendientes menores~~<br>al 5%<br>|
|C2|Infiltración|0.08|~~Normal, terrenos bien drenados, textura~~<br>mediana, limos arenosos, suelos arenosos.<br>|
|C3|Cobertura Vegetal|0.07|~~Regular a buena, 50% del área con praderas o~~<br>bosques.<br>|
|C4|Almacenamiento Superficial|0.09|~~Baja, sistema de cauces superficiales pequeños~~<br>bien definidos, sin zonas húmedas.|
|**C **<br>||**0.35**|**Coeficiente de escorrentía**|

Tabla 4-6. Factores de Coeficiente de Escorrentía, Cuenca "Cauce 2"

|Factor|Col2|Valor|Descripción|
|---|---|---|---|
|C1|Relieve|0.15|Normal, con cerros y pendientes entre 5 y 10%<br>|
|C2|Infiltración|0.08|~~Normal, terrenos bien drenados, textura~~<br>mediana, limos arenosos, suelos arenosos.<br>|
|C3|Cobertura Vegetal|0.05|~~Buena a Excelente, 90% del área con praderas,~~<br>bosques o cobertura equivalente.<br>|
|C4|Almacenamiento Superficial|0.07|~~Normal, posibilidad de almacenamiento buena,~~<br>zonas húmedas.|
|**C **<br>||**0.35**|**Coeficiente de escorrentía**|

Tabla 4-7. Coeficiente de Escorrentía, Cuencas "Cauce 1" y "Cauce 2".

|T|Factor|C|
|---|---|---|
|~~2 ~~<br>|~~1.0~~<br>|~~0.28~~<br>|
|~~5 ~~<br>|~~1.0~~<br>|~~0.28~~<br>|
|~~10~~<br>|~~1.0~~<br>|~~0.28~~<br>|
|~~25~~<br>|~~1.1~~<br>|~~0.308~~<br>|
|~~50~~<br>|~~1.2~~<br>|~~0.336~~<br>|
|~~100~~<br>|~~1.25~~<br>|~~0.35~~<br>|
|~~150~~|~~1.25~~|~~0.35~~|

Por su parte, los valores de precipitación y de intensidad, asociados a distintos periodos de
retorno, están determinados por la ecuación:

PP ttTT = C × PP 24TT

TT
ii ttTT = [PP] tt [24] cc



Donde:

TT
PP tt : precipitación de duración tt horas y periodo de retorno TT años (mm).
C **C** : coeficiente de duración para el periodo de retorno de la cuenca.
TT
PP 24 : precipitación de duración 24 horas y periodo de retorno TT años (mm).
ii ttTT : intensidad de precipitación para una duración tt horas y periodo de retorno TT años
(mm/h).
tt cc : tiempo de concentración de la cuenca (h).

La intensidad de la precipitación está relacionada con el tiempo de concentración, _t_ _c_, de la

cuenca, el cual se calcula en base a las ecuaciones:

Normas Españolas

tt cc = 0.3 SS [LL] [0.76][0.19]

**C**

**C**

California

Giandotti

**C**

**C**

tt cc = 0.95 ቆ [LL] HH [3]

**C**

**C**

0.385

**C**

**C**

[LL] HH [3] ~~[ቇ]~~

**C**

**C**

tt cc = [4√AA+ 1.5 LL]

0.8 √H

**C**

**C**

Al evaluar estas ecuaciones con las variables correspondientes se obtienen los tiempos de
concentración indicados en la Tabla 4-8. Para ambas cuencas, se adopta el valor obtenido
con las Normas Españolas, por presentar un valor intermedio entre los resultados obtenidos.

Tabla 4-8. Valores obtenidos de Tiempo de Concentración.

|Método|Tiempo de Concentración (h)|Col3|
|---|---|---|
|Método<br>|~~Cuenca "Quebrada 1"~~<br>|~~Cuenca "Quebrada 2"~~<br>|
|~~**Normas Españolas**~~<br>|~~**0.45**~~<br>|~~**0.82**~~<br>|
|~~California~~<br>|~~0.19~~<br>|~~0.41~~<br>|
|~~Giandotti~~|~~1.54~~|~~2.35~~|

Para estimar la precipitación para la tormenta de diseño se utilizó la ecuación de Bell, que es
válida para períodos de retorno de 2 a 100 años y duraciones de 5 a 120 minutos. Esta
ecuación se basa en la precipitación de una tormenta de duración 1 h para un período de
retorno _T_ años (PP 1TT ), que se obtiene con las ecuaciones:

PP ttTT = (0.54 tt 0.25 −0.50) × PP 1TT
PP 1TT = PP 24TT × C **C**



Donde:
PP ttTT : Precipitación de duración _t_ y período de retorno _T_ (mm).
PP 1TT : Precipitación de duración 1 h y período de retorno _T_ (mm).
PP 24TT : Precipitación de duración 24 h y período de retorno _T_ (mm).
tt : tiempo (min).
CCDD : Coeficiente de duración (0.13 para la zona de estudio).

En la Tabla 4-9 se indican los valores obtenidos de precipitación y de intensidad de
precipitación para cada cauce, y en la Tabla 4-10 se presentan los caudales obtenidos para

cada cauce.

|Tabla 4-9|9. Precipitaciones e intensidad de prec Quebrada 1|Col3|Col4|cipitación, Quebrada 1 y Quebrada 2. Quebrada 2|Col6|Col7|
|---|---|---|---|---|---|---|
|T (años)<br>|~~Quebrada 1~~<br>|~~Quebrada 1~~<br>|~~Quebrada 1~~<br>|~~Quebrada 2~~<br>|~~Quebrada 2~~<br>|~~Quebrada 2~~<br>|
|T (años)<br>|P24<br>T (m<br>) <br>|Pt<br>T (m<br>) <br>|it<br>T ቀ~~m~~<br>h~~ቁ~~ <br>|P24<br>T (m<br>) <br>|Pt<br>T (m<br>) <br>|it<br>T ቀ~~m~~<br>h~~ቁ~~ <br>|
|~~2 ~~<br>|~~73.0~~<br>|~~6.9~~<br>|~~15.5~~<br>|~~73.0~~<br>|~~8.8~~<br>|~~10.8~~<br>|
|~~5 ~~<br>|~~100.8~~<br>|~~9.6~~<br>|~~21.3~~<br>|~~100.8~~<br>|~~12.2~~<br>|~~14.9~~<br>|
|~~10~~<br>|~~121.0~~<br>|~~11.5~~<br>|~~25.6~~<br>|~~121.0~~<br>|~~14.6~~<br>|~~17.8~~<br>|
|~~25~~<br>|~~148.7~~<br>|~~14.1~~<br>|~~31.5~~<br>|~~148.7~~<br>|~~18.0~~<br>|~~21.9~~<br>|
|~~50~~<br>|~~171.1~~<br>|~~16.2~~<br>|~~36.2~~<br>|~~171.1~~<br>|~~20.7~~<br>|~~25.2~~<br>|
|~~100~~|~~195.0~~|~~18.5~~|~~41.3~~|~~195.0~~|~~23.6~~|~~28.8~~|

Tabla 4-10. Caudales máximos instantáneos, Quebrada 1 y Quebrada 2.

|T (años)|Quebrada 1|Quebrada 2|
|---|---|---|
|T (años)<br>|~~Q (m3/s)~~<br>|~~Q (m3/s)~~<br>|
|~~2 ~~<br>|~~0.36~~<br>|~~2.29~~<br>|
|~~5 ~~<br>|~~0.50~~<br>|~~3.17~~<br>|
|~~10~~<br>|~~0.60~~<br>|~~3.80~~<br>|
|~~25~~<br>|~~0.81~~<br>|~~5.14~~<br>|
|~~50~~<br>|~~1.01~~<br>|~~6.45~~<br>|
|~~100~~|~~1.20~~|~~7.65~~|



## 4.2 Modelación Hidráulica

A partir de los caudales definidos en la hidrología, se efectúa un análisis hidráulico a fin de
conocer las cotas de crecida asociadas a distintos periodos de retorno. El análisis consiste en
la construcción de un modelo hidráulico mediante el software HEC-RAS (Hydrologic
Engineering Center - River Analysis System), el que, como datos de entrada requiere de los
siguientes antecedentes:

 - Caudales.

 Perfiles topográficos.

 Coeficientes de rugosidad.

 - Condiciones de borde.

### 4.2.1 Caudales

Los caudales evaluados corresponden a los asociados a periodos de retorno T=100 años. En
la Tabla 4-11 se presentan los caudales de entrada asignados para cada cauce.

|Col1|Tabla 4-11. Caudales de Entrada. Q (m3/s)|Col3|Col4|
|---|---|---|---|
|T (años)<br>|~~Q (m3/s)~~<br>|~~Q (m3/s)~~<br>|~~Q (m3/s)~~<br>|
|T (años)<br>|Quebrada 1<br>|~~Quebrada 2~~<br><br>|~~Quebrada 2~~<br><br>|
|T (años)<br>|Quebrada 1<br>|~~Arriba Confluencia~~<br>|~~Abajo Confluencia~~<br>|
|~~100~~|~~1.20~~|~~7.65~~|~~8.85~~|

### 4.2.2 Perfiles Transversales

Para la Quebrada 1, se consideró un total de 8 perfiles transversales, desarrollados en un
tramo de 354 m. Para la Quebrada 2, se consideró un total de 13 perfiles transversales,
desarrollados en un tramo de 471 m. En la Figura 4-2 se muestra la ubicación en planta de
los perfiles utilizados.



Figura 4-2. Perfiles Transversales.

### 4.2.3 Rugosidad del Lecho

Para determinar el valor de la rugosidad de Manning en los cauces se utiliza la fórmula de

Cowan:

### nn= mm (nn 0 + nn 1 + nn 2 + nn 3 + nn 4 )

Donde:

nn: rugosidad de Manning
nn 0 : rugosidad base asociada al material del lecho
nn 1 : rugosidad adicional debida a irregularidades superficiales del perímetro mojado a lo largo

del tramo en estudio.

nn 2 : rugosidad adicional debida a variación de forma y de dimensiones de las secciones a lo
largo del tramo en estudio.
nn 3 : rugosidad adicional debida a la presencia de vegetación.
### nn 4 : rugosidad debida a la presencia de vegetación.

mm : factor de corrección para incorporar efecto de sinuosidad del cauce o presencia de

meandros.



En la Tabla 4-12 se indican los valores adoptados de las distintas variables de rugosidad.

Tabla 4-12. Valores adoptados de variables de rugosidad de Manning.

|Condiciones|Descripción|Símbolo|Valor|
|---|---|---|---|
|~~Material del Lecho~~<br>|~~Tierra~~|n0|~~0.020~~|
|~~Grado de Irregularidad Perímetro~~<br>Mojado<br>|Leve<br>|n1 <br>|0.005<br>|
|~~Variaciones de las Secciones~~<br>|~~Graduales~~<br>|n2 <br>|~~0.000~~<br>|
|~~Efecto Relativo de las Obstrucciones~~<br>|~~Despreciable~~<br>|n3 <br>|~~0.000~~<br>|
|~~Densidad de Vegetación~~<br>|~~Media~~<br>|n4 <br>|~~0.020~~<br>|
|~~Sinuosidad y Frecuencia de Meandros~~<br>|~~Leve~~<br>|m <br>|~~1 ~~<br>|
|~~**Coeficiente de Manning**~~<br>||~~**_n _**~~|~~**0.045**~~|

De esta forma, se obtiene una rugosidad de Manning para el cauce de _n_ = 0.045. De acuerdo

con el Manual de Carreteras V3, Tabla 3.707.104.A, este valor está asociado a cursos

menores, con curvas, algunas pozas y bancos de arena, con algo de maleza y piedras. Con
respecto a las riberas se adopta un valor de _n_ = 0.060, valor que de acuerdo con el Manual de
Carreteras V3, Tabla 3.707.104.A, está asociado a pocos matorrales y árboles.

Figura 4-3. Fotografías al interior del cauce del estero.



### 4.2.4 Condiciones de Borde

Para la Quebrada 1, aguas arriba, se adopta una condición de borde de altura normal, de S =
0.0114, de acuerdo con la pendiente de fondo del cauce; mientras que aguas abajo se
considera la presencia de la confluencia con la Quebrada 2.

Para esta último, aguas arriba y agua abajo se adopta una condición de borde de altura normal,
de S = 0.0027, de acuerdo con la pendiente de fondo del cauce.

### 4.2.5 Resultados

A continuación, se presentan los resultados de los modelos hidráulicos ejecutados. En la
Tabla 4-13 y Tabla 4-14 se presentan los resultados del modelo hidráulico para ambas
quebradas, mientras que en la Figura 4-4 y Figura 4-5 se muestra el perfil longitudinal del
escurrimiento para estas. Los Modelos Hidráulicos se encuentran en el Anexo Modelos HEC
RAS.

|Col1|Col2|Tabla 4-13 Min Ch|3. Resultados W.S.|s Quebrada 1|1, T = 100. Flow|Top|Froude #|
|---|---|---|---|---|---|---|---|
|River Sta<br>|Q Total<br>|~~Min Ch~~<br>El<br>|~~W.S.~~<br>Elev<br>|Vel Chnl<br>|~~Flow~~<br>Area<br>|~~Top~~<br>Width<br>|~~Froude #~~<br>Chl<br>|
|<br>|~~(m3/s)~~<br>|~~(m)~~<br>|~~(m)~~<br>|~~(m/s)~~<br>|~~(m2)~~<br>|~~(m)~~<br>|<br>|
|~~-5~~<br>|~~1.2~~<br>|~~97.2~~<br>|~~97.66~~<br>|~~0.62~~<br>|~~1.94~~<br>|~~15.34~~<br>|~~0.56~~<br>|
|~~-50~~<br>|~~1.2~~<br>|~~96.31~~<br>|~~96.63~~<br>|~~0.86~~<br>|~~1.4~~<br>|~~19.22~~<br>|~~1.02~~<br>|
|~~-100~~<br>|~~1.2~~<br>|~~95.83~~<br>|~~96.27~~<br>|~~0.23~~<br>|~~5.24~~<br>|~~34.69~~<br>|~~0.18~~<br>|
|~~-140~~<br>|~~1.2~~<br>|~~95.93~~<br>|~~96.09~~<br>|~~0.89~~<br>|~~1.35~~<br>|~~14.98~~<br>|~~0.95~~<br>|
|~~-200~~<br>|~~1.2~~<br>|~~95.13~~<br>|~~95.51~~<br>|~~0.51~~<br>|~~2.35~~<br>|~~11.87~~<br>|~~0.36~~<br>|
|~~-250~~<br>|~~1.2~~<br>|~~94.76~~<br>|~~95.34~~<br>|~~0.54~~<br>|~~2.22~~<br>|~~6.54~~<br>|~~0.3~~<br>|
|~~-300~~<br>|~~1.2~~<br>|~~94.46~~<br>|~~95.32~~<br>|~~0.22~~<br>|~~5.39~~<br>|~~9.66~~<br>|~~0.1~~<br>|
|~~-320~~<br>|~~1.2~~|~~94.3~~|~~95.32~~|~~0.19~~|~~6.32~~|~~10.6~~|~~0.08~~|

Figura 4-4. Perfil Longitudinal Quebrada 1



|Col1|Col2|Tabla 4-14 Min Ch|4. Resultados W.S.|s Quebrada 2|2, T = 100. Flow|Top|Froude #|
|---|---|---|---|---|---|---|---|
|River Sta<br>|Q Total<br>|~~Min Ch~~<br>El<br>|~~W.S.~~<br>Elev<br>|Vel Chnl<br>|~~Flow~~<br>Area<br>|~~Top~~<br>Width<br>|~~Froude #~~<br>Chl<br>|
|<br>|~~(m3/s)~~<br>|~~(m)~~<br>|~~(m)~~<br>|~~(m/s)~~<br>|~~(m2)~~<br>|~~(m)~~<br>|<br>|
|~~0 ~~<br>|~~7.65~~<br>|~~93.81~~<br>|~~95.42~~<br>|~~0.96~~<br>|~~9.79~~<br>|~~21.24~~<br>|~~0.32~~<br>|
|~~-50~~<br>|~~7.65~~<br>|~~93.58~~<br>|~~95.33~~<br>|~~0.86~~<br>|~~9.68~~<br>|~~12.91~~<br>|~~0.27~~<br>|
|~~-110~~<br>|~~8.85~~<br>|~~93.58~~<br>|~~95.13~~<br>|~~1.15~~<br>|~~7.7~~<br>|~~12.65~~<br>|~~0.45~~<br>|
|~~-150~~<br>|~~8.85~~<br>|~~93.56~~<br>|~~95.03~~<br>|~~0.8~~<br>|~~11.06~~<br>|~~15.28~~<br>|~~0.29~~<br>|
|~~-200~~<br>|~~8.85~~<br>|~~93.32~~<br>|~~94.79~~<br>|~~1.41~~<br>|~~6.26~~<br>|~~8.57~~<br>|~~0.53~~<br>|
|~~-250~~<br>|~~8.85~~<br>|~~93.11~~<br>|~~94.49~~<br>|~~1.26~~<br>|~~7.01~~<br>|~~10.4~~<br>|~~0.49~~<br>|
|~~-300~~<br>|~~8.85~~<br>|~~92.97~~<br>|~~94.3~~<br>|~~1.08~~<br>|~~8.27~~<br>|~~11.4~~<br>|~~0.37~~<br>|
|~~-350~~<br>|~~8.85~~<br>|~~92.51~~<br>|~~94.26~~<br>|~~0.69~~<br>|~~12.94~~<br>|~~11.9~~<br>|~~0.19~~<br>|
|~~-400~~<br>|~~8.85~~<br>|~~92.24~~<br>|~~94.19~~<br>|~~0.84~~<br>|~~10.68~~<br>|~~11.04~~<br>|~~0.25~~<br>|
|~~-439~~<br>|~~8.85~~<br>|~~92.12~~<br>|~~94.16~~<br>|~~0.71~~<br>|~~13.74~~<br>|~~15.75~~<br>|~~0.21~~<br>|
|~~-443~~<br>|~~Culvert~~<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|~~-446~~<br>|~~8.85~~<br>|~~92.06~~<br>|~~93.74~~<br>|~~1.57~~<br>|~~5.9~~<br>|~~7.92~~<br>|~~0.5~~<br>|
|~~-454~~<br>|~~8.85~~<br>|~~92.46~~<br>|~~93.76~~<br>|~~1.01~~<br>|~~8.76~~<br>|~~8.15~~<br>|~~0.31~~<br>|
|~~-463~~<br>|~~Culvert~~<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|~~-471~~<br>|~~8.85~~|~~92.54~~|~~93.67~~|~~1.05~~|~~8.44~~|~~8.83~~|~~0.34~~|

Figura 4-5. Perfil Longitudinal Quebrada 2.



Así, como se puede observar en la Figura 4-6, para el periodo de retorno de 100 años se
observan desbordes localizados en la quebrada 2, de los cuales una zona ingresan al area del
proyecto, pero no se intercepta con ninguna obra del parque, por lo que no existiria
interacción entre el area de inundación de la quebrada con el proyecto.

Figura 4-6. Área de inundación para T=100 años.



# 5 CONCLUSIONES

En el área de estudio, desde el punto de vista hídrico, solo se identifica un cauce natural
conformado por una serie de quebradas intermitentes que tributan en el estero Lonquen, a
unos 490 metros aguas abajo del polígono del proyecto.

Estas quebradas circulan en dirección norponiente a surporiente, y al acercarse al proyecto
cambian de dirección hacia el nororiente para descargar finalmente a través de una sola
quebrada común al citado rio Lonquen.

Para esta quebrada se estimó un caudal total, asociado a un periodo de retorno de 100 años,
de 8.85 m [3] /s. El área de inundación para este escenario presenta algunos desbordes
localizados en la quebrada que ingresan al área del proyecto, pero no interceptan ninguna
obra, por lo que se descarta la interacción entre la crecida de la quebrada y las obras del
parque fotovoltaico.

Considerando lo anterior, la Dirección General de Aguas a través de la Resolución DGA
N°135/20 y el Memo DGA N°118/20, ha definido que los cauces naturales que deberán
someterse al permiso de modificación de cauce deberán identificarse según la base de datos
oficiales asociada a la cartografía IGM, documentación técnica generada por la DGA, los
planes maestros de aguas lluvias y los demás antecedentes oficiales de gestión territorial,
evaluados para un periodo de retorno de 100 años; por lo que, dado que las obras del proyecto
se encuentran fuera del área de inundación de la quebrada no aplica el permiso de
modificación de cauce ni los permisos ambientales sectoriales 156 o 157 de competencia de

la DGA.

Alex García L.

Ingeniero Civil, M.Sc.

Dr. en Ciencias Ambientales

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1.: Estación San Agustín de Puñual.**

| Estación | Código BNA | Periodo de registro |
| --- | --- | --- |
| ~~San Agustín de Puñual~~<br> | ~~08118004-0~~ | ~~1993-2020~~ |

**Tabla 4-2.: Precipitaciones Máximas Anuales en 24 h.**

| Año | P (mm)<br>D | P (mm)<br>24 | Año | P (mm)<br>D | P (mm)<br>24 |
| --- | --- | --- | --- | --- | --- |
| ~~1993~~<br> | ~~72~~<br> | ~~79.2~~<br> | ~~2007~~<br> | ~~52~~<br> | ~~57.2~~<br> |
| ~~1994~~<br> | ~~44~~<br> | ~~48.4~~<br> | ~~2008~~<br> | ~~109~~<br> | ~~119.9~~<br> |
| ~~1995~~<br> | ~~76~~<br> | ~~83.6~~<br> | ~~2009~~<br> | ~~164~~<br> | ~~180.4~~<br> |
| ~~1996~~<br> | ~~66.6~~<br> | ~~73.26~~<br> | ~~2010~~<br> | ~~58~~<br> | ~~63.8~~<br> |
| ~~1997~~<br> | ~~95.8~~<br> | ~~105.38~~<br> | ~~2011~~<br> | ~~47.5~~<br> | ~~52.25~~<br> |
| ~~1998~~<br> | ~~30.5~~<br> | ~~33.55~~<br> | ~~2012~~<br> | ~~72.7~~<br> | ~~79.97~~<br> |
| ~~1999~~<br> | ~~63~~<br> | ~~69.3~~<br> | ~~2013~~<br> | ~~52~~<br> | ~~57.2~~<br> |
| ~~2000~~<br> | ~~59~~<br> | ~~64.9~~<br> | ~~2014~~<br> | ~~55~~<br> | ~~60.5~~<br> |
| ~~2001~~<br> | ~~92.4~~<br> | ~~101.64~~<br> | ~~2015~~<br> | ~~102~~<br> | ~~112.2~~<br> |
| ~~2002~~<br> | ~~106~~<br> | ~~116.6~~<br> | ~~2016~~<br> | ~~58.5~~<br> | ~~64.35~~<br> |
| ~~2003~~<br> | ~~69~~<br> | ~~75.9~~<br> | ~~2017~~<br> | ~~57.7~~<br> | ~~63.47~~<br> |
| ~~2004~~<br> | ~~46~~<br> | ~~50.6~~<br> | ~~2018~~<br> | ~~39.5~~<br> | ~~43.45~~<br> |
| ~~2005~~<br> | ~~106~~<br> | ~~116.6~~<br> | ~~2019~~<br> | ~~108~~<br> | ~~118.8~~<br> |
| ~~2006~~<br> | ~~76.4~~ | ~~84.04~~ | ~~2020~~ | ~~56.5~~ | ~~62.15~~ |

**Tabla 4-3.: Resultados del Análisis Estadístico de Precipitaciones.**

| T (años) | P (mm)<br>24 | Col3 | Col4 | Col5 | Col6 | Col7 | Valor-p | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T (años)<br> | ~~2 ~~<br> | ~~5 ~~<br> | ~~10~~<br> | ~~25~~<br> | ~~50~~<br> | ~~100~~<br> | ~~K - S~~<br> | ~~Chi 2~~<br> |
| ~~**Pearson 5**~~<br> | ~~**73.0**~~<br> | ~~**100.8**~~<br> | ~~**121.0**~~<br> | ~~**148.7**~~<br> | ~~**171.1**~~<br> | ~~**195.0**~~<br> | ~~0.946~~<br> | ~~0.332~~<br> |
| ~~Log-Pearson 3~~<br> | ~~73.6~~<br> | ~~101.7~~<br> | ~~121.3~~<br> | ~~147.4~~<br> | ~~167.6~~<br> | ~~188.7~~<br> | ~~0.922~~<br> | ~~0.691~~<br> |
| ~~Lognormal (3P)~~<br> | ~~73.6~~<br> | ~~101.4~~<br> | ~~120.6~~<br> | ~~145.6~~<br> | ~~164.7~~<br> | ~~184.3~~<br> | ~~0.916~~<br> | ~~0.698~~<br> |
| ~~Gamma (3P)~~<br> | ~~74.2~~<br> | ~~102.6~~<br> | ~~121.1~~<br> | ~~143.7~~<br> | ~~159.9~~<br> | ~~175.6~~<br> | ~~0.913~~<br> | ~~0.706~~<br> |
| ~~Pearson 5 (3P)~~<br> | ~~73.5~~ | ~~100.9~~ | ~~120.2~~ | ~~146.2~~ | ~~166.8~~ | ~~188.5~~ | ~~0.911~~ | ~~0.694~~ |

**Tabla 4-4.: Características Morfométricas de las Cuencas.**

| Característica | Símbolo (unidad) | Cuenca "Quebrada 1" | Cuenca "Quebrada 2" |
| --- | --- | --- | --- |
| Característica<br> | Símbolo (unidad)<br> | ~~Valor~~<br> | ~~Valor~~<br> |
| ~~Área~~<br> | ~~A (km2) ~~<br> | ~~0.24~~<br> | ~~2.19~~<br> |
| ~~Desnivel~~<br> | ~~H (m)~~ | ~~21~~ | ~~64~~ |
| ~~Desnivel entre cota~~<br>media y salida<br> | Hm (m)<br> | 6 <br> | 22<br> |
| ~~Pendiente Media~~<br> | ~~S ~~<br> | ~~0.0291~~<br> | ~~0.0714~~<br> |
| ~~Longitud de cauce~~<br> | ~~L (km)~~ | ~~0.70~~ | ~~1.94~~ |

**Tabla 4-5.: Factores de Coeficiente de Escorrentía, Cuenca "Cauce 1"**

| Factor | Col2 | Valor | Descripción |
| --- | --- | --- | --- |
| C1 | Relieve | 0.11 | ~~Relativamente plano, con pendientes menores~~<br>al 5%<br> |
| C2 | Infiltración | 0.08 | ~~Normal, terrenos bien drenados, textura~~<br>mediana, limos arenosos, suelos arenosos.<br> |
| C3 | Cobertura Vegetal | 0.07 | ~~Regular a buena, 50% del área con praderas o~~<br>bosques.<br> |
| C4 | Almacenamiento Superficial | 0.09 | ~~Baja, sistema de cauces superficiales pequeños~~<br>bien definidos, sin zonas húmedas. |
| **C **<br> |  | **0.35** | **Coeficiente de escorrentía** |

**Tabla 4-6.: Factores de Coeficiente de Escorrentía, Cuenca "Cauce 2"**

| Factor | Col2 | Valor | Descripción |
| --- | --- | --- | --- |
| C1 | Relieve | 0.15 | Normal, con cerros y pendientes entre 5 y 10%<br> |
| C2 | Infiltración | 0.08 | ~~Normal, terrenos bien drenados, textura~~<br>mediana, limos arenosos, suelos arenosos.<br> |
| C3 | Cobertura Vegetal | 0.05 | ~~Buena a Excelente, 90% del área con praderas,~~<br>bosques o cobertura equivalente.<br> |
| C4 | Almacenamiento Superficial | 0.07 | ~~Normal, posibilidad de almacenamiento buena,~~<br>zonas húmedas. |
| **C **<br> |  | **0.35** | **Coeficiente de escorrentía** |

**Tabla 4-7.: Coeficiente de Escorrentía, Cuencas "Cauce 1" y "Cauce 2".**

| T | Factor | C |
| --- | --- | --- |
| ~~2 ~~<br> | ~~1.0~~<br> | ~~0.28~~<br> |
| ~~5 ~~<br> | ~~1.0~~<br> | ~~0.28~~<br> |
| ~~10~~<br> | ~~1.0~~<br> | ~~0.28~~<br> |
| ~~25~~<br> | ~~1.1~~<br> | ~~0.308~~<br> |
| ~~50~~<br> | ~~1.2~~<br> | ~~0.336~~<br> |
| ~~100~~<br> | ~~1.25~~<br> | ~~0.35~~<br> |
| ~~150~~ | ~~1.25~~ | ~~0.35~~ |

**Tabla 4-8.: Valores obtenidos de Tiempo de Concentración.**

| Método | Tiempo de Concentración (h) | Col3 |
| --- | --- | --- |
| Método<br> | ~~Cuenca "Quebrada 1"~~<br> | ~~Cuenca "Quebrada 2"~~<br> |
| ~~**Normas Españolas**~~<br> | ~~**0.45**~~<br> | ~~**0.82**~~<br> |
| ~~California~~<br> | ~~0.19~~<br> | ~~0.41~~<br> |
| ~~Giandotti~~ | ~~1.54~~ | ~~2.35~~ |

**Tabla 4-10.: Caudales máximos instantáneos, Quebrada 1 y Quebrada 2.**

| T (años) | Quebrada 1 | Quebrada 2 |
| --- | --- | --- |
| T (años)<br> | ~~Q (m3/s)~~<br> | ~~Q (m3/s)~~<br> |
| ~~2 ~~<br> | ~~0.36~~<br> | ~~2.29~~<br> |
| ~~5 ~~<br> | ~~0.50~~<br> | ~~3.17~~<br> |
| ~~10~~<br> | ~~0.60~~<br> | ~~3.80~~<br> |
| ~~25~~<br> | ~~0.81~~<br> | ~~5.14~~<br> |
| ~~50~~<br> | ~~1.01~~<br> | ~~6.45~~<br> |
| ~~100~~ | ~~1.20~~ | ~~7.65~~ |

**Tabla 4-12.: Valores adoptados de variables de rugosidad de Manning.**

| Condiciones | Descripción | Símbolo | Valor |
| --- | --- | --- | --- |
| ~~Material del Lecho~~<br> | ~~Tierra~~ | n0 | ~~0.020~~ |
| ~~Grado de Irregularidad Perímetro~~<br>Mojado<br> | Leve<br> | n1 <br> | 0.005<br> |
| ~~Variaciones de las Secciones~~<br> | ~~Graduales~~<br> | n2 <br> | ~~0.000~~<br> |
| ~~Efecto Relativo de las Obstrucciones~~<br> | ~~Despreciable~~<br> | n3 <br> | ~~0.000~~<br> |
| ~~Densidad de Vegetación~~<br> | ~~Media~~<br> | n4 <br> | ~~0.020~~<br> |
| ~~Sinuosidad y Frecuencia de Meandros~~<br> | ~~Leve~~<br> | m <br> | ~~1 ~~<br> |
| ~~**Coeficiente de Manning**~~<br> |  | ~~**_n _**~~ | ~~**0.045**~~ |

**Tabla 4-13: y Tabla 4-14 se presentan los resultados del modelo hidráulico para ambas**

| Col1 | Col2 | Tabla 4-13 Min Ch | 3. Resultados W.S. | s Quebrada 1 | 1, T = 100. Flow | Top | Froude # |
| --- | --- | --- | --- | --- | --- | --- | --- |
| River Sta<br> | Q Total<br> | ~~Min Ch~~<br>El<br> | ~~W.S.~~<br>Elev<br> | Vel Chnl<br> | ~~Flow~~<br>Area<br> | ~~Top~~<br>Width<br> | ~~Froude #~~<br>Chl<br> |
| <br> | ~~(m3/s)~~<br> | ~~(m)~~<br> | ~~(m)~~<br> | ~~(m/s)~~<br> | ~~(m2)~~<br> | ~~(m)~~<br> | <br> |
| ~~-5~~<br> | ~~1.2~~<br> | ~~97.2~~<br> | ~~97.66~~<br> | ~~0.62~~<br> | ~~1.94~~<br> | ~~15.34~~<br> | ~~0.56~~<br> |
| ~~-50~~<br> | ~~1.2~~<br> | ~~96.31~~<br> | ~~96.63~~<br> | ~~0.86~~<br> | ~~1.4~~<br> | ~~19.22~~<br> | ~~1.02~~<br> |
| ~~-100~~<br> | ~~1.2~~<br> | ~~95.83~~<br> | ~~96.27~~<br> | ~~0.23~~<br> | ~~5.24~~<br> | ~~34.69~~<br> | ~~0.18~~<br> |
| ~~-140~~<br> | ~~1.2~~<br> | ~~95.93~~<br> | ~~96.09~~<br> | ~~0.89~~<br> | ~~1.35~~<br> | ~~14.98~~<br> | ~~0.95~~<br> |
| ~~-200~~<br> | ~~1.2~~<br> | ~~95.13~~<br> | ~~95.51~~<br> | ~~0.51~~<br> | ~~2.35~~<br> | ~~11.87~~<br> | ~~0.36~~<br> |
| ~~-250~~<br> | ~~1.2~~<br> | ~~94.76~~<br> | ~~95.34~~<br> | ~~0.54~~<br> | ~~2.22~~<br> | ~~6.54~~<br> | ~~0.3~~<br> |
| ~~-300~~<br> | ~~1.2~~<br> | ~~94.46~~<br> | ~~95.32~~<br> | ~~0.22~~<br> | ~~5.39~~<br> | ~~9.66~~<br> | ~~0.1~~<br> |
| ~~-320~~<br> | ~~1.2~~ | ~~94.3~~ | ~~95.32~~ | ~~0.19~~ | ~~6.32~~ | ~~10.6~~ | ~~0.08~~ |
