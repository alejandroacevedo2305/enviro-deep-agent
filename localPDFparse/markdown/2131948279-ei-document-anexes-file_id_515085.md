---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 53
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Estudio Hidrológico
-->

## Anexo 6

# Estudio Hidrológico

### IFBB

Cerro El Plomo 5630 Oficina 1501

Las Condes, Santiago
(56) 227144000

Marco Polo 8939

Hualpén, Concepción

(56) 412908700

|LAT SAN CARLOS - S/E MULCHÉN<br>MEMORIA DE CÁLCULO HIDRÁULICO<br>ÁREA INUNDACIÓN. ESTEROS Y QUEBRADAS<br>LÍNEA DE TRANSMISIÓN ELÉCTRICA<br>635-16-AMB-00-MC-HI-001|Col2|Col3|
|---|---|---|
|ACOGE COMENTARIOS CLIENTE|02.11.2016|F|
|ACOGE COMENTARIOS CLIENTE|27.10.2016|E|
|ACOGE COMENTARIOS CLIENTE|24.10.2016|D|
|ACOGE COMENTARIOS CLIENTE|20.10.2016|C|
|PARA REVISIÓN CLIENTE|19.10.2016|B|
|PARA REVISIÓN INTERNA|17.10.2016|A|
|**REVISIÓN**|**FECHA REVISIÓN**|**No REVISIÓN**|
||||
|**PREPARÓ**|Oscar Loyola N.|Oscar Loyola N.|
|**REVISÓ**|Ricardo González V.|Ricardo González V.|
|**APROBÓ**|Roberto Lüders R.|Roberto Lüders R.|

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas Línea<br>de Transmisión|**Hoja:** i de i|

**MEMORIA DE CÁLCULO HIDRÁULICO**

**ÁREA INUNDACIÓN ESTEROS Y QUEBRADAS**

**LÍNEA DE TRANSMISIÓN ELÉCTRICA**

ÍNDICE

Pág.

**1.** **INTRODUCCIÓN ...................................................................................... 1**

**2.** **ANTECEDENTES ...................................................................................... 1**
2.1 ANTECEDENTES TOPOGRÁFICOS ..................................................... 1
2.2 ANTECEDENTES BIBLIOGRÁFICOS ................................................... 1
2.3 DESCRIPCIÓN DEL PROYECTO DE TRANSMISIÓN ............................... 2

**3.** **HIDROLOGÍA .......................................................................................... 3**
3.1 SECCIONES DE INTERÉS ................................................................ 3
3.2 CAUDALES MÁXIMOS ..................................................................... 4

**4.** **EJE HIDRÁULICO DE LAS QUEBRADAS .................................................... 5**
4.1 GENERACIÓN MODELOS HIDRÁULICOS EN HEC-RAS .......................... 5

4.2 COEFICIENTE DE RUGOSIDAD ......................................................... 5
4.3 CONDICIONES DE BORDE PARA EL CÁLCULO EN HEC-RAS .................. 6
4.4 RESULTADOS CÁLCULO EJE HIDRÁULICO ......................................... 6

**5.** **ÁREAS DE INUNDACIÓN ....................................................................... 11**

**APÉNDICES**

Apéndice 1 Estudio Hidrológico Esteros Las Diucas, Licura y Quebrada Sin Nombre.

Apéndice 2 Perfiles Transversales Estero Las Diucas

Apéndice 3 Perfiles Transversales Estero Licura

Apéndice 4 Perfiles Transversales Quebrada Sin Nombre

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 1 de 14|

**1.** **INTRODUCCIÓN**

En este documento se presentan los cálculos asociados al eje hidráulico de tres esteros
o quebradas naturales que interceptan el trazado de la línea de alta tensión (LAT)
entre el sur de la localidad de San Carlos de Purén y la subestación eléctrica (S/E)
Mulchén. El trazado de la línea es paralela al este de a la ruta 5 Sur.

La línea de alta tensión se conecta a la subestación Mulchén ubicada a unos 4 km al
norte de la localidad del mismo nombre, en la región del Bío Bío. El trazado que se
aborda en este informe comprende un tramo de 9,26 km de longitud, comprendido
entre las torres de cruce de la Ruta 5 Sur hasta la llegada a la Subestación Mulchén,
un total de 28 torres de alta tensión.

El cálculo del eje hidráulico se realiza por el método del paso estándar utilizando el
programa computacional HEC-RAS. El procedimiento de cálculo está basado en la
solución de la ecuación de energía en una dimensión. La pérdida de energía se evalúa
por medio de la componente friccional utilizando la ecuación de Manning, y la
componente singular de contracción/expansión con un coeficiente multiplicado por el
cambio de altura de velocidad en secciones consecutivas.

El objetivo específico del presente documento es estimar el área de inundación para la
crecida asociada a un período de retorno de 100 años de tres quebradas identificadas,
esto con la finalidad de determinar si la ubicación de las torres de la línea de
transmisión interfiere con el cauce natural de las quebradas.

**2.** **ANTECEDENTES**

Para la elaboración de la presente memoria de cálculo se utilizaron antecedentes
topográficos, bibliografía técnica e informes de estudios anteriores relacionados con el
proyecto en desarrollo.

**2.1** **ANTECEDENTES TOPOGRÁFICOS**

a. Topografía proporcionada por el mandante. Curvas de nivel cada 0,5 m.

**2.2** **ANTECEDENTES BIBLIOGRÁFICOS**

a. “Precipitaciones Máximas en 1, 2 y 3 Días”. Dirección General de Aguas del

Ministerio de Obras Públicas, 1991.

b. “Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin

Información Fluviométrica”. Dirección General de Aguas del Ministerio de Obras
Públicas, 1995.

c. “Hidrología Aplicada”, Ven Te Chow, 2001.

d. “Hidráulica de Canales Abiertos”, Ven Te Chow, 1994.

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 2 de 14|

**2.3** **DESCRIPCIÓN DEL PROYECTO DE TRANSMISIÓN**

La conexión eléctrica al sistema se realiza en la subestación Mulchén, ubicada a unos 4
km al norte de la localidad del mismo nombre. El trazado que se analiza en el presente
informe comprende desde el cruce de las LAT con la Ruta 5 Sur hasta la conexión con
la subestación Mulchén, la longitud del tramo es de 9,26 km y considera la instalación
de 28 torres de alta tensión y un marco de línea en la llegada a la S/E. En el Cuadro
2.1 se presentan las coordenadas UTM de las torres y del marco, y en la Figura 2.1 se
muestra una vista en general del trazado de la línea que se analiza. La numeración de
las torres aumenta en dirección a la S/E Mulchén.

**Cuadro 2.1: Coordenadas Torres del trazado Línea de Transmisión.**

|Torre|Coordenadas UTM WGS84|Col3|
|---|---|---|
|**Torre**|**Norte [m]**|**Este [m]**|
|0|739.940,0|5.834.060,1|
|1|740.244,5|5.833.988,7|
|2|740.455,4|5.833.584,1|
|3|740.445,0|5.833.183,6|
|4|740.701,0|5.832.908,0|
|5|740.983,1|5.832.607,3|
|6|741.348,0|5.832.415,4|
|7|741.740,2|5.832.209,2|
|8|741.961,4|5.832.092,8|
|9|742.112,4|5.831.885,1|
|10|742.301,6|5.831.624,8|
|11|742.241,3|5.831.165,5|
|12|742.347,3|5.831.056,5|
|13|742.294,9|5.830.660,1|
|14|742.243,7|5.830.273,2|
|15|742.203,7|5.829.971,0|
|16|742.155,8|5.829.608,9|
|17|742.109,9|5.829.262,1|
|18|742.063,0|5.828.909,0|
|19|742.018,0|5.828.570,0|
|20|741.980,8|5.828.286,8|
|21|742.000,9|5.827.965,4|
|22|742.023,2|5.827.609,2|
|23|742.046,2|5.827.240,4|
|24|742.065,0|5.826.941,0|
|25|742.090,7|5.826.528,3|
|26|742.193,5|5.826.170,3|
|27|742.204,3|5.826.095,9|
|ML|742.214,6|5.826.012,8|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 3 de 14|

INICIO DEL

TRAMO LT

TRAZADO

TRAMO LT

2 km

**N**

**Figura 2.1 Trazado de Línea de Alta Tensión (Fuente: Google Earth)**

**3.** **HIDROLOGÍA**

La estimación de áreas de inundación requiere de la definición de condiciones de
escurrimiento en cada una de las quebradas en análisis. En este contexto, se desarrolla
una delimitación de cuencas afluentes y determinación de caudales en crecida, de las
distintas quebradas en análisis. Las quebradas a evaluar son cauces sin control
fluviométrico, por lo que se requiere de métodos indirectos para la determinación de
sus caudales en crecidas.

**3.1** **SECCIONES DE INTERÉS**

Sobre la base de la información topográfica del proyecto (2.1.a), se identificó tres
quebradas naturales que requieren ser analizadas respecto de su comportamiento en
condiciones de crecidas. Las torres de la línea de transmisión cercanas a cada una de
los puntos de interés se presentan en el Cuadro 3.1 .

Las áreas aportantes a cada una de las quebradas en estudio se delimitaron sobre la
información topográfica y cartográfica citada en el acápite 2.1.

