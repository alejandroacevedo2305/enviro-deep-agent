---
title: Sin título
author: OITEC-3
date: D:20240813182416-04'00'
language: es
type: report
pages: 34
has_toc: False
has_tables: True
extraction_quality: high
---

|PROYECTO:|INCREMENTO DE LA AUTONOMÍA PARA ASEGURAR<br>LA DISPONIBILIDAD DE COMBUSTIBLES, PLANTA<br>MEJILLONES|
|---|---|
|**MATERIA:**|**ESTUDIO DE INUNDACIONES**|
|**CLIENTE:**|**DAES**|
|**CÓDIGO:**|**2338-2310.139**|

|Rev.|Fecha|Realizado|Revisado|Aprobado|Descripción|
|---|---|---|---|---|---|
|A|19-01-24|CFR|AGL|AGL|Para revisión|
|B|13-05-24|CFR|FHG|AGL|Para revisión|
|C|09-07-24|FHG|AGL|AGL|Apto para tramitación|
|D|29-07-24|CFR|AGL|AGL|Apto para tramitación|
|0|13-08-24|||AGL|Apto para tramitación|
|||||||

|Rev.|Fecha|Revisión/aprobación cliente|Descripción|
|---|---|---|---|
|A|10-05-24|Revisión|Minuta de Observaciones|
|B|02-07-24|Revisión|Observación vía email|
|C|24-07-24|Revisión|Observaciones en reunión|
|D|13-08-24|Aprobación|Generar versión 0|
|||||

Página ii

**ÍNDICE**

1 INTRODUCCIÓN .......................................................................................................... 4

2 ZONA DE ESTUDIO ..................................................................................................... 5

3 TOPOGRAFÍA................................................................................................................ 6

4 ANÁLISIS HIDROLÓGICO .......................................................................................... 8

4.1 Análisis de Frecuencia ............................................................................................ 9

4.2 Análisis del Área Aportante de Caudal ................................................................ 12

4.3 Coeficiente de Escorrentía .................................................................................... 17

4.4 Tiempo de Concentración ..................................................................................... 18

4.4.1 Manual de Carreteras de España ...................................................................... 18

4.4.2 California Culverts Practice (1942) .................................................................. 18

4.4.3 V. T. Chow ....................................................................................................... 19

4.4.4 Ecuación de Manning ....................................................................................... 19

4.5 Intensidad de Precipitación ................................................................................... 20

4.6 Estimación de Caudal ........................................................................................... 22

4.6.1 Método Racional .............................................................................................. 22

4.6.2 Método DGA-AC ............................................................................................. 23

4.6.3 Método Verni-King Modificado ....................................................................... 23

4.6.4 Escorrentía generada dentro del polígono de modelación ................................ 24

4.7 Caudal Detrítico .................................................................................................... 24

5 ANÁLISIS HIDRÁULICO ........................................................................................... 26

5.1 Condiciones de Contorno ..................................................................................... 26

5.2 Modelo de Elevación Digital ................................................................................ 27

5.3 Malla de Cálculo ................................................................................................... 28

5.4 Coeficiente de Rugosidad ..................................................................................... 29

5.5 Parámetros de Modelación ................................................................................... 29

5.6 Resultados Modelación Hidráulica ....................................................................... 29

5.6.1 Caso 1: Escenario flujos puntuales ................................................................... 29

5.6.2 Caso 2: Escenario flujo distribuido .................................................................. 30

5.6.3 Caso 3: Escenario flujos puntuales tiempo de concentración California ......... 31

6 CONCLUSIONES ........................................................................................................ 33

Página iii

7 REFERENCIAS ............................................................................................................ 34



**1** **INTRODUCCIÓN**

El presente informe se da en el contexto del estudio hidrológico del proyecto “Incremento de
la autonomía para asegurar la disponibilidad de combustibles, planta Mejillones”, ubicado al
noroeste de la ciudad de Mejillones, en la comuna de Mejillones, provincia de Antofagasta,
región de Antofagasta. La Figura 1-1 presenta la ubicación del proyecto.

Figura 1-1. Mapa ubicación del proyecto.

El objetivo del presente análisis es determinar el área de inundación en la zona de estudio
donde se emplazarán las instalaciones del proyecto.

Se realizó un estudio hidrológico para determinar los caudales de crecida en los cauces que
se encuentran en el sector del proyecto. Los caudales se estimaron a partir de métodos
indirectos, para posteriormente efectuar un análisis hidráulico y caracterizar el escurrimiento,
evaluando la influencia en la zona en estudio para un caudal de crecida con periodo de retorno

de 100 años.



**2** **ZONA DE ESTUDIO**

La zona de estudio se ubica referencialmente en las coordenadas UTM (m) N: 7.446.604 y
E: 357.825, Datum WGS84, Huso 19 sur, al noroeste de la ciudad de Mejillones, en la
comuna de Mejillones, provincia de Antofagasta. La Figura 2-1 presenta el área de estudio
del proyecto.

Figura 2-1. Área de estudio del proyecto.

El proyecto consiste en incrementar la capacidad de almacenamiento de combustibles de la
Planta Mejillones mediante la construcción y operación de cinco nuevos estanques de 32.500
m [3] de capacidad máxima cada uno.

En las cercanías del sector donde se emplazará el proyecto se reconocen dos quebradas
intermitentes sin nombre, relativamente paralelas entre sí, que para fines de este informe se
identifican como “quebrada izquierda” y “quebrada derecha”. Estas quebradas se encuentran
altamente alteradas, estando rellenas de material en algunos tramos.



**3** **TOPOGRAFÍA**

La topografía se desarrolló mediante un levantamiento aerofotogramétrico utilizando un dron
marca DJI, modelo Mavic 3 Enterprise, el cual cuenta con GPS geodésico para levantamiento

RTK.

Figura 3-1: Levantamiento aerofotográfico en sector del proyecto.

Figura 3-2. Dron Mavic 3 Enterprise.

El levantamiento fue vinculado al punto SIRGAS BN02 de Bienes Nacionales, en
Antofagasta, considerando 2 PRs en terreno. En la Figura 3-3 se muestra uno de los PRs
vinculados. Las coordenadas de cada PR se presentan en la Tabla 3-1.



Figura 3-3. PR existente.

Tabla 3-1. Coordenadas PRs Construidos, UTM WGS84 Huso 19 sur.

|Punto|Este (m)|Norte (m)|Cota (m)|
|---|---|---|---|
|PR O1|358281.38|7446596.87|51.76|
|PR O2|357829.15|7446317.91|46.81|

Los detalles de la información topográfica levantada se encuentran en Anexo 01 Topografía.



**4** **ANÁLISIS HIDROLÓGICO**

La zona de estudio no posee estaciones fluviométricas (de caudal) dentro de su cuenca, por
lo tanto, la estimación de caudales de diferentes periodos de retorno se realizó en base a
métodos indirectos de precipitación escorrentía.

