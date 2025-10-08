---
title: Estudio de inundación
author: Luis Alberto Muñoz Vásquez – Ingeniero Civil
date: D:20210210173922-03'00'
language: es
type: general
pages: 43
has_toc: True
has_tables: True
extraction_quality: high
---

Anexo 1-05 Estudio de Inundación

**Pozo Lastrero Coyanco**

**Preparado para Áridos Cantaruta Ltda.**

**Febrero, 2021**

Estudio de inundación

Declaración de Impacto Ambiental - Pozo Lastrero Coyanco

**REV 0**

02/02/2021

**Elaborado para:**

**ÁRIDOS CANTARUTA LTDA**

**Por:**

**ÍNDICE**

1. Introducción ............................................................................................................ 3

2. Objetivos ................................................................................................................. 4

3. Ubicación del área de estudio ................................................................................. 5

4. Predio del titular y tramo de estudio ........................................................................ 6

5. Información topográfica ........................................................................................... 8

6. Estudio hidrológico ................................................................................................ 10

6.1. Información fluviométrica ................................................................................... 11

6.2. Análisis de frecuencia ........................................................................................ 11

6.2.1. Distribución Weibull .................................................................................... 12

6.2.2. Distribución Normal .................................................................................... 12

6.2.3. Distribución Log Normal (2P) ...................................................................... 13

6.2.4. Distribución Pearson Tipo III ....................................................................... 13

6.2.5. Distribución Log-Pearson Tipo III (3P) ........................................................ 13

6.2.6. Distribución Gumbel ................................................................................... 14

6.2.7. Prueba de bondad de ajuste ....................................................................... 14

6.3. Resultados ........................................................................................................ 15

7. Modelo hidráulico .................................................................................................. 18

7.1. Dominio del modelo y condición de contorno ..................................................... 21

7.2. Coeficiente de rugosidad de Manning ................................................................ 22

7.3. Resultados ........................................................................................................ 23

1

8. Conclusiones......................................................................................................... 34

9. Apéndice 1: Planos de inundación ........................................................................ 36

2

**1. INTRODUCCIÓN**

El estudio de riesgo de inundación desarrollado para el titular Áridos Cantaruta, tiene por

objetivo determinar, a través de herramientas numéricas y computacionales, las áreas

afectas a inundaciones producidas por crecidas extraordinarias del río Biobío, concluyendo,

en base a estos resultados, sobre la factibilidad de llevar a cabo un proyecto de extracción

de áridos desde pozo lastrero dentro del predio del titular.

El tramo estudiado se ubica en el río Biobío, aguas abajo del sector Coihue. Cuenta con

una extensión longitudinal de 3.200 metros, considerando, aproximadamente, 500 metros

aguas arriba y 500 metros aguas abajo de los límites prediales del titular.

La modelación hidráulica se llevó a cabo mediante el software HecRAS. Para su

elaboración, se empleó la información topo-batimétrica recogida por el titular y el registro

de caudales instantáneos máximos diarios obtenidos de las estaciones fluviométricas de la

Dirección General de Aguas. A partir de la información topo-batimétrica, se generó el

modelo digital de terreno del cauce y sus planicies de inundación. Por su parte, con el

registro de caudales instantáneos máximos diarios se llevó a cabo un análisis de frecuencia,

a través del cual se obtuvieron los caudales de crecida del río Biobío en el tramo de estudio

para los diferentes periodos de retorno.

Con especial énfasis, se determinó el límite de inundación para un caudal de crecida con

periodo de retorno de 5 años, lo cual, de acuerdo con lo establecido en el Decreto Supremo

609 del año 1979, permite establecer el límite riberano y deslinde con la propiedad particular

del titular. Por otro lado, se determinó el riesgo y límites de inundación para un evento de

crecida extraordinario de 100 años de periodo de retorno, a partir del cual, se establecieron

las áreas disponibles para el desarrollo de un proyecto de extracción y las recomendaciones

para su realización.

En los siguientes apartados, se presentan los antecedentes técnicos, procedimientos y

resultados del estudio de riesgo de inundación del río Biobío.

3

**2. OBJETIVOS**

Los objetivos del estudio son:

 Determinar la respuesta hidrológica de la cuenca hidrográfica con punto de drenaje

en el tramo de estudio para distintos periodos de retorno.

 Elaborar el modelo hidráulico del tramo de estudio que permita determinar los límites

de inundación para caudales de crecida con periodos de retorno de 5 y 100 años.

 Identificar las áreas disponibles para desarrollar un proyecto de extracción de áridos.

 Entregar las recomendaciones para el desarrollo de actividades de extracción en las

áreas fuera de inundación.

4

**3. UBICACIÓN DEL ÁREA DE ESTUDIO**

El área de estudio se encuentra ubicada en la Comuna de Los Ángeles, Región del Biobío,

sus coordenadas centrales son: Norte 5844062 m y Este 712953 m, según sistema UTM

Datum WGS 84 Huso 18H.

En la siguiente figura, se presenta la ubicación del área de estudio.

**Figura 1. Ubicación área de estudio.**

**Fuente: Elaboración propia.**

5

**4. PREDIO DEL TITULAR Y TRAMO DE ESTUDIO**

El predio propiedad del titular corresponde a la parcela n°18 del lote B Rol 1554-312, con

una superficie total de 78.1 há.

**Figura 2. Predio del titular - Lote B, Rol 1554-312.**

**Fuente: Antecedentes del titular.**

El tramo de estudio corresponde a 3.200 metros de extensión longitudinal, comprendiendo

una extensión transversal promedio de 2.500 metros, con lo cual se logra el objetivo de

modelar un caudal de crecida con periodo de retorno de 100 años dada la envergadura del

cauce natural.

En la siguiente figura, se presenta una imagen satelital referencial del predio del titular y el

tramo de estudio.

6

**Figura 3. Tramo de estudio y predio del titular.**

**Fuente: Elaboración propia.**

7

**5. INFORMACIÓN TOPOGRÁFICA**

El trabajo topográfico consistió en la medición de la geoforma del terreno en el cauce y

planicies de inundación del río Biobío. La medición se llevó a cabo realizando perfiles

transversales desde extremo a extremo de ribera, espaciados entre 150 a 250 metros, de

esta forma, recolectando los puntos que describen de mejor forma las singularidades del

terreno. Se realizaron dos levantamientos topográficos: abril de 2019 y octubre de 2020. En

este último se actualizó la información y se generaron puntos en las planicies de inundación

más alejadas del cauce, abarcando extensiones transversales por sobre los 1000 metros.

Para establecer el ancho del perfil se tuvo en cuenta el objetivo del levantamiento (estudio

de inundación), por lo tanto, donde el relieve era despreciable se distanció más la captura

de puntos, por el contrario, en las zonas de interés se aumentó la densidad de puntos.

Ambos levantamientos fueron realizados con base en los puntos de referencia

materializados por el titular en la campaña de 2019. Los puntos de referencia fueron

obtenidos a partir del procesamiento del registro estático (>2 horas) de la antena base. El

procesamiento se realizó a través del _Online Positioning User Service_ (OPUS) del _National_

_Oceanic and Atmospheric Administration_ (NOAA). A continuación, se indican las

coordenadas de los puntos de referencia:

**-**
**Tabla 1. Coordenadas puntos de referencia** **UTM Datum WGS 84, Huso 18H.**

|ID punto|Norte [m]|Este [m]|Elevación [m.s.n.m.]|
|---|---|---|---|
|PR1|5840780.007|713606.099|78.73|
|PR2|5841495.854|713185.852|86.55|

**Fuente: Levantamiento topográfico.**

La instrumentación utilizada fue la siguiente:

 - GPS RTK LEICA modelo PREXISO

 - Estación total TOPCON modelo GPT 3207N

 GNSS Spectra Precision SP80

 - Ecosonda GARMIN GPSMAP 527XS

 - Dron Phantom 4 pro v2.0

En la siguiente figura, se presentan los resultados del procesamiento de los datos de

terreno; el cual se denomina: modelo digital de terreno (MDT).

8

**Figura 4. Modelo digital de terreno (MDT).**

**Fuente: Elaboración propia.**

9

**6. ESTUDIO HIDROLÓGICO**

El estudio hidrológico se realizó en base a los datos fluviométricos registrados por la

estación río Biobío en Rucalhue (Código BNA: 08317001-8). Se seleccionó esta estación

fluviométrica debido a que cuenta con un registro continuo de 52 datos, iniciando en el año

1969, siendo la estación con el mayor registro continuo en el área. Su registro fue obtenido

desde las bases de datos de la Dirección General de Aguas y el Centro de Ciencia del Clima

y la Resiliencia (CR) [2] .

Se desestimó la utilización de la estación fluviométrica río Biobío en Desembocadura al

encontrarse en la parte baja de la cuenca hidrográfica, considerando los aportes de

afluentes importantes como río Laja y Vergara, y cuyo uso de suelo es principalmente

forestal, generando una respuesta de la escorrentía superficial mucho más rápida que la

observada en la parte media de la cuenca, la cual posee un uso principalmente agrícola.

En su conjunto, estas condiciones pueden producir una sobreestimación en los caudales

de crecida. Por otro lado, la estación río Biobío en Coihue presenta un registro discontinuo

durante una ventana de tiempo de 3 años. Cabe destacar, que, en cualquiera de las tres

estaciones antes mencionadas, se observa un registro fluviométrico fuertemente

influenciado por la operación de los embalses Angostura, Pangue y Ralco, ubicados en la

parte alta de la cuenca hidrográfica del Biobío, lo cual implica que los caudales de crecida

se verán amortiguados por el efecto de los embalses sobre el hidrograma de salida

De acuerdo con las recomendaciones de la Dirección General de Aguas y los

procedimientos hidrológicos frecuentemente utilizados en Chile cuando se poseen datos

fluviométricos, se realizó un análisis de frecuencia ajustando las siguientes funciones de

distribuciones acumulada:

 - Normal

 - Log-Normal

 - Pearson

 - Log-Pearson

 - Gumbel Max

En conformidad con los resultados de la prueba de bondad de Chi-Cuadrado y el

Coeficiente de Correlación obtenido para cada función, se seleccionó la función que mejor

se ajusta a los datos del registro fluviométrico presentado anteriormente y se determinaron

10

los caudales de crecida para la cuenca hidrográfica con punto de drenaje en la estación

fluviométrica río Biobío Rucalhue. Luego, se realizó una transposición de caudales desde

la estación fluviométrica al área de estudio.

La determinación de las cuencas hidrográficas se realizó utilizando el software QGIS y un

modelo de elevación digital (DEM, por sus siglas en inglés) ALOS PALSAR de 12.5 metros

de resolución, obtenido a partir de información SAR (Radar de Apertura Sintética, SAR por

sus siglas en inglés).

**6.1. Información fluviométrica**

A continuación, se presenta el registro fluviométrico obtenido de la estación río Biobío en

Rucalhue:

**Tabla 1. Registro fluviométrico estación río Biobío en Rucalhue.**

|Año|Q [m3/s]|Año|Q [m3/s]|Año|Q [m3/s]|
|---|---|---|---|---|---|
|1969|3480|1989|2267|2009|657|
|1970|2128|1990|2693|2010|1357|
|1971|2625|1991|4179|2011|1317|
|1972|6492|1992|2519|2012|1013|
|1973|1906|1993|4297|2013|1060|
|1974|2120|1994|3362|2014|1421|
|1975|2525|1995|2599|2015|1514|
|1976|2643|1996|1583|2016|698|
|1977|1944|1997|3014|2017|888|
|1978|2645|1998|515|2018|1695|
|1979|3589|1999|1363|2019|1407|
|1980|3082|2000|3260|2020|1035|
|1981|3147|2001|4803|||
|1982|3263|2002|3519|3519|3519|
|1983|2972|2003|4442|4442|4442|
|1984|2488|2004|1229|1229|1229|
|1985|3362|2005|1928|1928|1928|
|1986|3599|2006|5589|5589|5589|
|1987|2052|2007|759|759|759|
|1988|1510|2008|1345|1345|1345|

**Fuente: Dirección General de Aguas y (CR)** **[2]** **.**

**6.2. Análisis de frecuencia**

El análisis de frecuencia de información hidrológica relaciona los eventos extremos con su

frecuencia de ocurrencia mediante el uso de distribuciones de probabilidad (Chow, et al.

1994).

11

En este caso de estudio se efectuó un análisis de frecuencia al registro de datos ajustando

las distribuciones: Normal, Log-Normal, Pearson tipo III, Log-Pearson tipo III y Gumbel. Por

su parte, la serie de datos es confeccionada a través de la función de densidad de

probabilidad de Weibull. A continuación, se describen las distribuciones utilizadas.

**6.2.1. Distribución Weibull**

Ordenando los valores de la serie estadística en forma creciente, la probabilidad Weibull se

calcula utilizándola siguiente expresión:

m
P=
n+ 1

Donde:

P: Distribución de probabilidad.

m: Número de orden.

n: Número de datos de la serie.

**6.2.2. Distribución Normal**

La función de distribución de probabilidad se define con la siguiente expresión:

]

1
f(x) =

σ ~~√~~ 2π