**Cuadro 3.1: Torres y Áreas aportantes de quebradas.**

|Quebrada|A<br>Total|Torres de interés|
|---|---|---|
|**Quebrada**|**[km**~~**2**~~**] **|**[km**~~**2**~~**] **|
|Estero Las Diucas|2,3|27 y ML|
|Estero Licura|13,5|19 y 20|
|Quebrada sin nombre|1,3|6 y 7|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 4 de 14|

En la Figura 3.1 se presenta en forma esquemática, una vista en planta del trazado de
la línea y el área aportante a cada una de las quebradas.

**N**

Quebrada sin

nombre

Estero Licura

Estero Las

Diucas

2 km

**Figura 3.1: Áreas aportantes a Quebradas. (Fuente: Google Earth)**

**3.2** **CAUDALES MÁXIMOS**

Para determinar el caudal en crecida se utilizaron distintos métodos indirectos de
estimación de crecidas y los recomendados por la DGA en su publicación “Manual de
Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Información Fluviométrica”
(1995). Algunos de éstos tienen validez para cuencas entre 20 y 10.000 km [2] y para
periodos de retorno menores a 100 años.

Para determinar si las torres de la línea se ven comprometidas por el área de
inundación de las quebradas, se utiliza la crecida asociada a un período de retorno de
100 años. A continuación, se presentan los caudales máximos recomendados para
efectuar el análisis hidráulico. El detalle de los cálculos realizados para determinar
crecidas de cada uno de los cauces, puede ser revisado en el Apéndice 1.

**Cuadro 3.2: Resumen de caudales máximos instantáneos para T=100 años.**

|Quebrada|Q<br>100|
|---|---|
|**Quebrada**|**[m**~~**3**~~**/s]**|
|Estero Las Diucas|8,5|
|Estero Licura|39,0|
|Qda sin nombre|7,0|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 5 de 14|

**4.** **EJE HIDRÁULICO DE LAS QUEBRADAS**

En el presente numeral se describen los cálculos hidráulicos realizados para la
caracterización del tipo de escurrimiento de cada quebrada analizada. El estudio
hidráulico se realiza en el software HEC-RAS, específicamente para los caudales de
período de retorno de 1:100 años.

**4.1** **GENERACIÓN MODELOS HIDRÁULICOS EN HEC-RAS**

El estudio hidráulico tiene por objetivo principal determinar los niveles de
escurrimiento máximos asociados a los caudales de crecidas de cada quebrada, los
cuales fueron calculados en el estudio hidrológico, ver Apéndice 1.

Para estudiar el eje hidráulico de un cauce u obra se requiere del desarrollo de un
modelo geométrico basado en un modelo digital de terreno (MDT). Posteriormente, se
desarrolla el análisis hidráulico correspondiente. El análisis hidráulico se realiza en el
software HEC-RAS, para caudales de período de retorno de 100 años.

El modelo geométrico georeferenciado de cada quebrada fue elaborado utilizando el
software AutoCAD Civil 3D. Este permite obtener y exportar perfiles transversales
georeferenciados en base de un modelo de terreno para ser trabajados en HEC-RAS.

Los perfiles georeferenciados son importados como información geométrica dentro
HEC-RAS. Las características del modelo deben ser editadas según corresponda
(rugosidades, singularidades, diques, áreas inefectivas, etc), posteriormente se definen
las condiciones de borde y caudales a considerar para llevar a cabo las simulaciones.

Como metodología de cálculo, Hec-Ras utiliza el balance de energía entre dos
secciones sucesivas. Éste emplea como base de cálculo las secciones transversales, las
que representan la geometría del cauce en el tramo de interés, el caudal y el
coeficiente de rugosidad. Como resultado se pueden obtener para cada sección
transversal los niveles de agua y parámetros hidráulicos, tales como velocidad media
del flujo, alturas máximas, radio hidráulico, número de Froude, altura crítica, etc.

Fotografías de los modelos georeferenciados de cada cauce se presentan en el acápite
4.4, junto a los resultados obtenidos para el escenario de T=100 años. En los
Apéndices 2 a 4 se presentan los perfiles transversales ingresados en el modelo HECRAS para cada uno de los cauces analizados.

**4.2** **COEFICIENTE DE RUGOSIDAD**

En el cálculo de los ejes hidráulicos se utiliza la ecuación de Manning para determinar
la pérdida de carga por fricción entre tramos consecutivos. Esta ecuación requiere de
un coeficiente empírico de rugosidad “ _n_ ” (coeficiente de rugosidad de Manning), valor
que engloba de las asperezas propias del lecho y pérdidas provocadas por las
irregularidades de la sección (depósitos, socavaciones, vegetación, etc.).

Para determinar el coeficiente de rugosidad se consideró lo propuesto por Cowan
(Estimating hydraulic roughness coefficients, 1956), que desarrolló un procedimiento
para estimar el valor de _n_ de acuerdo a lo siguiente:

donde:

_n_ : Coeficiente de rugosidad de Manning, [m/s [1/3] ].

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 6 de 14|

_n_ 0 : Valor básico de _n_, para un canal recto, uniforme y liso en materiales
naturales.
_n_ 1 : Valor dependiente de las irregularidades de la superficie.
_n_ 2 : Valor dependiente de las variaciones en la sección transversal.
_n_ 3 : Valor dependiente de las obstrucciones en el cauce.
_n_ 4 : Valor dependiente del efecto de la vegetación.
_m_ 5 : Factor de corrección por la presencia de meandros.

**Cuadro 4.1: Rugosidad del cauce en quebrada**

|Parámetros|Cauce principal|Col3|Llanuras de inundación|Col5|
|---|---|---|---|---|
|Coeficiente rugosidad base (_n_0)|0,020|0,020|0,020|0,020|
|Grado de irregularidad (_n_1)|0,000|Leve|0,000|Leve|
|Variaciones sección transversal (_n_2)|0,005|Ocasionalmente|0,005|Ocasionalmente|
|Efecto de obstrucciones (_n_3)|0,000|Leve|0,000|Leve|
|Vegetación (_n_4)|0,020|Media|0,020|Media|
|Cantidad de meandros (_m_5)|1,000|Leve|1,000|Leve|
|**Coeficiente de rugosidad (n)**|**0,045**|**0,045**|**0,045**|**0,045**|

Para el cálculo se adopta un coeficiente base _n_ _o_ = 0,020 considerando un cauce de
tierra. No se aplica el coeficiente _n_ 3 debido a que el programa HEC-RAS considera en el
cálculo del eje hidráulico las variaciones en secciones transversales consecutivas por
medio de los coeficientes de expansión / contracción, por lo que se estaría tomando en
consideración dos veces el efecto de los cambios de sección.

Los coeficientes de contracción / expansión considerados en este estudio son 0,1 y 0,3
respectivamente.

El valor obtenido es igual a 0,045, según Ven Te Chow (Ant. 2.2.d), corresponde a un
cauce limpio, con curvas, algunas pozas y bancos de arena, algunos matorrales y
piedras. Por lo que, se considera adecuado estimar el eje hidráulico de los cauces con
el coeficiente adoptado.

**4.3** **CONDICIONES DE BORDE PARA EL CÁLCULO EN HEC-RAS**

Las condiciones de borde consideradas para iniciar el cálculo del eje hidráulico son las
siguientes:

 - Por aguas arriba: se considera altura normal.

 - Por aguas abajo: se considera altura normal.

**4.4** **RESULTADOS CÁLCULO EJE HIDRÁULICO**

En el Cuadro 4.2 al Cuadro 4.4 se presentan los resultados del cálculo de eje hidráulico
para cada uno de los cauces analizados, tomando en cuenta la crecida de 1:100 años
de periodo de retorno. La nomenclatura utilizada en cada uno de ellos se presenta a
continuación:

_Q_ : Caudal de crecida asociado al periodo de retorno _T_ [m [3] /s].

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 7 de 14|

_Z_ _F_ : Cota de fondo del perfil [m s.n.m.].
_Z_ _H_ : Cota del escurrimiento [m s.n.m.].
_Z_ _Cr_ : Cota escurrimiento crítico en la sección [msnm].
_Z_ _B_ : Cota de energía [msnm].
_J_ : Pendiente de la línea de energía [-].
_V_ : Velocidad media en la sección transversal [m/s].
_A_ : Área de la sección transversal [m [2] ].
_L_ : Ancho superficial del escurrimiento [m].
_R_ _h_ : Radio hidráulico en la sección [m].
_Fr_ : Número de Froude [-].

**Figura 4.1:Modelo georeferenciado Estero Las Diucas (Fuente: Elaboración Propia)**

**Cuadro 4.2: Eje Hidráulico Estero Las Diucas para** _**T**_ **=100 años**