Para el análisis de precipitaciones se identificaron cinco estaciones meteorológicas cercanas
a la zona de estudio (Figura 4-1), analizadas según su clasificación climática de KöppenGeiger, altitud y periodo de registro para cada una (Tabla 4-1). De las cinco estaciones, se
opta por considerar la estación meteorológica Antofagasta (Código BNA 02710003-1) para
desarrollar el estudio hidrológico ya que se encuentra en una zona limítrofe entre los climas
BWh y BWk y además posee un registro de datos de 44 años, por lo que se puede realizar un
análisis de precipitaciones consistente. Las demás están en un sector climático diferente o
tienen registros pluviométricos cortos.

Figura 4-1. Ubicación de estaciones meteorológicas cercanas al proyecto y Clasificación

Climática Köppen-Geiger.



Tabla 4-1.Estaciones meteorológicas analizadas.

|Estación|Distancia<br>(km)|Clima<br>Köppen-<br>Geiger|Altitud<br>(msnm)|Período de<br>registro<br>(Años)|
|---|---|---|---|---|
|LCHLC|52.2|BWk|45|9|
|Quebrada<br>la Chimba|52.6|BWh|37|8|
|Quebrada<br>Bonilla|55.3|BWk|100|8|
|Antofagasta|56.9|BWk|48|44|
|Baquedano|62.7|BWk|1038|49|

**4.1** **Análisis de Frecuencia**

Para el análisis de frecuencia se utilizaron los datos de precipitaciones máximas anuales de
duración 24 horas obtenidas de la estación meteorológica Antofagasta, la cual ha registrado
valores diarios de precipitación desde 1978. Los valores se presentan en la Tabla 4-2.

Tabla 4-2. Precipitaciones Máximas Anuales Estación Antofagasta.

|Año|Fecha|PP (mm)<br>24|Año|Fecha|PP (mm)<br>24|
|---|---|---|---|---|---|
|1978|01/01|0.00|2000|31/05|1.80|
|1979|26/03|0.50|2001|01/01|0.00|
|1980|27/10|0.40|2002|27/08|3.80|
|1981|05/08|0.70|2003|01/01|0.00|
|1982|27/08|3.50|2004|26/07|0.10|
|1983|13/01|6.00|2005|25/04|0.40|
|1984|07/06|2.00|2006|29/08|11.50|
|1985|01/01|0.00|2007|01/01|0.00|
|1986|18/05|1.00|2008|01/01|0.00|
|1987|28/07|13.20|2009|20/07|1.60|
|1988|01/01|0.00|2010|01/01|0.00|
|1989|20/08|0.50|2011|08/07|6.10|
|1990|01/01|0.00|2012|01/01|0.00|
|1991|17/06|17.00|2013|01/01|0.00|
|1992|28/05|3.00|2014|12/09|1.40|
|1993|01/01|0.00|2015|24/03|31.50|
|1994|20/07|0.80|2016|24/06|6.70|
|1995|20/05|1.00|2017|06/06|20.50|
|1996|15/04|0.50|2018|01/01|0.00|
|1997|01/01|0.00|2019|07/05|0.10|
|1998|01/01|0.00|2020|17/10|0.20|
|1999|01/01|0.00|2021|16/08|0.20|



Es posible observar en la Tabla 4-2 que en ciertos años no precipita, por lo cual el análisis de
frecuencia se realizó según las recomendaciones señaladas en Stöwhas (2016) para zonas
áridas o semiáridas, dado que estos valores nulos distorsionan la verdadera distribución de la
variable. Por lo tanto, se diferenciaron los años con precipitación de aquellos sin precipitación
y se trabajó con el subconjunto de años con valores no nulos, estimando probabilidades
condicionadas de que haya llovido, las cuales se multiplican por la probabilidad de que exista
lluvia para obtener probabilidades absolutas.

La probabilidad de un año con lluvia se estima según la siguiente expresión:

P (LL) = [N] [LL]

N T

Donde :

P (LL) : Probabilidad de que llueva

N LL : Número de años con valores no nulos

N T : Número de años totales de la serie

La probabilidad de excedencia se estima según la siguiente expresión:

1
P EXC = ∙
T P (LL)

Donde :

P EXC : Probabilidad de excedencia para años con lluvia
T : Periodo de retorno del evento (años)

Por lo tanto, el periodo de retorno condicional se estima según la siguiente expresión:

1
T ['] =
P EXC

Donde :
T ['] : Periodo de retorno condicional (años)

La serie de datos presente en la cuenta con información de 44 años en total, de los cuales 16
años presentan valores nulos de precipitación y 28 años presentan valores no nulos; por lo
tanto, la probabilidad de que llueva es del 64%. En la Tabla 4-3 se presentan los periodos de
retorno para años con lluvia.



Tabla 4-3. Periodos de retorno del evento y condicional para la estación Antofagasta.

|T (años)|P<br>EX|T' (años)|
|---|---|---|
|2|0.79|1.27|
|5|0.31|3.18|
|10|0.16|6.36|
|25|0.06|15.91|
|50|0.03|31.82|
|100|0.02|63.64|
|150|0.01|95.45|
|200|0.01|127.27|

Ya definidos los periodos de retorno y series de datos de ambas estaciones, se realizaron los
análisis de frecuencia con el software Hydrognomon en su versión 4.1.0. Se estudiaron
distintas funciones de distribución de probabilidades utilizadas comúnmente en hidrología, a
las cuales se les aplicó el test de bondad de ajuste Kolmogorov-Smirnov considerando un
nivel de confianza del 95%. Los resultados se presentan a continuación en la Tabla 4-4.

Tabla 4-4. Test de bondad de ajuste Kolmogorov-Smirnov.

|Kolmogorov-Smirnov|=5%|Ajuste|DMax|
|---|---|---|---|
|Log Pearson III|Acepta|98.90%|0.075|
|Weibull|Acepta|91.45%|0.097|
|Gamma|Acepta|75.75%|0.118|
|GEV-Max|Acepta|69.44%|0.125|
|GEV-Min|Acepta|59.12%|0.137|

Según se observa, la función de densidad de probabilidades que mejor se ajusta a los datos
de la estación Antofagasta es la distribución Log Pearson III, lo cual se puede observar de
manera gráfica en la Figura 4-2.



Figura 4-2. Gráfico probabilidad de excedencia v/s precipitación de la estación

Antofagasta.

De esta manera se estimaron las precipitaciones máximas de duración 24 horas asociadas a
distintas probabilidades de excedencia según la función de distribución Log Pearson III para
la estación Antofagasta, valores que se presentan en la Tabla 4-5.

Tabla 4-5. Precipitaciones asociadas a los distintos periodos de retorno.

|T (años)|Antofagasta PP (mm)<br>24|
|---|---|
|2|0.44|
|5|3.50|
|10|8.14|
|25|19.01|
|50|32.31|
|100|51.71|
|150|66.64|
|200|79.15|

**4.2** **Análisis del Área Aportante de Caudal**

Dado a que la zona del proyecto presenta superficies de terreno relativamente planas, sin
huellas marcadas de cauces desde las faldas de cerro hasta el mar, la definición y delimitación
de cuenca aportante a la zona de estudio se realizó de manera diferente a lo tradicional. En
particular, lo normal es definir un punto al cual drene una cuenca, pero en el caso de este
estudio, debido a lo plano del terreno (Figura 4-3), se consideró una línea como final de



cuenca, esto debido a la inexistencia de evidencias o vestigios del punto hacía donde drenan
las aguas provenientes desde aguas arriba de la zona estudiada. Con eso, se busca obtener
una envolvente de todas las cuencas que drenen a la línea definida como borde del dominio
de modelación y, consecuentemente, capturar toda el agua que drene a este dominio,
considerando de esta forma el escenario más desfavorable desde el punto de vista de la
posibilidad de escurrimiento de aguas. Particularmente, se consideró la arista sur del polígono
de modelación donde se encuentran las dos quebradas intermitentes (borde entre polígono
azul y verde en Figura 4-4).

Figura 4-3. Imagen del sector al cual se aplicó la modelación.

La delimitación de la cuenca aportante a la línea del dominio de modelación se realizó a partir
de las curvas de nivel generadas del Modelo de Elevación Digital ALOS Palsar, de resolución
12.5 metros por píxel, suministrado por JAXA ( _[Japan Aerospace Exploration Agency](http://global.jaxa.jp/)_ ),
utilizando los métodos estándar descritos por Reyes et al. (2014).

El estudio hidrológico del área aportante permite estimar caudales máximos de crecida a
partir de datos de precipitaciones obtenidos de la estación meteorológica y relaciones
precipitación-escorrentía. Esta área se delimitó en función de las quebradas y la topografía
observadas de imágenes satelitales y relieve de la zona. La Tabla 4-6 presenta las
características morfológicas principales del área aportante, tales como la superficie (A),
longitud del cauce principal (L), desnivel máximo (H) y medio (Hm), y pendiente media (S).



Figura 4-4. Área a aportante a la arista sur del polígono de modelación.

Tabla 4-6. Características morfológicas del área aportante de caudal.

|Parámetro|Símbolo|Valor|
|---|---|---|
|Área (km2)|A|9.2|
|Longitud de Cauce (km)|L|9.0|
|Desnivel Máximo (m)|H|536|
|Desnivel Medio (m)|Hm|63|
|Pendiente Media|S|0.11|

Por otro lado, en el sector poniente de las dos quebradas intermitentes analizadas se encuentra
la quebrada Mejillones, la cual posee una cuenca de gran tamaño. En la Figura 4-5 se presenta
la cuenca asociada a la quebrada Mejillones y la cuenca que drena hacia el sector del

proyecto.



Figura 4-5. Cuenca Mejillones y cuenca que drena hacía la zona del proyecto.

Por su parte, en la Figura 4-6 se presentan las curvas de nivel en la zona de estudio, las cuales
fueron generadas mediante el software Qgis a partir de Modelo de Elevación Digital ALOS
Palsar ( _[Japan Aerospace Exploration Agency](http://global.jaxa.jp/)_ ) Las curvas de nivel dan cuenta que la
dirección de escurrimiento en la zona del proyecto es de sur-oriente a nor-poniente, por lo
cual, las aguas provenientes de la cuenca de la quebrada Mejillones drenan en esta dirección,
alejándose del sector donde se proyectan los estanques nuevos. Consecuentemente, la
quebrada Mejillones no interactúa con las obras del proyecto y no forma parte del análisis
hidrológico-hidráulico.



Figura 4-6. Curvas de nivel y red de drenaje en zona de estudio.



**4.3** **Coeficiente de Escorrentía**

El coeficiente de escorrentía del área aportante se estimó según especifica el Manual de
Carreteras Volumen N°3 (MOP, 2022), considerando factores de relieve, infiltración,

cobertura vegetal y capacidad de almacenar agua, que se describen en la Tabla 4-7.

Tabla 4-7. Coeficientes de escorrentía según factor.

|Factor|Extremo|Alto|Normal|Bajo|
|---|---|---|---|---|
|**Relieve**|0.28-0.35<br>Escarpado con<br>pendientes<br>mayores que 30%|0.20-0.28<br>Montañoso con<br>pendientes entre<br>10 y 30%|0.14-0.20<br>Con cerros y<br>pendientes entre 5<br>y 10%|0.08-0.14<br>Relativamente<br>plano con<br>pendientes<br>menores al 5%|
|**Infiltración**|0.12-0.16<br>Suelo rocoso, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable|0.08-0.12<br>Suelos arcillosos<br>o limosos con<br>baja capacidad de<br>infiltración, mal<br>drenados|0.06-0.08<br>Normales, bien<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos|0.04-0.06<br>Suelos profundos<br>de arena u otros<br>suelos bien<br>drenados con alta<br>capacidad de<br>infiltración|
|**Cobertura**<br>**vegetal**|0.12-0.16<br>Cobertura escasa,<br>terreno sin<br>vegetación o<br>escasa cobertura|0.08-0.12<br>Poca vegetación,<br>terrenos<br>cultivados o<br>naturales, menos<br>del 20% del área<br>con buena<br>cobertura vegetal|0.06-0.08<br>Regular a buena,<br>50% del área con<br>praderas o<br>bosques, no más<br>del 50% cultivado|0.04-0.06<br>Buena a<br>excelente, 90%<br>del área con<br>praderas, bosques<br>o cobertura<br>equivalente|
|**Almacenamiento**<br>**superficial**|0.10-0.12<br>Despreciable,<br>pocas depresiones<br>superficiales, sin<br>zonas húmedas|0.08-0.10<br>Baja, sistema de<br>cauces<br>superficiales<br>pequeños bien<br>definidos, sin<br>zonas húmedas|0.06-0.08<br>Normal,<br>posibilidad de<br>almacenamiento<br>buena, zonas<br>húmedas,<br>pantanos, lagunas<br>y lagos|0.04-0.06<br>Capacidad alta,<br>sistema<br>hidrográfico poco<br>definido, buenas<br>planicies de<br>inundación o gran<br>cantidad de zonas<br>húmedas, lagunas<br>o pantanos.|

La tabla anterior muestra los coeficientes asociados a cada variable, y la suma de estos
factores entrega el valor del coeficiente de escorrentía del área aportante asociado a un
periodo de retorno de 10 años. El caudal de crecida se estima para un periodo de retorno de
100 años, por lo tanto, según indica el Manual de Carreteras el valor obtenido debe
amplificarse por 1.25 calculando así el coeficiente de escorrentía asociado a un periodo de
retorno de 100 años. Los coeficientes estimados se presentan en la Tabla 4-8.



Tabla 4-8. Coeficientes de escorrentía adoptados.

|Coeficiente de escorrentía|Col2|
|---|---|
|**Factor**|**Factor**|
|Relieve|0.21|
|Infiltración|0.06|
|Cobertura vegetal|0.16|
|Almacenamiento superficial|0.1|
|Suma (C para T=10)|0.53|
|Coeficiente de escorrentía T=100|0.66|

**4.4** **Tiempo de Concentración**
Existen diferentes formas de estimar el tiempo de concentración de cuencas y, para el
presente caso de estudio, se proponen cuatro métodos.

**4.4.1** **Manual de Carreteras de España**
Uno de los métodos corresponde a la ecuación propuesta por el Manual de Carreteras de
España, la cual es válida para cuencas o áreas aportantes con superficies menores a 3000
km [2] . La expresión definida es la siguiente:

[∙] [L] [0.76]
T c = [18]

S [0.19]

Donde :

T c : Tiempo de concentración (min)
L : Longitud del cauce principal (km)
S : Pendiente (m/m)

**4.4.2** **California Culverts Practice (1942)**
Otro método corresponde a la ecuación para cuencas o áreas aportantes de montaña
California Culverts Practice, la cual es válida para cuencas con superficies mayores a 2 km [2] .
La expresión definida es la siguiente:

T c = 57 ∙ H
~~(~~ [L] [3]

0.385

H [)]

Donde :

T c : Tiempo de concentración (min)
L : Longitud del cauce (km)
H : Diferencia de nivel total entre cotas extremas de la cuenca o área aportante (m)



**4.4.3** **V. T. Chow**
El método propuesto por V. T. Chow para cuencas menores a 3000 km [2] corresponde a:

T c = 0.1602 ∙
~~(~~ √S [L]

0.64

~~)~~

Donde:

L : Longitud del cauce (km)
S : Pendiente (m/m)

**4.4.4** **Ecuación de Manning**
Una forma para evaluar los métodos de estimación de tiempos de concentración, además de
las restricciones propias de cada método, es estimar las velocidades medias del agua que se
alcanzarían en la cuenca con dichos tiempos, y contrastarlos con un análisis hidráulico con
la ecuación de Manning.

V = [1] [∙][ R] [2/3] [∙][ S] [1/2]

n

Donde :

V : Velocidad (m/s)

n : Coeficiente de Manning
R : Radio hidráulico (A/P: m, que para flujos anchos, puede asimilarse a la profundidad)

S : (m/m)

En efecto, la razón entre la longitud y el tiempo de concentración entregan una “velocidad”,
que debe ser coherente con los procesos físicos que ocurran. En particular, para la zona de la
cuenca aportante, con una longitud de 9 km, una pendiente media de 0.11 m/m, un coeficiente
de Manning de 0.025 y una profundidad de escurrimiento de 10 cm se tiene una velocidad
estimada de 0.7 m/s; mientras que con una profundidad de 15 cm se alcanzarían velocidades
de 1.2 m/s. Por otro lado, en el caso de que el coeficiente de Manning fuera mayor, se tendrían
velocidades menores, por lo que este enfoque de Manning sería conservador, entregando las
velocidades máximas esperables para la cuenca aportante. Cabe indicar que los valores de
profundidad considerados en este análisis están en el rango de las profundidades modeladas
en sectores donde no hay huellas de cauce marcadas, según se presenta en el acápite 5.6.

En la Tabla 4-9 se presentan los tiempos de concentración estimados según cada método para
el área aportante, y se incluye la estimación de velocidad de flujo como elemento
comparativo.

Si bien existen otras ecuaciones ampliamente utilizadas, como la de Giandotti o Kirpich, en
el presente estudio se incluyeron las ecuaciones que cumplen con sus restricciones propias,

de modo de considerar de manera más adecuada condiciones naturales del área de estudio.

En consecuencia, y en virtud de lo presentado precedentemente, se considera el tiempo de



concentración estimado con las normas españolas como el más adecuado para la situación en
análisis, por cuanto se ajusta de mejor forma a la realidad del área de estudio en cuanto a una
eventual profundidad de escurrimiento y velocidad, lo que redunda en los tiempos de
concentración. Sin perjuicio de lo anterior y a modo de realizar un análisis de sensibilidad,
se ha realizado una modelación, calculando el caudal de crecida utilizando el tiempo de
concentración más desfavorable para el proyecto, es decir, con el menor tiempo estimado
según las expresiones validadas para la cuenca (expresión de California Culverts Practice).

Tabla 4-9. Tiempos de concentración estimados.

|Método|tc (h)|Condición|Velocidad (m/s)|
|---|---|---|---|
|**Normas Españolas**|**2.42**|**Cumple**|**1.03**|
|California|1.07|Cumple|2.34|
|V.T. Chow|1.33|Cumple|1.89|

**4.5** **Intensidad de Precipitación**

La intensidad de precipitación está determinada por la precipitación, de duración igual al
tiempo de concentración del área aportante (Tabla 4-9) con la siguiente ecuación:

i tT c =

P tT c

t c

T

T = [CD∗P] [24]

i t c

t c

Donde:
i tT c : Intensidad de la precipitación para tiempo de concentración _tc_ y período de retorno T.

P tT c : Precipitación para tiempo de concentración _tc_ y período de retorno T.

_CD_ : Coeficiente de duración.

Los coeficientes de duración se obtuvieron del Manual de Drenaje Urbano: Capítulo IV
(2013), correspondientes a la ciudad de Antofagasta. Para duraciones menores a 1 hora (y
mayores a 5 minutos) se estiman a partir de la ecuación de Bell (1959).

A los coeficientes tabulados en el Manual de Drenaje Urbano (Tabla 4-10) se calculó su línea
de tendencia (Figura 4-7 y Figura 4-8) para determinar valores para las duraciones de interés.



Tabla 4-10. Coeficientes de duración

|d (min)|d (h)|CD|d (min)|d (h)|CD|
|---|---|---|---|---|---|
|5|0.08|0.060|240|4.00|0.412|
|10|0.17|0.093|360|6.00|0.503|
|15|0.25|0.117|480|8.00|0.582|
|20|0.33|0.132|600|10.00|0.643|
|30|0.50|0.163|720|12.00|0.718|
|40|0.67|0.175|840|14.00|0.763|
|50|0.83|0.194|1080|18.00|0.882|
|60|1.00|0.206|1440|24.00|1.000|
|120|2.00|0.291|-|-|-|

Figura 4-7. Línea de tendencia Coeficientes de duración 1 a 24 horas.

Figura 4-8. Línea de tendencia Coeficientes de duración menores a una hora.



Efectuando un ajuste polinómico, la función de mejor ajuste entre duración, d, y coeficiente
de duración, CD, está dada por:

Entre 1 y 24 horas:

CD= 6 ∙10 [−5] d [3] −0.0033 d [2] + 0.0782 d+ 0.1461

Menores a una hora:

CD= 0.2365 d [3] −0.5376 d [2] + 0.4835 d+ 0.0244

Según el tiempo de concentración obtenido en el capítulo 4.4 se obtiene el coeficiente de
duración para el área aportante en estudio.

La intensidad de precipitación asociada a una precipitación con un periodo de retorno de 100
años y de duración igual al tiempo de concentración se presenta en la Tabla 4-11.

Tabla 4-11. Intensidad de precipitación T 100 años para el área aportante en estudio.

|CD<br>tc|P 100 (mm)<br>24|tc (h)|I100 (mm/h)|
|---|---|---|---|
|0.318|51.71|2.42|6.79|

**4.6** **Estimación de Caudal**

Para la estimación del caudal de crecida máximo proveniente desde aguas arriba del polígono
de modelación a modelar existen diferentes métodos. Debido a la ubicación y tamaño del
área aportante solo es aplicable el Método Racional, pero de manera comparativa se han
determinado los caudales mediante el método DGA-AC y Verni-King modificado.

Además, se incluyó la escorrentía generada en el polígono de modelación debido a una
precipitación con periodo de retorno de 100 años.

**4.6.1** **Método Racional**

Es un método ampliamente conocido en hidrología, se recomienda su uso sobre la base del
empleo de coeficientes de escorrentía que mejor se ajusten a los resultados de los análisis de
frecuencia efectuados en el estudio. El caudal instantáneo máximo de periodo de retorno T
años, se determina según la siguiente expresión:

[∙] [i] [∙] [A]
Q = [C]

3.6



Donde :
Q : Caudal instantáneo máximo de periodo de retorno T años (m [3] /s)

C : Coeficiente de escorrentía

i : Intensidad de lluvia de duración igual al tiempo de concentración y período de
retorno T años (mm/hr)
A : Área pluvial aportante (km [2] )

**4.6.2** **Método DGA-AC**
Es un método presentado en el Manual de Crecidas (DGA, 1995) de aplicación fácil y directa
para cuencas o áreas aportantes de áreas comprendidas entre 20 y 10000 km [2] y ubicadas entre
la III y IX región del país. Se debe determinar en primer lugar la curva de frecuencias de
caudal medio diario regional según la zona homogénea, luego la curva de frecuencias del
caudal medio diario máximo de la cuenca y por último en caudal instantáneo máximo de la
cuenca. Se asumió que el área de estudio se encuentra en la zona homogénea Dp y el caudal
medio diario máximo de periodo de retorno 10 años para cuencas de la III a IV región se
determina según la siguiente expresión:

3.108

Q 10 = 1.94 ∙ 10 [-7] ∙ Ap [0.776] ∙ (P 1024 )

Donde :
Q 10 : Caudal medio diario máximo de periodo de retorno 10 años (m [3] /s)
Ap : Área pluvial de la cuenca o área aportante (km [2] )
P 24 [10] : Precipitación diaria máxima de periodo de retorno 10 años (mm)

**4.6.3** **Método Verni-King Modificado**
Es un método también presentado en el Manual de Crecidas (DGA, 1995), basado en la
fórmula de Verni y King que relaciona el caudal instantáneo máximo con la precipitación
diaria máxima y el área del área aportante. Es válido para áreas aportantes comprendidas
entre 20 y 10000 km [2] y ubicadas entre la III y IX región del país. El caudal instantáneo
máximo para diferentes periodos de retorno se determina según la siguiente expresión:

Q 10 = 1.94 ∙ 10 [-7] ∙ Ap [0.776] ∙ (P 1024

10

24 )

Q = C ∙ 0.00618 ∙ (P 24 ) [1.24] ∙ Ap [0.88]

Donde :
Q : Caudal instantáneo máximo asociado a periodo de retorno T años (m [3] /s)
C : Coeficiente empírico de periodo de retorno T años
P 24 : Precipitación diaria máxima asociada a periodo de retorno T años (mm)
Ap : Área pluvial de la cuenca o área aportante (km [2] )

En la Tabla 4-12 se presentan los caudales máximos de crecida de periodo de retorno 100
años estimados según cada método para el área aportante en estudio.



Tabla 4-12. Cuadro resumen de caudales estimados (m [3] /s).

|Método|Caudal|
|---|---|
|**Racional**|**12.34**|
|DGA-AC|0.003|
|Verni-King Modificado|0.22|

El área aportante cuenta con superficie menor a 20 km [2] y según expresa la Guía de
Presentación de Proyectos de Modificación de Cauces (DGA, 2016), en cuencas sin
información fluviométrica y de áreas menores a 20 km [2], como es el caso, se acepta el Método
Racional, por lo cual, el caudal de crecida adoptado corresponde al estimado con dicho

método.

**4.6.4** **Escorrentía generada dentro del polígono de modelación**
Sobre el polígono de modelación se añadió la condición de lluvia para el periodo de retorno
analizado, para lo cual se incorporó un hietograma de intensidad de lluvia constante. El valor
de intensidad fue amplificado por el factor de escorrentía del período de retorno de 100 años
a fin de incorporar las perdidas contempladas en el método Racional. El valor de intensidad
de precipitación añadida al hietograma de la modelación y el caudal de crecida se presenta

en la Tabla 4-13

Tabla 4-13. Cuadro resumen de caudal de crecida e intensidad de precipitación asociada a

un periodo de retorno de 100 años.

**4.7** **Caudal Detrítico**

|Q (m3/s)|12.34|
|---|---|
|i·C (mm/hr)|1.49|

Una metodología basada en estudios realizados en los Alpes Suizos (Zimmerman et al., 1997)
y expuesta en la Guía de Presentación de Proyectos de Modificación de Cauces (DGA, 2016),
establece una relación entre la pendiente crítica que desencadena flujos detríticos y el área
de la cuenca o área aportante, la cual se presenta a continuación:

S c = 0.32 ∙ A [-0.2]

Donde :

S c : Pendiente crítica (m/m)
A : Área drenada de la cuenca o área aportante (km [2] )

Tomando en consideración los parámetros morfométricos del área aportante presentados en
la Tabla 4-6 se tiene que la pendiente critica para el área aportante en estudio es de 0.49 m/m.
Por lo tanto, como la pendiente media de la cuenca aportante es 0.11, que es menor que la



pendiente critica, se concluiría que no hay riesgo de que se desencadene un flujo con caudal

detrítico considerando el criterio de Zimmerman.

No obstante, considerando conservadoramente que si existiera suficiente material suelto,
posible de ser arrastrado por un flujo, podría haber un flujo detrítico en las quebradas de
estudio. Para determinar dicho caudal, se amplificó el caudal líquido, para el mismo periodo
de retorno, con la siguiente ecuación:

Q d = Q o ∙P

Donde:
Q d : Caudal detrítico, m [3] /s.
Q o : Caudal líquido, m [3] /s.
P: Factor de amplificación flujo líquido-detrítico.

El factor de amplificación a utilizar se obtuvo del estudio CONIC-BF Ltda. (2018). Este
factor se calibró a partir de un evento real de flujo detrítico de la Quebrada Cerrillos ubicada
en la región de Atacama. Se analizó el evento mediante tres métodos, los cuales son: Método
de Yablonskiy, Método de la Oficina de Planificación Municipal de Pekín y Método de
Takahashi, dando como resultado un factor ponderado de amplificación _P_ =1.49, que es
equivalente a una concentración de sedimentos de aproximadamente 33%.

Según lo anterior, se aplicó el factor ponderado de amplificación al caudal determinado
mediante el método Racional (Tabla 4-12) resultando en 18.38 m [3] /s, el cual será el caudal de

crecida de diseño utilizado en la modelación hidráulica.



**5** **ANÁLISIS HIDRÁULICO**

A partir del caudal de crecida ya definido en el capítulo 4, se efectúa un análisis hidráulico,
con el fin de conocer el comportamiento de la crecida asociada al periodo de retorno de 100
años con flujo detrítico. El análisis consiste en la construcción de modelos hidráulicos
bidimensionales mediante el software Iber en su versión 3.3.1, el cual corresponde a un
modelo hidrodinámico bidimensional, característica relevante dado el comportamiento del
flujo en la zona de estudio la cual cuenta con amplias planicies de inundación. Dicho modelo
simula flujos en ríos y estuarios, permitiendo así simular la hidrodinámica fluvial, rotura de
presas, transporte de sedimento, evaluación de inundaciones, entre otras. Cuenta con distintos
módulos de cálculo acoplados entre sí, entre los cuales se encuentra el módulo
hidrodinámico, el módulo de transporte sólido no estacionario, el módulo de turbulencia y el
módulo de calidad de aguas. Iber resuelve las ecuaciones de cada módulo sobre mallas

bidimensionales no estructuradas, utilizando el método de volúmenes finitos, las cuales

pueden ser mixtas formadas por elementos triangulares y/o cuadrangulares. Particularmente,
el módulo a utilizar en este estudio corresponde al módulo hidrodinámico, el cual resuelve
las ecuaciones de Saint Venant 2D promediadas en profundidad.

El software Iber considera los siguientes aspectos para su implementación, los cuales son

descritos más adelante:

 - Condiciones de contorno

 - Modelo de elevación digital

 - Malla de cálculo

 - Coeficientes de rugosidad

 - Parámetros de modelación

**5.1** **Condiciones de Contorno**

El caudal de crecida asignado corresponde al de periodo de retorno de 100 años. También, el
modelo considera precipitación, la cual fue asignada a través de un hietograma. El caudal de
crecida corresponde a un caudal de flujo detrítico de 18.38 m [3] /s y la intensidad de
precipitación de diseño a 1.49 mm/hr.

Para ingresar los caudales al dominio de modelación se consideraron dos escenarios: En el
primer escenario, más conservador, se ingresó el caudal detrítico distribuido de manera
equitativa al inicio de las quebradas en el polígono de modelación, es decir, un caudal de 9.19
m [3] /s a cada una. En el segundo escenario se ingresó el caudal total a lo largo de la arista sur



del polígono de modelación, permitiendo que el modelo lo distribuyera según la topografía

del sector.

Cabe destacar que el caudal fue modelado como flujo estacionario, lo cual corresponde a la
condición más desfavorable, debido a que las quebradas intermitentes en la zona de estudio
solamente presentan escurrimiento cuando ocurren eventos de precipitación, los cuales
generan un hidrograma en forma de campana, con un peak puntual en el tiempo y no
estacionario, por lo que se esperaría un menor volumen de agua escurriendo y
consecuentemente menores profundidades de escurrimiento.

Así como se definieron puntos de entrada, también se definieron las salidas de caudal, las
cuales corresponden a las aristas restantes del polígono de modelación, bajo condición de
flujo supercrítico/crítico.

**5.2** **Modelo de Elevación Digital**

El modelo de elevación digital utilizado en la modelación hidráulica tiene una resolución de
1x1 m y fue generado a partir del levantamiento aerofotogramétrico, descrito en el capítulo
3. En la Figura 5-1 se puede apreciar la representación de la superficie.

Figura 5-1. Representación tridimensional de la superficie. El color gris indica la zona del

levantamiento aerofotogramétrico.



**5.3** **Malla de Cálculo**

Para seleccionar un tamaño de malla adecuado se buscó una combinación equilibrada entre
calidad de resultados y tiempos de cálculos.

La malla generada cuenta con elementos de tamaño de 3x3 m. Mediante la estructuración
asignada se consiguió una malla conformada por 450 mil elementos aproximadamente, en la
Figura 5-2 se presenta la malla descrita.

Figura 5-2. Malla utilizada en el modelo hidráulico.



**5.4** **Coeficiente de Rugosidad**

Se determinó el coeficiente de rugosidad de Manning para los cauces reconocidos y sus
planicies de inundación según lo expuesto en el Manual de Carreteras: Volumen III (Tabla
3.707.104.A).

Para los cauces identificados, estos se clasificarán como cursos menores (ancho superficial
menor a 30 metros), correspondientes a cursos limpios, rectos, a capacidad plena sin vados o
charcas profundas, por ende, se les asignara un coeficiente de rugosidad _**n**_ =0.025. Las
planicies de inundación corresponden principalmente a arena sin la presencia de rocas o
bolones, por lo tanto, de igual manera se le asigna un coeficiente de rugosidad _**n**_ =0.025.

**5.5** **Parámetros de Modelación**

Las modelaciones hidráulicas bidimensionales con el software Iber se realizaron bajo los
siguientes parámetros para todos los casos:

Tabla 5-1. Parámetros de modelación.

|Parámetro|Descripción|
|---|---|
|Tiempo máximo simulación (s)|84600|
|Esquema numérico|1er Orden|
|CFL (máximo)|0.45|
|Δtmax (s)|1|
|Límite seco-mojado (m)|0.01|

**5.6** **Resultados Modelación Hidráulica**

A continuación, se presentan los resultados de los modelos hidráulicos ejecutados para el

caudal de crecida, considerando ambos escenarios de modelación.

**5.6.1** **Caso 1: Escenario flujos puntuales**
En la Figura 5-3 se presenta las profundidades de escurrimiento para el primer escenario,
donde ambas quebradas presentan en sus ejes de cauce los caudales detríticos de diseño. La
profundidad máxima alcanza los 7.01 m en la quebrada izquierda en la intersección con la
ruta B-262. Se puede observar también que las mayores profundidades se dan dentro del
cauce de las dos quebradas, y fuera de éstas se da un escurrimiento de altura menor a 0.10 m.
Cabe indicar que las profundidades máximas observadas ocurren justo en la intersección de
los cauces con las rutas debido a que no existen obras de atravieso que permitan el paso de
las aguas bajo ellas.

Se puede observar que, para este caso, el escurrimiento de la crecida en ambas quebradas no
alcanza los límites de la zona del proyecto.



Figura 5-3. Profundidades obtenidas para el caudal de crecida T igual 100 años (caso flujos

puntuales).

**5.6.2** **Caso 2: Escenario flujo distribuido**
En la Figura 5-4 se presenta las profundidades de escurrimiento para el segundo escenario,
donde el caudal detrítico de diseño se distribuye a lo largo de la arista sur del modelo. La
profundidad máxima alcanza los mismos 7.01 m en la quebrada izquierda, en la intersección
de esta con la ruta B-262. Se puede observar también que las mayores profundidades se dan
dentro del cauce de la quebrada izquierda, fuera de ésta se da un escurrimiento con altura
despreciable y que el flujo se da preferentemente dentro de esta quebrada. La quebrada
derecha solo presenta escurrimiento al final de su desarrollo, provocado por el trasvasije de
agua desde la quebrada izquierda.

Se puede observar que, para este caso, el escurrimiento de la crecida en las quebradas
tampoco alcanza los límites de la zona del proyecto.



Figura 5-4. Profundidades obtenidas para el caudal de crecida T igual 100 años (caso flujo

distribuido).

**5.6.3** **Caso 3: Escenario flujos puntuales tiempo de concentración California**

Con el fin de considerar la situación más desfavorable en cuanto a tiempos de concentración,
se incorporó en la evaluación la estimación con el método de California. Con este enfoque
se obtuvo un tiempo de concentración de 1.07 horas, que tiene asociado una intensidad de
precipitación 10.93 mm/h, y una caudal detrítico de 29.66 m [3] /s. Cabe destacar que este valor
es 61% mayor que el caudal estimado con las normas españolas.

En la siguiente figura se presenta las profundidades de escurrimiento para este escenario, con
flujo estacionario. En este caso, tal como en los anteriores, se observa que los flujos no
alcanzan el área de ejecución del proyecto.



Figura 5-5: Profundidades obtenidas para el caudal de crecida T igual 100 años (caso flujos

puntuales y tiempo de concentración de California).



**6** **CONCLUSIONES**

A una distancia superior a 500 metros del área de emplazamiento de las obras del Proyecto
“Incremento de la autonomía para asegurar la disponibilidad de combustibles, planta
Mejillones” se identifican cauces naturales que corresponden a dos quebradas intermitentes

sin nombre.

El tiempo de concentración para la cuenca se estimó en 2.42 horas según la ecuación de la
norma española, y en 1.07 horas según la ecuación de California. De éstas, la ecuación de las
normas españolas es más consistente con la realidad del área de estudio y en base a este
análisis se desarrolló la memoria hidrológica e hidráulica. El caudal detrítico de crecida
asociado a un periodo de retorno de retorno de 100 años se estimó en 18.38 m [3] /s en la zona

de estudio, considerando una concentración de sedimentos de 33%.

La modelación hidráulica consideró dos escenarios: El primero corresponde a un escenario
en el cual se considera que el caudal de crecida se distribuye equitativamente al inicio de
cada quebrada intermitente. El segundo corresponde a un escenario en el cual el caudal de
crecida se ingresa a lo largo de la arista sur del polígono de modelación y éste se distribuye
según la topografía.

Los resultados obtenidos indican que el escurrimiento de la crecida con flujo detrítico con
período de retorno 100 años, no interactúa con el área del Proyecto, en ninguno de los dos

escenarios evaluados.

Complementariamente, se realizó un análisis adicional, que consideró estimar
precipitaciones y caudales a partir del tiempo de concentración estimado con la ecuación de
California. Con este análisis, se estimaron caudales detríticos de 29.66 m [3] /s y la modelación
hidráulica correspondiente muestra que el flujo tampoco alcanzaría el área en que se
emplazarán las obras del Proyecto.

Por lo tanto, con los análisis complementarios presentados, se puede corroborar y concluir
que los flujos que pudiesen generarse en la cuenca no interactúan con el área de ejecución
del Proyecto.

Alex García L.

Ingeniero Civil, M.Sc.

Dr. en Ciencias Ambientales



**7** **REFERENCIAS**

Ministerio de Obras Públicas (1995). Dirección General de Aguas: Manual de Cálculo de
Crecidas y Caudales Mínimos en Cuencas Sin Información Fluviométrica. S.E.B. N°4

Ministerio de Obras Públicas (2013). Dirección de Obras Hidráulicas: Manual de Drenaje
Urbano, Capítulo 4.

Ministerio de Obras Públicas (2016). Dirección General de Aguas: Guías metodológicas para
presentación y revisión técnica de proyectos de modificación de cauces naturales y

artificiales.

Ministerio de Obras Públicas (2022). Manual de Carreteras, Volumen 3.

Reyes A., Barroso F. & Carvajal Y. (2014). Guía básica para la caracterización morfométrica
de cuencas hidrográficas. Universidad del Valle, Colombia.

Stöwhas L. (2016). Fundamentos de Hidrología Aplicada.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Coordenadas PRs Construidos, UTM WGS84 Huso 19 sur.**

| Punto | Este (m) | Norte (m) | Cota (m) |
| --- | --- | --- | --- |
| PR O1 | 358281.38 | 7446596.87 | 51.76 |
| PR O2 | 357829.15 | 7446317.91 | 46.81 |

**Tabla 4-1.: Estaciones meteorológicas analizadas.**

| Estación | Distancia<br>(km) | Clima<br>Köppen-<br>Geiger | Altitud<br>(msnm) | Período de<br>registro<br>(Años) |
| --- | --- | --- | --- | --- |
| LCHLC | 52.2 | BWk | 45 | 9 |
| Quebrada<br>la Chimba | 52.6 | BWh | 37 | 8 |
| Quebrada<br>Bonilla | 55.3 | BWk | 100 | 8 |
| Antofagasta | 56.9 | BWk | 48 | 44 |
| Baquedano | 62.7 | BWk | 1038 | 49 |

**Tabla 4-2.: Precipitaciones Máximas Anuales Estación Antofagasta.**

| Año | Fecha | PP (mm)<br>24 | Año | Fecha | PP (mm)<br>24 |
| --- | --- | --- | --- | --- | --- |
| 1978 | 01/01 | 0.00 | 2000 | 31/05 | 1.80 |
| 1979 | 26/03 | 0.50 | 2001 | 01/01 | 0.00 |
| 1980 | 27/10 | 0.40 | 2002 | 27/08 | 3.80 |
| 1981 | 05/08 | 0.70 | 2003 | 01/01 | 0.00 |
| 1982 | 27/08 | 3.50 | 2004 | 26/07 | 0.10 |
| 1983 | 13/01 | 6.00 | 2005 | 25/04 | 0.40 |
| 1984 | 07/06 | 2.00 | 2006 | 29/08 | 11.50 |
| 1985 | 01/01 | 0.00 | 2007 | 01/01 | 0.00 |
| 1986 | 18/05 | 1.00 | 2008 | 01/01 | 0.00 |
| 1987 | 28/07 | 13.20 | 2009 | 20/07 | 1.60 |
| 1988 | 01/01 | 0.00 | 2010 | 01/01 | 0.00 |
| 1989 | 20/08 | 0.50 | 2011 | 08/07 | 6.10 |
| 1990 | 01/01 | 0.00 | 2012 | 01/01 | 0.00 |
| 1991 | 17/06 | 17.00 | 2013 | 01/01 | 0.00 |
| 1992 | 28/05 | 3.00 | 2014 | 12/09 | 1.40 |
| 1993 | 01/01 | 0.00 | 2015 | 24/03 | 31.50 |
| 1994 | 20/07 | 0.80 | 2016 | 24/06 | 6.70 |
| 1995 | 20/05 | 1.00 | 2017 | 06/06 | 20.50 |
| 1996 | 15/04 | 0.50 | 2018 | 01/01 | 0.00 |
| 1997 | 01/01 | 0.00 | 2019 | 07/05 | 0.10 |
| 1998 | 01/01 | 0.00 | 2020 | 17/10 | 0.20 |
| 1999 | 01/01 | 0.00 | 2021 | 16/08 | 0.20 |

**Tabla 4-3.: Periodos de retorno del evento y condicional para la estación Antofagasta.**

| T (años) | P<br>EX | T' (años) |
| --- | --- | --- |
| 2 | 0.79 | 1.27 |
| 5 | 0.31 | 3.18 |
| 10 | 0.16 | 6.36 |
| 25 | 0.06 | 15.91 |
| 50 | 0.03 | 31.82 |
| 100 | 0.02 | 63.64 |
| 150 | 0.01 | 95.45 |
| 200 | 0.01 | 127.27 |

**Tabla 4-4.: Test de bondad de ajuste Kolmogorov-Smirnov.**

| Kolmogorov-Smirnov | =5% | Ajuste | DMax |
| --- | --- | --- | --- |
| Log Pearson III | Acepta | 98.90% | 0.075 |
| Weibull | Acepta | 91.45% | 0.097 |
| Gamma | Acepta | 75.75% | 0.118 |
| GEV-Max | Acepta | 69.44% | 0.125 |
| GEV-Min | Acepta | 59.12% | 0.137 |

**Tabla 4-5.: Precipitaciones asociadas a los distintos periodos de retorno.**

| T (años) | Antofagasta PP (mm)<br>24 |
| --- | --- |
| 2 | 0.44 |
| 5 | 3.50 |
| 10 | 8.14 |
| 25 | 19.01 |
| 50 | 32.31 |
| 100 | 51.71 |
| 150 | 66.64 |
| 200 | 79.15 |

**Tabla 4-6.: Características morfológicas del área aportante de caudal.**

| Parámetro | Símbolo | Valor |
| --- | --- | --- |
| Área (km2) | A | 9.2 |
| Longitud de Cauce (km) | L | 9.0 |
| Desnivel Máximo (m) | H | 536 |
| Desnivel Medio (m) | Hm | 63 |
| Pendiente Media | S | 0.11 |

**Tabla 4-7.: Coeficientes de escorrentía según factor.**

| Factor | Extremo | Alto | Normal | Bajo |
| --- | --- | --- | --- | --- |
| **Relieve** | 0.28-0.35<br>Escarpado con<br>pendientes<br>mayores que 30% | 0.20-0.28<br>Montañoso con<br>pendientes entre<br>10 y 30% | 0.14-0.20<br>Con cerros y<br>pendientes entre 5<br>y 10% | 0.08-0.14<br>Relativamente<br>plano con<br>pendientes<br>menores al 5% |
| **Infiltración** | 0.12-0.16<br>Suelo rocoso, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable | 0.08-0.12<br>Suelos arcillosos<br>o limosos con<br>baja capacidad de<br>infiltración, mal<br>drenados | 0.06-0.08<br>Normales, bien<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos | 0.04-0.06<br>Suelos profundos<br>de arena u otros<br>suelos bien<br>drenados con alta<br>capacidad de<br>infiltración |
| **Cobertura**<br>**vegetal** | 0.12-0.16<br>Cobertura escasa,<br>terreno sin<br>vegetación o<br>escasa cobertura | 0.08-0.12<br>Poca vegetación,<br>terrenos<br>cultivados o<br>naturales, menos<br>del 20% del área<br>con buena<br>cobertura vegetal | 0.06-0.08<br>Regular a buena,<br>50% del área con<br>praderas o<br>bosques, no más<br>del 50% cultivado | 0.04-0.06<br>Buena a<br>excelente, 90%<br>del área con<br>praderas, bosques<br>o cobertura<br>equivalente |
| **Almacenamiento**<br>**superficial** | 0.10-0.12<br>Despreciable,<br>pocas depresiones<br>superficiales, sin<br>zonas húmedas | 0.08-0.10<br>Baja, sistema de<br>cauces<br>superficiales<br>pequeños bien<br>definidos, sin<br>zonas húmedas | 0.06-0.08<br>Normal,<br>posibilidad de<br>almacenamiento<br>buena, zonas<br>húmedas,<br>pantanos, lagunas<br>y lagos | 0.04-0.06<br>Capacidad alta,<br>sistema<br>hidrográfico poco<br>definido, buenas<br>planicies de<br>inundación o gran<br>cantidad de zonas<br>húmedas, lagunas<br>o pantanos. |

**Tabla 4-8.: Coeficientes de escorrentía adoptados.**

| Coeficiente de escorrentía | Col2 |
| --- | --- |
| **Factor** | **Factor** |
| Relieve | 0.21 |
| Infiltración | 0.06 |
| Cobertura vegetal | 0.16 |
| Almacenamiento superficial | 0.1 |
| Suma (C para T=10) | 0.53 |
| Coeficiente de escorrentía T=100 | 0.66 |

**Tabla 4-9.: Tiempos de concentración estimados.**

| Método | tc (h) | Condición | Velocidad (m/s) |
| --- | --- | --- | --- |
| **Normas Españolas** | **2.42** | **Cumple** | **1.03** |
| California | 1.07 | Cumple | 2.34 |
| V.T. Chow | 1.33 | Cumple | 1.89 |

**Tabla 4-10.: Coeficientes de duración**

| d (min) | d (h) | CD | d (min) | d (h) | CD |
| --- | --- | --- | --- | --- | --- |
| 5 | 0.08 | 0.060 | 240 | 4.00 | 0.412 |
| 10 | 0.17 | 0.093 | 360 | 6.00 | 0.503 |
| 15 | 0.25 | 0.117 | 480 | 8.00 | 0.582 |
| 20 | 0.33 | 0.132 | 600 | 10.00 | 0.643 |
| 30 | 0.50 | 0.163 | 720 | 12.00 | 0.718 |
| 40 | 0.67 | 0.175 | 840 | 14.00 | 0.763 |
| 50 | 0.83 | 0.194 | 1080 | 18.00 | 0.882 |
| 60 | 1.00 | 0.206 | 1440 | 24.00 | 1.000 |
| 120 | 2.00 | 0.291 | - | - | - |

**Tabla 4-11.: Intensidad de precipitación T 100 años para el área aportante en estudio.**

| CD<br>tc | P 100 (mm)<br>24 | tc (h) | I100 (mm/h) |
| --- | --- | --- | --- |
| 0.318 | 51.71 | 2.42 | 6.79 |

**Tabla 4-12.: Cuadro resumen de caudales estimados (m [3] /s).**

| Método | Caudal |
| --- | --- |
| **Racional** | **12.34** |
| DGA-AC | 0.003 |
| Verni-King Modificado | 0.22 |

**Tabla 4-13.: Cuadro resumen de caudal de crecida e intensidad de precipitación asociada a**

| Q (m3/s) | 12.34 |
| --- | --- |
| i·C (mm/hr) | 1.49 |

**Tabla 5-1.: Parámetros de modelación.**

| Parámetro | Descripción |
| --- | --- |
| Tiempo máximo simulación (s) | 84600 |
| Esquema numérico | 1er Orden |
| CFL (máximo) | 0.45 |
| Δtmax (s) | 1 |
| Límite seco-mojado (m) | 0.01 |