exp[− 2 [1]

2 [(x−μ] σ

2

σ )

Donde:

x: precipitación.

μ: media.

σ: varianza.

Las hipótesis para que se cumpla la distribución normal de una muestra son las siguientes:

 - La variable es continua.

 Los valores consecutivos son eventos independientes.

 Las probabilidades son estables.

12

**6.2.3. Distribución Log Normal (2P)**

La función de distribución de probabilidad se define con la siguiente expresión:

2

]

1
f(y) =

σ y ~~√~~ 2π

exp[− 2 [1] [(]

x−μ y

σ
y

~~)~~

Donde:

x: precipitación.

μ y : Media.

σ : Varianza.
y

**6.2.4. Distribución Pearson Tipo III**

La función de distribución de probabilidad se define con la siguiente expresión:

f(x) = f(x 0 [x]
) (1 +

α
δ exp⁡ (− [x]

α ~~[)]~~

δ [)]

Donde:

x: precipitación.

X m : Modo.

δ: diferencia entre la media y el modo.

α : parámetro de escala de la distribución.

**6.2.5. Distribución Log-Pearson Tipo III (3P)**

La función de distribución de probabilidad se define con la siguiente expresión:

~~)~~

f(y) = f(y 0 [y]
) (1 +

α

δy

δ

exp⁡ (− [y] y

[y]

α [)]

δ
y

Donde:

13

y: logaritmo natural de la precipitación.

x: precipitación.

Y m : Modo de y.

δ: diferencia entre la media y el modo.

α : parámetro de escala de la distribución.

**6.2.6. Distribución Gumbel**

La función de distribución de probabilidad se define con la siguiente expresión:

f(x) = exp(exp⁡(−b))

Con:

b= [x−μ]

α

μ= ~~x~~ −0.5772α

S x
α=
1.2825

Donde:

x: Precipitación.

~~x~~ ~~:~~ Media aritmética de la muestra.

S x : Desviación típica de la muestra.

**6.2.7. Prueba de bondad de ajuste**

El objetivo de la prueba de bondad de ajuste es comprobar estadísticamente, o

gráficamente en algunos casos, si la frecuencia empírica de la serie analizada se ajusta a

una determinada función de probabilidad teórica seleccionada previamente, cuyos

parámetros fueron estimados en base a los valores muestrales. De esta forma, es posible

14

calificar la suposición de que una variable aleatoria se distribuya de acuerdo con una

determinada función de probabilidad.

Para este caso en particular, se utilizó la prueba de bondad de ajuste Chi-cuadrado (X [2] ), la

cual se basa en el cálculo de frecuencias de los valores observados y valores esperados.

La expresión general está dada por:

k

2

C

= ∑ [(θ] [i] [−e] e [i] [)] [2]

X C

i=1

e i

Donde:

k

i
∑θ

i=1

k

i = N
= ∑e

i=1

X C2 : Valor cálculado de Chi-cuadrado a partir de los datos.

θ i : Número de valores observados en el intervalo de clase i.

e i : Número de valores esperados en el intervalo de clase i.

k: Número de intervalos de clase.

**6.3. Resultados**

A continuación, se presentan los resultados del análisis de frecuencia realizado al registro

fluviométrico:

15

**Tabla 2. Resultado análisis de frecuencia.**

|Col1|Col2|Col3|Col4|Funciones de distribución acumulada [m3/s]|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**m**|**Q [m3/s]**|**p**|**1-p**|**Normal**|**Log-Normal**|**Pearson**|**Log-Pearson**|**Gumbel Max**|
|1|515|0.019|0.981|-253|643|500|559|463|
|2|657|0.038|0.962|136|763|677|696|657|
|3|698|0.057|0.943|387|853|800|799|791|
|4|759|0.075|0.925|578|927|900|886|897|
|5|888|0.094|0.906|736|994|986|963|989|
|6|1013|0.113|0.887|872|1055|1064|1034|1070|
|7|1035|0.132|0.868|993|1113|1135|1100|1144|
|8|1060|0.151|0.849|1102|1168|1201|1163|1213|
|9|1229|0.170|0.830|1202|1220|1264|1223|1278|
|10|1317|0.189|0.811|1296|1271|1324|1281|1340|
|11|1345|0.208|0.792|1384|1322|1381|1338|1399|
|12|1357|0.226|0.774|1467|1371|1438|1394|1457|
|13|1363|0.245|0.755|1547|1420|1492|1449|1513|
|14|1407|0.264|0.736|1623|1468|1546|1503|1568|
|15|1421|0.283|0.717|1696|1516|1599|1557|1621|
|16|1510|0.302|0.698|1768|1564|1651|1610|1675|
|17|1514|0.321|0.679|1837|1613|1703|1664|1727|
|18|1583|0.340|0.660|1904|1661|1755|1717|1779|
|19|1695|0.358|0.642|1970|1710|1806|1771|1831|
|20|1906|0.377|0.623|2035|1760|1858|1824|1883|
|21|1928|0.396|0.604|2099|1810|1910|1879|1935|
|22|1944|0.415|0.585|2162|1861|1962|1933|1987|
|23|2052|0.434|0.566|2225|1913|2014|1989|2039|
|24|2120|0.453|0.547|2287|1966|2067|2045|2092|
|25|2128|0.472|0.528|2348|2020|2121|2102|2146|
|26|2267|0.491|0.509|2410|2075|2175|2160|2200|
|27|2488|0.509|0.491|2471|2131|2231|2219|2255|
|28|2519|0.528|0.472|2532|2190|2287|2279|2311|
|29|2525|0.547|0.453|2594|2250|2345|2341|2368|
|30|2599|0.566|0.434|2656|2312|2404|2404|2427|
|31|2625|0.585|0.415|2718|2376|2465|2469|2487|
|32|2643|0.604|0.396|2782|2443|2528|2537|2548|
|33|2645|0.623|0.377|2845|2513|2592|2606|2612|
|34|2693|0.642|0.358|2910|2586|2659|2678|2678|
|35|2972|0.660|0.340|2976|2662|2729|2753|2746|
|36|3014|0.679|0.321|3044|2742|2801|2830|2817|
|37|3082|0.698|0.302|3113|2827|2877|2912|2891|
|38|3147|0.717|0.283|3184|2917|2957|2997|2969|
|39|3260|0.736|0.264|3258|3013|3042|3088|3052|
|40|3263|0.755|0.245|3334|3115|3131|3183|3139|
|41|3362|0.774|0.226|3414|3226|3227|3285|3231|
|42|3362|0.792|0.208|3497|3346|3330|3394|3331|
|43|3480|0.811|0.189|3585|3478|3442|3512|3439|
|44|3519|0.830|0.170|3678|3624|3564|3640|3557|
|45|3589|0.849|0.151|3779|3788|3700|3782|3687|
|46|3599|0.868|0.132|3888|3974|3852|3940|3833|
|47|4179|0.887|0.113|4009|4191|4027|4120|3999|
|48|4297|0.906|0.094|4145|4449|4233|4329|4194|
|49|4442|0.925|0.075|4302|4768|4484|4580|4430|
|50|4803|0.943|0.057|4494|5187|4807|4898|4731|
|51|5589|0.962|0.038|4745|5792|5265|5335|5150|
|52|6492|0.981|0.019|5134|6873|6057|6058|5861|
||||**R2**|**0.9447**|**0.9805**|**0.9904**|**0.9891**|**0.9898**|

**Fuente: Elaboración propia.**

La función Pearson fue la que presentó el mejor ajuste y a partir de ella fueron determinados

los caudales de crecida en la estación fluviométrica río Biobío en Rucalhue.

16

**Tabla 3. Caudales de crecida, estación fluviométrica río Biobío en Rucalhue.**

|T [años]|p|1-p|Q [m3/s]|
|---|---|---|---|
|2|0.5|0.5|2203|
|5|0.8|0.2|3374|
|10|0.9|0.1|4168|
|25|0.96|0.04|5199|
|50|0.98|0.02|5990|
|100|0.99|0.01|6803|

**Fuente: Elaboración propia.**

Para obtener los caudales de crecida en el área de estudio se realizó una transposición de

caudales. Esta operación se traduce en la obtención del coeficiente de transposición,

obtenidos de la relación de áreas entre las cuencas de interés. En este caso, se tiene la

cuenca hidrográfica correspondiente a la estación fluviométrica río Biobío en Rucalhue y la

cuenca hidrográfica con punto de drenaje inmediatamente aguas arriba del tramo de

estudio.

**Figura 5.Cuencas hidrográficas área de estudio y estación fluviométrica río Biobío**

**en Rucalhue.**
**Fuente: Elaboración propia.**

Las áreas determinadas y su respectivo Coeficiente de Trasposición fueron:

17

 Cuenca Área de estudio: 11.183 [km [2] ]

 Cuenca Estación fluviométrica río Biobío en Rucalhue: 7.277 [km [2] ]

 Coeficiente de transposición: 1,537

De esto forma, los caudales de crecida obtenidos en el área de estudio fueron los

siguientes:

**Tabla 4. Caudales de crecida, Área de Estudio.**

**Fuente: Elaboración propia.**

**7. MODELO HIDRÁULICO**

Para caracterizar el comportamiento hidráulico del cauce se utilizó el modelo

unidimensional HEC-RAS, desarrollado por el Cuerpo de Ingenieros del Ejército de EE.UU.

Los supuestos principales de este tipo de modelos son lecho fijo, régimen permanente y

flujo unidimensional. Por su parte, el análisis hidráulico tiene por objetivo analizar los

principales parámetros hidráulicos como velocidad, ancho superficial, perímetro mojado,

etc., también determinar los márgenes de inundación para la condición hidrológica

centenaria y resolver sobre posibles afectaciones de esta situación de crecida.

18

**Figura 6. Representación gráfico método numérico.**

**Fuente: Elaboración propia.**

Este programa computacional se basa en una solución unidimensional de la ecuación de

energía. De esta manera, es posible obtener el eje hidráulico del cauce a lo largo de la zona

de interés para los diferentes periodos de retorno determinados, considerando un

escurrimiento gradualmente variado y los coeficientes de rugosidad de Manning

determinados mediante el Método de Cowan.

El cálculo del flujo permanente gradualmente variado se realiza a partir de la siguiente

ecuación:

2 2

+ Z + a 2  V 2 = Y + Z + a 1  V 1 + h

2 2 1 1

2g 2g

2

+ Z + a 1  V 1

1 1

Y + Z + a 2  V 2 = Y + Z + a 1  V 1 +

 V 2 = Y + Z + a 1  V

1 1

2g 2g

e

Donde:

Y1. Y2: profundidad del agua en la sección;

Z1. Z2: elevación de la sección principal;

V1. V2: velocidad media;

19

a1. a2: coeficiente de carga de la velocidad;

g: aceleración de gravedad;

h e : pérdida principal de energía.

La pérdida de energía (h e ) entre dos secciones transversales se atribuye a las pérdidas por

fricción y a las pérdidas debido a contracciones y/o expansiones. La ecuación utilizada para

el cálculo de pérdidas es:

e = L  S f + C  a 2  V 22 − a 1  V 12

h = L  S f + C  a 2  V

 V 2 − a 1  V

2g 2g

= L  S f + C  2  2 − 1 

Donde:

L: Longitud de alcance de descarga;

S
f

: Pendiente representativa de la fricción entre dos secciones;

C: Coeficiente de contracción o expansión.

La pérdida de fricción se calculó para cada sección de la siguiente forma:

 Q 
S f =
 K 

2

Donde:

Q: transporte para la sección;

K: transporte para la subdivisión.

La determinación del transporte total y del coeficiente de velocidad para una sección

transversal requiere que el flujo esté subdividido en las unidades para las cuales la

velocidad se distribuye uniformemente. El software HEC-RAS 4.1.0 subdivide el flujo,

separando las planicies de inundación del cauce principal a partir de los puntos medidos.

El flujo es calculado para cada subsección con la siguiente ecuación:

20

Q = K  S 1f 2

K = 1.486  A  R 2 3

n

Donde:

K: transporte para la subdivisión;

n: coeficiente de rugosidad de Manning para la subdivisión;

A: área de flujo de la subdivisión;

R: radio hidráulico para la subdivisión.

El programa requiere como datos de entrada la topografía del cauce, vale decir, secciones

transversales del cauce en el tramo de interés, las cuales fueron extraídas desde la

topografía, rugosidad del material del lecho, definidas por el método de Cowan, y

características del flujo, condición inicial y de borde. Como resultados HEC-RAS 4.1.0

entrega parámetros como la profundidad y velocidad media del flujo, sección de

escurrimiento, perímetro mojado, profundidad crítica, número de Froude, entre otros.

**7.1. Dominio del modelo y condición de contorno**

Para el modelo hidráulico se consideró una extensión longitudinal de 3.200 metros. Las

secciones transversales fueron espaciadas cada 100 metros y su extensión transversal de,

aproximadamente, 2.500 metros, siendo esta la necesaria para delimitar de manera

correcta el cauce y sus planicies de inundación para una condición de crecida centenaria.

Para la condición de contorno se definió un régimen subcrítico controlado desde agua abajo

por su altura normal S=0.0085.

En la siguiente figura, se presenta la extensión del modelo y sus secciones transversales

en una vista en planta.

21

**Figura 7. Vista en planta modelo hidráulico.**

**Fuente: Modelo hidráulico.**

**7.2. Coeficiente de rugosidad de Manning**

Para estimar los coeficientes de rugosidad de Manning se empleó la expresión propuesta

en el Método de Cowan, la cual bajo una función relaciona 6 parámetros característicos del

cauce. De esta forma, se definieron 2 coeficientes de rugosidad: cauce principal y planicies

de inundación. En la siguiente tabla, se presentan los valores de cada parámetro:

**Tabla 5. Coeficiente de rugosidad de Manning - Método de Cowan.**

|Col1|cauce principal|planicies de<br>inundación|
|---|---|---|
|n0|0.027|0.020|
|n1|0.000|0.000|
|n2|0.000|0.000|
|n3|0.000|0.005|
|n4|0.000|0.010|
|m5|1.000|1.000|
|n|0.027|0.035|

**Fuente: Elaboración propia.**

El parámetro n0 fue determinado mediante la expresión de Strickler, la cual utilizada el D90

(129.3 mm) obtenido de la granulometría del lecho del cauce.

22

**7.3. Resultados**

Como resultado de la modelación se obtuvo el eje hidráulico para los diferentes periodos

de retorno y las principales variables de flujo, tales como: velocidad, ancho superficial,

número de Froude y área mojada. Por otro lado, se generaron las líneas de inundación para

los caudales de crecida con periodo de retorno de 5 y 100 años. [1]

A continuación, se muestran los ejes hidráulicos para cada periodo de retorno:

**Figura 8. Ejes hidráulicos.**

**Fuente: Modelo hidráulico.**

1 Si bien no resulta de relevancia para el análisis, el programa también entrega los resultados para T=2.

23

**Figura 9. Vista en perspectiva eje hidráulico T100.**

**Fuente: Modelo hidráulico.**

En las siguientes tablas se presentan los resultados numéricos de la modelación para cada

periodo de retorno:

24

**Tabla 6. Resultados modelo hidráulico - T2.**

|Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400|Periodo<br>retorno<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2|Q Total<br>[m3/s]<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385|Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35|Eje<br>hidráulico<br>[m]<br>75.95<br>75.96<br>75.28<br>75.30<br>75.34<br>75.33<br>75.34<br>75.29<br>75.22<br>75.18<br>75.12<br>75.09<br>74.88<br>74.84<br>74.76|Velocidad<br>[m/s]<br>2.56<br>1.86<br>3.82<br>2.64<br>1.84<br>1.56<br>1.23<br>1.51<br>1.69<br>1.75<br>1.84<br>1.81<br>2.57<br>2.45<br>2.50|Área mojada<br>[m2]<br>2191.53<br>2238.90<br>1048.85<br>1297.25<br>1835.42<br>2171.01<br>2745.83<br>2244.05<br>2010.30<br>2015.01<br>2004.09<br>2132.04<br>1636.94<br>1949.67<br>1993.07|Ancho<br>superficial<br>[m]<br>1664.68<br>1689.08<br>612.71<br>632.61<br>609.31<br>569.37<br>543.34<br>511.89<br>571.70<br>843.15<br>952.94<br>935.53<br>1100.77<br>1262.45<br>1185.30|Froude #<br>Chl<br>0.37<br>0.35<br>0.71<br>0.56<br>0.34<br>0.25<br>0.18<br>0.23<br>0.28<br>0.29<br>0.31<br>0.26<br>0.44<br>0.41<br>0.42|
|---|---|---|---|---|---|---|---|---|
|km 1+500|T2|3385<br>|69.99<br>|74.56<br>|2.98<br>|1744.13<br>|1094.97<br>|0.50<br>|
|km 1+600<br>km 1+700<br>km 1+800|T2<br>T2<br>T2|3385<br>3385<br>3385<br>|70.07<br>69.93<br>69.40<br>|74.53<br>74.48<br>74.55<br>|2.64<br>2.41<br>1.27<br>|1999.38<br>2184.12<br>4031.48<br>|1066.06<br>1070.59<br>1541.82<br>|0.43<br>0.39<br>0.20<br>|
|km 1+900<br>km 2+000<br>km 2+100|T2<br>T2<br>T2|3385<br>3385<br>3385<br>|69.42<br>69.41<br>69.30<br>|74.33<br>73.80<br>73.36<br>|2.52<br>3.88<br>1.82<br>|2096.99<br>1385.71<br>2071.22<br>|1118.24<br>1137.68<br>1181.55<br>|0.41<br>0.69<br>0.31<br>|
|km 2+200<br>km 2+300|T2<br>T2|3385<br>3385|69.51<br>69.11|72.76<br>72.89|3.70<br>2.27|1182.24<br>1800.34|960.42<br>1146.05|0.72<br>0.42|
|km 2+400<br>km 2+500|T2<br>T2|3385<br>3385|69.18<br>68.64|72.74<br>72.51|2.45<br>2.73|1631.37<br>1498.00|1149.88<br>1274.06|0.50<br>0.57|
|km 2+600<br>km 2+700<br>km 2+800|T2<br>T2<br>T2|3385<br>3385<br>3385|69.11<br>66.95<br>67.39|71.96<br>71.93<br>71.10|3.56<br>2.65<br>4.18|1027.21<br>1359.78<br>809.81|938.14<br>1013.89<br>346.88|0.82<br>0.54<br>0.87|
|km 2+900|T2|3385<br>|66.82<br>|71.33<br>|2.59<br>|1308.23<br>|335.09<br>|0.42<br>|
|km 3+000|T2|3385|66.24|71.02|3.22|1052.05|274.29|0.52|
|km 3+100<br>km 3+200|T2<br>T2|3385<br>3385|66.21<br>65.85|70.40<br>69.82|4.27<br>4.75|792.46<br>712.72|253.34<br>246.60|0.77<br>0.89|

**Fuente: Elaboración propia.**

25

**Tabla 7. Resultados modelo hidráulico - T5.**

|Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400|Periodo<br>retorno<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5|Q Total<br>[m3/s]<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184|Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35|Eje<br>hidráulico<br>[m]<br>76.61<br>76.61<br>76.08<br>75.98<br>76.01<br>76.00<br>76.02<br>75.92<br>75.84<br>75.78<br>75.72<br>75.66<br>75.46<br>75.43<br>75.34|Velocidad<br>[m/s]<br>2.80<br>2.05<br>3.80<br>3.04<br>2.29<br>2.02<br>1.66<br>2.01<br>2.20<br>2.24<br>2.33<br>2.38<br>3.03<br>2.81<br>2.88|Área mojada<br>[m2]<br>3368.94<br>3394.21<br>2159.59<br>1797.58<br>2264.88<br>2619.30<br>3121.89<br>2601.00<br>2384.03<br>2624.70<br>2620.03<br>2767.29<br>2358.73<br>2701.52<br>2686.39|Ancho<br>superficial<br>[m]<br>1874.67<br>1909.46<br>1700.22<br>807.86<br>705.60<br>815.06<br>573.13<br>608.63<br>640.20<br>1135.51<br>1121.39<br>1284.49<br>1293.93<br>1273.64<br>1195.01|Froude #<br>Chl<br>0.38<br>0.35<br>0.64<br>0.57<br>0.39<br>0.31<br>0.22<br>0.29<br>0.35<br>0.34<br>0.36<br>0.32<br>0.48<br>0.44<br>0.45|
|---|---|---|---|---|---|---|---|---|
|km 1+500|T5|5184<br>|69.99<br>|75.13<br>|3.39<br>|2370.39<br>|1105.48<br>|0.53<br>|
|km 1+600<br>km 1+700<br>km 1+800|T5<br>T5<br>T5|5184<br>5184<br>5184<br>|70.07<br>69.93<br>69.40<br>|75.08<br>75.02<br>75.11<br>|3.09<br>2.88<br>1.58<br>|2590.43<br>2762.77<br>4900.59<br>|1076.62<br>1080.87<br>1557.53<br>|0.48<br>0.44<br>0.24<br>|
|km 1+900<br>km 2+000<br>km 2+100|T5<br>T5<br>T5|5184<br>5184<br>5184<br>|69.42<br>69.41<br>69.30<br>|74.82<br>74.21<br>73.92<br>|3.05<br>4.51<br>2.27<br>|2645.84<br>1860.66<br>2735.96<br>|1130.17<br>1146.14<br>1198.76<br>|0.47<br>0.76<br>0.36<br>|
|km 2+200<br>km 2+300|T5<br>T5|5184<br>5184|69.51<br>69.11|73.32<br>73.40|4.12<br>2.76|1844.80<br>2433.55|1312.15<br>1318.06|0.73<br>0.47|
|km 2+400<br>km 2+500|T5<br>T5|5184<br>5184|69.18<br>68.64|73.24<br>73.06|2.88<br>3.02|2249.34<br>2225.70|1313.45<br>1332.43|0.54<br>0.56|
|km 2+600<br>km 2+700<br>km 2+800|T5<br>T5<br>T5|5184<br>5184<br>5184|69.11<br>66.95<br>67.39|72.85<br>72.78<br>72.68|3.16<br>2.70<br>2.89|2131.79<br>2387.79<br>2530.08|1327.60<br>1291.13<br>1258.88|0.60<br>0.47<br>0.47|
|km 2+900|T5|5184<br>|66.82<br>|72.67<br>|2.44<br>|2911.53<br>|1191.39<br>|0.34<br>|
|km 3+000|T5|5184|66.24|72.46|2.99|2452.38|1176.88|0.42|
|km 3+100<br>km 3+200|T5<br>T5|5184<br>5184|66.21<br>65.85|71.39<br>70.69|4.94<br>5.55|1049.32<br>933.67|264.01<br>255.40|0.79<br>0.93|

**Fuente: Elaboración propia.**

26

**Tabla 8. Resultados modelo hidráulico - T10.**

|Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400|Periodo<br>retorno<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10|Q Total<br>[m3/s]<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404|Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35|Eje<br>hidráulico<br>[m]<br>76.91<br>76.90<br>76.52<br>76.44<br>76.41<br>76.39<br>76.41<br>76.28<br>76.17<br>76.12<br>76.04<br>75.98<br>75.80<br>75.77<br>75.68|Velocidad<br>[m/s]<br>2.99<br>2.22<br>3.62<br>2.91<br>2.47<br>2.25<br>1.88<br>2.29<br>2.50<br>2.51<br>2.61<br>2.67<br>3.22<br>3.00<br>3.10|Área mojada<br>[m2]<br>3938.72<br>3958.58<br>2921.11<br>2789.95<br>2892.30<br>3187.02<br>3797.85<br>3087.28<br>2602.38<br>3020.71<br>3012.17<br>3190.93<br>2805.52<br>3140.40<br>3087.29|Ancho<br>superficial<br>[m]<br>1926.29<br>2016.61<br>1765.77<br>1604.89<br>1476.15<br>1463.72<br>1447.40<br>1427.11<br>674.87<br>1265.67<br>1286.02<br>1331.91<br>1300.78<br>1278.48<br>1200.59|Froude #<br>Chl<br>0.40<br>0.37<br>0.58<br>0.51<br>0.40<br>0.33<br>0.24<br>0.32<br>0.38<br>0.37<br>0.39<br>0.35<br>0.49<br>0.45<br>0.46|
|---|---|---|---|---|---|---|---|---|
|km 1+500|T10|6404<br>|69.99<br>|75.45<br>|3.62<br>|2729.65<br>|1111.61<br>|0.54<br>|
|km 1+600<br>km 1+700<br>km 1+800|T10<br>T10<br>T10|6404<br>6404<br>6404<br>|70.07<br>69.93<br>69.40<br>|75.39<br>75.33<br>75.44<br>|3.35<br>3.15<br>1.76<br>|2929.71<br>3095.11<br>5404.32<br>|1082.64<br>1086.73<br>1566.56<br>|0.50<br>0.47<br>0.25<br>|
|km 1+900<br>km 2+000<br>km 2+100|T10<br>T10<br>T10|6404<br>6404<br>6404<br>|69.42<br>69.41<br>69.30<br>|75.09<br>74.45<br>74.21<br>|3.35<br>4.86<br>2.53<br>|2958.82<br>2131.72<br>3086.10<br>|1136.91<br>1150.94<br>1208.40<br>|0.50<br>0.79<br>0.39<br>|
|km 2+200<br>km 2+300|T10<br>T10|6404<br>6404|69.51<br>69.11|73.86<br>73.88|3.76<br>2.77|2569.94<br>3073.66|1345.30<br>1335.18|0.61<br>0.44|
|km 2+400<br>km 2+500|T10<br>T10|6404<br>6404|69.18<br>68.64|73.78<br>73.69|2.77<br>2.75|2964.11<br>3061.86|1326.75<br>1336.69|0.47<br>0.47|
|km 2+600<br>km 2+700<br>km 2+800|T10<br>T10<br>T10|6404<br>6404<br>6404|69.11<br>66.95<br>67.39|73.60<br>73.55<br>73.49|2.70<br>2.43<br>2.55|3129.00<br>3375.42<br>3557.80|1338.74<br>1292.27<br>1259.32|0.46<br>0.38<br>0.38|
|km 2+900|T10|6404<br>|66.82<br>|73.46<br>|2.33<br>|3893.75<br>|1232.45<br>|0.30<br>|
|km 3+000|T10|6404|66.24|73.35|2.70|3497.55|1177.67|0.35|
|km 3+100<br>km 3+200|T10<br>T10|6404<br>6404|66.21<br>65.85|71.99<br>71.22|5.29<br>5.99|1210.28<br>1068.38|270.65<br>260.25|0.80<br>0.94|

**Fuente: Elaboración propia.**

27

**Tabla 9. Resultados modelo hidráulico - T25.**

|Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400|Periodo<br>retorno<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25|Q Total<br>[m3/s]<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989|Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35|Eje<br>hidráulico<br>[m]<br>77.33<br>77.33<br>77.01<br>76.93<br>76.87<br>76.84<br>76.86<br>76.71<br>76.55<br>76.51<br>76.44<br>76.36<br>76.21<br>76.18<br>76.07|Velocidad<br>[m/s]<br>3.08<br>2.28<br>3.58<br>2.95<br>2.63<br>2.47<br>2.12<br>2.56<br>2.87<br>2.79<br>2.88<br>2.97<br>3.43<br>3.20<br>3.33|Área mojada<br>[m2]<br>4769.43<br>5074.15<br>3809.22<br>3587.47<br>3582.93<br>3853.92<br>4456.96<br>3706.92<br>2866.71<br>3556.87<br>3542.09<br>3697.63<br>3335.24<br>3657.30<br>3558.55|Ancho<br>superficial<br>[m]<br>1954.44<br>2483.01<br>1937.98<br>1713.88<br>1490.94<br>1469.91<br>1468.62<br>1445.54<br>753.94<br>1399.32<br>1369.26<br>1339.45<br>1308.85<br>1284.16<br>1207.12|Froude #<br>Chl<br>0.40<br>0.36<br>0.54<br>0.48<br>0.40<br>0.34<br>0.27<br>0.34<br>0.42<br>0.39<br>0.41<br>0.38<br>0.50<br>0.46<br>0.48|
|---|---|---|---|---|---|---|---|---|
|km 1+500|T25|7989<br>|69.99<br>|75.83<br>|3.88<br>|3151.25<br>|1118.77<br>|0.56<br>|
|km 1+600<br>km 1+700<br>km 1+800|T25<br>T25<br>T25|7989<br>7989<br>7989<br>|70.07<br>69.93<br>69.40<br>|75.76<br>75.69<br>75.82<br>|3.65<br>3.45<br>1.96<br>|3328.79<br>3486.29<br>6000.36<br>|1089.68<br>1093.59<br>1577.18<br>|0.52<br>0.49<br>0.27<br>|
|km 1+900<br>km 2+000<br>km 2+100|T25<br>T25<br>T25|7989<br>7989<br>7989<br>|69.42<br>69.41<br>69.30<br>|75.41<br>74.71<br>74.69<br>|3.68<br>5.28<br>2.72<br>|3327.55<br>2432.93<br>3659.92<br>|1144.81<br>1156.25<br>1224.04<br>|0.53<br>0.83<br>0.40<br>|
|km 2+200<br>km 2+300|T25<br>T25|7989<br>7989|69.51<br>69.11|74.49<br>74.48|3.51<br>2.77|3426.24<br>3880.67|1371.09<br>1356.47|0.53<br>0.41|
|km 2+400<br>km 2+500|T25<br>T25|7989<br>7989|69.18<br>68.64|74.41<br>74.35|2.71<br>2.66|3799.89<br>3940.05|1342.67<br>1341.63|0.43<br>0.41|
|km 2+600<br>km 2+700<br>km 2+800|T25<br>T25<br>T25|7989<br>7989<br>7989|69.11<br>66.95<br>67.39|74.28<br>74.24<br>74.20|2.59<br>2.41<br>2.50|4046.83<br>4266.89<br>4558.93|1348.91<br>1293.30<br>1360.16|0.40<br>0.35<br>0.34|
|km 2+900|T25|7989<br>|66.82<br>|74.16<br>|2.38<br>|4755.40<br>|1232.59<br>|0.30<br>|
|km 3+000|T25|7989|66.24|74.07|2.72|4342.70|1178.31|0.33|
|km 3+100<br>km 3+200|T25<br>T25|7989<br>7989|66.21<br>65.85|73.96<br>71.83|2.99<br>6.49|4005.81<br>1230.30|1172.49<br>265.95|0.38<br>0.96|

**Fuente: Elaboración propia.**

28

**Tabla 10. Resultados modelo hidráulico - T50.**

|Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400|Periodo<br>retorno<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50|Q Total<br>[m3/s]<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205|Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35|Eje<br>hidráulico<br>[m]<br>77.63<br>77.64<br>77.32<br>77.24<br>77.17<br>77.13<br>77.14<br>76.99<br>76.84<br>76.79<br>76.72<br>76.63<br>76.49<br>76.46<br>76.34|Velocidad<br>[m/s]<br>3.15<br>2.30<br>3.68<br>3.00<br>2.76<br>2.63<br>2.29<br>2.74<br>3.00<br>2.97<br>3.04<br>3.17<br>3.57<br>3.35<br>3.50|Área mojada<br>[m2]<br>5362.82<br>5838.66<br>4485.95<br>4135.85<br>4027.24<br>4280.68<br>4879.20<br>4103.60<br>3580.60<br>3953.93<br>3928.93<br>4057.24<br>3707.90<br>4019.63<br>3890.46|Ancho<br>superficial<br>[m]<br>1999.18<br>2483.01<br>2343.82<br>1811.55<br>1500.38<br>1473.86<br>1475.96<br>1457.22<br>1442.16<br>1474.18<br>1376.15<br>1344.78<br>1314.49<br>1288.13<br>1211.69|Froude #<br>Chl<br>0.40<br>0.35<br>0.53<br>0.47<br>0.41<br>0.35<br>0.28<br>0.36<br>0.42<br>0.41<br>0.42<br>0.40<br>0.50<br>0.47<br>0.49|
|---|---|---|---|---|---|---|---|---|
|km 1+500|T50|9205<br>|69.99<br>|76.09<br>|4.07<br>|3447.05<br>|1123.76<br>|0.57<br>|
|km 1+600<br>km 1+700<br>km 1+800|T50<br>T50<br>T50|9205<br>9205<br>9205<br>|70.07<br>69.93<br>69.40<br>|76.02<br>75.94<br>76.08<br>|3.85<br>3.66<br>2.10<br>|3609.13<br>3762.01<br>6422.82<br>|1094.60<br>1098.40<br>1584.67<br>|0.54<br>0.51<br>0.29<br>|
|km 1+900<br>km 2+000<br>km 2+100|T50<br>T50<br>T50|9205<br>9205<br>9205<br>|69.42<br>69.41<br>69.30<br>|75.64<br>74.89<br>74.77<br>|3.92<br>5.56<br>3.05<br>|3586.89<br>2647.19<br>3763.59<br>|1150.33<br>1160.02<br>1226.84<br>|0.55<br>0.86<br>0.44<br>|
|km 2+200<br>km 2+300|T50<br>T50|9205<br>9205|69.51<br>69.11|74.49<br>74.48|4.04<br>3.19|3426.75<br>3873.49|1371.10<br>1356.28|0.61<br>0.47|
|km 2+400<br>km 2+500|T50<br>T50|9205<br>9205|69.18<br>68.64|74.37<br>74.28|3.16<br>3.14|3749.21<br>3845.17|1340.38<br>1340.67|0.50<br>0.49|
|km 2+600<br>km 2+700<br>km 2+800|T50<br>T50<br>T50|9205<br>9205<br>9205|69.11<br>66.95<br>67.39|74.18<br>74.11<br>74.04|3.10<br>2.89<br>3.03|3904.06<br>4097.98<br>4347.49|1347.34<br>1293.11<br>1360.16|0.49<br>0.43<br>0.42|
|km 2+900|T50|9205<br>|66.82<br>|73.99<br>|2.88<br>|4541.93<br>|1232.55<br>|0.36<br>|
|km 3+000|T50|9205|66.24|73.82|3.37|4051.02|1178.09|0.42|
|km 3+100<br>km 3+200|T50<br>T50|9205<br>9205|66.21<br>65.85|73.58<br>72.79|3.87<br>5.18|3563.52<br>2529.52|1171.51<br>1131.38|0.50<br>0.70|

**Fuente: Elaboración propia.**

29

**Tabla 11. Resultados modelo hidráulico - T100.**

|Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400|Periodo<br>retorno<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100|Q Total<br>[m3/s]<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454|Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35|Eje<br>hidráulico<br>[m]<br>77.90<br>77.91<br>77.64<br>77.55<br>77.47<br>77.42<br>77.43<br>77.26<br>77.11<br>77.07<br>76.99<br>76.89<br>76.77<br>76.73<br>76.61|Velocidad<br>[m/s]<br>3.23<br>2.35<br>3.57<br>3.03<br>2.86<br>2.77<br>2.44<br>2.91<br>3.16<br>3.12<br>3.18<br>3.36<br>3.69<br>3.49<br>3.65|Área mojada<br>[m2]<br>5898.12<br>6508.48<br>5282.98<br>4705.20<br>4473.35<br>4709.91<br>5303.38<br>4509.83<br>3978.68<br>4369.37<br>4305.92<br>4408.56<br>4069.19<br>4370.38<br>4211.93|Ancho<br>superficial<br>[m]<br>2018.24<br>2483.01<br>2479.96<br>1860.96<br>1519.69<br>1501.84<br>1483.30<br>1472.59<br>1489.06<br>1567.79<br>1386.12<br>1349.96<br>1319.94<br>1291.96<br>1216.11|Froude #<br>Chl<br>0.40<br>0.34<br>0.50<br>0.46<br>0.41<br>0.36<br>0.29<br>0.37<br>0.43<br>0.42<br>0.43<br>0.41<br>0.51<br>0.48<br>0.50|
|---|---|---|---|---|---|---|---|---|
|km 1+500|T100|10454<br>|69.99<br>|76.35<br>|4.24<br>|3733.34<br>|1128.57<br>|0.58<br>|
|km 1+600<br>km 1+700<br>km 1+800|T100<br>T100<br>T100|10454<br>10454<br>10454<br>|70.07<br>69.93<br>69.40<br>|76.26<br>76.18<br>76.34<br>|4.04<br>3.86<br>2.25<br>|3880.84<br>4029.81<br>6834.38<br>|1099.34<br>1103.05<br>1610.32<br>|0.55<br>0.52<br>0.30<br>|
|km 1+900<br>km 2+000<br>km 2+100|T100<br>T100<br>T100|10454<br>10454<br>10454<br>|69.42<br>69.41<br>69.30<br>|75.86<br>75.07<br>75.02<br>|4.14<br>5.83<br>3.22<br>|3837.50<br>2854.45<br>4067.23<br>|1155.64<br>1163.65<br>1235.02<br>|0.57<br>0.88<br>0.46<br>|
|km 2+200<br>km 2+300|T100<br>T100|10454<br>10454|69.51<br>69.11|74.79<br>74.76|4.09<br>3.31|3828.13<br>4256.50|1379.84<br>1366.27|0.60<br>0.48|
|km 2+400<br>km 2+500|T100<br>T100|10454<br>10454|69.18<br>68.64|74.66<br>74.56|3.25<br>3.23|4133.86<br>4233.40|1359.98<br>1348.28|0.50<br>0.49|
|km 2+600<br>km 2+700<br>km 2+800|T100<br>T100<br>T100|10454<br>10454<br>10454|69.11<br>66.95<br>67.39|74.47<br>74.40<br>74.34|3.19<br>3.00<br>3.14|4299.41<br>4473.88<br>4745.77|1351.70<br>1293.54<br>1360.16|0.48<br>0.43<br>0.42|
|km 2+900|T100|10454<br>|66.82<br>|74.28<br>|3.03<br>|4893.06<br>|1232.61<br>|0.37<br>|
|km 3+000|T100|10454|66.24|74.09|3.54|4376.72|1178.33|0.43|
|km 3+100<br>km 3+200|T100<br>T100|10454<br>10454|66.21<br>65.85|73.85<br>73.03|4.03<br>5.39|3884.42<br>2810.44|1172.22<br>1132.35|0.51<br>0.71|

**Fuente: Elaboración propia.**

De acuerdo con los resultados, el régimen del cauce es subcrítico; conforme con lo definido

al inicio de la modelación. Por otro lado, se observan velocidades que varían de 1.23 a 4.75

[m/s] para el periodo de retorno de 2 años, hasta 2.35 a 5.83 [m/s] para el periodo de retorno

de 100 años. Se observan aumentos puntuales de velocidad en los sectores donde el cauce

se profundiza y genera el desarrollo de sus meandros. Las velocidades más altas hacen

presumir se observarán efectos de inestabilidad en las riberas del cauce, lo cual implica,

que en ninguna circunstancia se deberán realizar actividades que alteren la geoforma de

las riberas

Conforme con los objetivos definidos para el estudio, a continuación, se presentan las líneas

de inundación para los periodos de retorno de 5 y 100 años sobre una imagen satelital del

área de estudio y con respecto a los límites del predio.

30

**Figura 10. Línea de inundación T5.**

**Fuente: Modelo hidráulico.**

Como se puede observar, los límites prediales se encuentran, en una primera parte del

tramo estudiado, sobre los límites de inundación para un caudal con periodo de retorno de

5 años, lo cual permite definir con seguridad las áreas ocupadas por el cauce en sus

crecidas recurrentes.

Es importante destacar que se observan inundaciones en la ribera izquierda, principalmente

debida a que en algunos sectores las planicies de inundación presentan depresiones que

permiten el ingreso del flujo en las secciones aguas arriba del modelo.

31

**Figura 11. Línea de inundación T100.**

**Fuente: Modelo hidráulico.**

Para el caudal centenario, se tiene una línea de inundación que ingresa al predio en su

parte inicial, abarcando prácticamente todo el ancho de la sección transversal. Aguas abajo,

se observa que la línea de inundación queda limitada por la terraza aluvial presente en la

parte interna del meandro, cuyas diferencias de altura con respecto a la ribera izquierda

van desde los 2 a 3 metros, lo cual, en todo evento de crecida, facilita que el flujo mantenga

anegada la ribera de la localidad de Nacimiento

Se observa que la planicie de inundación izquierda la conforman extensiones llanas de

terreno de menor elevación que la planicie derecha, descartándose así inundaciones en el

área de proyecto.

A continuación, se presentan algunas secciones transversales que caracterizan la

inundación para T5 y T100.

32

**Figura 12. Secciones trasversales con líneas de inundación T5 y T100.**

**Fuente: Modelo hidráulico.**

33

**8. CONCLUSIONES**

Para el escenario de crecida con un periodo de retorno de 5 años no se espera una

variabilidad relevante en los resultados, dado que el cauce principal resulta con capacidad

suficiente, en la mayoría de las secciones transversales, para portear dicho caudal, lo cual,

en definitiva, permite establecer con una seguridad aceptable los límites riberanos entre el

cauce y la propiedad del titular.

Para el escenario de crecida con periodo de retorno de 100 años existirá una variabilidad

mucho mayor en los resultados, pues para esta condición fluvial, y principalmente, de gran

escala meteorológica, los cambios morfológicos que puedan producirse en el cauce, ya sea

por acción individual o conjunta de fenómenos mecánico-fluviales (socavación y arrastre de

sólidos), puede conllevar cambios en los resultados de la modelación hidráulica. Cabe

señalar, sin embargo, que el área de proyecto al estar ubicada en la terraza aluvial de la

ribera derecha, se mantendrá siempre menos expuesta a inundaciones en comparación

con la ribera izquierda o de la localidad de Nacimiento, la cual se desarrolla en una

extensión mucho más llana y menos elevada y es donde se prevé pueda verse reflejada

variabilidad de resultados para período de retorno igual 100.

Por lo tanto, y en base a los resultados del estudio de inundación, se desestima la aplicación

del Permiso Ambiental Sectorial 159 toda vez que el proyecto de extracción se emplazará

fuera del límite de inundación para un caudal de crecida con periodo de retorno de 5 años.

Así también, no se requiere de obras de defensa fluvial dado que el proyecto se emplazará

fuera del límite de inundación del cauce para un caudal de crecida de 100 años de periodo

de retorno, desestimando la aplicabilidad del Permiso Ambiental Sectorial 157

Finalmente, es también importante considerar que el río Biobío se encuentra regulado

desde la parte alta de su cuenca hidrográfica por tres grandes embalses y sus respectivas

centrales hidroeléctricas: Angostura, Pangue y Ralco. Esto, por una parte, significa una

ventaja cuando hay un manejo adecuado y oportuno de estas obras, ya que logran atenuar

y retardar el hidrograma de entrada producido por una tormenta, resultando en caudales de

crecida de mucho menor magnitud a los determinados en la hidrología de este estudio. Por

el contrario, y teniendo como referencia lo ocurrido en el año 2006, una operación deficiente

de los embalses, o también fallas en la infraestructura, puede conllevar una respuesta

hidrológica fuera del alcance de las predicciones realizadas con los datos fluviométricos

actualmente registrados. Sin embargo, desde octubre de 2008, la Dirección General de

34

Aguas, a través de la Ley de Embalses, declaro el Embalse Ralco como embalse de control

de crecidas, definiendo nuevos criterios frente a contingencias y escenarios de crecidas

extraordinarias.

35

**9. APÉNDICE 1: PLANOS DE INUNDACIÓN**

36

|710500.00 711200.00 711900.00 712600.00 713300.00 714000.00 714700.00<br>ZONA DE<br>PROYECTO<br>5845700.00 5845700.00<br>5845000.00 5845000.00<br>DIAGRAMA DE UBICACIÓN<br>SIN ESCALA<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>V1<br>V13 V14<br>V15 V16 V2<br>V3<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>5844300.00 5844300.00<br>V11<br>C3<br>V4<br>V12<br>V10<br>C2<br>V9<br>SIMBOLOGIA<br>C1 5843600.00 5843600.00<br>V8<br>5842900.00 5842900.00<br>5842200.00 5842200.00<br>0 08-02-2021 INGRESO SEA L.M. I.P. I.P. 5841500.00 5841500.00<br>REV FECHA EMITIDO PARA EJECUTÓ REVISÓ APROBÓ<br>TITULAR: PROYECTISTA:<br>Áridos Cantarruta Ltda Luis Alberto Muñoz Vasquez<br>77.070.170-8 Ingeniero Civil, U. del Biobío<br>17.041.810-7<br>PROYECTO:<br>Extracción de áridos - Pozo Coyanco<br>PLANTA GENERAL DE PROYECTO CONTENIDO:<br>ESCALA 1:5000 PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>5840800.00 5840800.00<br>LÁMINA: CÓDIGO:<br>1 DE 5 CTRT-2021<br>710500.00 711200.00 711900.00 712600.00 713300.00 714000.00 714700.00 FECHA: ESCALA Y UNIDADES: FORMATO: REVISIÓN:<br>08-02-2021 INDICADAS/[m] A1 0|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|||||||
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|||||||
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|||||||
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|||||||
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|||||||
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|||||||
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|**0**|**08-02-2021**|**INGRESO S**|**EA**<br>**L.M.**|**I.P.**|**I.P.**|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|REV<br>FECHA<br>EMITIDO PA<br>TITULAR:|REV<br>FECHA<br>EMITIDO PA<br>TITULAR:|REV<br>FECHA<br>EMITIDO PA<br>TITULAR:|RA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>PROYECTISTA:|RA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>PROYECTISTA:|RA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>PROYECTISTA:|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|**Áridos Cantarruta Ltda**<br>**77.070.170-8**|**Áridos Cantarruta Ltda**<br>**77.070.170-8**|**Áridos Cantarruta Ltda**<br>**77.070.170-8**|**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>CONTENIDO:|PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>CONTENIDO:|PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>CONTENIDO:|PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>CONTENIDO:|PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>CONTENIDO:|PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>CONTENIDO:|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|LÁMINA:<br>**1 DE 5**|LÁMINA:<br>**1 DE 5**|LÁMINA:<br>**1 DE 5**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|
|V1<br>V2<br>V3<br>V4<br>V8<br>V9<br>V10<br>V11<br>V12<br>V13V14<br>V15<br>V16<br>PREDIO ROL 1554-312 LOTE B (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)<br>C1<br>C2<br>C3<br>PLANTA INUNDACIÓN Y PUNTOS DE REFERENCIA<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**1 DE 5**<br>**0**<br>**08-02-2021**<br>**INGRESO SEA**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>**DIAGRAMA DE UBICACIÓN**<br>**SIN ESCALA**<br>**ZONA DE**<br>**PROYECTO**<br> PLANTA GENERAL DE PROYECTO<br>ESCALA 1:5000<br>SIMBOLOGIA<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>710500.00<br>711200.00<br>711900.00<br>712600.00<br>713300.00<br>714000.00<br>714700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00<br>5840800.00<br>5841500.00<br>5842200.00<br>5842900.00<br>5843600.00<br>5844300.00<br>5845000.00<br>5845700.00|FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|REVISIÓN:<br>**0**<br>FORMATO:<br>**A1**|REVISIÓN:<br>**0**<br>FORMATO:<br>**A1**|REVISIÓN:<br>**0**<br>FORMATO:<br>**A1**|

|7<br>00.00|10500.00 711200.00 711900.00 7|12600.00 713300.00 714000.00 7147|00.00<br>00.00|
|---|---|---|---|
|00.00<br>58457|||00.00<br>58457|
|00.00<br>58450|V1<br>PREDIO ROL 1554-312 LOTE B|V1<br>V2<br>V3<br>3V14<br>V15<br>V16<br> (78.1 há)<br>ÁREA DE EXTRACCIÓN (41.8 há)|00.00<br>58450|
|00.00<br>58443||V4<br>V9<br>V10<br>V11<br>V12<br>C1<br>C2<br>C3|00.00<br>58443|
|0.00<br>58436||V8|0.00<br>58436|
|00.00<br>584290|||00.00<br>584290|
|5841500.00<br>58422|||5841500.00<br>58422|
|PLA<br>ESCA<br>0.00|NTA GENERAL DE PROYECTO<br>LA 1:5000||0.00|
|7<br>584080|10500.00<br>711200.00<br>711900.00<br>7|12600.00<br>713300.00<br>714000.00<br>7147|00.00<br>584080|

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
|**08-02-2021**|**INGRESO SEA**|**L.M.**|**I.P.**|**I.P.**|

|SIMBOLOGIA<br>0 08-02-2021 INGRESO SEA L.M. I.P. I.P.<br>REV FECHA EMITIDO PARA EJECUTÓ REVISÓ APROBÓ<br>TITULAR: PROYECTISTA:<br>Áridos Cantarruta Ltda Luis Alberto Muñoz Vasquez<br>77.070.170-8 Ingeniero Civil, U. del Biobío<br>17.041.810-7<br>PROYECTO:<br>Extracción de áridos - Pozo Coyanco<br>CONTENIDO:<br>SECCIONES TRANSVERSALES<br>LÁMINA: CÓDIGO:<br>PERFILES TRANSVERSALES 2 DE 5 CTRT-2021<br>ESCALA HORIZONTAL 1:4000 FECHA: ESCALA Y UNIDADES: FORMATO: REVISIÓN:<br>ESCALA VERTICAL 1:400 08-02-2021 INDICADAS/[m] A1 0|Col2|Col3|Col4|
|---|---|---|---|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**2 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>SIMBOLOGIA<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**2 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>SIMBOLOGIA<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**2 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>SIMBOLOGIA<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|FORMATO:<br>**A1**|REVISIÓN:<br>**0**|

|PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>SIMBOLOGIA<br>0 08-02-2021 INGRESO SEA L.M. I.P. I.P.<br>REV FECHA EMITIDO PARA EJECUTÓ REVISÓ APROBÓ<br>TITULAR: PROYECTISTA:<br>Áridos Cantarruta Ltda Luis Alberto Muñoz Vasquez<br>77.070.170-8 Ingeniero Civil, U. del Biobío<br>17.041.810-7<br>PROYECTO:<br>Extracción de áridos - Pozo Coyanco<br>CONTENIDO:<br>SECCIONES TRANSVERSALES<br>LÁMINA: CÓDIGO:<br>3 DE 5 CTRT-2021<br>FECHA: ESCALA Y UNIDADES: FORMATO: REVISIÓN:<br>08-02-2021 INDICADAS/[m] A1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**0**|**08-02-2021**|**08-02-2021**|**INGRESO SEA**|**INGRESO SEA**|**L.M.**|**I.P.**|**I.P.**|**I.P.**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|REV|FECHA|FECHA|EMITIDO PARA|EMITIDO PARA|EJECUTÓ|REVISÓ|REVISÓ|APROBÓ|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|LÁMINA:<br>**3 DE 5**|LÁMINA:<br>**3 DE 5**|LÁMINA:<br>**3 DE 5**|LÁMINA:<br>**3 DE 5**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**3 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|FECHA:<br>**08-02-2021**|FECHA:<br>**08-02-2021**|ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|FORMATO:<br>**A1**|FORMATO:<br>**A1**|FORMATO:<br>**A1**|REVISIÓN:<br>**0**|REVISIÓN:<br>**0**|

|SIMBOLOGIA<br>0 08-02-2021 INGRESO SEA L.M. I.P. I.P.<br>REV FECHA EMITIDO PARA EJECUTÓ REVISÓ APROBÓ<br>TITULAR: PROYECTISTA:<br>Áridos Cantarruta Ltda Luis Alberto Muñoz Vasquez<br>77.070.170-8 Ingeniero Civil, U. del Biobío<br>17.041.810-7<br>PROYECTO:<br>Extracción de áridos - Pozo Coyanco<br>CONTENIDO:<br>SECCIONES TRANSVERSALES<br>LÁMINA: CÓDIGO:<br>PERFILES TRANSVERSALES<br>4 DE 5 CTRT-2021<br>ESCALA HORIZONTAL 1:4000 FECHA: ESCALA Y UNIDADES: FORMATO: REVISIÓN:<br>ESCALA VERTICAL 1:400 08-02-2021 INDICADAS/[m] A1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**||||||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**0**|**08-02-2021**|**08-02-2021**|**INGRESO SEA**|**INGRESO SEA**|**L.M.**|**I.P.**|**I.P.**|**I.P.**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|REV|FECHA<br>|FECHA<br>|EMITIDO PARA|EMITIDO PARA|EJECUTÓ<br>|REVISÓ<br>|REVISÓ<br>|APROBÓ<br>|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>PROYECTO:|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|**SECCIONES TRANSVERSALES**<br>CONTENIDO:|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|LÁMINA:<br>**4 DE 5**|LÁMINA:<br>**4 DE 5**|LÁMINA:<br>**4 DE 5**|LÁMINA:<br>**4 DE 5**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|CÓDIGO:<br>**CTRT-2021**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**4 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|FECHA:<br>**08-02-2021**|FECHA:<br>**08-02-2021**|ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|ESCALA Y UNIDADES:<br>**INDICADAS/[m]**|FORMATO:<br>**A1**|FORMATO:<br>**A1**|FORMATO:<br>**A1**|REVISIÓN:<br>**0**|REVISIÓN:<br>**0**|

|PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>0 08-02-2021 INGRESO SEA L.M. I.P. I.P.<br>REV FECHA EMITIDO PARA EJECUTÓ REVISÓ APROBÓ<br>TITULAR: PROYECTISTA:<br>Áridos Cantarruta Ltda Luis Alberto Muñoz Vasquez<br>77.070.170-8 Ingeniero Civil, U. del Biobío<br>17.041.810-7<br>PROYECTO:<br>Extracción de áridos - Pozo Coyanco<br>SIMBOLOGIA<br>CONTENIDO:<br>SECCIONES TRANSVERSALES<br>LÁMINA: CÓDIGO:<br>5 DE 5 CTRT-2021<br>FECHA: ESCALA Y UNIDADES: FORMATO: REVISIÓN:<br>08-02-2021 INDICADAS/[m] A1 0|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|||||||
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**0**<br>**08-02-20**|**21**<br>**INGRESO SEA**|**21**<br>**INGRESO SEA**|**L.M.**|**I.P.**|**I.P.**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|REV<br>FECHA<br><br>|EMITIDO PARA<br><br>|EMITIDO PARA<br><br>|EJECUTÓ<br>|REVISÓ<br>|APROBÓ<br>|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>ITULAR:<br>P|**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>ITULAR:<br>P|ROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|ROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|ROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|ROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**Extracción de áridos - Pozo Coyanco**<br>ROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>ROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>ROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>ROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>ROYECTO:|**Extracción de áridos - Pozo Coyanco**<br>ROYECTO:|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|**SECCIONES TRANSVERSALES**<br><br><br>ONTENIDO:|**SECCIONES TRANSVERSALES**<br><br><br>ONTENIDO:|**SECCIONES TRANSVERSALES**<br><br><br>ONTENIDO:|**SECCIONES TRANSVERSALES**<br><br><br>ONTENIDO:|**SECCIONES TRANSVERSALES**<br><br><br>ONTENIDO:|**SECCIONES TRANSVERSALES**<br><br><br>ONTENIDO:|
|**SECCIONES TRANSVERSALES**<br>**Extracción de áridos - Pozo Coyanco**<br>FECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>REVISIÓN:<br>**0**<br>CÓDIGO:<br>FORMATO:<br>**A1**<br>LÁMINA:<br>CONTENIDO:<br>PROYECTO:<br>REV<br>FECHA<br>EMITIDO PARA<br>EJECUTÓ<br>REVISÓ<br>APROBÓ<br>**CTRT-2021**<br>**5 DE 5**<br>**0**<br>**08-02-2021**<br>**L.M.**<br>**I.P.**<br>**Áridos Cantarruta Ltda**<br>**77.070.170-8**<br>TITULAR:<br>PROYECTISTA:<br>**Luis Alberto Muñoz Vasquez**<br>**Ingeniero Civil, U. del Biobío**<br>**17.041.810-7**<br>**I.P.**<br>SIMBOLOGIA<br>PERFILES TRANSVERSALES<br>ESCALA HORIZONTAL 1:4000<br>ESCALA VERTICAL 1:400<br>**INGRESO SEA**|ECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>C<br>FO<br>ÁMINA:<br>**5 DE 5**|ECHA:<br>**08-02-2021**<br>ESCALA Y UNIDADES:<br>**INDICADAS/[m]**<br>C<br>FO<br>ÁMINA:<br>**5 DE 5**|REVISIÓN:<br>**0**<br>ÓDIGO:<br>RMATO:<br>**A1**<br>**CTRT-2021**|REVISIÓN:<br>**0**<br>ÓDIGO:<br>RMATO:<br>**A1**<br>**CTRT-2021**|REVISIÓN:<br>**0**<br>ÓDIGO:<br>RMATO:<br>**A1**<br>**CTRT-2021**|REVISIÓN:<br>**0**<br>ÓDIGO:<br>RMATO:<br>**A1**<br>**CTRT-2021**|

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Registro fluviométrico estación río Biobío en Rucalhue.****

| Año | Q [m3/s] | Año | Q [m3/s] | Año | Q [m3/s] |
| --- | --- | --- | --- | --- | --- |
| 1969 | 3480 | 1989 | 2267 | 2009 | 657 |
| 1970 | 2128 | 1990 | 2693 | 2010 | 1357 |
| 1971 | 2625 | 1991 | 4179 | 2011 | 1317 |
| 1972 | 6492 | 1992 | 2519 | 2012 | 1013 |
| 1973 | 1906 | 1993 | 4297 | 2013 | 1060 |
| 1974 | 2120 | 1994 | 3362 | 2014 | 1421 |
| 1975 | 2525 | 1995 | 2599 | 2015 | 1514 |
| 1976 | 2643 | 1996 | 1583 | 2016 | 698 |
| 1977 | 1944 | 1997 | 3014 | 2017 | 888 |
| 1978 | 2645 | 1998 | 515 | 2018 | 1695 |
| 1979 | 3589 | 1999 | 1363 | 2019 | 1407 |
| 1980 | 3082 | 2000 | 3260 | 2020 | 1035 |
| 1981 | 3147 | 2001 | 4803 |  |  |
| 1982 | 3263 | 2002 | 3519 | 3519 | 3519 |
| 1983 | 2972 | 2003 | 4442 | 4442 | 4442 |
| 1984 | 2488 | 2004 | 1229 | 1229 | 1229 |
| 1985 | 3362 | 2005 | 1928 | 1928 | 1928 |
| 1986 | 3599 | 2006 | 5589 | 5589 | 5589 |
| 1987 | 2052 | 2007 | 759 | 759 | 759 |
| 1988 | 1510 | 2008 | 1345 | 1345 | 1345 |

**Tabla 2.: Resultado análisis de frecuencia.****

| Col1 | Col2 | Col3 | Col4 | Funciones de distribución acumulada [m3/s] | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **m** | **Q [m3/s]** | **p** | **1-p** | **Normal** | **Log-Normal** | **Pearson** | **Log-Pearson** | **Gumbel Max** |
| 1 | 515 | 0.019 | 0.981 | -253 | 643 | 500 | 559 | 463 |
| 2 | 657 | 0.038 | 0.962 | 136 | 763 | 677 | 696 | 657 |
| 3 | 698 | 0.057 | 0.943 | 387 | 853 | 800 | 799 | 791 |
| 4 | 759 | 0.075 | 0.925 | 578 | 927 | 900 | 886 | 897 |
| 5 | 888 | 0.094 | 0.906 | 736 | 994 | 986 | 963 | 989 |
| 6 | 1013 | 0.113 | 0.887 | 872 | 1055 | 1064 | 1034 | 1070 |
| 7 | 1035 | 0.132 | 0.868 | 993 | 1113 | 1135 | 1100 | 1144 |
| 8 | 1060 | 0.151 | 0.849 | 1102 | 1168 | 1201 | 1163 | 1213 |
| 9 | 1229 | 0.170 | 0.830 | 1202 | 1220 | 1264 | 1223 | 1278 |
| 10 | 1317 | 0.189 | 0.811 | 1296 | 1271 | 1324 | 1281 | 1340 |
| 11 | 1345 | 0.208 | 0.792 | 1384 | 1322 | 1381 | 1338 | 1399 |
| 12 | 1357 | 0.226 | 0.774 | 1467 | 1371 | 1438 | 1394 | 1457 |
| 13 | 1363 | 0.245 | 0.755 | 1547 | 1420 | 1492 | 1449 | 1513 |
| 14 | 1407 | 0.264 | 0.736 | 1623 | 1468 | 1546 | 1503 | 1568 |
| 15 | 1421 | 0.283 | 0.717 | 1696 | 1516 | 1599 | 1557 | 1621 |
| 16 | 1510 | 0.302 | 0.698 | 1768 | 1564 | 1651 | 1610 | 1675 |
| 17 | 1514 | 0.321 | 0.679 | 1837 | 1613 | 1703 | 1664 | 1727 |
| 18 | 1583 | 0.340 | 0.660 | 1904 | 1661 | 1755 | 1717 | 1779 |
| 19 | 1695 | 0.358 | 0.642 | 1970 | 1710 | 1806 | 1771 | 1831 |
| 20 | 1906 | 0.377 | 0.623 | 2035 | 1760 | 1858 | 1824 | 1883 |
| 21 | 1928 | 0.396 | 0.604 | 2099 | 1810 | 1910 | 1879 | 1935 |
| 22 | 1944 | 0.415 | 0.585 | 2162 | 1861 | 1962 | 1933 | 1987 |
| 23 | 2052 | 0.434 | 0.566 | 2225 | 1913 | 2014 | 1989 | 2039 |
| 24 | 2120 | 0.453 | 0.547 | 2287 | 1966 | 2067 | 2045 | 2092 |
| 25 | 2128 | 0.472 | 0.528 | 2348 | 2020 | 2121 | 2102 | 2146 |
| 26 | 2267 | 0.491 | 0.509 | 2410 | 2075 | 2175 | 2160 | 2200 |
| 27 | 2488 | 0.509 | 0.491 | 2471 | 2131 | 2231 | 2219 | 2255 |
| 28 | 2519 | 0.528 | 0.472 | 2532 | 2190 | 2287 | 2279 | 2311 |
| 29 | 2525 | 0.547 | 0.453 | 2594 | 2250 | 2345 | 2341 | 2368 |
| 30 | 2599 | 0.566 | 0.434 | 2656 | 2312 | 2404 | 2404 | 2427 |
| 31 | 2625 | 0.585 | 0.415 | 2718 | 2376 | 2465 | 2469 | 2487 |
| 32 | 2643 | 0.604 | 0.396 | 2782 | 2443 | 2528 | 2537 | 2548 |
| 33 | 2645 | 0.623 | 0.377 | 2845 | 2513 | 2592 | 2606 | 2612 |
| 34 | 2693 | 0.642 | 0.358 | 2910 | 2586 | 2659 | 2678 | 2678 |
| 35 | 2972 | 0.660 | 0.340 | 2976 | 2662 | 2729 | 2753 | 2746 |
| 36 | 3014 | 0.679 | 0.321 | 3044 | 2742 | 2801 | 2830 | 2817 |
| 37 | 3082 | 0.698 | 0.302 | 3113 | 2827 | 2877 | 2912 | 2891 |
| 38 | 3147 | 0.717 | 0.283 | 3184 | 2917 | 2957 | 2997 | 2969 |
| 39 | 3260 | 0.736 | 0.264 | 3258 | 3013 | 3042 | 3088 | 3052 |
| 40 | 3263 | 0.755 | 0.245 | 3334 | 3115 | 3131 | 3183 | 3139 |
| 41 | 3362 | 0.774 | 0.226 | 3414 | 3226 | 3227 | 3285 | 3231 |
| 42 | 3362 | 0.792 | 0.208 | 3497 | 3346 | 3330 | 3394 | 3331 |
| 43 | 3480 | 0.811 | 0.189 | 3585 | 3478 | 3442 | 3512 | 3439 |
| 44 | 3519 | 0.830 | 0.170 | 3678 | 3624 | 3564 | 3640 | 3557 |
| 45 | 3589 | 0.849 | 0.151 | 3779 | 3788 | 3700 | 3782 | 3687 |
| 46 | 3599 | 0.868 | 0.132 | 3888 | 3974 | 3852 | 3940 | 3833 |
| 47 | 4179 | 0.887 | 0.113 | 4009 | 4191 | 4027 | 4120 | 3999 |
| 48 | 4297 | 0.906 | 0.094 | 4145 | 4449 | 4233 | 4329 | 4194 |
| 49 | 4442 | 0.925 | 0.075 | 4302 | 4768 | 4484 | 4580 | 4430 |
| 50 | 4803 | 0.943 | 0.057 | 4494 | 5187 | 4807 | 4898 | 4731 |
| 51 | 5589 | 0.962 | 0.038 | 4745 | 5792 | 5265 | 5335 | 5150 |
| 52 | 6492 | 0.981 | 0.019 | 5134 | 6873 | 6057 | 6058 | 5861 |
|  |  |  | **R2** | **0.9447** | **0.9805** | **0.9904** | **0.9891** | **0.9898** |

**Tabla 3.: Caudales de crecida, estación fluviométrica río Biobío en Rucalhue.****

| T [años] | p | 1-p | Q [m3/s] |
| --- | --- | --- | --- |
| 2 | 0.5 | 0.5 | 2203 |
| 5 | 0.8 | 0.2 | 3374 |
| 10 | 0.9 | 0.1 | 4168 |
| 25 | 0.96 | 0.04 | 5199 |
| 50 | 0.98 | 0.02 | 5990 |
| 100 | 0.99 | 0.01 | 6803 |

**Tabla 5.: Coeficiente de rugosidad de Manning - Método de Cowan.****

| Col1 | cauce principal | planicies de<br>inundación |
| --- | --- | --- |
| n0 | 0.027 | 0.020 |
| n1 | 0.000 | 0.000 |
| n2 | 0.000 | 0.000 |
| n3 | 0.000 | 0.005 |
| n4 | 0.000 | 0.010 |
| m5 | 1.000 | 1.000 |
| n | 0.027 | 0.035 |

**Tabla 6.: Resultados modelo hidráulico - T2.****

| Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400 | Periodo<br>retorno<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2<br>T2 | Q Total<br>[m3/s]<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385<br>3385 | Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35 | Eje<br>hidráulico<br>[m]<br>75.95<br>75.96<br>75.28<br>75.30<br>75.34<br>75.33<br>75.34<br>75.29<br>75.22<br>75.18<br>75.12<br>75.09<br>74.88<br>74.84<br>74.76 | Velocidad<br>[m/s]<br>2.56<br>1.86<br>3.82<br>2.64<br>1.84<br>1.56<br>1.23<br>1.51<br>1.69<br>1.75<br>1.84<br>1.81<br>2.57<br>2.45<br>2.50 | Área mojada<br>[m2]<br>2191.53<br>2238.90<br>1048.85<br>1297.25<br>1835.42<br>2171.01<br>2745.83<br>2244.05<br>2010.30<br>2015.01<br>2004.09<br>2132.04<br>1636.94<br>1949.67<br>1993.07 | Ancho<br>superficial<br>[m]<br>1664.68<br>1689.08<br>612.71<br>632.61<br>609.31<br>569.37<br>543.34<br>511.89<br>571.70<br>843.15<br>952.94<br>935.53<br>1100.77<br>1262.45<br>1185.30 | Froude #<br>Chl<br>0.37<br>0.35<br>0.71<br>0.56<br>0.34<br>0.25<br>0.18<br>0.23<br>0.28<br>0.29<br>0.31<br>0.26<br>0.44<br>0.41<br>0.42 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| km 1+500 | T2 | 3385<br> | 69.99<br> | 74.56<br> | 2.98<br> | 1744.13<br> | 1094.97<br> | 0.50<br> |
| km 1+600<br>km 1+700<br>km 1+800 | T2<br>T2<br>T2 | 3385<br>3385<br>3385<br> | 70.07<br>69.93<br>69.40<br> | 74.53<br>74.48<br>74.55<br> | 2.64<br>2.41<br>1.27<br> | 1999.38<br>2184.12<br>4031.48<br> | 1066.06<br>1070.59<br>1541.82<br> | 0.43<br>0.39<br>0.20<br> |
| km 1+900<br>km 2+000<br>km 2+100 | T2<br>T2<br>T2 | 3385<br>3385<br>3385<br> | 69.42<br>69.41<br>69.30<br> | 74.33<br>73.80<br>73.36<br> | 2.52<br>3.88<br>1.82<br> | 2096.99<br>1385.71<br>2071.22<br> | 1118.24<br>1137.68<br>1181.55<br> | 0.41<br>0.69<br>0.31<br> |
| km 2+200<br>km 2+300 | T2<br>T2 | 3385<br>3385 | 69.51<br>69.11 | 72.76<br>72.89 | 3.70<br>2.27 | 1182.24<br>1800.34 | 960.42<br>1146.05 | 0.72<br>0.42 |
| km 2+400<br>km 2+500 | T2<br>T2 | 3385<br>3385 | 69.18<br>68.64 | 72.74<br>72.51 | 2.45<br>2.73 | 1631.37<br>1498.00 | 1149.88<br>1274.06 | 0.50<br>0.57 |
| km 2+600<br>km 2+700<br>km 2+800 | T2<br>T2<br>T2 | 3385<br>3385<br>3385 | 69.11<br>66.95<br>67.39 | 71.96<br>71.93<br>71.10 | 3.56<br>2.65<br>4.18 | 1027.21<br>1359.78<br>809.81 | 938.14<br>1013.89<br>346.88 | 0.82<br>0.54<br>0.87 |
| km 2+900 | T2 | 3385<br> | 66.82<br> | 71.33<br> | 2.59<br> | 1308.23<br> | 335.09<br> | 0.42<br> |
| km 3+000 | T2 | 3385 | 66.24 | 71.02 | 3.22 | 1052.05 | 274.29 | 0.52 |
| km 3+100<br>km 3+200 | T2<br>T2 | 3385<br>3385 | 66.21<br>65.85 | 70.40<br>69.82 | 4.27<br>4.75 | 792.46<br>712.72 | 253.34<br>246.60 | 0.77<br>0.89 |

**Tabla 7.: Resultados modelo hidráulico - T5.****

| Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400 | Periodo<br>retorno<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5<br>T5 | Q Total<br>[m3/s]<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184<br>5184 | Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35 | Eje<br>hidráulico<br>[m]<br>76.61<br>76.61<br>76.08<br>75.98<br>76.01<br>76.00<br>76.02<br>75.92<br>75.84<br>75.78<br>75.72<br>75.66<br>75.46<br>75.43<br>75.34 | Velocidad<br>[m/s]<br>2.80<br>2.05<br>3.80<br>3.04<br>2.29<br>2.02<br>1.66<br>2.01<br>2.20<br>2.24<br>2.33<br>2.38<br>3.03<br>2.81<br>2.88 | Área mojada<br>[m2]<br>3368.94<br>3394.21<br>2159.59<br>1797.58<br>2264.88<br>2619.30<br>3121.89<br>2601.00<br>2384.03<br>2624.70<br>2620.03<br>2767.29<br>2358.73<br>2701.52<br>2686.39 | Ancho<br>superficial<br>[m]<br>1874.67<br>1909.46<br>1700.22<br>807.86<br>705.60<br>815.06<br>573.13<br>608.63<br>640.20<br>1135.51<br>1121.39<br>1284.49<br>1293.93<br>1273.64<br>1195.01 | Froude #<br>Chl<br>0.38<br>0.35<br>0.64<br>0.57<br>0.39<br>0.31<br>0.22<br>0.29<br>0.35<br>0.34<br>0.36<br>0.32<br>0.48<br>0.44<br>0.45 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| km 1+500 | T5 | 5184<br> | 69.99<br> | 75.13<br> | 3.39<br> | 2370.39<br> | 1105.48<br> | 0.53<br> |
| km 1+600<br>km 1+700<br>km 1+800 | T5<br>T5<br>T5 | 5184<br>5184<br>5184<br> | 70.07<br>69.93<br>69.40<br> | 75.08<br>75.02<br>75.11<br> | 3.09<br>2.88<br>1.58<br> | 2590.43<br>2762.77<br>4900.59<br> | 1076.62<br>1080.87<br>1557.53<br> | 0.48<br>0.44<br>0.24<br> |
| km 1+900<br>km 2+000<br>km 2+100 | T5<br>T5<br>T5 | 5184<br>5184<br>5184<br> | 69.42<br>69.41<br>69.30<br> | 74.82<br>74.21<br>73.92<br> | 3.05<br>4.51<br>2.27<br> | 2645.84<br>1860.66<br>2735.96<br> | 1130.17<br>1146.14<br>1198.76<br> | 0.47<br>0.76<br>0.36<br> |
| km 2+200<br>km 2+300 | T5<br>T5 | 5184<br>5184 | 69.51<br>69.11 | 73.32<br>73.40 | 4.12<br>2.76 | 1844.80<br>2433.55 | 1312.15<br>1318.06 | 0.73<br>0.47 |
| km 2+400<br>km 2+500 | T5<br>T5 | 5184<br>5184 | 69.18<br>68.64 | 73.24<br>73.06 | 2.88<br>3.02 | 2249.34<br>2225.70 | 1313.45<br>1332.43 | 0.54<br>0.56 |
| km 2+600<br>km 2+700<br>km 2+800 | T5<br>T5<br>T5 | 5184<br>5184<br>5184 | 69.11<br>66.95<br>67.39 | 72.85<br>72.78<br>72.68 | 3.16<br>2.70<br>2.89 | 2131.79<br>2387.79<br>2530.08 | 1327.60<br>1291.13<br>1258.88 | 0.60<br>0.47<br>0.47 |
| km 2+900 | T5 | 5184<br> | 66.82<br> | 72.67<br> | 2.44<br> | 2911.53<br> | 1191.39<br> | 0.34<br> |
| km 3+000 | T5 | 5184 | 66.24 | 72.46 | 2.99 | 2452.38 | 1176.88 | 0.42 |
| km 3+100<br>km 3+200 | T5<br>T5 | 5184<br>5184 | 66.21<br>65.85 | 71.39<br>70.69 | 4.94<br>5.55 | 1049.32<br>933.67 | 264.01<br>255.40 | 0.79<br>0.93 |

**Tabla 8.: Resultados modelo hidráulico - T10.****

| Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400 | Periodo<br>retorno<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10<br>T10 | Q Total<br>[m3/s]<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404<br>6404 | Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35 | Eje<br>hidráulico<br>[m]<br>76.91<br>76.90<br>76.52<br>76.44<br>76.41<br>76.39<br>76.41<br>76.28<br>76.17<br>76.12<br>76.04<br>75.98<br>75.80<br>75.77<br>75.68 | Velocidad<br>[m/s]<br>2.99<br>2.22<br>3.62<br>2.91<br>2.47<br>2.25<br>1.88<br>2.29<br>2.50<br>2.51<br>2.61<br>2.67<br>3.22<br>3.00<br>3.10 | Área mojada<br>[m2]<br>3938.72<br>3958.58<br>2921.11<br>2789.95<br>2892.30<br>3187.02<br>3797.85<br>3087.28<br>2602.38<br>3020.71<br>3012.17<br>3190.93<br>2805.52<br>3140.40<br>3087.29 | Ancho<br>superficial<br>[m]<br>1926.29<br>2016.61<br>1765.77<br>1604.89<br>1476.15<br>1463.72<br>1447.40<br>1427.11<br>674.87<br>1265.67<br>1286.02<br>1331.91<br>1300.78<br>1278.48<br>1200.59 | Froude #<br>Chl<br>0.40<br>0.37<br>0.58<br>0.51<br>0.40<br>0.33<br>0.24<br>0.32<br>0.38<br>0.37<br>0.39<br>0.35<br>0.49<br>0.45<br>0.46 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| km 1+500 | T10 | 6404<br> | 69.99<br> | 75.45<br> | 3.62<br> | 2729.65<br> | 1111.61<br> | 0.54<br> |
| km 1+600<br>km 1+700<br>km 1+800 | T10<br>T10<br>T10 | 6404<br>6404<br>6404<br> | 70.07<br>69.93<br>69.40<br> | 75.39<br>75.33<br>75.44<br> | 3.35<br>3.15<br>1.76<br> | 2929.71<br>3095.11<br>5404.32<br> | 1082.64<br>1086.73<br>1566.56<br> | 0.50<br>0.47<br>0.25<br> |
| km 1+900<br>km 2+000<br>km 2+100 | T10<br>T10<br>T10 | 6404<br>6404<br>6404<br> | 69.42<br>69.41<br>69.30<br> | 75.09<br>74.45<br>74.21<br> | 3.35<br>4.86<br>2.53<br> | 2958.82<br>2131.72<br>3086.10<br> | 1136.91<br>1150.94<br>1208.40<br> | 0.50<br>0.79<br>0.39<br> |
| km 2+200<br>km 2+300 | T10<br>T10 | 6404<br>6404 | 69.51<br>69.11 | 73.86<br>73.88 | 3.76<br>2.77 | 2569.94<br>3073.66 | 1345.30<br>1335.18 | 0.61<br>0.44 |
| km 2+400<br>km 2+500 | T10<br>T10 | 6404<br>6404 | 69.18<br>68.64 | 73.78<br>73.69 | 2.77<br>2.75 | 2964.11<br>3061.86 | 1326.75<br>1336.69 | 0.47<br>0.47 |
| km 2+600<br>km 2+700<br>km 2+800 | T10<br>T10<br>T10 | 6404<br>6404<br>6404 | 69.11<br>66.95<br>67.39 | 73.60<br>73.55<br>73.49 | 2.70<br>2.43<br>2.55 | 3129.00<br>3375.42<br>3557.80 | 1338.74<br>1292.27<br>1259.32 | 0.46<br>0.38<br>0.38 |
| km 2+900 | T10 | 6404<br> | 66.82<br> | 73.46<br> | 2.33<br> | 3893.75<br> | 1232.45<br> | 0.30<br> |
| km 3+000 | T10 | 6404 | 66.24 | 73.35 | 2.70 | 3497.55 | 1177.67 | 0.35 |
| km 3+100<br>km 3+200 | T10<br>T10 | 6404<br>6404 | 66.21<br>65.85 | 71.99<br>71.22 | 5.29<br>5.99 | 1210.28<br>1068.38 | 270.65<br>260.25 | 0.80<br>0.94 |

**Tabla 9.: Resultados modelo hidráulico - T25.****

| Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400 | Periodo<br>retorno<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25<br>T25 | Q Total<br>[m3/s]<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989<br>7989 | Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35 | Eje<br>hidráulico<br>[m]<br>77.33<br>77.33<br>77.01<br>76.93<br>76.87<br>76.84<br>76.86<br>76.71<br>76.55<br>76.51<br>76.44<br>76.36<br>76.21<br>76.18<br>76.07 | Velocidad<br>[m/s]<br>3.08<br>2.28<br>3.58<br>2.95<br>2.63<br>2.47<br>2.12<br>2.56<br>2.87<br>2.79<br>2.88<br>2.97<br>3.43<br>3.20<br>3.33 | Área mojada<br>[m2]<br>4769.43<br>5074.15<br>3809.22<br>3587.47<br>3582.93<br>3853.92<br>4456.96<br>3706.92<br>2866.71<br>3556.87<br>3542.09<br>3697.63<br>3335.24<br>3657.30<br>3558.55 | Ancho<br>superficial<br>[m]<br>1954.44<br>2483.01<br>1937.98<br>1713.88<br>1490.94<br>1469.91<br>1468.62<br>1445.54<br>753.94<br>1399.32<br>1369.26<br>1339.45<br>1308.85<br>1284.16<br>1207.12 | Froude #<br>Chl<br>0.40<br>0.36<br>0.54<br>0.48<br>0.40<br>0.34<br>0.27<br>0.34<br>0.42<br>0.39<br>0.41<br>0.38<br>0.50<br>0.46<br>0.48 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| km 1+500 | T25 | 7989<br> | 69.99<br> | 75.83<br> | 3.88<br> | 3151.25<br> | 1118.77<br> | 0.56<br> |
| km 1+600<br>km 1+700<br>km 1+800 | T25<br>T25<br>T25 | 7989<br>7989<br>7989<br> | 70.07<br>69.93<br>69.40<br> | 75.76<br>75.69<br>75.82<br> | 3.65<br>3.45<br>1.96<br> | 3328.79<br>3486.29<br>6000.36<br> | 1089.68<br>1093.59<br>1577.18<br> | 0.52<br>0.49<br>0.27<br> |
| km 1+900<br>km 2+000<br>km 2+100 | T25<br>T25<br>T25 | 7989<br>7989<br>7989<br> | 69.42<br>69.41<br>69.30<br> | 75.41<br>74.71<br>74.69<br> | 3.68<br>5.28<br>2.72<br> | 3327.55<br>2432.93<br>3659.92<br> | 1144.81<br>1156.25<br>1224.04<br> | 0.53<br>0.83<br>0.40<br> |
| km 2+200<br>km 2+300 | T25<br>T25 | 7989<br>7989 | 69.51<br>69.11 | 74.49<br>74.48 | 3.51<br>2.77 | 3426.24<br>3880.67 | 1371.09<br>1356.47 | 0.53<br>0.41 |
| km 2+400<br>km 2+500 | T25<br>T25 | 7989<br>7989 | 69.18<br>68.64 | 74.41<br>74.35 | 2.71<br>2.66 | 3799.89<br>3940.05 | 1342.67<br>1341.63 | 0.43<br>0.41 |
| km 2+600<br>km 2+700<br>km 2+800 | T25<br>T25<br>T25 | 7989<br>7989<br>7989 | 69.11<br>66.95<br>67.39 | 74.28<br>74.24<br>74.20 | 2.59<br>2.41<br>2.50 | 4046.83<br>4266.89<br>4558.93 | 1348.91<br>1293.30<br>1360.16 | 0.40<br>0.35<br>0.34 |
| km 2+900 | T25 | 7989<br> | 66.82<br> | 74.16<br> | 2.38<br> | 4755.40<br> | 1232.59<br> | 0.30<br> |
| km 3+000 | T25 | 7989 | 66.24 | 74.07 | 2.72 | 4342.70 | 1178.31 | 0.33 |
| km 3+100<br>km 3+200 | T25<br>T25 | 7989<br>7989 | 66.21<br>65.85 | 73.96<br>71.83 | 2.99<br>6.49 | 4005.81<br>1230.30 | 1172.49<br>265.95 | 0.38<br>0.96 |

**Tabla 10.: Resultados modelo hidráulico - T50.****

| Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400 | Periodo<br>retorno<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50<br>T50 | Q Total<br>[m3/s]<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205<br>9205 | Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35 | Eje<br>hidráulico<br>[m]<br>77.63<br>77.64<br>77.32<br>77.24<br>77.17<br>77.13<br>77.14<br>76.99<br>76.84<br>76.79<br>76.72<br>76.63<br>76.49<br>76.46<br>76.34 | Velocidad<br>[m/s]<br>3.15<br>2.30<br>3.68<br>3.00<br>2.76<br>2.63<br>2.29<br>2.74<br>3.00<br>2.97<br>3.04<br>3.17<br>3.57<br>3.35<br>3.50 | Área mojada<br>[m2]<br>5362.82<br>5838.66<br>4485.95<br>4135.85<br>4027.24<br>4280.68<br>4879.20<br>4103.60<br>3580.60<br>3953.93<br>3928.93<br>4057.24<br>3707.90<br>4019.63<br>3890.46 | Ancho<br>superficial<br>[m]<br>1999.18<br>2483.01<br>2343.82<br>1811.55<br>1500.38<br>1473.86<br>1475.96<br>1457.22<br>1442.16<br>1474.18<br>1376.15<br>1344.78<br>1314.49<br>1288.13<br>1211.69 | Froude #<br>Chl<br>0.40<br>0.35<br>0.53<br>0.47<br>0.41<br>0.35<br>0.28<br>0.36<br>0.42<br>0.41<br>0.42<br>0.40<br>0.50<br>0.47<br>0.49 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| km 1+500 | T50 | 9205<br> | 69.99<br> | 76.09<br> | 4.07<br> | 3447.05<br> | 1123.76<br> | 0.57<br> |
| km 1+600<br>km 1+700<br>km 1+800 | T50<br>T50<br>T50 | 9205<br>9205<br>9205<br> | 70.07<br>69.93<br>69.40<br> | 76.02<br>75.94<br>76.08<br> | 3.85<br>3.66<br>2.10<br> | 3609.13<br>3762.01<br>6422.82<br> | 1094.60<br>1098.40<br>1584.67<br> | 0.54<br>0.51<br>0.29<br> |
| km 1+900<br>km 2+000<br>km 2+100 | T50<br>T50<br>T50 | 9205<br>9205<br>9205<br> | 69.42<br>69.41<br>69.30<br> | 75.64<br>74.89<br>74.77<br> | 3.92<br>5.56<br>3.05<br> | 3586.89<br>2647.19<br>3763.59<br> | 1150.33<br>1160.02<br>1226.84<br> | 0.55<br>0.86<br>0.44<br> |
| km 2+200<br>km 2+300 | T50<br>T50 | 9205<br>9205 | 69.51<br>69.11 | 74.49<br>74.48 | 4.04<br>3.19 | 3426.75<br>3873.49 | 1371.10<br>1356.28 | 0.61<br>0.47 |
| km 2+400<br>km 2+500 | T50<br>T50 | 9205<br>9205 | 69.18<br>68.64 | 74.37<br>74.28 | 3.16<br>3.14 | 3749.21<br>3845.17 | 1340.38<br>1340.67 | 0.50<br>0.49 |
| km 2+600<br>km 2+700<br>km 2+800 | T50<br>T50<br>T50 | 9205<br>9205<br>9205 | 69.11<br>66.95<br>67.39 | 74.18<br>74.11<br>74.04 | 3.10<br>2.89<br>3.03 | 3904.06<br>4097.98<br>4347.49 | 1347.34<br>1293.11<br>1360.16 | 0.49<br>0.43<br>0.42 |
| km 2+900 | T50 | 9205<br> | 66.82<br> | 73.99<br> | 2.88<br> | 4541.93<br> | 1232.55<br> | 0.36<br> |
| km 3+000 | T50 | 9205 | 66.24 | 73.82 | 3.37 | 4051.02 | 1178.09 | 0.42 |
| km 3+100<br>km 3+200 | T50<br>T50 | 9205<br>9205 | 66.21<br>65.85 | 73.58<br>72.79 | 3.87<br>5.18 | 3563.52<br>2529.52 | 1171.51<br>1131.38 | 0.50<br>0.70 |

**Tabla 11.: Resultados modelo hidráulico - T100.****

| Sección<br>km 0+000<br>km 0+100<br>km 0+200<br>km 0+300<br>km 0+400<br>km 0+500<br>km 0+600<br>km 0+700<br>km 0+800<br>km 0+900<br>km 1+000<br>km 1+100<br>km 1+200<br>km 1+300<br>km 1+400 | Periodo<br>retorno<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100<br>T100 | Q Total<br>[m3/s]<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454<br>10454 | Cota de<br>fondo<br>[m]<br>69.60<br>71.05<br>71.27<br>70.59<br>70.17<br>69.37<br>67.53<br>68.97<br>70.04<br>69.88<br>69.50<br>68.12<br>69.58<br>69.94<br>70.35 | Eje<br>hidráulico<br>[m]<br>77.90<br>77.91<br>77.64<br>77.55<br>77.47<br>77.42<br>77.43<br>77.26<br>77.11<br>77.07<br>76.99<br>76.89<br>76.77<br>76.73<br>76.61 | Velocidad<br>[m/s]<br>3.23<br>2.35<br>3.57<br>3.03<br>2.86<br>2.77<br>2.44<br>2.91<br>3.16<br>3.12<br>3.18<br>3.36<br>3.69<br>3.49<br>3.65 | Área mojada<br>[m2]<br>5898.12<br>6508.48<br>5282.98<br>4705.20<br>4473.35<br>4709.91<br>5303.38<br>4509.83<br>3978.68<br>4369.37<br>4305.92<br>4408.56<br>4069.19<br>4370.38<br>4211.93 | Ancho<br>superficial<br>[m]<br>2018.24<br>2483.01<br>2479.96<br>1860.96<br>1519.69<br>1501.84<br>1483.30<br>1472.59<br>1489.06<br>1567.79<br>1386.12<br>1349.96<br>1319.94<br>1291.96<br>1216.11 | Froude #<br>Chl<br>0.40<br>0.34<br>0.50<br>0.46<br>0.41<br>0.36<br>0.29<br>0.37<br>0.43<br>0.42<br>0.43<br>0.41<br>0.51<br>0.48<br>0.50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| km 1+500 | T100 | 10454<br> | 69.99<br> | 76.35<br> | 4.24<br> | 3733.34<br> | 1128.57<br> | 0.58<br> |
| km 1+600<br>km 1+700<br>km 1+800 | T100<br>T100<br>T100 | 10454<br>10454<br>10454<br> | 70.07<br>69.93<br>69.40<br> | 76.26<br>76.18<br>76.34<br> | 4.04<br>3.86<br>2.25<br> | 3880.84<br>4029.81<br>6834.38<br> | 1099.34<br>1103.05<br>1610.32<br> | 0.55<br>0.52<br>0.30<br> |
| km 1+900<br>km 2+000<br>km 2+100 | T100<br>T100<br>T100 | 10454<br>10454<br>10454<br> | 69.42<br>69.41<br>69.30<br> | 75.86<br>75.07<br>75.02<br> | 4.14<br>5.83<br>3.22<br> | 3837.50<br>2854.45<br>4067.23<br> | 1155.64<br>1163.65<br>1235.02<br> | 0.57<br>0.88<br>0.46<br> |
| km 2+200<br>km 2+300 | T100<br>T100 | 10454<br>10454 | 69.51<br>69.11 | 74.79<br>74.76 | 4.09<br>3.31 | 3828.13<br>4256.50 | 1379.84<br>1366.27 | 0.60<br>0.48 |
| km 2+400<br>km 2+500 | T100<br>T100 | 10454<br>10454 | 69.18<br>68.64 | 74.66<br>74.56 | 3.25<br>3.23 | 4133.86<br>4233.40 | 1359.98<br>1348.28 | 0.50<br>0.49 |
| km 2+600<br>km 2+700<br>km 2+800 | T100<br>T100<br>T100 | 10454<br>10454<br>10454 | 69.11<br>66.95<br>67.39 | 74.47<br>74.40<br>74.34 | 3.19<br>3.00<br>3.14 | 4299.41<br>4473.88<br>4745.77 | 1351.70<br>1293.54<br>1360.16 | 0.48<br>0.43<br>0.42 |
| km 2+900 | T100 | 10454<br> | 66.82<br> | 74.28<br> | 3.03<br> | 4893.06<br> | 1232.61<br> | 0.37<br> |
| km 3+000 | T100 | 10454 | 66.24 | 74.09 | 3.54 | 4376.72 | 1178.33 | 0.43 |
| km 3+100<br>km 3+200 | T100<br>T100 | 10454<br>10454 | 66.21<br>65.85 | 73.85<br>73.03 | 4.03<br>5.39 | 3884.42<br>2810.44 | 1172.22<br>1132.35 | 0.51<br>0.71 |