|Perfil|Q|ZF|ZH|ZCr|ZB|J|V|A|L|Rh|Fr|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**(m3/s)**|**[m]**|**[m]**|**[m]**|**[m]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|**[-]**|
|27|8,5|165,0|165,4|165,3|165,5|0,0105|1,0|8,3|27,1|0,30|0,60|
|26|8,5|164,2|165,2|165,1|165,3|0,0124|1,1|7,6|25,0|0,30|0,64|
|25|8,5|164,0|164,9|164,9|165,0|0,0296|1,9|4,6|13,3|0,34|1,01|
|24|8,5|163,5|164,7|164,3|164,7|0,0046|0,8|10,7|28,0|0,38|0,41|
|23|8,5|163,5|164,3|164,3|164,5|0,0284|1,9|4,6|12,8|0,35|1,00|
|22|8,5|163,0|163,9|163,8|164,0|0,0170|1,5|5,9|16,3|0,35|0,77|
|21|8,5|162,6|163,5||163,6|0,0130|1,4|6,0|14,2|0,42|0,69|
|20|8,5|162,5|163,4||163,5|0,0044|0,9|9,4|19,2|0,48|0,42|
|19|8,5|162,8|163,2|163,2|163,3|0,0301|1,7|5,1|17,9|0,28|1,00|
|18|8,5|162,0|163,0|162,7|163,0|0,0026|0,7|11,5|21,5|0,53|0,32|
|17|8,5|162,0|163,0||163,0|0,0024|0,8|10,9|17,6|0,61|0,32|
|16|8,5|161,6|162,9||163,0|0,0013|0,7|12,5|15,3|0,80|0,24|
|15|8,5|161,5|162,9||162,9|0,0047|0,9|9,2|18,8|0,48|0,42|
|14|8,5|161,5|162,8||162,9|0,0039|0,9|9,6|18,7|0,51|0,39|
|13|8,5|161,5|162,8||162,8|0,0020|0,7|11,6|18,3|0,62|0,29|
|12|8,5|161,5|162,8||162,8|0,0032|0,8|10,1|17,9|0,55|0,36|
|11|8,5|161,5|162,5|162,5|162,7|0,0297|1,9|4,5|12,6|0,35|1,01|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 8 de 14|

|Perfil|Q|ZF|ZH|ZCr|ZB|J|V|A|L|Rh|Fr|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**(m3/s)**|**[m]**|**[m]**|**[m]**|**[m]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|**[-]**|
|10|8,5|161,1|161,7|161,8|162,0|0,1001|2,6|3,3|14,5|0,22|1,74|
|9|8,5|161,0|161,2|161,3|161,6|0,1871|2,6|3,3|23,8|0,14|2,21|
|8|8,5|160,5|161,3|161,1|161,3|0,0027|0,6|13,6|34,2|0,40|0,32|
|7|8,5|160,9|161,1|161,1|161,2|0,0359|1,3|6,6|39,3|0,17|1,00|
|6|8,5|160,5|161,1|160,8|161,1|0,0012|0,4|19,3|43,7|0,44|0,21|
|5|8,5|160,5|161,1||161,1|0,0021|0,6|14,8|35,7|0,42|0,28|
|4|8,5|160,1|161,0||161,1|0,0013|0,5|15,7|28,2|0,55|0,23|
|3|8,5|160,0|161,0||161,0|0,0006|0,4|21,5|32,5|0,66|0,16|
|2|8,5|160,0|161,0||161,0|0,0005|0,4|22,4|32,8|0,68|0,15|
|1|8,5|160,0|161,0||161,0|0,0009|0,5|18,8|34,6|0,54|0,20|
|0|8,5|160,0|161,0|160,4|161,0|0,0010|0,5|17,4|30,0|0,58|0,20|

**Figura 4.2:Modelo georeferenciado Estero Licura (Fuente: Elaboración Propia)**

**Cuadro 4.3: Eje Hidráulico Estero Licura para** _**T**_ **=100 años**

|Perfil|Q|ZF|ZH|ZCr|ZB|J|V|A|L|Rh|Fr|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**(m3/s)**|**[m]**|**[m]**|**[m]**|**[m]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|**[-]**|
|15|39,0|123,5|124,3|124,0|124,3|0,0023|0,7|58,6|117,7|0,5|0,3|
|14|39,0|123,2|124,1||124,1|0,0034|0,8|47,3|93,6|0,5|0,4|
|13|39,0|123,0|123,9||123,9|0,0044|0,9|43,4|91,2|0,5|0,4|
|12|39,0|122,5|123,6||123,7|0,0067|1,0|37,5|86,3|0,4|0,5|
|11|39,0|122,5|123,6||123,6|0,0022|0,7|55,8|101,1|0,6|0,3|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 9 de 14|

|Perfil|Q|ZF|ZH|ZCr|ZB|J|V|A|L|Rh|Fr|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**(m3/s)**|**[m]**|**[m]**|**[m]**|**[m]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|**[-]**|
|10|39,0|122,5|123,5||123,5|0,0011|0,6|67,7|98,0|0,7|0,2|
|9|39,0|122,5|123,5||123,5|0,0021|0,8|52,2|82,6|0,6|0,3|
|8|39,0|122,0|123,3||123,3|0,0052|1,1|35,4|61,9|0,6|0,5|
|7|39,0|122,0|123,2||123,3|0,0020|0,7|53,3|83,1|0,6|0,3|
|6|39,0|122,0|123,1||123,1|0,0019|0,8|48,8|66,0|0,7|0,3|
|5|39,0|122,0|122,9||123,0|0,0048|1,0|39,5|76,7|0,5|0,4|
|4|39,0|122,0|122,8||122,9|0,0114|1,4|28,4|64,1|0,4|0,7|
|3|39,0|121,5|122,7||122,7|0,0023|0,8|49,6|77,2|0,6|0,3|
|2|39,0|121,5|122,6||122,6|0,0011|0,6|62,8|79,5|0,8|0,2|
|1|39,0|121,5|122,5||122,6|0,0028|0,9|41,3|57,4|0,7|0,4|
|0|39,0|121,1|122,0|122,0|122,2|0,0270|2,1|18,3|41,0|0,5|1,0|

**Figura 4.3:Modelo georeferenciado Quebrada Sin Nombre (Fuente: Elaboración Propia)**

**Cuadro 4.4: Eje Hidráulico Quebrada Sin Nombre para** _**T**_ **=100 años**

|Perfil|Q|ZF|ZH|ZCr|ZB|J|V|A|L|Rh|Fr|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**(m3/s)**|**[m]**|**[m]**|**[m]**|**[m]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|**[-]**|
|26|7,0|152,0|152,6|152,5|152,6|0,0237|1,3|5,5|23,8|0,23|0,85|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén<br>Tema: MC Hidráulico Área Inundación. Esteros y Quebradas Hoja: 10 de 14<br>Línea de Transmisión|Col3|
|---|---|---|
||**Proyecto:** LAT San Carlos - S/E Mulchén <br>**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión<br> **Hoja:** 10 de 14|**Hoja:** 10 de 14|

|Perfil|Q|ZF|ZH|ZCr|ZB|J|V|A|L|Rh|Fr|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**(m3/s)**|**[m]**|**[m]**|**[m]**|**[m]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|**[-]**|
|25.500*|7,0|151,7|152,3|152,3|152,4|0,0262|1,4|4,9|19,3|0,25|0,91|
|25|7,0|151,5|152,2||152,2|0,0093|1,1|6,7|19,4|0,34|0,57|
|24|7,0|151,5|152,0||152,1|0,0140|1,0|6,9|28,8|0,24|0,66|
|23.667*|7,0|151,5|151,9||152,0|0,0046|0,6|11,0|39,6|0,28|0,39|
|23.333*|7,0|151,5|151,8||151,9|0,0065|0,7|10,4|45,2|0,23|0,45|
|23|7,0|151,5|151,7||151,8|0,0054|0,6|11,8|54,0|0,22|0,40|
|22.667*|7,0|151,0|151,7||151,7|0,0060|0,6|11,8|59,0|0,20|0,42|
|22.333*|7,0|151,0|151,6||151,6|0,0025|0,4|16,0|64,4|0,25|0,28|
|22|7,0|151,0|151,5||151,5|0,0111|1,1|6,3|18,9|0,33|0,62|
|21.500*|7,0|151,0|151,2|151,2|151,3|0,0354|1,4|5,1|27,6|0,19|1,01|
|21|7,0|150,5|151,1|150,9|151,1|0,0079|0,8|9,3|39,1|0,24|0,50|
|20.500*|7,0|150,5|151,0||151,0|0,0064|0,7|10,1|41,2|0,24|0,45|
|20|7,0|150,2|150,9||150,9|0,0037|0,6|11,7|39,2|0,30|0,35|
|19.833*|7,0|150,4|150,8||150,8|0,0042|0,5|13,3|60,7|0,22|0,36|
|19.667*|7,0|150,0|150,7||150,8|0,0039|0,5|14,9|75,5|0,20|0,34|
|19.500*|7,0|150,0|150,5|150,5|150,6|0,0295|1,0|6,9|50,5|0,14|0,87|
|19.333*|7,0|150,0|150,4||150,5|0,0030|0,6|12,1|36,7|0,33|0,32|
|19.167*|7,0|150,0|150,4||150,4|0,0039|0,6|11,7|40,7|0,29|0,36|
|19|7,0|150,0|150,3||150,3|0,0054|0,6|12,2|59,2|0,21|0,40|
|18.500*|7,0|149,8|150,1|150,1|150,1|0,0398|1,0|7,1|67,3|0,11|0,97|
|18|7,0|149,5|150,0|149,7|150,0|0,0013|0,4|17,2|46,0|0,37|0,21|
|17.800*|7,0|149,5|149,9||149,9|0,0016|0,4|16,9|54,3|0,31|0,24|
|17.600*|7,0|149,5|149,9||149,9|0,0013|0,4|18,0|54,0|0,33|0,22|
|17.400*|7,0|149,5|149,9||149,9|0,0019|0,5|16,8|75,4|0,22|0,26|
|17.200*|7,0|149,5|149,8||149,8|0,0034|0,5|15,7|85,9|0,18|0,32|
|17|7,0|149,4|149,7|149,7|149,7|0,0258|1,0|7,6|69,9|0,11|0,82|
|16|7,0|148,4|148,8|148,8|149,0|0,0329|1,5|4,7|21,2|0,22|1,00|
|15|7,0|147,9|148,5|148,4|148,5|0,0114|1,1|6,5|21,2|0,31|0,62|
|14.500*|7,0|147,8|148,3||148,3|0,0192|1,0|6,9|36,1|0,19|0,75|
|14|7,0|147,5|147,8|147,8|147,9|0,0319|1,6|4,4|17,4|0,25|1,01|
|13|7,0|146,8|147,2|147,3|147,4|0,0406|1,8|3,9|15,3|0,25|1,14|
|12|7,0|146,5|146,9|146,9|147,0|0,0314|1,7|4,2|15,3|0,27|1,01|
|11|7,0|145,3|146,1|145,7|146,1|0,0020|0,7|10,7|20,2|0,53|0,29|
|10|7,0|145,5|145,9||146,0|0,0183|1,4|5,1|16,1|0,31|0,79|
|9|7,0|145,0|145,8||145,9|0,0057|1,1|6,2|11,0|0,55|0,48|
|8.5000*|7,0|145,0|145,6|145,6|145,7|0,0307|1,7|4,2|14,5|0,29|1,01|
|8|7,0|144,5|145,0|145,0|145,2|0,0392|1,9|3,7|12,9|0,28|1,13|
|7.5000*|7,0|143,6|144,2|144,1|144,3|0,0056|0,9|8,3|22,5|0,37|0,45|
|7|7,0|143,5|143,9|143,9|144,1|0,0293|1,8|3,9|11,6|0,33|1,01|
|6.5000*|7,0|143,0|143,5|143,5|143,7|0,0377|2,1|3,3|9,7|0,34|1,15|
|6|7,0|142,5|143,5|143,1|143,5|0,0040|0,9|7,5|13,6|0,55|0,40|
|5.5000*|7,0|142,7|143,4||143,4|0,0087|1,1|6,2|15,1|0,41|0,57|
|5|7,0|142,8|143,3||143,4|0,0043|0,7|9,7|27,8|0,35|0,39|
|4.5000*|7,0|142,5|143,1|143,1|143,2|0,0269|1,9|3,8|10,3|0,36|0,98|
|4|7,0|142,2|142,7|142,7|142,9|0,0265|1,7|4,1|12,4|0,33|0,95|
|3|7,0|142,0|142,6||142,7|0,0045|0,9|7,8|16,6|0,47|0,42|
|2.5000*|7,0|141,8|142,6||142,6|0,0022|0,7|9,7|16,7|0,58|0,30|
|2|7,0|141,5|142,6||142,6|0,0012|0,6|12,0|17,3|0,68|0,23|
|1.5000*|7,0|142,0|142,4|142,4|142,6|0,0303|1,7|4,1|14,1|0,29|1,00|
|1|7,0|141,5|142,2|142,0|142,3|0,0058|1,1|6,4|12,2|0,52|0,48|
|0|7,0|141,5|142,1|141,9|142,2|0,0060|1,1|6,5|12,9|0,50|0,49|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 11 de 14|

**5.** **ÁREAS DE INUNDACIÓN**

Con la información obtenida en el acápite 4.4, se puede generar el área de inundación
para cada una de las quebradas en análisis. Esta área corresponderá a la inundación
asociada a un período de retorno de 100 años.

En la Figura 5.1 se presenta el área de inundación del Estero Las Diucas. Se aprecia
que la torre de la línea de tensión 27 y el marco de línea ML se ubican fuera del área
de inundación asociada al período de retorno de 100 años. Esto quiere decir, que las
torres no afectarán el cauce natural de la crecida del estero Las Diucas.

**N**

Inundación crecida

Tr=100 años

100 m

**Figura 5.1:Área de inundación Estero Las Diucas T=100 años (Fuente: Elaboración**

**Propia)**

En Figura 5.2 se presenta las profundidades máximas en el Estero Las Diucas para un
caudal asociado a un período de retorno de 100 años. Se aprecia la profundidad
máxima en el estero es del orden de 1,4 m, luego habrá una distancia libre entre el
nivel máximo de escurrimiento y el conductor de al menos 5,8 m, considerando que la
altura reglamentaria mínima de los conductores sobre el suelo es de 7,32 m. Por lo
tanto, el conductor no se ve afectado por la crecida asociada a un período de retorno
de 100 años.

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 12 de 14|

100 m

**N**

**Figura 5.2:Profundida de Escurrimiento Estero Las Diucas T=100 años (Fuente:**

**Elaboración Propia)**

En la Figura 5.3 se puede observar el área de inundación del Estero Licura. Se observa
que las torres 19 y 20 de la línea de tensión se ubican fuera del área de inundación
asociada al período de retorno de 100 años. Esto quiere decir que las torres no
afectarán el cauce natural de la crecida del estero Licura.

**N**

Inundación crecida

Tr=100 años

100 m

**Figura 5.3:Área de inundación Estero Licura T=100 años**

En Figura 5.4 se presenta las profundidades máximas en el Estero Licura para un caudal
asociado a un período de retorno de 100 años. Se aprecia la profundidad de
escurrimiento máxima en el trazado de la línea de transmisión es del orden de 1,1 m,
luego habrá una distancia libre entre el nivel máximo de escurrimiento y el conductor

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 13 de 14|

de al menos 6,22 m, considerando que la altura reglamentaria mínima de los
conductores sobre el suelo es de 7,32 m. Por lo tanto, el conductor no se ve afectado
por la crecida asociada a un período de retorno de 100 años.

**N**

100 m

**Figura 5.4:Profundida de Escurrimiento Estero Licura T=100 años (Fuente: Elaboración**

**Propia)**

En la Figura 5.5 se puede observar el área de inundación de la Quebrada Sin Nombre.
Se observa que las torres de la línea de tensión 6 y 7 se ubican fuera del área de
inundación asociada al período de retorno de 100 años. Esto quiere decir que las torres
no estarán afectando el cauce natural de la crecida de la quebrada.

**N**

Inundación crecida

Tr=100 años

100 m

**Figura 5.5:Área de inundación Quebrada Sin Nombre T=100 años (Fuente: Elaboración**

**Propia)**

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión|**Hoja:** 14 de 14|

En Figura 5.6 se presenta las profundidades máximas en la Quebrada Sin Nombre para
un caudal asociado a un período de retorno de 100 años. Se aprecia la profundidad de
escurrimiento máxima en el trazado de la línea de transmisión es del orden de 0,9 m,
luego habrá una distancia libre entre el nivel máximo de escurrimiento y el conductor
de al menos 6,42 m, considerando que la altura reglamentaria mínima de los
conductores sobre el suelo es de 7,32 m. Por lo tanto, el conductor no se ve afectado
por la crecida asociada a un período de retorno de 100 años.

**N**

100 m

**Figura 5.6:Profundida de Escurrimiento Quebrada Sin Nombre T=100 años (Fuente:**

**Elaboración Propia)**

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 1)|**Hoja:** 1 de 1|

**APÉNDICE 1**

**ESTUDIO HIDROLÓGICO ESTEROS LAS DIUCAS, LICURA Y**

**QUEBRADA SIN NOMBRE.**

635-16-AMB-00-MC-HI-001

|LAT SAN CARLOS - S/E MULCHÉN<br>ESTUDIO HIDROLÓGICO<br>ESTEROS LAS DIUCAS, LICURA Y QUEBRADA<br>SIN NOMBRE<br>LÍNEA DE TRANSMISIÓN ELECTRICA<br>635-16-AMB-00-MC-HI-002|Col2|Col3|
|---|---|---|
|ACOGE COMENTARIOS CLIENTE|02.11.2016|F|
|ACOGE COMENTARIOS CLIENTE|27.10.2016|E|
|ACOGE COMENTARIOS CLIENTE|24.10.2016|D|
|ACOGE COMENTARIOS CLIENTE|20.10.2016|C|
|PARA REVISIÓN CLIENTE|19.10.2016|B|
|PARA REVISIÓN INTERNA|13.10.2016|A|
|**REVISIÓN**|**FECHA REVISIÓN**|**No REVISIÓN**|
||||
|**PREPARÓ**|Ricardo González V.|Ricardo González V.|
|**REVISÓ**|Roberto Lüders R.|Roberto Lüders R.|
|**APROBÓ**|Roberto Lüders R.|Roberto Lüders R.|

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre|**Hoja:** i de i|

**ÍNDICE**

Pág.

**1.** **INTRODUCCIÓN ...................................................................................... 1**

**2.** **ANTECEDENTES ...................................................................................... 1**
2.1 ESTACIONES PLUVIOMÉTRICAS. ...................................................... 1
2.2 ANTECEDENTES BIBLIOGRÁFICOS. .................................................. 1

**3.** **METODOLOGÍA ADOPTADA ..................................................................... 2**

**4.** **ESTUDIO DE PRECIPITACIONES MÁXIMAS DIARIAS .............................. 2**

**5.** **ESTUDIO DE CRECIDAS ........................................................................... 3**
5.1 DETERMINACIÓN DEL ÁREA APORTANTE .......................................... 3
5.2 METODOLOGÍA PLANTEADA ............................................................ 5

5.2.1 Fórmula de Verni y King (Ref. 4) .......................................... 5

5.2.2 Fórmula Racional ............................................................... 5

5.2.3 Fórmula de Verni-King modificada (Ref. 2). ........................... 6

5.2.4 Método DGA-AC (Ref. 2). .................................................... 7

5.2.5 Racional Modificado (Ref.2). ................................................ 7

5.3 RESULTADOS OBTENIDOS .............................................................. 8

5.3.1 Cálculo del tiempo de concentración ..................................... 8

5.3.2 Cálculo de los caudales máximos instantáneos ....................... 8

**ANEXOS**

Anexo A Precipitaciones Máximas Diarias

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 1 de 13|

**1.** **INTRODUCCIÓN**

En este documento se presentan los cálculos asociados al estudio de Crecidas de tres
quebradas naturales que interceptan el trazado de la línea de transmisión eléctrica
desde San Carlos a la S/E Mulchén, los períodos de retorno considerados están
comprendidos entre T = 10 años y T = 100 años.

La línea de alta tensión va desde el sur la localidad de San Carlos de Purén hasta la
subestación eléctrica Mulchén ubicada a unos 4 km al norte de la localidad del mismo
nombre, en la región del Bío Bío. El trazado que se aborda en este informe comprende
un tramo de 9,26 km de longitud, comprendido entre las torres de cruce de la Ruta 5
Sur hasta la llegada a la Subestación Mulchén, un total de 28 torres de alta tensión.

**2.** **ANTECEDENTES**

**2.1** **ESTACIONES PLUVIOMÉTRICAS.**

Las estadísticas utilizadas corresponden a las registradas en las estaciones de medición
de precipitaciones cercanas a la zona de interés. En el Cuadro 2-1 se indican las
principales características de las estaciones pluviométricas disponibles.

**Cuadro 2.1.**

**Estaciones Pluviométricas Utilizadas** .

|Estación|Ubicación|Col3|Altitud|Información|Col6|
|---|---|---|---|---|---|
|Estación|Lat.|Long.|msnm|Inicio|Fin|
|LOS ÁNGELES|37° 30' 08''|72° 24' 30''|129|1963|2015|
|MULCHÉN|37° 42' 53''|72° 14' 37''|142|1980|2015|
|SAN JOSÉ DE MUNILQUE|37° 35' 09''|72° 19' 14''|120|1963|2015|
|SAN CARLOS DE PURÉN|37° 35' 43''|72° 16' 37''|155|1985|2015|

Las estadísticas de las estaciones fluviométricas recién mencionadas fueron obtenidas
del Banco Nacional de Aguas de la Dirección General de Aguas del MOP

**2.2** **ANTECEDENTES BIBLIOGRÁFICOS.**

Para la elaboración del presente estudio se utilizaron los siguientes antecedentes
bibliográficos:

**Ref.1.** Precipitaciones Máximas en 1, 2 y 3 Días”. Dirección General de Aguas del
Ministerio de Obras Públicas, 1991.

**Ref.2.** Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin
Información Fluviométrica”. Dirección General de Aguas del Ministerio de Obras
Públicas, 1995.

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 2 de 13|

**Ref.3.** Hidrología Aplicada, Ven Te Chow, 2001.

**Ref.4.** Estimación de crecidas en cuencas no controladas. Verni, F. y King. H.
Tercer Coloquio Nacional. SOCHID. 1977.

**Ref.5.** Manual de Carreteras, Volumen N°3, Instrucciones y Criterios de Diseño.
MOP, Marzo 2008.

**Ref.6.** Espildora, B, Brown, E, Isensee, P. y Cabrera, G. Elementos de Hidrología.
Universidad de Chile (1975).

**Ref.7** . Cartografía IGM. Escala 1:50.000.

**3.** **METODOLOGÍA ADOPTADA**

Cabe señalar que en los cauces de interés no se dispone de control fluviométrico ni
tampoco se dispone de control en cauces laterales al río Biobío que tengan un tamaño
similar a las cuencas analizadas (< 15 km2). Por lo anterior, para efectuar el estudio
de crecidas se definió el uso de los denominados métodos indirectos basados en
fórmulas empíricas (racional, Verni-King, DGA-AC, etc.) que dependen básicamente de
las precipitaciones máximas y las área aportantes.

Los métodos del tipo indirecto requieren, en términos generales, de la siguiente
información:

 Análisis de la información pluviométrica disponible en la zona.
 Determinación de precipitación máxima en 24 horas para distintos períodos
de retorno en la estación meteorológica de interés (análisis de frecuencia )
 Determinación de las áreas aportantes y parámetros geomorfológicos de
interés (alturas máximas y mínima largo del cauce principal, etc.)
 Utilización de fórmulas empíricas para la determinación de caudales
máximos instantáneos.

 Selección del método más apropiado para el cálculo de caudales de
crecidas

En el capítulo 4 se describe el procedimiento utilizado para caracterizar
probabilísticamente las precipitaciones máximas en 24 horas y en el capítulo 5 el
cálculo de crecidas pluviales para distintos períodos de retorno.

**4.** **ESTUDIO DE PRECIPITACIONES MÁXIMAS DIARIAS**

Para efectuar la caracterización de precipitaciones máximas diarias, en atención a su
cercanía a la zona de interés, se definió como estación base la estación pluviométrica
Mulchén, cuyos registros están disponibles desde el año 1980 en adelante y son
bastantes completos, faltando información solo en los años 1988 y 1989.

Por lo anterior, para completar la serie de precipitaciones máximas diarias se
establecieron correlaciones con los registros de las estaciones Los Ángeles y San Carlos
de Purén, las cuales se presentan en las Figuras A4-1 y A4-2 respectivamente (ver
Anexo A). Utilizando dichas correlaciones se procedió a rellenar la estadística de
Mulchén, la cual se presenta en el Cuadro A4-1.

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 3 de 13|

Dicha serie fue sometida a un análisis de frecuencia que consideró a las distribuciones
Normal, Log - Normal, Pearson III, Log -Pearson III y Gumbel. Para seleccionar la
distribución de mejor ajuste se consideró el criterio gráfico y el analítico (test  [2] ).

Los estadísticos resultantes del análisis de frecuencia se presentan en el Cuadro 4-1,
en donde se observa que el test  [2 ] solo rechaza la distribución Normal, las restantes
distribuciones son aceptadas por el citado test. Considerando el tipo de datos
analizados y los resultados obtenidos, se decidió adoptar el ajuste analítico Gumbel.

**Cuadro 4-1: Análisis estadístico de las distribuciones. Serie Precipitaciones**

**Máximas Diarias. Estación Mulchén**

|Distribución|Normal|Log<br>Normal|Pearson III|Log Pearson<br>III|Gumbel|
|---|---|---|---|---|---|
|Coeficiente R2|0,887|0,952|0,964|0,969|0,960|
|<br>Calc /2<br>1-|1,52|0,76|0,83|0,68|0,71|

En el Cuadro 4-2 se presentan los resultados obtenidos para los distintos períodos de
retorno analizados, en tanto que, el ajuste gráfico se muestra en la Figura A4-3.

**Cuadro 4-2: Precipitaciones Máximas Diarias (mm) para distintos períodos de**

**retorno. Estación Mulchén**

|T<br>(años)|Pmáxd<br>(mm)|
|---|---|
|10<br>50<br>100|125<br>165<br>180|

Los valores de precipitación que se presentan en el Cuadro 4-2 fueron corregidos por
un factor K = 1,1 para transformarlos de precipitaciones máximas diarias a máximas
en 24 horas, de acuerdo a las recomendaciones disponibles en la Ref. 6.

**5.** **ESTUDIO DE CRECIDAS**

**5.1** **DETERMINACIÓN DEL ÁREA APORTANTE**

Sobre la base de la información cartográfica disponible (Ref. 7) se identificó tres
cauces naturales que requieren ser analizadas respecto de su comportamiento en
condiciones de crecidas.

Las áreas aportantes a cada una de los puntos de interés se delimitaron sobre la
información topográfica y cartográfica citada en el acápite 2.2. En el Cuadro 5-1 se

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 4 de 13|

presentan el área aportante y los parámetros geomorfológicos de las cuencas
analizadas.

**Cuadro 5-1:**

**Áreas aportantes y parámetros geomorfológicos de cauces de interés**

|Parámetro|Unidad|Estero<br>Las Diucas|Estero<br>Locura|Quebrada sin<br>nombre|
|---|---|---|---|---|
|Cota superior<br>Cota inferior<br>Largo cauce principal<br>Pendiente<br>Área aportante|msnm<br>msnm<br>Km<br>m/m<br>Km2|301<br>172<br>1,8<br>0,07<br>2,3|300<br>135<br>4,7<br>0,04<br>13,5|330<br>158<br>1,0<br>0,17<br>1,3|

En la Figura 5-1 se presenta en forma esquemática, una vista de la zona de la línea
(color amarillo) y el trazado del área aportante (color rojo) a cada uno de los cauces
de interés.

**N**

Quebrada sin

nombre

Estero Licura

Estero Las

Diucas

2 km

**Figura 5-1: Áreas aportantes de cauces de interés** **(Fuente: Elaboración Propia)**

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 5 de 13|

**5.2** **METODOLOGÍA PLANTEADA**

Para la estimación indirecta de crecidas se consideró la utilización de las siguientes
metodologías de cálculo:

**5.2.1** **Fórmula de Verni y King (Ref. 4)**

La fórmula de Verni - King tiene la siguiente expresión:
###### Q ,000615   P T 24 ,124  A p,088

Donde:

_Q_ : Caudal máximo instantáneo de período de retorno T años, expresado en m [3] /s.

_P_ _T24_ : Precipitación máxima diaria de período de retorno T años, expresada en mm.

_A_ _p_ : Área pluvial aportante, en km [2 ]

**5.2.2** **Fórmula Racional**

El caudal máximo instantáneo está dado por:

_C_  _i_  _A_


_Q_

6,3

Donde:

Q : Caudal máximo instantáneo en m [3] /s.

C : Coeficiente de escorrentía asociado al período de retorno T en años
i : Intensidad máxima de la lluvia de duración igual al tiempo de concentración
de la cuenca, en mm/hr.

A : Área pluvial aportante en km [2] .

Tiempo de concentración

Los tiempos de concentración se calcularon utilizando expresiones de uso habitual en
estudios hidrológicos (Ref. 5 y 6), según se describe en la Cuadro 5-2.

**Cuadro 5-2: Fórmulas para el cálculo del tiempo de concentración**

|Autor|Expresión|
|---|---|
|Normas Españolas||
|California Culverts Practice (1942)||
|Giandotti|<br>|

Donde:

_Tc_ : Tiempo de concentración (min)

_L_ : Longitud del cauce (km)

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 6 de 13|

_S_ : Pendiente (m/m)

_A_ : Área de la cuenca en km [2]

_Hm_ : Diferencia de nivel en m entre la cota media de la cuenca y la de salida

_H_ : diferencia de nivel total entre cotas extremas de la cuenca (m)

El uso de las expresiones empíricas citadas en el Cuadro 5-2 usualmente conduce a
resultados que entregan un rango de valores entre los cuales se podría fluctuar la
variable analizada (tiempo de concentración).

Por lo anterior, se decidió utilizar las tres expresiones de cálculo ya señaladas y
revisar / verificar los resultados obtenidos en términos de la velocidad flujo promedio
del cauce principal.

Utilizando las recomendaciones disponibles en la Ref. 6 (Elementos de Hidrología,
1975) se adoptó una velocidad promedio igual a 1,0 m/s para los esteros Las Diucas y
Licura y 1,5 m/s para la quebrada sin nombre.

Intensidades máximas de la lluvia de diseño

Para la determinación de las intensidades máximas de las lluvias de diseño de
duraciones menores a 1 hora se aplicará la fórmula de Bell dada por la siguiente
expresión, en relación a la lluvia de 60 minutos de duración:

_CD_ _t_ ,054 _t_,025 ,050

Donde t es la duración en minutos.

Para intensidades mayores a 1 hora fue utilizada la fórmula de Grunsky (Ref. 6), la
cual se describe a continuación:

It = I 24 - (24/t)

Donde:

I 24 : Intensidad media en 24 horas (mm/hr)

It: intensidad media en t horas (mm/hr)

t: duración considerada de la lluvia (horas)

Coeficiente de escorrentía (C)

El coeficiente de escorrentía se adoptó igual a 0,36 de acuerdo a las recomendaciones
de la Ref. 2.

**5.2.3** **Fórmula de Verni-King modificada (Ref. 2).**

Este método permite obtener caudales máximos instantáneos a través del uso de la
precipitación máxima en 24 horas y del área pluvial de la cuenca:

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 7 de 13|

_T_



,124

_Q_ _T_  _C_  _T_ ,000618  _A_ _p_,088  _P_ 24 _T_

En donde,
Q : Caudal máximo instantáneo asociado a período de retorno T años (m [3] /s)

C : Coeficiente empírico de período de retorno T años

P 24 [T] : Precipitación máxima en 24 hrs asociada al período de retorno T (mm/hr)

**5.2.4** **Método DGA-AC (Ref. 2).**

El método consiste en determinar una curva de frecuencia para el caudal máximo
instantáneo, en función del caudal medio diario máximo de período de retorno 10
años. El procedimiento del cálculo es el que se detalla a continuación:

- Determinación Zona Homogénea, en este caso corresponde a Tp (VIII región Biobío)

- Determinación del caudal medio máximo de período de retorno 10 años. Se
determina a través de formulas que utilizan el área pluvial y precipitación máxima
diaria para T = 10 años (P [10] 24 [ en mm). Las fórmulas mencionadas abarcan entre la III ]

y IX Región, para los cálculos se considera la curva correspondiente a la VIII Región.

- Determinación de la Curva de Frecuencia Regional

- Selección de la Curva de Frecuencia del caudal Instantáneo Máximo (Q T /Q 10 )

El método DGA-AC considera que el caudal máximo instantáneo es proporcional al
caudal máximo medio diario de igual período de retorno. El factor de proporcionalidad
 en este caso es igual 1,28.

**5.2.5** **Racional Modificado (Ref.2).**

Para la aplicación del método racional modificado se han utilizado las recomendaciones
de la REf.2, en este caso, el caudal máximo se estima a través de la siguiente fórmula:

_T_ _T_

_Q_  _C_ ( _T_ )  _I_ _tc_  _A_ / 6,3

Donde:

Q [T] : Caudal máximo asociado al período de retorno T (m3/s)

C(T) : Coeficiente de escorrentía de la cuenca asociado al periodo T, el cual se

obtiene sobre la base de las recomendaciones de la Ref.2.

I tcT : Intensidad máxima de lluvia durante un tiempo igual al tiempo de

concentración de la cuenca, para un período de retorno T (mm/hr)

A : Área de la cuenca aportante (Km2)

Para estimar las variables I tcT y A se ha considerado lo expuesto en el acápite 5.1 y

5.2.2 del presente informe.

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 8 de 13|

**5.3** **RESULTADOS OBTENIDOS**

**5.3.1** **Cálculo del tiempo de concentración**

Considerando lo expuesto en el acápite 5.2.2 se obtuvieron los tiempos de
concentración que se presentan en el Cuadro 5-3. En el mismo Cuadro se presenta el
tiempo de concentración adoptado para caso analizado, el cual obedece
fundamentalmente al análisis de los resultados obtenidos con fórmulas empíricas y el
contraste con las velocidades de escurrimiento establecidas en el acápite 5.2.2.

**Cuadro 5-3: Cálculo del tiempo de Concentración.**

**Cauces de interés.**

|Col1|Tiempo de concentración (hrs)|Col3|Col4|
|---|---|---|---|
|Autor|Estero<br>Las Diucas|Estero<br>Licura|Quebrada sin<br>nombre|
|Normas Españolas<br>California<br>Giandotti<br>Adoptado|0,8<br>0,3<br>1,4<br>0,5|1,8<br>0,8<br>3,0<br>1,2|0,4<br>0,1<br>0,8<br>0,2|

**5.3.2** **Cálculo de los caudales máximos instantáneos**

Considerando las precipitaciones máximas diarias estimadas en el capítulo 4, el área
aportante señalada en el acápite 5.1, los tiempos de concentración indicados en
acápite 5.3.1 y las fórmulas empíricas descritas en el acápite 5.2 se obtienen los
caudales máximos instantáneos (Qmi) que se presentan en los Cuadros 5-4, 5-5 y 5-6,
para cada uno de los cauces analizados.

**Cuadro 5-4: Caudales Máximos Instantáneos (m** **[3]** **/s).**

**Estero Las Diucas**

|T [años]|DGA - AC|Verni King|V- K Modif|F. Rac. Modif|F. Rac.|
|---|---|---|---|---|---|
|10<br>50<br>100|2.1<br>3.0<br>3.4|5.1<br>7.2<br>8.0|4.0<br>5.9<br>6.6|7.0<br>9.5<br>10.4|7.0<br>9.3<br>10.1|

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 9 de 13|

**Cuadro 5-5: Caudales Máximos Instantáneos (m** **[3]** **/s).**

**Estero Licura**

|T [años]|DGA - AC|Verni King|V- K Modif|F. Rac. Modif|F. Rac.|
|---|---|---|---|---|---|
|10<br>50<br>100|13.3<br>19.0<br>21.4|27.2<br>38.4<br>42.8|21.6<br>31.7<br>35.3|27.8<br>37.5<br>41.3|27.8<br>36.8<br>40.1|

**Cuadro 5-6: Caudales Máximos Instantáneos (m** **[3]** **/s).**

**Quebrada sin nombre.**

|T [años]|DGA - AC|Verni King|V- K Modif|F. Rac. Modif|F. Rac.|
|---|---|---|---|---|---|
|10<br>50<br>100|1.4<br>1.9<br>2.2|3.5<br>4.9<br>5.5|2.8<br>4.0<br>4.5|7.2<br>9.7<br>10.7|7.2<br>9.5<br>10.4|

Analizando los resultados presentados en los Cuadros 5-4, 5-5 y 5-6 es posible
establecer que la fórmula DGA-AC subestima los Qmi en forma sistemática para todas
las cuencas analizadas. Por otra parte, las formulas racional, racional modificada y el
método de Verni-King entregan resultados mayores al de las restantes metodologías.

Por lo anterior, se decidió descartar del análisis el mayor y el menor valor obtenido con
las metodologías utilizadas y se calculó como valor de referencia el promedio sin
considerar el mínimo y máximo. Considerando los resultados obtenidos, la experiencia
del consultor en este tipo de análisis y efectuando un redondeo de los valores
obtenidos, se recomienda considerar los Qmi que se presentan el Cuadro 5-7.

**Cuadro 5-7: Caudales Máximos Instantáneos (m** **[3]** **/s).**
**Estero Las Diucas, Estero Licura y Quebrada sin nombre.**

|Col1|Qmi (m3/s)|Col3|Col4|
|---|---|---|---|
|T <br>(años)|Estero<br>Las Diucas|Estero<br>Licura|Quebrada sin<br>nombre|
|10<br>50<br>100|5,5<br>7,5<br>8,5|25,5<br>35,5<br>39|5 <br>6,5<br>7|

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 10 de 13|

**ANEXO A**

**PRECIPITACIONES MÁXIMAS DIARIAS**

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 11 de 13|

**Cuadro A4-1.**

**Mulchén**

**Precipitaciones Máximas Diarias (mm)**

|||<br>|
|---|---|---|
|<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>|<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>|<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>|

Rellenado con Los Ángeles
Rellenado con San Carlos de Puren

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 12 de 13|

**Figura A4-1**

**Mulchén v/s Los Ángeles**

**Correlaciones precipitaciones máximas diarias**

160

140

120

100

80

60

40

20

0

160

140

120

100

80

60

40

20

0

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||y = 0,645|6x + 30,136|
|||R2 =|0,8484|
|||||

0,00 50,00 100,00 150,00 200,00

**Pmáx24h Los Angeles (mm)**

**Figura A4-2**

**Mulchén v/s San Carlos de Purén**

**Correlaciones precipitaciones máximas diarias**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
||||||y =|0,7352x|+ 29,827|
|||||||R2 = 0,7|646|
|||||||||

0 20 40 60 80 100 120 140 160

**Pmáx24h San Carlos de Purén (mm)**

635-16-AMB-00-MC-HI-002

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||** Tema:** Estudio Hidrológico. Estero Las Diucas, Licura y<br>Quebrada sin nombre. Línea de Transmisión eléctrica.|**Hoja:** 13 de 13|

**Figura A4-3: Análisis de Frecuencia - Serie Precipitaciones Máximas Diarias.**

**Mulchén**

**Mulchén - Ajuste Gumbel**

**Periodo de Retorno (años)**

200

180

160

140

120

100

80

60

40

20

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||2|||||5||1|20<br>0|50<br>|1|00|
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||

99 95 90 85 80 70 60

635-16-AMB-00-MC-HI-002

2

1

**Probabilidad de Excedencia (%)**

50 40 30

20 15

10

5

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 2)|**Hoja:** 1 de 6|

**APÉNDICE 2**

**PERFILES TRANSVERSALES ESTERO LAS DIUCAS**

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 2)|**Hoja:** 2 de 6|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 2)|**Hoja:** 3 de 6|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 2)|**Hoja:** 4 de 6|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 2)|**Hoja:** 5 de 6|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 2)|**Hoja:** 6 de 6|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 3)|**Hoja:** 1 de 4|

**APÉNDICE 3**

**PERFILES TRANSVERSALES ESTERO LICURA**

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 3)|**Hoja:** 2 de 4|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 3)|**Hoja:** 3 de 4|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 3)|**Hoja:** 4 de 4|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 1 de 10|

**APÉNDICE 4**

**PERFILES TRANSVERSALES QUEBRADA SIN NOMBRE**

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 2 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 3 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 4 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 5 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 6 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 7 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 8 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 9 de 10|

635-16-AMB-00-MC-HI-001

|Col1|Proyecto: LAT San Carlos - S/E Mulchén|Col3|
|---|---|---|
||**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión (Apéndice 4)|**Hoja:** 10 de 10|

635-16-AMB-00-MC-HI-001

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1: Coordenadas Torres del trazado Línea de Transmisión.****

| Torre | Coordenadas UTM WGS84 | Col3 |
| --- | --- | --- |
| **Torre** | **Norte [m]** | **Este [m]** |
| 0 | 739.940,0 | 5.834.060,1 |
| 1 | 740.244,5 | 5.833.988,7 |
| 2 | 740.455,4 | 5.833.584,1 |
| 3 | 740.445,0 | 5.833.183,6 |
| 4 | 740.701,0 | 5.832.908,0 |
| 5 | 740.983,1 | 5.832.607,3 |
| 6 | 741.348,0 | 5.832.415,4 |
| 7 | 741.740,2 | 5.832.209,2 |
| 8 | 741.961,4 | 5.832.092,8 |
| 9 | 742.112,4 | 5.831.885,1 |
| 10 | 742.301,6 | 5.831.624,8 |
| 11 | 742.241,3 | 5.831.165,5 |
| 12 | 742.347,3 | 5.831.056,5 |
| 13 | 742.294,9 | 5.830.660,1 |
| 14 | 742.243,7 | 5.830.273,2 |
| 15 | 742.203,7 | 5.829.971,0 |
| 16 | 742.155,8 | 5.829.608,9 |
| 17 | 742.109,9 | 5.829.262,1 |
| 18 | 742.063,0 | 5.828.909,0 |
| 19 | 742.018,0 | 5.828.570,0 |
| 20 | 741.980,8 | 5.828.286,8 |
| 21 | 742.000,9 | 5.827.965,4 |
| 22 | 742.023,2 | 5.827.609,2 |
| 23 | 742.046,2 | 5.827.240,4 |
| 24 | 742.065,0 | 5.826.941,0 |
| 25 | 742.090,7 | 5.826.528,3 |
| 26 | 742.193,5 | 5.826.170,3 |
| 27 | 742.204,3 | 5.826.095,9 |
| ML | 742.214,6 | 5.826.012,8 |

**Tabla 3.1: Torres y Áreas aportantes de quebradas.****

| Quebrada | A<br>Total | Torres de interés |
| --- | --- | --- |
| **Quebrada** | **[km**~~**2**~~**] ** | **[km**~~**2**~~**] ** |
| Estero Las Diucas | 2,3 | 27 y ML |
| Estero Licura | 13,5 | 19 y 20 |
| Quebrada sin nombre | 1,3 | 6 y 7 |

**Tabla 3.2: Resumen de caudales máximos instantáneos para T=100 años.****

| Quebrada | Q<br>100 |
| --- | --- |
| **Quebrada** | **[m**~~**3**~~**/s]** |
| Estero Las Diucas | 8,5 |
| Estero Licura | 39,0 |
| Qda sin nombre | 7,0 |

**Tabla 4.1: Rugosidad del cauce en quebrada****

| Parámetros | Cauce principal | Col3 | Llanuras de inundación | Col5 |
| --- | --- | --- | --- | --- |
| Coeficiente rugosidad base (_n_0) | 0,020 | 0,020 | 0,020 | 0,020 |
| Grado de irregularidad (_n_1) | 0,000 | Leve | 0,000 | Leve |
| Variaciones sección transversal (_n_2) | 0,005 | Ocasionalmente | 0,005 | Ocasionalmente |
| Efecto de obstrucciones (_n_3) | 0,000 | Leve | 0,000 | Leve |
| Vegetación (_n_4) | 0,020 | Media | 0,020 | Media |
| Cantidad de meandros (_m_5) | 1,000 | Leve | 1,000 | Leve |
| **Coeficiente de rugosidad (n)** | **0,045** | **0,045** | **0,045** | **0,045** |

**Tabla 4.2: Eje Hidráulico Estero Las Diucas para** _**T**_ **=100 años****

| Perfil | Q | ZF | ZH | ZCr | ZB | J | V | A | L | Rh | Fr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **(m3/s)** | **[m]** | **[m]** | **[m]** | **[m]** | **[m/m]** | **[m/s]** | **[m2]** | **[m]** | **[m]** | **[-]** |
| 27 | 8,5 | 165,0 | 165,4 | 165,3 | 165,5 | 0,0105 | 1,0 | 8,3 | 27,1 | 0,30 | 0,60 |
| 26 | 8,5 | 164,2 | 165,2 | 165,1 | 165,3 | 0,0124 | 1,1 | 7,6 | 25,0 | 0,30 | 0,64 |
| 25 | 8,5 | 164,0 | 164,9 | 164,9 | 165,0 | 0,0296 | 1,9 | 4,6 | 13,3 | 0,34 | 1,01 |
| 24 | 8,5 | 163,5 | 164,7 | 164,3 | 164,7 | 0,0046 | 0,8 | 10,7 | 28,0 | 0,38 | 0,41 |
| 23 | 8,5 | 163,5 | 164,3 | 164,3 | 164,5 | 0,0284 | 1,9 | 4,6 | 12,8 | 0,35 | 1,00 |
| 22 | 8,5 | 163,0 | 163,9 | 163,8 | 164,0 | 0,0170 | 1,5 | 5,9 | 16,3 | 0,35 | 0,77 |
| 21 | 8,5 | 162,6 | 163,5 |  | 163,6 | 0,0130 | 1,4 | 6,0 | 14,2 | 0,42 | 0,69 |
| 20 | 8,5 | 162,5 | 163,4 |  | 163,5 | 0,0044 | 0,9 | 9,4 | 19,2 | 0,48 | 0,42 |
| 19 | 8,5 | 162,8 | 163,2 | 163,2 | 163,3 | 0,0301 | 1,7 | 5,1 | 17,9 | 0,28 | 1,00 |
| 18 | 8,5 | 162,0 | 163,0 | 162,7 | 163,0 | 0,0026 | 0,7 | 11,5 | 21,5 | 0,53 | 0,32 |
| 17 | 8,5 | 162,0 | 163,0 |  | 163,0 | 0,0024 | 0,8 | 10,9 | 17,6 | 0,61 | 0,32 |
| 16 | 8,5 | 161,6 | 162,9 |  | 163,0 | 0,0013 | 0,7 | 12,5 | 15,3 | 0,80 | 0,24 |
| 15 | 8,5 | 161,5 | 162,9 |  | 162,9 | 0,0047 | 0,9 | 9,2 | 18,8 | 0,48 | 0,42 |
| 14 | 8,5 | 161,5 | 162,8 |  | 162,9 | 0,0039 | 0,9 | 9,6 | 18,7 | 0,51 | 0,39 |
| 13 | 8,5 | 161,5 | 162,8 |  | 162,8 | 0,0020 | 0,7 | 11,6 | 18,3 | 0,62 | 0,29 |
| 12 | 8,5 | 161,5 | 162,8 |  | 162,8 | 0,0032 | 0,8 | 10,1 | 17,9 | 0,55 | 0,36 |
| 11 | 8,5 | 161,5 | 162,5 | 162,5 | 162,7 | 0,0297 | 1,9 | 4,5 | 12,6 | 0,35 | 1,01 |

**Tabla 4.3: Eje Hidráulico Estero Licura para** _**T**_ **=100 años****

| Perfil | Q | ZF | ZH | ZCr | ZB | J | V | A | L | Rh | Fr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **(m3/s)** | **[m]** | **[m]** | **[m]** | **[m]** | **[m/m]** | **[m/s]** | **[m2]** | **[m]** | **[m]** | **[-]** |
| 15 | 39,0 | 123,5 | 124,3 | 124,0 | 124,3 | 0,0023 | 0,7 | 58,6 | 117,7 | 0,5 | 0,3 |
| 14 | 39,0 | 123,2 | 124,1 |  | 124,1 | 0,0034 | 0,8 | 47,3 | 93,6 | 0,5 | 0,4 |
| 13 | 39,0 | 123,0 | 123,9 |  | 123,9 | 0,0044 | 0,9 | 43,4 | 91,2 | 0,5 | 0,4 |
| 12 | 39,0 | 122,5 | 123,6 |  | 123,7 | 0,0067 | 1,0 | 37,5 | 86,3 | 0,4 | 0,5 |
| 11 | 39,0 | 122,5 | 123,6 |  | 123,6 | 0,0022 | 0,7 | 55,8 | 101,1 | 0,6 | 0,3 |

**Tabla 4.4: Eje Hidráulico Quebrada Sin Nombre para** _**T**_ **=100 años****

| Col1 | Proyecto: LAT San Carlos - S/E Mulchén<br>Tema: MC Hidráulico Área Inundación. Esteros y Quebradas Hoja: 10 de 14<br>Línea de Transmisión | Col3 |
| --- | --- | --- |
|  | **Proyecto:** LAT San Carlos - S/E Mulchén <br>**Tema:** MC Hidráulico Área Inundación. Esteros y Quebradas<br>Línea de Transmisión<br> **Hoja:** 10 de 14 | **Hoja:** 10 de 14 |

**Tabla 2.1.: ****

| Estación | Ubicación | Col3 | Altitud | Información | Col6 |
| --- | --- | --- | --- | --- | --- |
| Estación | Lat. | Long. | msnm | Inicio | Fin |
| LOS ÁNGELES | 37° 30' 08'' | 72° 24' 30'' | 129 | 1963 | 2015 |
| MULCHÉN | 37° 42' 53'' | 72° 14' 37'' | 142 | 1980 | 2015 |
| SAN JOSÉ DE MUNILQUE | 37° 35' 09'' | 72° 19' 14'' | 120 | 1963 | 2015 |
| SAN CARLOS DE PURÉN | 37° 35' 43'' | 72° 16' 37'' | 155 | 1985 | 2015 |

**Tabla 4-1: Análisis estadístico de las distribuciones. Serie Precipitaciones****

| Distribución | Normal | Log<br>Normal | Pearson III | Log Pearson<br>III | Gumbel |
| --- | --- | --- | --- | --- | --- |
| Coeficiente R2 | 0,887 | 0,952 | 0,964 | 0,969 | 0,960 |
| <br>Calc /2<br>1- | 1,52 | 0,76 | 0,83 | 0,68 | 0,71 |

**Tabla 4-2: Precipitaciones Máximas Diarias (mm) para distintos períodos de****

| T<br>(años) | Pmáxd<br>(mm) |
| --- | --- |
| 10<br>50<br>100 | 125<br>165<br>180 |

**Tabla 5-1: ****

| Parámetro | Unidad | Estero<br>Las Diucas | Estero<br>Locura | Quebrada sin<br>nombre |
| --- | --- | --- | --- | --- |
| Cota superior<br>Cota inferior<br>Largo cauce principal<br>Pendiente<br>Área aportante | msnm<br>msnm<br>Km<br>m/m<br>Km2 | 301<br>172<br>1,8<br>0,07<br>2,3 | 300<br>135<br>4,7<br>0,04<br>13,5 | 330<br>158<br>1,0<br>0,17<br>1,3 |

**Tabla 5-2: Fórmulas para el cálculo del tiempo de concentración****

| Autor | Expresión |
| --- | --- |
| Normas Españolas |  |
| California Culverts Practice (1942) |  |
| Giandotti | <br> |

**Tabla 5-3: Cálculo del tiempo de Concentración.****

| Col1 | Tiempo de concentración (hrs) | Col3 | Col4 |
| --- | --- | --- | --- |
| Autor | Estero<br>Las Diucas | Estero<br>Licura | Quebrada sin<br>nombre |
| Normas Españolas<br>California<br>Giandotti<br>Adoptado | 0,8<br>0,3<br>1,4<br>0,5 | 1,8<br>0,8<br>3,0<br>1,2 | 0,4<br>0,1<br>0,8<br>0,2 |

**Tabla 5-4: Caudales Máximos Instantáneos (m** **[3]** **/s).****

| T [años] | DGA - AC | Verni King | V- K Modif | F. Rac. Modif | F. Rac. |
| --- | --- | --- | --- | --- | --- |
| 10<br>50<br>100 | 2.1<br>3.0<br>3.4 | 5.1<br>7.2<br>8.0 | 4.0<br>5.9<br>6.6 | 7.0<br>9.5<br>10.4 | 7.0<br>9.3<br>10.1 |

**Tabla 5-5: Caudales Máximos Instantáneos (m** **[3]** **/s).****

| T [años] | DGA - AC | Verni King | V- K Modif | F. Rac. Modif | F. Rac. |
| --- | --- | --- | --- | --- | --- |
| 10<br>50<br>100 | 13.3<br>19.0<br>21.4 | 27.2<br>38.4<br>42.8 | 21.6<br>31.7<br>35.3 | 27.8<br>37.5<br>41.3 | 27.8<br>36.8<br>40.1 |

**Tabla 5-6: Caudales Máximos Instantáneos (m** **[3]** **/s).****

| T [años] | DGA - AC | Verni King | V- K Modif | F. Rac. Modif | F. Rac. |
| --- | --- | --- | --- | --- | --- |
| 10<br>50<br>100 | 1.4<br>1.9<br>2.2 | 3.5<br>4.9<br>5.5 | 2.8<br>4.0<br>4.5 | 7.2<br>9.7<br>10.7 | 7.2<br>9.5<br>10.4 |

**Tabla 5-7: Caudales Máximos Instantáneos (m** **[3]** **/s).****

| Col1 | Qmi (m3/s) | Col3 | Col4 |
| --- | --- | --- | --- |
| T <br>(años) | Estero<br>Las Diucas | Estero<br>Licura | Quebrada sin<br>nombre |
| 10<br>50<br>100 | 5,5<br>7,5<br>8,5 | 25,5<br>35,5<br>39 | 5 <br>6,5<br>7 |
