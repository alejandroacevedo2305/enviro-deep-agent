---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 57
has_toc: True
has_tables: True
extraction_quality: high
---

**ANEXO 7**

**ESTUDIO DE AGUAS**

**ADENDA**
**“FRIGORÍFICO KARMAC”**

**COMUNA DE LAUTARO**
**REGIÓN DE LA ARAUCANÍA**

**ANEXO 7.1**
**INFORME DE MODELACIÓN HIDRÁULICA**

**ADENDA**
**“FRIGORÍFICO KARMAC”**

**COMUNA DE LAUTARO**
**REGIÓN DE LA ARAUCANÍA**

**INFORME DE MODELACIÓN HIDRÁULICA**

**PROYECTO FRIGORÍFICO KARMAC**

**REGIÓN DE LA ARAUCANÍA**

AGOSTO - 2022

CURICÓ - CHILE

**Índice**

1. INTRODUCCIÓN .................................................................................................................................................................................. 4

2. ANTECEDENTES DEL PROYECTO ................................................................................................................................................... 5

2.1. UBICACIÓN DEL PROYECTO .................................................................................................................................................. 5

2.2. HIDROLOGÍA REGIONAL ......................................................................................................................................................... 6

2.3. HIDROLOGÍA LOCAL ................................................................................................................................................................ 7

2.5. TOPOGRAFÍA DISPONIBLE ................................................................................................................................................... 10

2.5.1. Zona de análisis .................................................................................................................................................................. 10

2.6. VISITA A TERRENO ................................................................................................................................................................ 11

2.7. CAUDALES DE CRECIDA ....................................................................................................................................................... 13

2.7.1. TIEMPO DE CONCENTRACIÓN ........................................................................................................................................ 14

2.7.2. PRECIPITACIONES DE DISEÑO ....................................................................................................................................... 15

2.7.3. CAUDALES MÁXIMOS PARA ÁREAS APORTANTES ...................................................................................................... 21

4. METODOLOGÍA MODELACIÓN 1D .................................................................................................................................................. 22

4.1. Características geométricas del modelo .................................................................................................................................. 22

4.2. Estimación del coeficiente de rugosidad .................................................................................................................................. 23

4.3. Características de la modelación ............................................................................................................................................. 24

4.4. Caudales modelados ............................................................................................................................................................... 24

5. RESULTADOS ................................................................................................................................................................................... 25

5.1. Caudal de operación ................................................................................................................................................................ 25

5.2. Caudal de crecida .................................................................................................................................................................... 27

6. CONCLUSIÓN Y COMENTARIOS ..................................................................................................................................................... 29

Contacto : contacto@emergeingenieria.cl
**1**
Teléfono : 752313453

**Índice de figuras**

Figura 2.1 Ubicación del Proyecto................................................................................................................................................................. 5

Figura 2.2 Hidrología regional ....................................................................................................................................................................... 6

Figura 2.3 Hidrología local - Carta IGM G-072 Lautaro ................................................................................................................................ 7

Figura 2.4 Hidrología local- Detalle canal Pillanlelbún .................................................................................................................................. 8

Figura 2.5 Canal Pillanlelbún - Foto de terreno ............................................................................................................................................ 9

Figura 2.6 Topografía disponible ................................................................................................................................................................. 10

Figura 2.7 Visita a terreno proyecto “Proyecto Frigorífico Karmac” ............................................................................................................ 11

Figura 2.8 Áreas aportantes a la zona de estudio ....................................................................................................................................... 13

Figura 2.9 Estaciones meteorológicas cercanas al proyecto, isoyetas de prec. máxima diaria y clasificación de climas de Köppen ........ 15

Figura 4.1 Perfiles de modelación ............................................................................................................................................................... 22

Figura 5.1 Perfil Longitudinal Qoperacional ................................................................................................................................................ 26

Figura 5.2 Profundidad áreas de inundación Qoperacional ........................................................................................................................ 26

Figura 5.3 Perfil longitudinal Canal Pillanlelbún -QAALL ............................................................................................................................ 28

Figura 5.4 Perfil transversal Canal Pillanlelbún -QAALL ............................................................................... **¡Error! Marcador no definido.**

Figura 5.5 Profundidad área de inundación Qaguaslluvias ......................................................................................................................... 28

Contacto : contacto@emergeingenieria.cl
**2**
Teléfono : 752313453

**Índice de tablas**

Tabla 2.1 Datos de la cuenca donde se ubica el Proyecto ........................................................................................................................... 6

Tabla 2.2 Set fotográfico visita a terreno 02/06/2022 .................................................................................................................................. 12

Tabla 2.3 Parámetros morfométricos .......................................................................................................................................................... 14

Tabla 2.4 Fórmulas tiempo de concentración ............................................................................................................................................. 14

Tabla 2.5 Resultados tiempo de concentración .......................................................................................................................................... 15

Tabla 2.6 Datos estaciones meteorológicas cercanas ................................................................................................................................ 16

Tabla 2.7 Registro de precipitación máxima diaria, estación Lautaro ......................................................................................................... 16

Tabla 2.8 Resultados prueba de bondad de ajuste Kolmogorov-Smirnov .................................................................................................. 18

Tabla 2.9 Precipitaciones máximas diarias ................................................................................................................................................. 18

Tabla 2.10 Precipitaciones máximas diaria para distintos periodos de retorno .......................................................................................... 18

Tabla 2.11 Coeficientes de escorrentía (C) para T = 10 años .................................................................................................................... 19

Tabla 2.12 Coeficientes de escorrentía (C) para distintos periodos de retorno(T)...................................................................................... 19

Tabla 2.13 Resultados Método Racional para Área Aportante 1 ................................................................................................................ 21

Tabla 2.14 Resultados Método Racional para Área Aportante 2 ................................................................................................................ 21

Tabla 2.15 Resultados Método Racional para Área Aportante 3 ................................................................................................................ 21

Tabla 2.16 Caudales máximos (m [3] /s) ......................................................................................................................................................... 21

Tabla 4.1 Definición y valores para parámetros de la ecuación de Cowan ................................................................................................. 23

Tabla 4.2 Rugosidad asignada al modelo ................................................................................................................................................... 23

Tabla 4.3 Parámetros de modelación utilizados .......................................................................................................................................... 24

Tabla 4.4 Caudales de crecida .................................................................................................................................................................... 24

Tabla 5.1 Resultados caudal operacional (Q Op ) .......................................................................................................................................... 25

Tabla 5.2 Resultados caudal pluvial (Q AALL ) ................................................................................................................................................ 27

Contacto : contacto@emergeingenieria.cl
**3**
Teléfono : 752313453

**1.** **INTRODUCCIÓN**

Este estudio se realiza en marco al proyecto “Frigorífico Karmac” (en adelante “el Proyecto”) la cual es una planta certificada para la

producción de productos cárnicos que abastecen a todos los segmentos del mercado tanto a nivel nacional como internacional ubicada

en la comuna de Lautaro, región de la Araucanía.

En este informe se presentan los parámetros utilizados obtener la modelación 1D del cauce identificado según la carta IGM y la visita a

terreno. En base a la información obtenida desde el SEIA, la carta IGM correspondiente y la red hidrográfica del sector, se identificó un

cauce que bordea el área de estudio. Al tratarse de un canal (Canal Pillanlelbún), se evaluó tanto la situación con el caudal de captación

como con el caudal de crecida asociado a áreas aportantes pluviales para los meses de invierno. Lo anterior permitirá conocer el área de

inundación asociado a la ubicación de la planta. La modelación fue realizada utilizando el software de libre acceso HEC-RAS (Hydraulic

Engineering Center - River Analysis System), desarrollado por el US Corp Engineers, el cual es aceptado en proyectos hidráulicos por la

Dirección General de Aguas (DGA) y la Dirección de Obras Hidráulicas (DOH).

Contacto : contacto@emergeingenieria.cl
**4**
Teléfono : 752313453

**2.** **ANTECEDENTES DEL PROYECTO**

**2.1.** **UBICACIÓN DEL PROYECTO**

El Proyecto se encuentra emplazado en la comuna de Lautaro, provincia de Cautín, Región de la Araucanía.

En la Figura 2.1 se muestra la ubicación general y local del Proyecto.

**Figura 2.1 Ubicación del Proyecto**

Contacto : contacto@emergeingenieria.cl
**5**
Teléfono : 752313453

**2.2.** **HIDROLOGÍA REGIONAL**

La zona de estudio se encuentra al centro de la cuenca Río Imperial (código DGA-BNA 091), específicamente en la subcuenca Cautín

Alto (hasta antes junta R. Quepe) (código DGA-BNA 0912), en la subsubcuenca Río Cautín entre arriba junta Estero Guacolda y río Muco.

El sistema de cuencas se aprecia en la Figura 2.2 y la información de las cuencas mencionadas anteriormente se presenta en la Tabla

2.1.

**Figura 2.2 Hidrología regional**

**Tabla 2.1 Datos de la cuenca donde se ubica el Proyecto**

|Unidad|Nombre|Código<br>DGA|Área<br>(km2)|
|---|---|---|---|
|Cuenca|Río Imperial|091|12668,84|
|Subcuenca|Río Cautín Alto (hasta antes junta R. Quepe)|0912|3223,8|
|Subsubcuenca|Río Cautín entre arriba junta Estero Guacolda y río Muco|09124|267,06|

Contacto : contacto@emergeingenieria.cl
**6**
Teléfono : 752313453

**2.3.** **HIDROLOGÍA LOCAL**

La caracterización hidrográfica local, se realizó con el fin de identificar los principales cursos de agua en la zona de estudio, lo cual se

llevó a cabo con la carta IGM Lautaro (G-072) complementando con la red hidrográfica e información satelital disponible. De esta forma

se identificó la red de drenaje local (Figura 2.3).

**Figura 2.3 Hidrología local - Carta IGM G-072 Lautaro**

Se identifica que el proyecto se ubica en las cercanías de las riberas del río Cautín. Es posible verificar que existe un cauce que bordea

el área del proyecto por el oeste en dirección al sur que corresponde según simbología a un canal. De acuerdo a la información cartográfica

y documentación revisada, este cauce corresponde al Canal Pilllanlelbún. Si bien en la Carta IGM se observa como un canal continuo

proveniente desde el norte pasando por la ciudad de Lautaro, el canal Pillanlelbún nace en el río Cautín desde una bocatoma al sur de la

ciudad de Lautaro (Figura 2.4) y sigue su curso hacia el sur pasando por la ciudad de Temuco hasta conectar con el Canal imperial, que

Contacto : contacto@emergeingenieria.cl
**7**
Teléfono : 752313453

llega hasta el poblado de Nueva Imperial. El canal está diseñado para transportar 4,5 m [3] /s, de los cuales 3,5 m [3] /s corresponden a

satisfacer la demanda del mismo canal, mientras que 1 m [3] /s está destinado a abastecer al canal imperial [1]

**Figura 2.4 Hidrología local- Detalle canal Pillanlelbún**

_Fuente: Adaptado de informe “Transferencia de capacidad para constituir junta de vigilancia río cautín - Informe final” - Infraeco, Comisión_

_Nacional de Riego, Ministerio de Agricultura - Enero, 2016._

1 _Programa “Transferencia de capacidad para constituir junta de vigilancia río cautín - Informe final” - Infraeco, Comisión Nacional de_
_Riego, Ministerio de Agricultura - Enero, 2016._

Contacto : contacto@emergeingenieria.cl
**8**
Teléfono : 752313453

Se trata de un canal trapezoidal excavado en tierra, que en la actualidad se encuentra cubierto de vegetación según se verificó en la visita

a terreno como se muestra en la Figura 2.5.

**Figura 2.5 Canal Pillanlelbún - Foto de terreno**

Contacto : contacto@emergeingenieria.cl
**9**
Teléfono : 752313453

**2.5.** **TOPOGRAFÍA DISPONIBLE**

**2.5.1.** **Zona de análisis**

Se trabajo con la topografía disponible en la zona del proyecto. Esta abarca exclusivamente el canal dentro de los límites de la planta del

frigorífico, como se muestra en la Figura 2.6.

**Figura 2.6 Topografía disponible**

Contacto : contacto@emergeingenieria.cl
**10**
Teléfono : 752313453

**2.6.** **VISITA A TERRENO**

La visita a terreno se realizó el día 02 de junio de 2022, donde se constató la interacción de la hidrología local con la zona del proyecto,

obteniendo así, un set fotográfico georreferenciado que permite respaldar el trabajo de gabinete cuya distribución se muestra

espacialmente en la Figura 2.7.

**Figura 2.7 Visita a terreno proyecto “Proyecto Frigorífico Karmac”**

Contacto : contacto@emergeingenieria.cl
**11**
Teléfono : 752313453

En la Tabla 2.2, se presentan las fotografías referidas en la figura presentada anteriormente.

**Tabla 2.2 Set fotográfico visita a terreno 02/06/2022**

|Col1|Col2|
|---|---|
|**F-1:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta|**F-2:** Drenaje para aguas lluvias sector patio de planta|
|||
|**F-3:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta|**F-4:** Patio de carga, aguas escurren hacia drenajes que<br>trasladan RILes, hacia la planta de tratamiento (externo)|
|||
|**F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br>|**F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br>|

Contacto : contacto@emergeingenieria.cl
**12**
Teléfono : 752313453

**2.7.** **CAUDALES DE CRECIDA**

De acuerdo con la “ _Guías Metodológicas para Proyectos de Modificación de Cauces_ ” (DGA, 2016), la generalidad es que los canales

operen en primavera-verano mientras que las escorrentías máximas de aguas lluvias ocurren en los meses de invierno. Por lo tanto, si

bien el canal Pillanlelbún tiene un caudal de operación conocido, adicionalmente se obtuvieron áreas aportantes para evaluar la situación

del canal en los meses de invierno donde este capta aguas lluvias las cuales se muestran en la Figura 2.8.

**Figura 2.8 Áreas aportantes a la zona de estudio**

Cabe destacar que el área aportante 3 es una quebrada que se identifica en la carta IGM, mientras que las áreas 1 y 2 no tienen un cauce

con un trazado definido, pero son áreas que generan escurrimientos en dirección al canal. En la Tabla 2.3 se muestran los principales

parámetros morfométricos de las áreas aportantes delimitadas en la Figura 2.8, estos parámetros fueron obtenidos mediante análisis de

información geográfica obtenida con el software Arcgis v.10.3.

Contacto : contacto@emergeingenieria.cl
**13**
Teléfono : 752313453

**Tabla 2.3 Parámetros morfométricos**

Donde:

A t : Área total

|Área|A (km2)<br>t|L (km)|H (m)<br>máx|H (m)<br>min|
|---|---|---|---|---|
|Área aportante 1|0,152|0,368|260|240|
|Área aportante 2|0,511|0,915|265|220|
|Área aportante 3|1,296|2,109|274|226|

L : Longitud cauce principal
H max : Cota mayor área aportante
H min : Cota menor área aportante

**2.7.1.** **TIEMPO DE CONCENTRACIÓN**

La determinación del tiempo de concentración del área aportante se calculó por medio de expresiones producto de resultados empíricos,

las que se indican a continuación:

**Tabla 2.4 Fórmulas tiempo de concentración**

|Fórmula|Expresión|Aplicación|
|---|---|---|
|Kirpich|tc= 0,066 ∗~~( ~~L<br>√S<br>~~)~~<br>0,77<br>|Cuencas rurales relativamente planas con escurrimiento<br>preferentemente superficial|
|Normas españolas|tc= 0,3 ∗( L<br>Sp<br>1 4<br>⁄ )<br>0,76<br>|Cuencas de 1 km2 hasta 3.000 km2 con tiempos de<br>concentración desde los 15 minutos hasta las 24 horas|
|California Culverts Practice|tc= 0,95 ∗(L3<br>H)<br>0,385<br>|Adaptación fórmula de Kirpich. Cuencas rurales no<br>planas con escurrimiento preferentemente concentrado|
|Giandotti|tc= (4√A+ 1,5L)<br>(0,8√H)<br>|Siempre queL/3,6 ≥ tc≥L/5,4. Cuencas pequeñas<br>con pendiente|

Donde:

t c : Tiempo de concentración (hr)
L : Longitud cauce principal (km)
S : Pendiente (m/m)
A : Área pluvial aportante (km [2] )
H : Diferencia de nivel total entre cotas extremas (m)
S p : Pendiente media del cauce principal

Empleando las expresiones expuestas, los resultados obtenidos para el área aportante se presentan en la siguiente tabla:

Contacto : contacto@emergeingenieria.cl
**14**
Teléfono : 752313453

**Tabla 2.5 Resultados tiempo de concentración**

|Área|Kirpich|Normas<br>españolas|California Culverts<br>Practice|Giandotti|Col6|tc adoptado<br>(hr)|tc adoptado<br>(min)|
|---|---|---|---|---|---|---|---|
|**Área**|**Kirpich**|**Normas**<br>**españolas**|**California Culverts**<br>**Practice**|**tc**|**L/3.6≥tc≥L/5.4**|**L/3.6≥tc≥L/5.4**|**L/3.6≥tc≥L/5.4**|
|Área aportante 1|0,094|-|0,094|0,590|No cumple|0,167|10|
|Área aportante 2|0,197|-|0,198|0,789|No cumple|0,197|11,79|
|Área aportante 3|0,503|1,085|0,507|1,392|No cumple|0,503|30,18|

Debido a las condiciones del terreno, la aplicabilidad de cada fórmula y el orden de magnitud de los resultados, como tiempo de

concentración se adoptó la fórmula de Kirpich. En el caso del área aportante 1, se adoptó un tiempo de concentración de 10 minutos,

correspondiente al valor mínimo según lo indicado en el “Manual de Carreteras Volumen N°3, MOP (2018)”.

**2.7.2.** **PRECIPITACIONES DE DISEÑO**

2.7.2.1. Registros de precipitaciones

El cálculo de las precipitaciones máximas se realizó verificando las estaciones cercanas al lugar de estudio y que cumplieran con ciertas

características. Estas son: que se localicen en las proximidades del proyecto, que se encuentren en estado vigente y que posean una

altitud similar a la zona de estudio. En la Figura 2.9 se presentan las estaciones cercanas a la zona del proyecto que cumplen con estos

requerimientos, junto a las isoyetas de precipitación media anual y la clasificación climática de Köppen. En la Tabla 2.6 se presentan los

datos de las estaciones meteorológicas presentadas en el mapa.

**Figura 2.9 Estaciones meteorológicas cercanas al proyecto, isoyetas de prec. máxima diaria y clasificación de climas de**

**Köppen**

Contacto : contacto@emergeingenieria.cl
**15**
Teléfono : 752313453

**Tabla 2.6 Datos estaciones meteorológicas cercanas**

|Código<br>estación|Nombre Estación|Institución|Coordenadas WGS 84<br>UTM18S|Col5|Altitud<br>(msnm)|Vigencia|Fecha<br>Inicio|
|---|---|---|---|---|---|---|---|
|**Código**<br>**estación**|**Nombre Estación**|**Institución**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|09124001-7|Lautaro|DGA|722.862|5.732.790|200|Vigente|01/07/1953|
|09111002-4|Quillén|DGA|728.005|5.739.450|285|Vigente|01/11/1959|
|09112000-3|Perquenco|DGA|728.966|5.744.488|290|Vigente|01/05/2002|

Al observar el plano de isoyetas, es posible verificar que las tres estaciones mencionadas en la Tabla 2.6 presentan similares alturas y

distancia respecto al proyecto y se encuentran entre los valores de precipitación máxima diaria de entre 80 y 90 mm. En tanto, al contrastar

esta información con la clasificación de clima de Köppen, se concluye que la zona de estudio y las estaciones meteorológicas se

encuentran en la misma zona climática la cual corresponde a clima mediterráneo de lluvia invernal (Csb).

Al verificar la disponibilidad de datos en las tres estaciones, la estación “Perquenco” presenta información disponible entre los años 2002

y 2020 mientras que la estación “Quillén” tiene un registro completo entre los años 1959 y 2020, completando 62 años de información.

Finalmente, la estación “Lautaro”, presenta un registro completo a partir del año 1953, siendo la que posee más información disponible

en la cercanía del proyecto con 68 años de información. Dado lo anterior, el análisis de precipitaciones se realiza utilizando la estación

“Lautaro” (Código BNA: 09124001-7).

Los registros de precipitación máxima diaria anual entre los años 1953 y 2020 en la estación seleccionada se presentan en la Tabla 2.7.

<!-- INICIO TABLA 2.7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Lautaro” (Código BNA: 09124001-7). Los registros de precipitación máxima diaria anual entre los años 1953 y 2020 en la estación seleccionada se presentan en la Tabla 2.7. -->

**Tabla 2.7: Registro de precipitación máxima diaria, estación Lautaro****

| Año | Fecha | Precipitación máxima diaria<br>(mm) |
| --- | --- | --- |
| 1953 | 15/07 | 42,00 |
| 1954 | 22/06 | 76,00 |
| 1955 | 13/02 | 32,00 |
| 1956 | 01/01 | 50,00 |
| 1957 | 07/06 | 45,00 |
| 1958 | 23/09 | 64,00 |
| 1959 | 24/01 | 65,00 |
| 1960 | 16/05 | 85,00 |
| 1961 | 15/07 | 48,00 |
| 1962 | 29/08 | 40,50 |
| 1963 | 29/10 | 58,50 |
| 1964 | 20/05 | 47,50 |
| 1965 | 16/06 | 71,00 |
| 1966 | 13/06 | 61,50 |
| 1967 | 14/07 | 62,00 |
| 1968 | 07/09 | 55,00 |
| 1969 | 12/08 | 50,00 |
| 1970 | 15/06 | 64,00 |
| 1971 | 28/06 | 51,00 |
| 1972 | 04/07 | 59,00 |
| 1973 | 20/10 | 52,00 |
| 1974 | 06/06 | 62,00 |
| 1975 | 17/06 | 47,00 |
| 1976 | 24/12 | 49,90 |

<!-- Estadísticas: 24 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Contacto : contacto@emergeingenieria.cl **17** Teléfono : 752313453 -->
<!-- FIN TABLA 2.7 -->


**Tabla 2.7 Registro de precipitación máxima diaria, estación Lautaro**

Contacto : contacto@emergeingenieria.cl
**16**
Teléfono : 752313453

|Año|Fecha|Precipitación máxima diaria<br>(mm)|
|---|---|---|
|1953|15/07|42,00|
|1954|22/06|76,00|
|1955|13/02|32,00|
|1956|01/01|50,00|
|1957|07/06|45,00|
|1958|23/09|64,00|
|1959|24/01|65,00|
|1960|16/05|85,00|
|1961|15/07|48,00|
|1962|29/08|40,50|
|1963|29/10|58,50|
|1964|20/05|47,50|
|1965|16/06|71,00|
|1966|13/06|61,50|
|1967|14/07|62,00|
|1968|07/09|55,00|
|1969|12/08|50,00|
|1970|15/06|64,00|
|1971|28/06|51,00|
|1972|04/07|59,00|
|1973|20/10|52,00|
|1974|06/06|62,00|
|1975|17/06|47,00|
|1976|24/12|49,90|

Contacto : contacto@emergeingenieria.cl
**17**
Teléfono : 752313453

|Año|Fecha|Precipitación máxima diaria<br>(mm)|
|---|---|---|
|1977|07/05|99,00|
|1978|02/07|53,00|
|1979|29/08|62,50|
|1980|13/05|72,00|
|1981|06/05|86,00|
|1981|03/06|50,00|
|1983|28/05|48,50|
|1984|01/05|100,00|
|1985|23/05|56,00|
|1986|25/11|42,00|
|1987|26/03|63,00|
|1988|17/01|50,00|
|1989|28/06|49,50|
|1990|09/10|51,50|
|1991|08/04|73,00|
|1992|04/06|90,00|
|1993|16/05|85,00|
|1994|23/07|50,50|
|1995|25/06|59,00|
|1996|23/08|53,00|
|1997|27/06|110,50|
|1998|14/08|37,40|
|1999|19/06|43,50|
|2000|02/05|32,60|
|2001|09/03|34,70|
|2002|23/08|90,00|
|2003|16/11|50,00|
|2004|22/07|70,00|
|2005|06/06|50,00|
|2006|06/06|48,00|
|2007|21/06|47,00|
|2008|31/08|81,00|
|2009|13/06|71,00|
|2010|23/07|37,00|
|2011|12/04|59,50|
|2012|12/06|55,50|
|2013|30/05|47,00|
|2014|22/01|56,00|
|2015|01/06|72,00|
|2016|13/07|37,50|
|2017|16/06|66,00|
|2018|16/03|34,00|
|2019|27/06|63,00|
|2020|09/07|52,00|

2.7.2.2. Análisis de frecuencias

Los datos de precipitación de la estación seleccionada fueron analizados a través del software Hydrognomon V.4, donde se realizó la

prueba de bondad de ajuste de Kolmogorov-Smirnov para las distribuciones recomendadas por la DGA según el documento “Guías

Metodológicas para Proyectos de Modificación de Cauces (2016)”, obteniendo los resultados mostrados en la Tabla 2.8.

<!-- INICIO TABLA 2.8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- prueba de bondad de ajuste de Kolmogorov-Smirnov para las distribuciones recomendadas por la DGA según el documento “Guías Metodológicas para Proyectos de Modificación de Cauces (2016)”, obteniendo los resultados mostrados en la Tabla 2.8. -->

**Tabla 2.8: Resultados prueba de bondad de ajuste Kolmogorov-Smirnov****

| Test Kolmogorov-Smirnoff | a=1% | a=5% | a=10% | Porcentaje Alcanzado | Dmax |
| --- | --- | --- | --- | --- | --- |
| Normal | Aceptado | Aceptado | Aceptado | 28,54% | 0,11956 |
| Log Normal | Aceptado | Aceptado | Aceptado | 81,89% | 0,07667 |
| Pearson III | Aceptado | Aceptado | Aceptado | 71,63% | 0,08452 |
| Gumbel | Aceptado | Aceptado | Aceptado | 81,37% | 0,0771 |
| Log Pearson III | Aceptado | Aceptado | Aceptado | **85,19%** | 0,07387 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo con los resultados obtenidos mostrados en la Tabla 2.8, la distribución que presenta el mayor ajuste en comparación a las restantes es la Log Pearson III que se muestra en negrita. En la Tabla 2.9 se muestran las precipitaciones obtenidas para distintos -->
<!-- FIN TABLA 2.8 -->


**Tabla 2.8 Resultados prueba de bondad de ajuste Kolmogorov-Smirnov**

|Test Kolmogorov-Smirnoff|a=1%|a=5%|a=10%|Porcentaje Alcanzado|Dmax|
|---|---|---|---|---|---|
|Normal|Aceptado|Aceptado|Aceptado|28,54%|0,11956|
|Log Normal|Aceptado|Aceptado|Aceptado|81,89%|0,07667|
|Pearson III|Aceptado|Aceptado|Aceptado|71,63%|0,08452|
|Gumbel|Aceptado|Aceptado|Aceptado|81,37%|0,0771|
|Log Pearson III|Aceptado|Aceptado|Aceptado|**85,19%**|0,07387|

De acuerdo con los resultados obtenidos mostrados en la Tabla 2.8, la distribución que presenta el mayor ajuste en comparación a las

restantes es la Log Pearson III que se muestra en negrita. En la Tabla 2.9 se muestran las precipitaciones obtenidas para distintos

periodos de retorno en la estación “Lautaro” con la distribución seleccionada.

**Tabla 2.9 Precipitaciones máximas diarias**

|Periodo de retorno|Precipitación máxima diaria (mm)|
|---|---|
|**T (años)**|**Lautaro**|
|2|55,70|
|5|70,67|
|10|80,59|
|20|90,10|
|25|93,12|
|50|102,42|
|100|111,64|
|150|117,03|
|200|120,84|

2.7.2.3. Precipitaciones máximas de diseño

A partir de las precipitaciones máximas diarias presentadas en la Tabla 2.10, se realizó un ajuste para obtener precipitaciones máximas

en 24 horas a través del coeficiente de corrección 1,1 según lo indicado en el “Manual de Carreteras Volumen N°3, MOP (2018)”.

**Tabla 2.10 Precipitaciones máximas diaria para distintos periodos de retorno**

|Periodo de retorno (años)|Precipitación máxima diaria (mm)|Precipitación máxima 24 horas (mm)|
|---|---|---|
|2|55,70|61,26|
|5|70,67|77,74|
|10|80,59|88,65|
|20|90,10|99,11|
|25|93,12|102,43|
|50|102,42|112,66|
|100|111,64|122,81|
|150|117,03|128,73|
|200|120,84|132,92|

Contacto : contacto@emergeingenieria.cl
**18**
Teléfono : 752313453

2.7.2.4. MÉTODO RACIONAL (Cuencas < 20 km [2] )

La fórmula Racional es un método ampliamente conocido en hidrología y se recomienda su uso en cuencas relativamente pequeñas,

menores que 20 km [2] . A continuación, se detallan los parámetros utilizados en la aplicación de este método:

**a)** **Coeficiente de escorrentía**

El coeficiente de escorrentía asociado a distintos periodos de retorno se obtuvo según los dispuesto en “Manual de Carreteras Volumen

N°3, MOP (2018)”. Los distintos factores que componen el coeficiente de escorrentía para un en periodo de retorno de 10 años se

presentan en la Tabla 2.11

**Tabla 2.11 Coeficientes de escorrentía (C) para T = 10 años**

_Fuente: Tabla 3.702.503.B “Manual de Carreteras Volumen N°3, MOP,2018”_

|Factor|Extremo|Alto|Normal|Bajo|Valor adoptado|
|---|---|---|---|---|---|
|Relieve|0,28-0,35|0,20-0,28|0,14-0,20|0,08-0,14|0,08|
|Relieve|Escarpado con<br>pendientes<br>mayores que 30%|Montañoso con<br>pendientes entre 10 y<br>30%|Con cerros y<br>pendientes entre<br>5 y 10%|Relativamente plano<br>con pendientes<br>menores al 5%|Relativamente plano<br>con pendientes<br>menores al 5%|
|Infiltración|0,12-0,16|0,08-0,12|0,06-0,08|0,04-0,06|0,06|
|Infiltración|Suelos rocosos, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable|Suelos arcillosos o<br>limosos con baja<br>capacidad de<br>infiltración, mal<br>drenados|Normales, bien<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos|Suelos profundos de<br>arena u otros suelos<br>bien drenados con alta<br>capacidad de infiltración|Suelos profundos de<br>arena u otros suelos<br>bien drenados con alta<br>capacidad de infiltración|
|Cobertura<br>vegetal|0,12-0,16|0,08-0,12|0,06-0,08|0,04-0,06|0,08|
|Cobertura<br>vegetal|Cobertura escasa,<br>terreno sin<br>vegetación o<br>escasa cobertura|Poca vegetación<br>terrenos cultivados o<br>naturales, menos del<br>20% del área con<br>buena cobertura<br>vegetal|Regular a buena;<br>50% del área con<br>praderas o<br>bosques, no más<br>del 50% cultivado|Buena a excelente;<br>90% del área con<br>praderas, bosques o<br>cobertura equivalente|Buena a excelente;<br>90% del área con<br>praderas, bosques o<br>cobertura equivalente|
|Almacenamiento<br>superficial|0,10-0,12|0,08-0,10|0,06-0,08|0,04-0,06|0,08|
|Almacenamiento<br>superficial|Despreciable,<br>pocas depresiones<br>superficiales sin<br>zonas húmedas|Baja, sistema de<br>cauces superficiales<br>pequeños bien<br>definidos, sin zonas<br>húmedas|Normal;<br>posibilidad de<br>almacenamiento<br>buena, zonas<br>húmedas,<br>pantanos, lagunas<br>y lagos|Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas<br>planicies de inundación<br>o gran cantidad de<br>zonas húmedas,<br>lagunas o pantanos|Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas<br>planicies de inundación<br>o gran cantidad de<br>zonas húmedas,<br>lagunas o pantanos|
|Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25|Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25|Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25|Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25|Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25|Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25|

Los coeficientes de escorrentía utilizados para cada periodo de retorno analizado se aprecian a continuación:

**Tabla 2.12 Coeficientes de escorrentía (C) para distintos periodos de retorno(T)**

Contacto : contacto@emergeingenieria.cl
**19**
Teléfono : 752313453

|Años|C(T)|
|---|---|
|2|0,3|
|5|0,3|
|10|0,3|
|25|0,33|

**a)** **Coeficiente de duración**

|50|0,36|
|---|---|
|100|0,375|

Para obtener la precipitación con periodo de retorno T años y duración de una hora se consideró el coeficiente de duración de la ciudad

de Temuco indicado en la Tabla 3.702.403.A del “Manual de Carreteras Volumen N°3, MOP, 2021” el que tiene un valor de CD t,1 hr =

0,21 .

**a)** **Intensidad de lluvia**

La intensidad de las precipitaciones obtenidas para el tiempo de concentración (tc) y cada periodo de retorno se obtiene por medio de la

siguiente expresión:

T

T = [P] [tc]

i tc

t c

Donde:
i tcT

i tcT : Intensidad con periodo de retorno T, asociada a una duración tc horas (mm/hr)

P tcT : Precipitación con periodo de retorno T, asociada a una duración tc horas (mm)

P tcT : Precipitación con periodo de retorno T, asociada a una duración tc horas (mm)

t c : Tiempo de concentración de la cuenca (hr)

**b)** **Caudal para cada periodo de retorno**

Para estimar los caudales máximos de crecida, se emplea la siguiente expresión:

T ∗A

Q= [C(T) ∗i] [tc]

3,6

Donde:
Q : Caudal instantáneo máximo de periodo de retorno T (m [3] /s)
C : Coeficiente de escorrentía asociada al periodo de retorno T
i tcT : Intensidad media de lluvia asociada al periodo de retorno T y una duración igual al tiempo de concentración de la cuenca

pluvial (mm/hr)
A : Área pluvial aportante (km [2] )

Contacto : contacto@emergeingenieria.cl
**20**
Teléfono : 752313453

En las Tabla 2.13, Tabla 2.14 y Tabla 2.15 se muestran los resultados obtenidos empleando el método racional para las áreas aportantes
1, 2 y 3.

**Tabla 2.13 Resultados Método Racional para Área Aportante 1**

|Años|C(T)|CD (Bell)<br>tc|PT (mm)<br>tc|iT (mm/hr)<br>tc|Q(m3/s)|
|---|---|---|---|---|---|
|2|0,3|0,46|5,71|34,18|0,43|
|5|0,3|0,46|7,36|44,07|0,56|
|10|0,3|0,46|8,61|51,54|0,65|
|25|0,33|0,46|10,26|61,43|0,86|
|50|0,36|0,46|11,51|68,90|1,05|
|100|0,375|0,46|12,76|76,38|1,21|

**Tabla 2.14 Resultados Método Racional para Área Aportante 2**

|Años|C(T)|CD (Bell)<br>tc|PT (mm)<br>tc|iT (mm/hr)<br>tc|Q(m3/s)|
|---|---|---|---|---|---|
|2|0,3|0,50|6,20|31,56|1,34|
|5|0,3|0,50|8,00|40,69|1,73|
|10|0,3|0,50|9,35|47,59|2,03|
|25|0,33|0,50|11,15|56,72|2,66|
|50|0,36|0,50|12,50|63,62|3,25|
|100|0,375|0,50|13,86|70,52|3,75|

**Tabla 2.15 Resultados Método Racional para Área Aportante 3**

|Años|C(T)|CD (Bell)<br>tc|PT (mm)<br>tc|iT (mm/hr)<br>tc|Q(m3/s)|
|---|---|---|---|---|---|
|2|0,3|0,77|9,49|18,86|2,04|
|5|0,3|0,77|12,23|24,31|2,63|
|10|0,3|0,77|14,30|28,44|3,07|
|25|0,33|0,77|17,05|33,89|4,03|
|50|0,36|0,77|19,12|38,02|4,93|
|100|0,375|0,77|21,20|42,14|5,69|

**2.7.3.** **CAUDALES MÁXIMOS PARA ÁREAS APORTANTES**

En la Tabla 2.16 se muestran los caudales máximos para un periodo de retorno de 100 años obtenidos para las áreas aportantes

mostradas en la Figura 2.8.

**Tabla 2.16 Caudales máximos (m** **[3]** **/s)**

|Periodo de retorno<br>(años)|Área aportante 1|Área aportante 2|Área aportante 3|
|---|---|---|---|
|**100**<br>|1,21|3,75|5,69|

Contacto : contacto@emergeingenieria.cl
**21**
Teléfono : 752313453

**4.** **METODOLOGÍA MODELACIÓN 1D**

Para la modelación hidrológica del canal identificado, se utilizó el software de libre acceso HEC-RAS (Hydraulic Engineering CenterRiver Analysis System), desarrollado por el US Corp Engineers, el cual resuelve la ecuación unidimensional del balance de energía, y en

situaciones donde la superficie del agua varía rápidamente se utiliza la ecuación de momento.

Los datos requeridos para la modelación son: (1) geometría del tramo en estudio, (2) rugosidad relativa del tramo a modelar (n de

Manning), (3) pendiente media aguas abajo y aguas arriba de la zona de interés, dependiendo del régimen del flujo.

**4.1.** **Características geométricas del modelo**

Se realizó un modelo, abarcando una longitud de 700 metros del cauce en estudio dentro de la limitación de la topografía disponible del

sector. En cuanto a la caracterización geométrica se utilizó el levantamiento topográfico disponible, caracterizado por medio de perfiles

transversales en sentido del escurrimiento, los cuales fueron extraídos cada 20 metros, con un ancho de 20 metros (Figura 4.1)

**Figura 4.1 Perfiles de modelación**

Contacto : contacto@emergeingenieria.cl
**22**
Teléfono : 752313453

**4.2.** **Estimación del coeficiente de rugosidad**

El coeficiente de rugosidad para el cauce principal se obtuvo mediante el método de Cowan, el cual estima el número de Manning a partir

de la separación de diversos factores, dado por la siguiente ecuación:

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m 5

La definición y los valores de los parámetros de dicha relación se definen en la siguiente tabla:

**Tabla 4.1 Definición y valores** **para** **parámetros** **de la** **ecuación de** **Cowan**

|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Material del lecho|Tierra|n0|0,02|
|Material del lecho|Roca cortada|Roca cortada|0,025|
|Material del lecho|Grava fina|Grava fina|0,024|
|Material del lecho|Grava gruesa|Grava gruesa|0,028|
|Grado de irregularidad perímetro mojado|Despreciable|n1|0|
|Grado de irregularidad perímetro mojado|Leve|Leve|0,001-0,005|
|Grado de irregularidad perímetro mojado|Moderado|Moderado|0,006-0,010|
|Grado de irregularidad perímetro mojado|Alto|Alto|0,011-0,020|
|Variación de las secciones|Graduales|n2|0|
|Variación de las secciones|Alternándose ocasionalmente|Alternándose ocasionalmente|0,001-0,005|
|Variación de las secciones|Alternándose frecuentemente|Alternándose frecuentemente|0,010-0,015|
|Efecto relativo de las obstrucciones|Despreciable|n3|0-0,004|
|Efecto relativo de las obstrucciones|Leve|Leve|0,005-0,015|
|Efecto relativo de las obstrucciones|Apreciable|Apreciable|0,020-0,030|
|Efecto relativo de las obstrucciones|Alto|Alto|0,040-0,060|
|Densidad de vegetación|Baja|n4|0,005-0,010|
|Densidad de vegetación|Media|Media|0,010-0,025|
|Densidad de vegetación|Alta|Alta|0,025-0,050|
|Densidad de vegetación|Muy alta|Muy alta|0,050-0,100|
|Sinuosidad y frecuencia de meandros|Leve|m5|1|
|Sinuosidad y frecuencia de meandros|Apreciable|Apreciable|1,15|
|Sinuosidad y frecuencia de meandros|Alto|Alto|1,3|

En la Tabla 4.2 se presentan los valores de los parámetros para el coeficiente de rugosidad (n) determinado mediante el método de

Cowan en el cauce analizado.

**Tabla 4.2 Rugosidad asignada al modelo**

|n<br>0|n<br>1|n<br>2|n<br>3|n<br>4|m<br>5|Valor adoptado|
|---|---|---|---|---|---|---|
|0,02|0,001|0,001|0,015|0,02|1|0,057|

Contacto : contacto@emergeingenieria.cl
**23**
Teléfono : 752313453

**4.3.** **Características de la modelación**

Dado que no se observa la presencia de grandes obstrucciones ni cambios bruscos en el eje del flujo, se consideran los coeficientes de

contracción y expansión C CON = 0,1 y C EXP = 0,3 sugeridos por defecto en el software HEC-RAS según la guía “ _Flow Transitions in Bridge_

_Backwater Analysis_, Hydrologic Engineering Center (HEC), 1995”.

En la Tabla 4.3 se aprecian las condiciones de borde ingresadas al modelo, las cuales se asignaron aguas abajo utilizando la pendiente

promedio a partir de la topografía utilizada, considerando un régimen de flujo subcrítico.

**Tabla 4.3 Parámetros de modelación utilizados**

|Cauce|Condición de borde|Tipo de régimen|
|---|---|---|
|**Cauce**|**Aguas abajo**|**Aguas abajo**|
|**Canal Pillanlelbún**|0,0029|Subcrítico|

**4.4.** **Caudales modelados**

Como fue mencionado anteriormente, dado que el cauce en estudio se trata de un canal con un caudal de operación conocido en los

meses de primavera-verano, adicionalmente se realizó un análisis estadístico para el aporte de aguas lluvias durante los meses de

invierno.

Finalmente, se modelaron dos situaciones, utilizando los caudales de crecida con periodo de retorno T=100 años y el caudal captado por

la bocatoma Pillanlelbún en el sector, los cuales se muestran en la Tabla 4.4 según el perfil en que se considera cada uno.

**Tabla 4.4 Caudales de crecida**

|Escenario|Perfil|Q (m3/s)|
|---|---|---|
|Qoperacional|700|4,5|
|Qaguaslluvias<br>|700|1,21|
|Qaguaslluvias<br>|500|4,96|
|Qaguaslluvias<br>|20|10,65|

Contacto : contacto@emergeingenieria.cl
**24**
Teléfono : 752313453

**5.** **RESULTADOS**

**5.1.** **Caudal de operación**

A continuación, se presenta los resultados obtenidos para el caudal de captación (Q Op ) en los perfiles analizados.

**Tabla 5.1 Resultados caudal operacional (Q** **Op** **)**

|Perfil|Q total<br>(m3/s)|Cota de<br>fondo<br>(m.s.n.m.)|Cota de<br>agua<br>(m.s.n.m.)|Pendiente<br>de energía<br>(m/m)|Velocidad<br>(m/s)|Fr|
|---|---|---|---|---|---|---|
|**0 **|4,5|204,04|205,24|0,00290|0,82|0,26|
|**20**|4,5|204,04|205,30|0,00275|0,81|0,25|
|**40**|4,5|204,13|205,36|0,00266|0,80|0,25|
|**60**|4,5|204,14|205,41|0,00245|0,77|0,24|
|**80**|4,5|204,11|205,46|0,00198|0,72|0,22|
|**100**|4,5|204,19|205,50|0,00220|0,75|0,23|
|**120**|4,5|204,21|205,54|0,00200|0,72|0,22|
|**140**|4,5|204,21|205,58|0,00185|0,71|0,21|
|**160**|4,5|204,28|205,62|0,00197|0,72|0,21|
|**180**|4,5|204,30|205,66|0,00193|0,72|0,21|
|**200**|4,5|204,31|205,70|0,00170|0,68|0,20|
|**220**|4,5|204,32|205,73|0,00160|0,67|0,19|
|**240**|4,5|204,34|205,77|0,00148|0,65|0,19|
|**260**|4,5|204,36|205,80|0,00156|0,66|0,19|
|**280**|4,5|205,22|205,76|0,04270|1,99|0,95|
|**300**|4,5|205,54|206,30|0,01238|1,31|0,52|
|**320**|4,5|205,60|206,51|0,00653|1,08|0,38|
|**340**|4,5|205,62|206,63|0,00547|1,03|0,35|
|**360**|4,5|205,38|206,73|0,00255|0,78|0,25|
|**380**|4,5|205,21|206,78|0,00141|0,64|0,19|
|**400**|4,5|205,27|206,81|0,00112|0,59|0,16|
|**420**|4,5|205,50|206,83|0,00184|0,69|0,21|
|**440**|4,5|205,45|206,87|0,00161|0,66|0,20|
|**460**|4,5|205,38|206,90|0,00134|0,63|0,18|
|**480**|4,5|205,34|206,93|0,00117|0,60|0,17|
|**500**|4,5|205,31|206,95|0,00119|0,60|0,17|
|**520**|4,5|205,63|206,98|0,00200|0,72|0,22|
|**540**|4,5|205,95|207,02|0,00429|0,94|0,32|
|**560**|4,5|206,27|207,12|0,00876|1,21|0,45|
|**580**|4,5|206,28|207,28|0,00554|1,04|0,36|
|**600**|4,5|206,07|207,37|0,00265|0,81|0,25|
|**620**|4,5|205,86|207,43|0,00187|0,71|0,21|
|**640**|4,5|205,91|207,47|0,00232|0,73|0,22|
|**660**|4,5|206,11|207,51|0,00245|0,76|0,23|
|**680**|4,5|206,16|207,56|0,00224|0,75|0,22|
|**700**|4,5|206,11|207,60|0,00165|0,68|0,19|

Contacto : contacto@emergeingenieria.cl
**25**
Teléfono : 752313453

**Figura 5.1 Perfil Longitudinal Qoperacional**

Según los resultados obtenidos para el caudal operacional, no se presentan desbordes en ningún perfil del canal, manteniendo

velocidades bajas, exceptuando zonas con cambios bruscos de pendiente como se observa en los perfiles 280 y 560, donde existe una

variación del fondo observable en el perfil longitudinal (Figura 5.1). Respecto a la profundidad del escurrimiento, está alcanza una

profundidad máxima de 1,64 metros y el flujo se concentra exclusivamente en la geometría del canal sin desbordes (Figura 5.2).

**Figura 5.2 Profundidad áreas de inundación Qoperacional**

Contacto : contacto@emergeingenieria.cl
**26**
Teléfono : 752313453

**5.2.** **Caudal de crecida**

A continuación, se presenta los resultados obtenidos para el caudal pluvial (Q AALL ), en los perfiles analizados.

**Tabla 5.2 Resultados caudal pluvial (Q** **AALL** **)**

|Perfil|Q total (m3/s)|Cota de fondo<br>(m.s.n.m.)|Cota de agua<br>(m.s.n.m.)|Pendiente de<br>energía (m/m)|Velocidad (m/s)|Fr|
|---|---|---|---|---|---|---|
|**0 **|10,65|204,04|206,04|0,00290|1,05|0,26|
|**20**|10,65|204,04|206,10|0,00286|1,05|0,26|
|**40**|4,96|204,13|206,18|0,00057|0,47|0,12|
|**60**|4,96|204,14|206,19|0,00059|0,48|0,12|
|**80**|4,96|204,11|206,20|0,00052|0,46|0,11|
|**100**|4,96|204,19|206,21|0,00061|0,49|0,12|
|**120**|4,96|204,21|206,23|0,00059|0,47|0,12|
|**140**|4,96|204,21|206,24|0,00062|0,49|0,12|
|**160**|4,96|204,28|206,25|0,00067|0,50|0,13|
|**180**|4,96|204,30|206,26|0,00068|0,51|0,13|
|**200**|4,96|204,31|206,28|0,00064|0,49|0,12|
|**220**|4,96|204,32|206,29|0,00065|0,50|0,12|
|**240**|4,96|204,34|206,30|0,00063|0,49|0,12|
|**260**|4,96|204,36|206,32|0,00067|0,49|0,13|
|**280**|4,96|205,22|206,32|0,00394|0,92|0,31|
|**300**|4,96|205,54|206,42|0,00931|1,22|0,46|
|**320**|4,96|205,60|206,58|0,00614|1,09|0,37|
|**340**|4,96|205,62|206,70|0,00539|1,06|0,35|
|**360**|4,96|205,38|206,80|0,00258|0,81|0,25|
|**380**|4,96|205,21|206,85|0,00147|0,67|0,19|
|**400**|4,96|205,27|206,88|0,00117|0,61|0,17|
|**420**|4,96|205,50|206,90|0,00186|0,71|0,21|
|**440**|4,96|205,45|206,94|0,00166|0,69|0,20|
|**460**|4,96|205,38|206,97|0,00139|0,65|0,18|
|**480**|4,96|205,34|207,00|0,00122|0,63|0,17|
|**500**|4,96|205,31|207,03|0,00125|0,63|0,17|
|**520**|4,96|205,63|207,05|0,00202|0,75|0,22|
|**540**|1,21|205,95|207,10|0,00024|0,23|0,08|
|**560**|1,21|206,27|207,11|0,00066|0,33|0,12|
|**580**|1,21|206,28|207,12|0,00072|0,34|0,13|
|**600**|1,21|206,07|207,13|0,00040|0,28|0,10|
|**620**|1,21|205,86|207,14|0,00029|0,25|0,08|
|**640**|1,21|205,91|207,15|0,00041|0,27|0,09|
|**660**|1,21|206,11|207,16|0,00053|0,30|0,11|
|**680**|1,21|206,16|207,17|0,00050|0,30|0,10|
|**700**|1,21|206,11|207,18|0,00037|0,27|0,09|

De los resultados de la modelación realizada, se observa que la situación con caudales de crecida presenta una elevación del eje

hidráulico, produciendo mayores profundidades como se observa en el perfil longitudinal (Figura 5.3) alcanzando un máximo de 2,09

metros. Existe una disminución de la velocidad del flujo, exceptuando los últimos perfiles donde se incorporan los aportes del área

aportante 3.

Contacto : contacto@emergeingenieria.cl
**27**
Teléfono : 752313453

**Figura 5.3 Perfil longitudinal Canal Pillanlelbún -QAALL**

Respecto a la profundidad y extensión de la inundación, según se observa en la Figura 5.4, las profundidades alcanzadas por el canal

con caudales de crecida son mayores, pero el canal aún tiene capacidad para su retención.

**Figura 5.4 Profundidad área de inundación Qaguaslluvias**

Contacto : contacto@emergeingenieria.cl
**28**
Teléfono : 752313453

**6.** **CONCLUSIÓN Y COMENTARIOS**

 - Se caracterizó la hidrología a nivel local según la información obtenida de la carta IGM Lautaro (G-072) complementando con

imágenes satelitales actualizadas e informes de la zona de estudio y la visita a terreno realizada. Se identifica un canal que

bordea el área del proyecto, reconocido como Canal Pillanlelbún.

 - Si bien el canal tiene un caudal de captación conocido, debido a la operación normal de un canal de riego en meses de primavera

y verano, adicionalmente se obtuvieron áreas aportantes donde se calculó un caudal pluvial, que se consideraría como el aporte

de aguas lluvias al canal en meses de invierno. Cabe destacar que estos aportes no son de la planta hacia el canal, ya que la

planta no descarga aguas lluvias hacia el cauce.

 - Se desarrollo un modelo unidimensional considerando ambas situaciones (caudal operacional y caudal de aguas lluvias)

utilizando el software de libre acceso HEC-RAS (Hydraulic Engineering Center - River Analysis System), desarrollado por el US

Corp Engineers a partir de la información hidrológica del área en estudio y la topografía del sector.

 - De acuerdo a los resultados obtenidos en la modelación, tanto para el caudal operacional como para el caudal proveniente de

aguas lluvias no se presentan desbordes hacia la planta. Sí existe un aumento en la elevación del eje hidráulico, y por ende de

la profundidad para el caudal de aguas lluvias, pero el canal aún posee capacidad para contener el flujo.

 - Finalmente, el área de inundación del cauce estudiado tanto para el caudal de operación como para caudales de crecida con

periodo de retorno de 100 años no afecta al área del proyecto “Frigorífico Karmac”.

**JORGE SMITH IRAZABAL**

**INGENIERO CIVIL**
**EMERGE INGENIERÍA**

**CURICÓ, 11 DE AGOSTO DE 2022**

Contacto : contacto@emergeingenieria.cl
**29**
Teléfono : 752313453

**ANEXO 7.2**
**MEMORIA DE CALCULO EVACUACIÓN Y**

**DRENAJE DE AGUAS LLUVIAS**

**ADENDA**
**“FRIGORÍFICO KARMAC”**

**COMUNA DE LAUTARO**
**REGIÓN DE LA ARAUCANÍA**

**M.C EVACUACIÓN Y DRENAJE DE AGUAS LLUVIAS**

**PROYECTO FRIGORÍFICO KARMAC**

**REGIÓN DE LA ARAUCANÍA**

AGOSTO- 2022

CURICÓ - CHILE

**Índice**

1. INTRODUCCIÓN .................................................................................................................................................................................. 4

2. GENERALIDADES ............................................................................................................................................................................... 5

2.1. UBICACIÓN DEL PROYECTO .................................................................................................................................................. 5

3. CARACTERIZACIÓN HIDROLÓGICA ................................................................................................................................................. 6

3.1. HIDROLOGÍA REGIONAL ......................................................................................................................................................... 6

3.2. HIDROLOGÍA LOCAL ................................................................................................................................................................ 7

4. PRECIPITACIONES DE DISEÑO ........................................................................................................................................................ 9

4.1. Registros de precipitaciones ...................................................................................................................................................... 9

4.2. Análisis de frecuencias ............................................................................................................................................................ 12

4.3. Precipitaciones máximas de diseño ......................................................................................................................................... 13

4.4. Curvas IDF ............................................................................................................................................................................... 14

5. CÁLCULO DE CAUDAL ..................................................................................................................................................................... 17

5.1. ÁREAS APORTANTES ............................................................................................................................................................ 17

5.2. Método racional ........................................................................................................................................................................ 18

5.2.1. Coeficiente de escorrentía .................................................................................................................................................. 18

5.2.2. Intensidad de lluvia .............................................................................................................................................................. 19

6. PUNTOS DE DESCARGA .................................................................................................................................................................. 20

7. CONCLUSIONES Y COMENTARIOS ................................................................................................................................................ 23

Contacto : contacto@emergeingenieria.cl
**1**
Teléfono : 752313453

**Índice de figuras**

Figura 2.1 Ubicación general del proyecto .................................................................................................................................................... 5

Figura 3.1 Hidrología regional ....................................................................................................................................................................... 6

Figura 3.2 Hidrología local - Carta IGM G-072 Lautaro ................................................................................................................................ 7

Figura 3.3 Hidrología local- Detalle canal Pillanlelbún .................................................................................................................................. 8

Figura 3.4 Canal Pillanlelbún - Foto de terreno ............................................................................................................................................ 9

Figura 4.1 Estaciones meteorológicas cercanas al proyecto, isoyetas de prec. máxima diaria y clasificación de climas de Köppen ........ 10

Figura 4.2 Tormenta de diseño ................................................................................................................................................................... 15

Figura 4.3 Curvas IDF ................................................................................................................................................................................. 15

Figura 5.1 Áreas aportantes planta Frigorífico Karmac ............................................................................................................................... 17

Figura 6.1 Visita a terreno proyecto “Proyecto Frigorífico Karmac” ............................................................................................................ 20

Contacto : contacto@emergeingenieria.cl
**2**
Teléfono : 752313453

**Índice de tablas**

Tabla 3.1 Datos de la cuenca ........................................................................................................................................................................ 6

Tabla 4.1 Datos estaciones meteorológicas cercanas ................................................................................................................................ 10

Tabla 4.2 Registro de precipitación máxima diaria, estación Lautaro ......................................................................................................... 11

Tabla 4.3 Resultados prueba de bondad de ajuste Kolmogorov-Smirnov .................................................................................................. 12

Tabla 4.4 Precipitaciones máximas diarias ................................................................................................................................................. 13

Tabla 4.5 Precipitaciones máximas en 24 horas para distintos periodos de retorno .................................................................................. 13

Tabla 4.6 Coeficientes de duración ............................................................................................................................................................. 14

Tabla 4.7 Coeficientes de duración utilizados ............................................................................................................................................. 14

Tabla 4.8 Tormenta de diseño..................................................................................................................................................................... 16

Tabla 4.9 Curva IDF .................................................................................................................................................................................... 16

Tabla 5.1 Datos áreas aportantes ............................................................................................................................................................... 18

Tabla 5.2 Coeficientes de escorrentía para zonas de nuevas urbanizaciones ........................................................................................... 18

Tabla 5.3. Caudales pluviales áreas aportantes ......................................................................................................................................... 19

Tabla 6.1 Set fotográfico visita a terreno 02/06/2022 .................................................................................................................................. 21

Contacto : contacto@emergeingenieria.cl
**3**
Teléfono : 752313453

**1.** **INTRODUCCIÓN**

Este estudio se realiza en marco al proyecto “Frigorífico Karmac” (en adelante “el Proyecto”) la cual es una planta certificada para la

producción de productos cárnicos que abastecen a todos los segmentos del mercado tanto a nivel nacional como internacional ubicada

en la comuna de Lautaro, región de la Araucanía.

El presente documento tiene por finalidad detallar el cálculo de la precipitación máxima para distintos periodos de retorno, utilizada como

base para obtener caudales pluviales provenientes de la planta del frigorífico, considerando los cambios de uso de suelo producto de la

construcción de esta. Para su ejecución se utilizó información hidrológica del sector, datos provenientes de estaciones meteorológicas y

la topografía disponible, complementando los puntos de descarga con información obtenida en terreno.

Contacto : contacto@emergeingenieria.cl
**4**
Teléfono : 752313453

**2.** **GENERALIDADES**

**2.1.** **UBICACIÓN DEL PROYECTO**

El proyecto _“Frigorífico Karmac_ ” se encuentra emplazado en la comuna de Lautaro, provincia de Cautín, Región de la Araucanía (Figura

2.1).

**Figura 2.1 Ubicación general del proyecto**

Contacto : contacto@emergeingenieria.cl
**5**
Teléfono : 752313453

**3.** **CARACTERIZACIÓN HIDROLÓGICA**

**3.1.** **HIDROLOGÍA REGIONAL**

La zona de estudio se encuentra al centro de la cuenca Río Imperial (código DGA-BNA 091), específicamente en la subcuenca Cautín

Alto (hasta antes junta R. Quepe)(código DGA-BNA 0912), en la subsubcuenca Río Cautín entre arriba junta Estero Guacolda y río Muco.

El sistema de cuencas se aprecia en la Figura 3.1 y la información de las cuencas mencionadas anteriormente se presenta en la Tabla

3.1.

**Figura 3.1 Hidrología regional**

**Tabla 3.1 Datos de la cuenca**

|Unidad|Nombre|Código<br>DGA|Área<br>(km2)|
|---|---|---|---|
|Cuenca|Río Imperial|091|12668,84|
|Subcuenca|Río Cautín Alto (hasta antes junta R. Quepe)|0912|3223,8|
|Subsubcuenca|Río Cautín entre arriba junta Estero Guacolda y río Muco|09124|267,06|

Contacto : contacto@emergeingenieria.cl
**6**
Teléfono : 752313453

**3.2.** **HIDROLOGÍA LOCAL**

La caracterización hidrográfica local, se realizó con el fin de identificar los principales cursos de agua en la zona de estudio, lo cual se

llevó a cabo con la carta IGM Lautaro (G-072) complementando con la red hidrográfica, documentación del área de estudio e información

satelital disponible. De esta forma se identificó la red de drenaje local (Figura 3.2).

**Figura 3.2 Hidrología local - Carta IGM G-072 Lautaro**

Se identifica que el proyecto se ubica en las cercanías de las riberas del río Cautín. Es posible verificar que existe un cauce que bordea

el área del proyecto por el oeste en dirección al sur que corresponde según simbología a un canal. De acuerdo a la información cartográfica

y la documentación revisada, este cauce corresponde al Canal Pilllanlelbún. Si bien en la Carta IGM se observa como un canal continuo

proveniente desde el norte pasando por la ciudad de Lautaro, el canal Pillanlelbún nace en el río Cautín desde una bocatoma al sur de la

ciudad de Lautaro (Figura 3.3) y sigue su curso hacia el sur pasando por la ciudad de Temuco hasta conectar con el Canal imperial, que

Contacto : contacto@emergeingenieria.cl
**7**
Teléfono : 752313453

llega hasta el poblado de Nueva Imperial. El canal está diseñado para transportar 4,5 m [3] /s, de los cuales 3,5 m [3] /s corresponden a

satisfacer la demanda del mismo canal, mientras que 1 m [3] /s está destinado a abastecer al canal Imperial [1]

**Figura 3.3 Hidrología local- Detalle canal Pillanlelbún**

_Fuente: Adaptado de informe “Transferencia de capacidad para constituir junta de vigilancia río cautín - Informe final” - Infraeco,_

_Comisión Nacional de Riego, Ministerio de Agricultura - Enero, 2016._

_1_ _Programa “Transferencia de capacidad para constituir junta de vigilancia río cautín - Informe final” - Infraeco, Comisión Nacional de_
_Riego, Ministerio de Agricultura - Enero, 2016._

Contacto : contacto@emergeingenieria.cl
**8**
Teléfono : 752313453

Se trata de un canal trapezoidal excavado en tierra, que en la actualidad se encuentra cubierto de vegetación según se verificó en la visita

a terreno como se muestra en la Figura 3.4.

**Figura 3.4 Canal Pillanlelbún - Foto de terreno**

**4.** **PRECIPITACIONES DE DISEÑO**

**4.1.** **Registros de precipitaciones**

El cálculo de las precipitaciones máximas se realizó verificando las estaciones cercanas al lugar de estudio y que cumplieran con ciertas

características. Estas son: que se localicen en las proximidades del proyecto, que se encuentren en estado vigente y que posean una

altitud similar a la zona de estudio. En la Figura 4.1 se presentan las estaciones cercanas a la zona del proyecto que cumplen con estos

requerimientos, junto a las isoyetas de precipitación media anual y la clasificación climática de Köppen. En la Tabla 4.1 se presentan los

datos de las estaciones meteorológicas presentadas en el mapa.

Contacto : contacto@emergeingenieria.cl
**9**
Teléfono : 752313453

**Figura 4.1 Estaciones meteorológicas cercanas al proyecto, isoyetas de prec. máxima diaria y clasificación de climas de**

**Köppen**

**Tabla 4.1 Datos estaciones meteorológicas cercanas**

|Código<br>estación|Nombre Estación|Institución|Coordenadas WGS 84<br>UTM18S|Col5|Altitud<br>(msnm)|Vigencia|Fecha<br>Inicio|
|---|---|---|---|---|---|---|---|
|**Código**<br>**estación**|**Nombre Estación**|**Institución**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|09124001-7|Lautaro|DGA|722.862|5.732.790|200|Vigente|01/07/1953|
|09111002-4|Quillén|DGA|728.005|5.739.450|285|Vigente|01/11/1959|
|09112000-3|Perquenco|DGA|728.966|5.744.488|290|Vigente|01/05/2002|

Al observar el plano de isoyetas, es posible verificar que las tres estaciones mencionadas en la Tabla 4.1 presentan similares alturas y

distancia respecto al proyecto y se encuentran entre los valores de precipitación máxima diaria de entre 80 y 90 mm. En tanto, al contrastar

esta información con la clasificación de clima de Köppen, se concluye que la zona de estudio y las estaciones meteorológicas se

encuentran en la misma zona climática la cual corresponde a clima mediterráneo de lluvia invernal (Csb).

Al verificar la disponibilidad de datos en las tres estaciones, la estación “Perquenco” presenta información disponible entre los años 2002

y 2020 mientras que la estación “Quillén” tiene un registro completo entre los años 1959 y 2020, completando 62 años de información.

Finalmente, la estación “Lautaro”, presenta un registro completo a partir del año 1953, siendo la que posee más información disponible

Contacto : contacto@emergeingenieria.cl
**10**
Teléfono : 752313453

en la cercanía del proyecto con 68 años de información. Dado lo anterior, el análisis de precipitaciones se realiza utilizando la estación

“Lautaro” (Código BNA: 09124001-7).

Los registros de precipitación máxima diaria anual entre los años 1953 y 2020 en la estación seleccionada se presentan en la Tabla 4.2.

<!-- INICIO TABLA 4.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Lautaro” (Código BNA: 09124001-7). Los registros de precipitación máxima diaria anual entre los años 1953 y 2020 en la estación seleccionada se presentan en la Tabla 4.2. -->

**Tabla 4.2: Registro de precipitación máxima diaria, estación Lautaro****

| Año | Fecha | Precipitación máxima diaria<br>(mm) |
| --- | --- | --- |
| 1953 | 15/07 | 42,00 |
| 1954 | 22/06 | 76,00 |
| 1955 | 13/02 | 32,00 |
| 1956 | 01/01 | 50,00 |
| 1957 | 07/06 | 45,00 |
| 1958 | 23/09 | 64,00 |
| 1959 | 24/01 | 65,00 |
| 1960 | 16/05 | 85,00 |
| 1961 | 15/07 | 48,00 |
| 1962 | 29/08 | 40,50 |
| 1963 | 29/10 | 58,50 |
| 1964 | 20/05 | 47,50 |
| 1965 | 16/06 | 71,00 |
| 1966 | 13/06 | 61,50 |
| 1967 | 14/07 | 62,00 |
| 1968 | 07/09 | 55,00 |
| 1969 | 12/08 | 50,00 |
| 1970 | 15/06 | 64,00 |
| 1971 | 28/06 | 51,00 |
| 1972 | 04/07 | 59,00 |
| 1973 | 20/10 | 52,00 |
| 1974 | 06/06 | 62,00 |
| 1975 | 17/06 | 47,00 |
| 1976 | 24/12 | 49,90 |
| 1977 | 07/05 | 99,00 |
| 1978 | 02/07 | 53,00 |
| 1979 | 29/08 | 62,50 |
| 1980 | 13/05 | 72,00 |
| 1981 | 06/05 | 86,00 |
| 1981 | 03/06 | 50,00 |
| 1983 | 28/05 | 48,50 |
| 1984 | 01/05 | 100,00 |
| 1985 | 23/05 | 56,00 |
| 1986 | 25/11 | 42,00 |
| 1987 | 26/03 | 63,00 |
| 1988 | 17/01 | 50,00 |
| 1989 | 28/06 | 49,50 |
| 1990 | 09/10 | 51,50 |
| 1991 | 08/04 | 73,00 |
| 1992 | 04/06 | 90,00 |
| 1993 | 16/05 | 85,00 |
| 1994 | 23/07 | 50,50 |
| 1995 | 25/06 | 59,00 |
| 1996 | 23/08 | 53,00 |
| 1997 | 27/06 | 110,50 |

<!-- Estadísticas: 45 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- |Año|Fecha|Precipitación máxima diaria<br>(mm)| |---|---|---| |1998|14/08|37,40| |1999|19/06|43,50| -->
<!-- FIN TABLA 4.2 -->


**Tabla 4.2 Registro de precipitación máxima diaria, estación Lautaro**

Contacto : contacto@emergeingenieria.cl
**11**
Teléfono : 752313453

|Año|Fecha|Precipitación máxima diaria<br>(mm)|
|---|---|---|
|1953|15/07|42,00|
|1954|22/06|76,00|
|1955|13/02|32,00|
|1956|01/01|50,00|
|1957|07/06|45,00|
|1958|23/09|64,00|
|1959|24/01|65,00|
|1960|16/05|85,00|
|1961|15/07|48,00|
|1962|29/08|40,50|
|1963|29/10|58,50|
|1964|20/05|47,50|
|1965|16/06|71,00|
|1966|13/06|61,50|
|1967|14/07|62,00|
|1968|07/09|55,00|
|1969|12/08|50,00|
|1970|15/06|64,00|
|1971|28/06|51,00|
|1972|04/07|59,00|
|1973|20/10|52,00|
|1974|06/06|62,00|
|1975|17/06|47,00|
|1976|24/12|49,90|
|1977|07/05|99,00|
|1978|02/07|53,00|
|1979|29/08|62,50|
|1980|13/05|72,00|
|1981|06/05|86,00|
|1981|03/06|50,00|
|1983|28/05|48,50|
|1984|01/05|100,00|
|1985|23/05|56,00|
|1986|25/11|42,00|
|1987|26/03|63,00|
|1988|17/01|50,00|
|1989|28/06|49,50|
|1990|09/10|51,50|
|1991|08/04|73,00|
|1992|04/06|90,00|
|1993|16/05|85,00|
|1994|23/07|50,50|
|1995|25/06|59,00|
|1996|23/08|53,00|
|1997|27/06|110,50|

|Año|Fecha|Precipitación máxima diaria<br>(mm)|
|---|---|---|
|1998|14/08|37,40|
|1999|19/06|43,50|
|2000|02/05|32,60|
|2001|09/03|34,70|
|2002|23/08|90,00|
|2003|16/11|50,00|
|2004|22/07|70,00|
|2005|06/06|50,00|
|2006|06/06|48,00|
|2007|21/06|47,00|
|2008|31/08|81,00|
|2009|13/06|71,00|
|2010|23/07|37,00|
|2011|12/04|59,50|
|2012|12/06|55,50|
|2013|30/05|47,00|
|2014|22/01|56,00|
|2015|01/06|72,00|
|2016|13/07|37,50|
|2017|16/06|66,00|
|2018|16/03|34,00|
|2019|27/06|63,00|
|2020|09/07|52,00|

**4.2.** **Análisis de frecuencias**

Los datos de precipitación de la estación seleccionada fueron analizados a través del software Hydrognomon V.4, donde se realizó la

prueba de bondad de ajuste de Kolmogorov-Smirnov para las distribuciones recomendadas por la DGA según el documento “Guías

Metodológicas para Proyectos de Modificación de Cauces (2016)”, obteniendo los resultados mostrados en la Tabla 4.3.

<!-- INICIO TABLA 4.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- prueba de bondad de ajuste de Kolmogorov-Smirnov para las distribuciones recomendadas por la DGA según el documento “Guías Metodológicas para Proyectos de Modificación de Cauces (2016)”, obteniendo los resultados mostrados en la Tabla 4.3. -->

**Tabla 4.3: Resultados prueba de bondad de ajuste Kolmogorov-Smirnov****

| Test Kolmogorov-Smirnoff | a=1% | a=5% | a=10% | Porcentaje Alcanzado | Dmax |
| --- | --- | --- | --- | --- | --- |
| Normal | Aceptado | Aceptado | Aceptado | 28,54% | 0,11956 |
| Log Normal | Aceptado | Aceptado | Aceptado | 81,89% | 0,07667 |
| Pearson III | Aceptado | Aceptado | Aceptado | 71,63% | 0,08452 |
| Gumbel | Aceptado | Aceptado | Aceptado | 81,37% | 0,0771 |
| Log Pearson III | Aceptado | Aceptado | Aceptado | **85,19%** | 0,07387 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo con los resultados obtenidos mostrados en la Tabla 4.3, la distribución que presenta el mayor ajuste en comparación a las restantes es la Log Pearson III que se muestra en negrita. En la Tabla 4.4 se muestran las precipitaciones obtenidas para distintos -->
<!-- FIN TABLA 4.3 -->


**Tabla 4.3 Resultados prueba de bondad de ajuste Kolmogorov-Smirnov**

|Test Kolmogorov-Smirnoff|a=1%|a=5%|a=10%|Porcentaje Alcanzado|Dmax|
|---|---|---|---|---|---|
|Normal|Aceptado|Aceptado|Aceptado|28,54%|0,11956|
|Log Normal|Aceptado|Aceptado|Aceptado|81,89%|0,07667|
|Pearson III|Aceptado|Aceptado|Aceptado|71,63%|0,08452|
|Gumbel|Aceptado|Aceptado|Aceptado|81,37%|0,0771|
|Log Pearson III|Aceptado|Aceptado|Aceptado|**85,19%**|0,07387|

De acuerdo con los resultados obtenidos mostrados en la Tabla 4.3, la distribución que presenta el mayor ajuste en comparación a las

restantes es la Log Pearson III que se muestra en negrita. En la Tabla 4.4 se muestran las precipitaciones obtenidas para distintos

periodos de retorno en la estación “Lautaro” con la distribución seleccionada.

Contacto : contacto@emergeingenieria.cl
**12**
Teléfono : 752313453

**Tabla 4.4 Precipitaciones máximas diarias**

|Periodo de retorno|Precipitación máxima diaria (mm)|
|---|---|
|**T (años)**|**Lautaro**|
|2|55,70|
|5|70,67|
|10|80,59|
|20|90,10|
|25|93,12|
|50|102,42|
|100|111,64|
|150|117,03|
|200|120,84|

**4.3.** **Precipitaciones máximas de diseño**

A partir de las precipitaciones máximas diarias presentadas en la Tabla 4.5, se realizó un ajuste para obtener precipitaciones máximas

en 24 horas a través del coeficiente de corrección 1,1 según lo indicado en el “Manual de Carreteras Volumen N°3, MOP (2018)”.

**Tabla 4.5 Precipitaciones máximas en 24 horas para distintos periodos de retorno**

|Periodo de retorno (años)|Precipitación máxima diaria (mm)|Precipitación máxima 24 horas (mm)|
|---|---|---|
|2|55,70|61,26|
|5|70,67|77,74|
|10|80,59|88,65|
|20|90,10|99,11|
|25|93,12|102,43|
|50|102,42|112,66|
|100|111,64|122,81|
|150|117,03|128,73|
|200|120,84|132,92|

Contacto : contacto@emergeingenieria.cl
**13**
Teléfono : 752313453

**4.4.** **Curvas IDF**

La estimación de las curvas IDF se realizó según la siguiente expresión:

T = 1,1 ∙P 24

P t

T=10 ∙CF T ∙CD t

Donde:
P tT

P tT : Precipitación (mm) con periodo de retorno T años y duración t (horas).

P 24T=10

P 24T=10 : Precipitación máxima diaria con período de retorno 10 años obtenida en una estación pluviométrica.

CF [T] : Coeficiente de frecuencia para T años de periodo de retorno.
CD t : Coeficiente de duración para t horas (entre 1 y 24 horas)

Los coeficientes de duración considerados se aprecian en la Tabla 4.6.

<!-- INICIO TABLA 4.6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- CF [T] : Coeficiente de frecuencia para T años de periodo de retorno. CD t : Coeficiente de duración para t horas (entre 1 y 24 horas) Los coeficientes de duración considerados se aprecian en la Tabla 4.6. -->

**Tabla 4.6: Coeficientes de duración****

| Ciudad | Duración (hrs) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ciudad** | **1 ** | **2 ** | **4 ** | **6 ** | **8 ** | **10** | **12** | **14** | **18** | **24** |
| Temuco | 0,21 | 0,32 | 0,5 | 0,59 | 0,67 | 0,73 | 0,79 | 0,84 | 0,91 | 1 |

<!-- Estadísticas: 2 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- En el caso de lluvias con duraciones menores a una hora se utilizó la expresión propuesta por Bell, la cual permite estimar precipitaciones para duraciones entre 5 minutos y 2 horas, asociadas a periodos de retorno comprendidos entre 2 y 100 años. El cálculo del coeficiente -->
<!-- FIN TABLA 4.6 -->


**Tabla 4.6 Coeficientes de duración**
_Fuente: Extracto de Tabla 3.702.403.A “Manual de Carreteras Volumen N°3 (2018)”_

|Ciudad|Duración (hrs)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Ciudad**|**1 **|**2 **|**4 **|**6 **|**8 **|**10**|**12**|**14**|**18**|**24**|
|Temuco|0,21|0,32|0,5|0,59|0,67|0,73|0,79|0,84|0,91|1|

En el caso de lluvias con duraciones menores a una hora se utilizó la expresión propuesta por Bell, la cual permite estimar precipitaciones

para duraciones entre 5 minutos y 2 horas, asociadas a periodos de retorno comprendidos entre 2 y 100 años. El cálculo del coeficiente

de duración según esta metodología se aprecia a continuación:

CD t = (0,54t [0,25] −0,50) ∙CD t=1 hora

Donde:

t : Duración de la lluvia (minutos)

En la Tabla 4.7 se aprecian los coeficientes de duración utilizados para este estudio.

**Tabla 4.7 Coeficientes de duración utilizados**

|t (horas)|t (minutos)|CD|
|---|---|---|
|0,08|5|0,06|
|0,17|10|0,10|
|0,25|15|0,12|
|0,33|20|0,13|
|0,5|30|0,16|
|0,67|40|0,18|
|0,83|50|0,20|
|1|60|0,21|
|2|120|0,32|
|4|240|0,50|
|6|360|0,59|
|8|480|0,67|
|10|600|0,73|
|12|720|0,79|
|14|840|0,84|
|18|1080|0,91|
|24<br>|1440|1,00|

Contacto : contacto@emergeingenieria.cl
**14**
Teléfono : 752313453

Una vez determinados los coeficientes de duración a utilizar, se obtuvo la tormenta de diseño para duraciones de 5 minutos a 24 horas

cuya gráfica se muestra en la Figura 4.2 y las curvas IDF, mostradas en la Figura 4.3.

**Figura 4.2 Tormenta de diseño**

**Figura 4.3 Curvas IDF**

Contacto : contacto@emergeingenieria.cl
**15**
Teléfono : 752313453

Los valores utilizados para generar los gráficos anteriormente presentados respecto a la tormenta de diseño y las curvas IDF se muestran

en la Tabla 4.8 y Tabla 4.9.

<!-- INICIO TABLA 4.9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**720**|12|48,40|61,41|70,03|78,30|80,92|89,00|97,02|101,70|105,01| |**840**|14|51,47|65,30|74,47|83,25|86,04|94,64|103,16|108,14|111,66| |**1080**|18|55,76|70,74|80,67|90,19|93,21|102,52|111,75|117,15|120,96| |**1440**|24|61,27|77,74|88,65|99,11|102,43|112,66|122,80|128,73|132,92| -->

**Tabla 4.9: Curva IDF****

| T (minutos) | T (horas) | Periodo de retorno (años) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **T (minutos)** | **T (horas)** | **T=2** | **T=5** | **T=10** | **T=20** | **T=25** | **T=50** | **T=100** | **T=150** | **T=200** |
| **5** | 0,08 | 47,48 | 60,24 | 68,69 | 76,80 | 79,37 | 87,30 | 95,16 | 99,75 | 103,00 |
| **10** | 0,17 | 35,53 | 45,08 | 51,41 | 57,48 | 59,40 | 65,34 | 71,22 | 74,66 | 77,09 |
| **15** | 0,25 | 28,96 | 36,74 | 41,90 | 46,85 | 48,42 | 53,25 | 58,05 | 60,85 | 62,83 |
| **20** | 0,33 | 24,78 | 31,44 | 35,85 | 40,08 | 41,43 | 45,56 | 49,67 | 52,06 | 53,76 |
| **30** | 0,50 | 19,65 | 24,94 | 28,44 | 31,79 | 32,86 | 36,14 | 39,39 | 41,30 | 42,64 |
| **40** | 0,67 | 16,56 | 21,01 | 23,96 | 26,79 | 27,69 | 30,45 | 33,19 | 34,79 | 35,93 |
| **50** | 0,83 | 14,45 | 18,33 | 20,91 | 23,38 | 24,16 | 26,57 | 28,96 | 30,36 | 31,35 |
| **60** | 1 | 12,87 | 16,32 | 18,62 | 20,81 | 21,51 | 23,66 | 25,79 | 27,03 | 27,91 |
| **120** | 2 | 9,80 | 12,44 | 14,18 | 15,86 | 16,39 | 18,03 | 19,65 | 20,60 | 21,27 |
| **240** | 4 | 7,66 | 9,72 | 11,08 | 12,39 | 12,80 | 14,08 | 15,35 | 16,09 | 16,62 |
| **360** | 6 | 6,02 | 7,64 | 8,72 | 9,75 | 10,07 | 11,08 | 12,08 | 12,66 | 13,07 |
| **480** | 8 | 5,13 | 6,51 | 7,42 | 8,30 | 8,58 | 9,44 | 10,28 | 10,78 | 11,13 |
| **600** | 10 | 4,47 | 5,67 | 6,47 | 7,24 | 7,48 | 8,22 | 8,96 | 9,40 | 9,70 |
| **720** | 12 | 4,03 | 5,12 | 5,84 | 6,52 | 6,74 | 7,42 | 8,08 | 8,47 | 8,75 |
| **840** | 14 | 3,68 | 4,66 | 5,32 | 5,95 | 6,15 | 6,76 | 7,37 | 7,72 | 7,98 |
| **1080** | 18 | 3,10 | 3,93 | 4,48 | 5,01 | 5,18 | 5,70 | 6,21 | 6,51 | 6,72 |
| **1440** | 24 | 2,55 | 3,24 | 3,69 | 4,13 | 4,27 | 4,69 | 5,12 | 5,36 | 5,54 |

<!-- Estadísticas: 18 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Contacto : contacto@emergeingenieria.cl **16** Teléfono : 752313453 -->
<!-- FIN TABLA 4.9 -->


**Tabla 4.8 Tormenta de diseño**

|T (minutos)|T (horas)|Periodo de retorno (años)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**T (minutos)**|**T (horas)**|**T=2**|**T=5**|**T=10**|**T=20**|**T=25**|**T=50**|**T=100**|**T=150**|**T=200**|
|**5**|0,08|3,96|5,02|5,72|6,40|6,61|7,27|7,93|8,31|8,58|
|**10**|0,17|5,92|7,51|8,57|9,58|9,90|10,89|11,87|12,44|12,85|
|**15**|0,25|7,24|9,19|10,48|11,71|12,10|13,31|14,51|15,21|15,71|
|**20**|0,33|8,26|10,48|11,95|13,36|13,81|15,19|16,56|17,35|17,92|
|**30**|0,50|9,83|12,47|14,22|15,90|16,43|18,07|19,70|20,65|21,32|
|**40**|0,67|11,04|14,01|15,97|17,86|18,46|20,30|22,13|23,20|23,95|
|**50**|0,83|12,04|15,28|17,42|19,48|20,13|22,14|24,14|25,30|26,13|
|**60**|1|12,87|16,32|18,62|20,81|21,51|23,66|25,79|27,03|27,91|
|**120**|2|19,61|24,88|28,37|31,72|32,78|36,05|39,30|41,19|42,54|
|**240**|4|30,64|38,87|44,32|49,56|51,22|56,33|61,40|64,37|66,46|
|**360**|6|36,15|45,86|52,30|58,47|60,43|66,47|72,45|75,95|78,43|
|**480**|8|41,05|52,08|59,39|66,40|68,63|75,48|82,28|86,25|89,06|
|**600**|10|44,73|56,75|64,71|72,35|74,78|82,24|89,65|93,98|97,03|
|**720**|12|48,40|61,41|70,03|78,30|80,92|89,00|97,02|101,70|105,01|
|**840**|14|51,47|65,30|74,47|83,25|86,04|94,64|103,16|108,14|111,66|
|**1080**|18|55,76|70,74|80,67|90,19|93,21|102,52|111,75|117,15|120,96|
|**1440**|24|61,27|77,74|88,65|99,11|102,43|112,66|122,80|128,73|132,92|

**Tabla 4.9 Curva IDF**

|T (minutos)|T (horas)|Periodo de retorno (años)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**T (minutos)**|**T (horas)**|**T=2**|**T=5**|**T=10**|**T=20**|**T=25**|**T=50**|**T=100**|**T=150**|**T=200**|
|**5**|0,08|47,48|60,24|68,69|76,80|79,37|87,30|95,16|99,75|103,00|
|**10**|0,17|35,53|45,08|51,41|57,48|59,40|65,34|71,22|74,66|77,09|
|**15**|0,25|28,96|36,74|41,90|46,85|48,42|53,25|58,05|60,85|62,83|
|**20**|0,33|24,78|31,44|35,85|40,08|41,43|45,56|49,67|52,06|53,76|
|**30**|0,50|19,65|24,94|28,44|31,79|32,86|36,14|39,39|41,30|42,64|
|**40**|0,67|16,56|21,01|23,96|26,79|27,69|30,45|33,19|34,79|35,93|
|**50**|0,83|14,45|18,33|20,91|23,38|24,16|26,57|28,96|30,36|31,35|
|**60**|1|12,87|16,32|18,62|20,81|21,51|23,66|25,79|27,03|27,91|
|**120**|2|9,80|12,44|14,18|15,86|16,39|18,03|19,65|20,60|21,27|
|**240**|4|7,66|9,72|11,08|12,39|12,80|14,08|15,35|16,09|16,62|
|**360**|6|6,02|7,64|8,72|9,75|10,07|11,08|12,08|12,66|13,07|
|**480**|8|5,13|6,51|7,42|8,30|8,58|9,44|10,28|10,78|11,13|
|**600**|10|4,47|5,67|6,47|7,24|7,48|8,22|8,96|9,40|9,70|
|**720**|12|4,03|5,12|5,84|6,52|6,74|7,42|8,08|8,47|8,75|
|**840**|14|3,68|4,66|5,32|5,95|6,15|6,76|7,37|7,72|7,98|
|**1080**|18|3,10|3,93|4,48|5,01|5,18|5,70|6,21|6,51|6,72|
|**1440**|24|2,55|3,24|3,69|4,13|4,27|4,69|5,12|5,36|5,54|

Contacto : contacto@emergeingenieria.cl
**16**
Teléfono : 752313453

**5.** **CÁLCULO DE CAUDAL**

**5.1.** **ÁREAS APORTANTES**

Para estimar los caudales de diseño se identificaron las áreas aportantes de origen pluvial asociadas a la extensión local del Proyecto.

Dichos caudales se estimaron para 2, 5, 10 y 100 años de periodo de retorno. Las áreas aportantes se identificaron según el escurrimiento

superficial sujeto al tipo de superficie.

En la Figura 5.1 se muestra la delimitación de las áreas aportantes, las cuales se identifican como homogéneas, conformadas por techos,

patio de carga y terreno intervenido por la planta.

**Figura 5.1 Áreas aportantes planta Frigorífico Karmac**

Las superficies asociadas a cada área aportante se muestra en la Tabla 5.1.

<!-- INICIO TABLA 5.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Contacto : contacto@emergeingenieria.cl **17** Teléfono : 752313453 -->

**Tabla 5.1: Datos áreas aportantes****

| Área aportante | Superficie (km2) |
| --- | --- |
| **A.1.1** | 0,003 |
| **A.1.2** | 0,005 |
| **A.1.3** | 0,003 |
| **A.2** | 0,010 |
| **A.3** | 0,020 |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **5.2.** **Método racional** El gasto aportante (Qd) se calcula utilizando el Método Racional, ya que se trata de cuencas con superficies inferiores a 20 km [2] . El Método -->
<!-- FIN TABLA 5.1 -->


Contacto : contacto@emergeingenieria.cl
**17**
Teléfono : 752313453

**Tabla 5.1 Datos áreas aportantes**

|Área aportante|Superficie (km2)|
|---|---|
|**A.1.1**|0,003|
|**A.1.2**|0,005|
|**A.1.3**|0,003|
|**A.2**|0,010|
|**A.3**|0,020|

**5.2.** **Método racional**

El gasto aportante (Qd) se calcula utilizando el Método Racional, ya que se trata de cuencas con superficies inferiores a 20 km [2] . El Método

Racional se basa en calcular el caudal máximo para un determinado período de retorno según la siguiente expresión:

Q = [ C ∗ I ∗ A]

3,6

Donde:

Q : Gasto aportante en m [3] /s con una probabilidad de ocurrencia igual a las intensidades de lluvia correspondiente

C : Coeficiente de escorrentía

I : Intensidad media de la lluvia en mm/hr para el período de retorno seleccionado y con una duración igual al tiempo de

concentración (tc)

A : Área aportante de la cuenca considerada (en km [2] )

**5.2.1.** **Coeficiente de escorrentía**

Para la obtención del coeficiente de escorrentía en zonas urbanizadas, se trabajó de acuerdo con el Manual de Drenaje Urbano (DOH

MOP) para techos y superficies tanto pavimentadas como de tierra según se muestra en la Tabla 5.2.

<!-- INICIO TABLA 5.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para la obtención del coeficiente de escorrentía en zonas urbanizadas, se trabajó de acuerdo con el Manual de Drenaje Urbano (DOH MOP) para techos y superficies tanto pavimentadas como de tierra según se muestra en la Tabla 5.2. -->

**Tabla 5.2: Coeficientes de escorrentía para zonas de nuevas urbanizaciones****

| Tipo de superficie | Coeficiente de escorrentía<br>(valor medio) | Área aplicada |
| --- | --- | --- |
| **Techos** |  |  |
| Zinc, latón, metálicos en general | 0,9 | A.1.1, A.1.2, A.1.3 |
| **Patios** |  |  |
| Baldosas, hormigón | 0,87 | A.2 |
| Tierra sin cobertura | 0,5 | A.3 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Contacto : contacto@emergeingenieria.cl **18** Teléfono : 752313453 -->
<!-- FIN TABLA 5.2 -->


**Tabla 5.2 Coeficientes de escorrentía para zonas de nuevas urbanizaciones**

_Fuente: Tabla 4.3.16 “Manual de drenaje urbano, MOP,2013”_

|Tipo de superficie|Coeficiente de escorrentía<br>(valor medio)|Área aplicada|
|---|---|---|
|**Techos**|||
|Zinc, latón, metálicos en general|0,9|A.1.1, A.1.2, A.1.3|
|**Patios**|||
|Baldosas, hormigón|0,87|A.2|
|Tierra sin cobertura|0,5|A.3|

Contacto : contacto@emergeingenieria.cl
**18**
Teléfono : 752313453

**5.2.2.** **Intensidad de lluvia**

Para obtener la precipitación con periodo de retorno T años y duración de una hora se consideró el coeficiente de duración de la ciudad

de Temuco indicado en la Tabla 3.702.403.A del “Manual de Carreteras Volumen N°3, MOP, 2021” el que tiene un valor de CD t,1 hr =

0,21 .

La intensidad de las precipitaciones obtenidas para el tiempo de concentración (tc) y cada periodo de retorno se obtiene por medio de la

siguiente expresión:

T

T = [P] [tc]

i tc

t c

Donde:
i tcT

i tcT : Intensidad con periodo de retorno T, asociada a una duración tc horas (mm/hr)

P tcT : Precipitación con periodo de retorno T, asociada a una duración tc horas (mm)

P tcT : Precipitación con periodo de retorno T, asociada a una duración tc horas (mm)

t c : Tiempo de concentración de la cuenca (hr)

Para el cálculo de caudales se utilizó la intensidad con un tiempo de concentración mínimo de 10 minutos, para un periodo de retorno de

2, 5, 10 y 100 años, el cual se presenta en la Tabla 5.3.

**Tabla 5.3. Caudales pluviales áreas aportantes**

|Áreas<br>aportantes|Superficie|Coeficiente<br>Escorrentía|Caudal|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Áreas**<br>**aportantes**|**Superficie**|**Coeficiente**<br>**Escorrentía**|**Q = C*I*A/3,6 (m3/s)**|**Q = C*I*A/3,6 (m3/s)**|**Q = C*I*A/3,6 (m3/s)**|**Q = C*I*A/3,6 (m3/s)**|
|**AP**|**km2 **|**C **|**Q (T=2 años)**|**Q (T=5 años)**|**Q (T=10 años)**|**Q (T=100 años)**|
|A1.1|0,003|0,9|0,027|0,035|0,041|0,061|
|A1.2|0,005|0,9|0,044|0,057|0,067|0,099|
|A1.3|0,003|0,9|0,023|0,040|0,047|0,070|
|A.2|0,010|0,87|0,079|0,102|0,119|0,176|
|A.3|0,020|0,5|0,096|0,124|0,145|0,215|

Contacto : contacto@emergeingenieria.cl
**19**
Teléfono : 752313453

**6.** **PUNTOS DE DESCARGA**

Los puntos de descarga se identificaron en la visita a terreno realizada según se muestra en la Figura 6.1 y cuyo registro fotográfico se

muestra en la Tabla 6.1.

<!-- INICIO TABLA 6.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Contacto : contacto@emergeingenieria.cl **20** Teléfono : 752313453 -->

**Tabla 6.1: Set fotográfico visita a terreno 02/06/2022****

| Col1 | Col2 |
| --- | --- |
| **F-1:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta | **F-2:** Drenaje para aguas lluvias sector patio de planta |
|  |  |
| **F-3:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta | **F-4:** Patio de carga, aguas escurren hacia drenajes que<br>trasladan RILes, hacia la planta de tratamiento (externo) |
|  |  |
| **F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br> | **F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br> |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Contacto : contacto@emergeingenieria.cl **21** Teléfono : 752313453 -->
<!-- FIN TABLA 6.1 -->


**Figura 6.1 Visita a terreno proyecto “Proyecto Frigorífico Karmac”**

Contacto : contacto@emergeingenieria.cl
**20**
Teléfono : 752313453

**Tabla 6.1 Set fotográfico visita a terreno 02/06/2022**

|Col1|Col2|
|---|---|
|**F-1:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta|**F-2:** Drenaje para aguas lluvias sector patio de planta|
|||
|**F-3:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta|**F-4:** Patio de carga, aguas escurren hacia drenajes que<br>trasladan RILes, hacia la planta de tratamiento (externo)|
|||
|**F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br>|**F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br>|

Contacto : contacto@emergeingenieria.cl
**21**
Teléfono : 752313453

De acuerdo a lo observado, se verificó que los escurrimientos provenientes de techos de la planta escurren a través de tuberías que

drenan hacia el terreno para su infiltración, como se muestran en las fotografías F-1 y F-3, cuya localización según la Figura 6.1 coincide

con las descargas provenientes de las techumbres A1.1 y A1.2

En el caso de los patios, al tratarse de patios de carga, descarga y lavado donde pudiera existir contaminación de los escurrimientos de

aguas lluvias (Fotografía F-4), estos descargan sus aguas hacia drenajes (Fotografía F-2) en dirección a la planta de tratamientos de

Aguas Araucanía al costado de la planta.

En el caso de las aguas lluvias sobre el terreno natural o sobre patios no considerados como de lavado, los escurrimientos descargan

hacia áreas verdes a través de zanjas (Fotografía F-5) para su infiltración.

Contacto : contacto@emergeingenieria.cl
**22**
Teléfono : 752313453

**7.** **CONCLUSIONES Y COMENTARIOS**

En base al análisis realizado es posible comentar lo siguiente:

 - El Proyecto se encuentra ubicado en la comuna de Lautaro, provincia de Cautín, Región de la Araucanía. La caracterización

hidrográfica a nivel regional ubica al proyecto en la cuenca del Río Imperial, específicamente en la subcuenca Río Cautín Alto.

 - La hidrología a nivel local está representada según la información obtenida de la carta IGM Lautaro (G-072) complementando

con imágenes satelitales actualizadas de la zona de estudio y la visita a terreno realizada. Se identifica un canal que bordea el

área del proyecto, identificado como Canal Pillanlelbún.

 - La precipitación de diseño se obtuvo mediante el uso de los registros de la estación meteorológica “Lautaro” donde a partir de

un análisis de frecuencias con distintas distribuciones de probabilidad se obtuvo que la precitación máxima en 24 horas para

100 años de periodo de retorno es de 122,81 mm.

 - Se obtuvieron áreas aportantes dentro de la planta desde techumbres y patios para obtener los aportes pluviales de estas zonas

utilizando el método racional a través del uso de coeficientes de escorrentías adecuados para urbanizaciones. Los

escurrimientos obtenidos son de baja magnitud y pueden ser acumulados mediante la pendiente de las techumbres y de la

planta hacia puntos de descarga.

 - A partir de la visita a terreno se verifica que las aguas que escurren desde la zona de carga debido al posible arrastre de

contaminantes, se direccionan a la planta de tratamiento y las aguas lluvias provenientes de la planta son direccionadas y

descargadas hacia áreas verdes donde se infiltran a través de drenes y desagües dentro de la planta.

**JORGE SMITH IRAZABAL**

**INGENIERO CIVIL**
**EMERGE INGENIERÍA**

**CURICÓ, 11 DE AGOSTO DE 2022**

Contacto : contacto@emergeingenieria.cl
**23**
Teléfono : 752313453

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1: Datos de la cuenca donde se ubica el Proyecto****

| Unidad | Nombre | Código<br>DGA | Área<br>(km2) |
| --- | --- | --- | --- |
| Cuenca | Río Imperial | 091 | 12668,84 |
| Subcuenca | Río Cautín Alto (hasta antes junta R. Quepe) | 0912 | 3223,8 |
| Subsubcuenca | Río Cautín entre arriba junta Estero Guacolda y río Muco | 09124 | 267,06 |

**Tabla 2.2: Set fotográfico visita a terreno 02/06/2022****

| Col1 | Col2 |
| --- | --- |
| **F-1:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta | **F-2:** Drenaje para aguas lluvias sector patio de planta |
|  |  |
| **F-3:** Drenaje para infiltración de aguas lluvias desde techo de la<br>planta | **F-4:** Patio de carga, aguas escurren hacia drenajes que<br>trasladan RILes, hacia la planta de tratamiento (externo) |
|  |  |
| **F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br> | **F-5:** Zanja recolectora de aguas bordeando la zona del proyecto<br><br> |

**Tabla 2.3: Parámetros morfométricos****

| Área | A (km2)<br>t | L (km) | H (m)<br>máx | H (m)<br>min |
| --- | --- | --- | --- | --- |
| Área aportante 1 | 0,152 | 0,368 | 260 | 240 |
| Área aportante 2 | 0,511 | 0,915 | 265 | 220 |
| Área aportante 3 | 1,296 | 2,109 | 274 | 226 |

**Tabla 2.4: Fórmulas tiempo de concentración****

| Fórmula | Expresión | Aplicación |
| --- | --- | --- |
| Kirpich | tc= 0,066 ∗~~( ~~L<br>√S<br>~~)~~<br>0,77<br> | Cuencas rurales relativamente planas con escurrimiento<br>preferentemente superficial |
| Normas españolas | tc= 0,3 ∗( L<br>Sp<br>1 4<br>⁄ )<br>0,76<br> | Cuencas de 1 km2 hasta 3.000 km2 con tiempos de<br>concentración desde los 15 minutos hasta las 24 horas |
| California Culverts Practice | tc= 0,95 ∗(L3<br>H)<br>0,385<br> | Adaptación fórmula de Kirpich. Cuencas rurales no<br>planas con escurrimiento preferentemente concentrado |
| Giandotti | tc= (4√A+ 1,5L)<br>(0,8√H)<br> | Siempre queL/3,6 ≥ tc≥L/5,4. Cuencas pequeñas<br>con pendiente |

**Tabla 2.5: Resultados tiempo de concentración****

| Área | Kirpich | Normas<br>españolas | California Culverts<br>Practice | Giandotti | Col6 | tc adoptado<br>(hr) | tc adoptado<br>(min) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Área** | **Kirpich** | **Normas**<br>**españolas** | **California Culverts**<br>**Practice** | **tc** | **L/3.6≥tc≥L/5.4** | **L/3.6≥tc≥L/5.4** | **L/3.6≥tc≥L/5.4** |
| Área aportante 1 | 0,094 | - | 0,094 | 0,590 | No cumple | 0,167 | 10 |
| Área aportante 2 | 0,197 | - | 0,198 | 0,789 | No cumple | 0,197 | 11,79 |
| Área aportante 3 | 0,503 | 1,085 | 0,507 | 1,392 | No cumple | 0,503 | 30,18 |

**Tabla 2.6: Datos estaciones meteorológicas cercanas****

| Código<br>estación | Nombre Estación | Institución | Coordenadas WGS 84<br>UTM18S | Col5 | Altitud<br>(msnm) | Vigencia | Fecha<br>Inicio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Código**<br>**estación** | **Nombre Estación** | **Institución** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| 09124001-7 | Lautaro | DGA | 722.862 | 5.732.790 | 200 | Vigente | 01/07/1953 |
| 09111002-4 | Quillén | DGA | 728.005 | 5.739.450 | 285 | Vigente | 01/11/1959 |
| 09112000-3 | Perquenco | DGA | 728.966 | 5.744.488 | 290 | Vigente | 01/05/2002 |

**Tabla 2.9: Precipitaciones máximas diarias****

| Periodo de retorno | Precipitación máxima diaria (mm) |
| --- | --- |
| **T (años)** | **Lautaro** |
| 2 | 55,70 |
| 5 | 70,67 |
| 10 | 80,59 |
| 20 | 90,10 |
| 25 | 93,12 |
| 50 | 102,42 |
| 100 | 111,64 |
| 150 | 117,03 |
| 200 | 120,84 |

**Tabla 2.10: Precipitaciones máximas diaria para distintos periodos de retorno****

| Periodo de retorno (años) | Precipitación máxima diaria (mm) | Precipitación máxima 24 horas (mm) |
| --- | --- | --- |
| 2 | 55,70 | 61,26 |
| 5 | 70,67 | 77,74 |
| 10 | 80,59 | 88,65 |
| 20 | 90,10 | 99,11 |
| 25 | 93,12 | 102,43 |
| 50 | 102,42 | 112,66 |
| 100 | 111,64 | 122,81 |
| 150 | 117,03 | 128,73 |
| 200 | 120,84 | 132,92 |

**Tabla 2.11: Coeficientes de escorrentía (C) para T = 10 años****

| Factor | Extremo | Alto | Normal | Bajo | Valor adoptado |
| --- | --- | --- | --- | --- | --- |
| Relieve | 0,28-0,35 | 0,20-0,28 | 0,14-0,20 | 0,08-0,14 | 0,08 |
| Relieve | Escarpado con<br>pendientes<br>mayores que 30% | Montañoso con<br>pendientes entre 10 y<br>30% | Con cerros y<br>pendientes entre<br>5 y 10% | Relativamente plano<br>con pendientes<br>menores al 5% | Relativamente plano<br>con pendientes<br>menores al 5% |
| Infiltración | 0,12-0,16 | 0,08-0,12 | 0,06-0,08 | 0,04-0,06 | 0,06 |
| Infiltración | Suelos rocosos, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable | Suelos arcillosos o<br>limosos con baja<br>capacidad de<br>infiltración, mal<br>drenados | Normales, bien<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos | Suelos profundos de<br>arena u otros suelos<br>bien drenados con alta<br>capacidad de infiltración | Suelos profundos de<br>arena u otros suelos<br>bien drenados con alta<br>capacidad de infiltración |
| Cobertura<br>vegetal | 0,12-0,16 | 0,08-0,12 | 0,06-0,08 | 0,04-0,06 | 0,08 |
| Cobertura<br>vegetal | Cobertura escasa,<br>terreno sin<br>vegetación o<br>escasa cobertura | Poca vegetación<br>terrenos cultivados o<br>naturales, menos del<br>20% del área con<br>buena cobertura<br>vegetal | Regular a buena;<br>50% del área con<br>praderas o<br>bosques, no más<br>del 50% cultivado | Buena a excelente;<br>90% del área con<br>praderas, bosques o<br>cobertura equivalente | Buena a excelente;<br>90% del área con<br>praderas, bosques o<br>cobertura equivalente |
| Almacenamiento<br>superficial | 0,10-0,12 | 0,08-0,10 | 0,06-0,08 | 0,04-0,06 | 0,08 |
| Almacenamiento<br>superficial | Despreciable,<br>pocas depresiones<br>superficiales sin<br>zonas húmedas | Baja, sistema de<br>cauces superficiales<br>pequeños bien<br>definidos, sin zonas<br>húmedas | Normal;<br>posibilidad de<br>almacenamiento<br>buena, zonas<br>húmedas,<br>pantanos, lagunas<br>y lagos | Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas<br>planicies de inundación<br>o gran cantidad de<br>zonas húmedas,<br>lagunas o pantanos | Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas<br>planicies de inundación<br>o gran cantidad de<br>zonas húmedas,<br>lagunas o pantanos |
| Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25 | Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25 | Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25 | Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25 | Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25 | Si T > 10 años amplificar resultado por T = 25 ; C x 1,10 T = 50 ; C x 1,20 T = 100 ; C x 1,25 |

**Tabla 2.12: Coeficientes de escorrentía (C) para distintos periodos de retorno(T)****

| Años | C(T) |
| --- | --- |
| 2 | 0,3 |
| 5 | 0,3 |
| 10 | 0,3 |
| 25 | 0,33 |

**Tabla 2.13: Resultados Método Racional para Área Aportante 1****

| Años | C(T) | CD (Bell)<br>tc | PT (mm)<br>tc | iT (mm/hr)<br>tc | Q(m3/s) |
| --- | --- | --- | --- | --- | --- |
| 2 | 0,3 | 0,46 | 5,71 | 34,18 | 0,43 |
| 5 | 0,3 | 0,46 | 7,36 | 44,07 | 0,56 |
| 10 | 0,3 | 0,46 | 8,61 | 51,54 | 0,65 |
| 25 | 0,33 | 0,46 | 10,26 | 61,43 | 0,86 |
| 50 | 0,36 | 0,46 | 11,51 | 68,90 | 1,05 |
| 100 | 0,375 | 0,46 | 12,76 | 76,38 | 1,21 |

**Tabla 2.14: Resultados Método Racional para Área Aportante 2****

| Años | C(T) | CD (Bell)<br>tc | PT (mm)<br>tc | iT (mm/hr)<br>tc | Q(m3/s) |
| --- | --- | --- | --- | --- | --- |
| 2 | 0,3 | 0,50 | 6,20 | 31,56 | 1,34 |
| 5 | 0,3 | 0,50 | 8,00 | 40,69 | 1,73 |
| 10 | 0,3 | 0,50 | 9,35 | 47,59 | 2,03 |
| 25 | 0,33 | 0,50 | 11,15 | 56,72 | 2,66 |
| 50 | 0,36 | 0,50 | 12,50 | 63,62 | 3,25 |
| 100 | 0,375 | 0,50 | 13,86 | 70,52 | 3,75 |

**Tabla 2.15: Resultados Método Racional para Área Aportante 3****

| Años | C(T) | CD (Bell)<br>tc | PT (mm)<br>tc | iT (mm/hr)<br>tc | Q(m3/s) |
| --- | --- | --- | --- | --- | --- |
| 2 | 0,3 | 0,77 | 9,49 | 18,86 | 2,04 |
| 5 | 0,3 | 0,77 | 12,23 | 24,31 | 2,63 |
| 10 | 0,3 | 0,77 | 14,30 | 28,44 | 3,07 |
| 25 | 0,33 | 0,77 | 17,05 | 33,89 | 4,03 |
| 50 | 0,36 | 0,77 | 19,12 | 38,02 | 4,93 |
| 100 | 0,375 | 0,77 | 21,20 | 42,14 | 5,69 |

**Tabla 2.16: Caudales máximos (m** **[3]** **/s)****

| Periodo de retorno<br>(años) | Área aportante 1 | Área aportante 2 | Área aportante 3 |
| --- | --- | --- | --- |
| **100**<br> | 1,21 | 3,75 | 5,69 |

**Tabla 4.1: Datos estaciones meteorológicas cercanas****

| Código<br>estación | Nombre Estación | Institución | Coordenadas WGS 84<br>UTM18S | Col5 | Altitud<br>(msnm) | Vigencia | Fecha<br>Inicio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Código**<br>**estación** | **Nombre Estación** | **Institución** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| 09124001-7 | Lautaro | DGA | 722.862 | 5.732.790 | 200 | Vigente | 01/07/1953 |
| 09111002-4 | Quillén | DGA | 728.005 | 5.739.450 | 285 | Vigente | 01/11/1959 |
| 09112000-3 | Perquenco | DGA | 728.966 | 5.744.488 | 290 | Vigente | 01/05/2002 |

**Tabla 4.4: Precipitaciones máximas diarias****

| Periodo de retorno | Precipitación máxima diaria (mm) |
| --- | --- |
| **T (años)** | **Lautaro** |
| 2 | 55,70 |
| 5 | 70,67 |
| 10 | 80,59 |
| 20 | 90,10 |
| 25 | 93,12 |
| 50 | 102,42 |
| 100 | 111,64 |
| 150 | 117,03 |
| 200 | 120,84 |

**Tabla 3.1: Datos de la cuenca****

| Unidad | Nombre | Código<br>DGA | Área<br>(km2) |
| --- | --- | --- | --- |
| Cuenca | Río Imperial | 091 | 12668,84 |
| Subcuenca | Río Cautín Alto (hasta antes junta R. Quepe) | 0912 | 3223,8 |
| Subsubcuenca | Río Cautín entre arriba junta Estero Guacolda y río Muco | 09124 | 267,06 |

**Tabla 4.5: Precipitaciones máximas en 24 horas para distintos periodos de retorno****

| Periodo de retorno (años) | Precipitación máxima diaria (mm) | Precipitación máxima 24 horas (mm) |
| --- | --- | --- |
| 2 | 55,70 | 61,26 |
| 5 | 70,67 | 77,74 |
| 10 | 80,59 | 88,65 |
| 20 | 90,10 | 99,11 |
| 25 | 93,12 | 102,43 |
| 50 | 102,42 | 112,66 |
| 100 | 111,64 | 122,81 |
| 150 | 117,03 | 128,73 |
| 200 | 120,84 | 132,92 |

**Tabla 4.7: Coeficientes de duración utilizados****

| t (horas) | t (minutos) | CD |
| --- | --- | --- |
| 0,08 | 5 | 0,06 |
| 0,17 | 10 | 0,10 |
| 0,25 | 15 | 0,12 |
| 0,33 | 20 | 0,13 |
| 0,5 | 30 | 0,16 |
| 0,67 | 40 | 0,18 |
| 0,83 | 50 | 0,20 |
| 1 | 60 | 0,21 |
| 2 | 120 | 0,32 |
| 4 | 240 | 0,50 |
| 6 | 360 | 0,59 |
| 8 | 480 | 0,67 |
| 10 | 600 | 0,73 |
| 12 | 720 | 0,79 |
| 14 | 840 | 0,84 |
| 18 | 1080 | 0,91 |
| 24<br> | 1440 | 1,00 |

**Tabla 4.8: Tormenta de diseño****

| T (minutos) | T (horas) | Periodo de retorno (años) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **T (minutos)** | **T (horas)** | **T=2** | **T=5** | **T=10** | **T=20** | **T=25** | **T=50** | **T=100** | **T=150** | **T=200** |
| **5** | 0,08 | 3,96 | 5,02 | 5,72 | 6,40 | 6,61 | 7,27 | 7,93 | 8,31 | 8,58 |
| **10** | 0,17 | 5,92 | 7,51 | 8,57 | 9,58 | 9,90 | 10,89 | 11,87 | 12,44 | 12,85 |
| **15** | 0,25 | 7,24 | 9,19 | 10,48 | 11,71 | 12,10 | 13,31 | 14,51 | 15,21 | 15,71 |
| **20** | 0,33 | 8,26 | 10,48 | 11,95 | 13,36 | 13,81 | 15,19 | 16,56 | 17,35 | 17,92 |
| **30** | 0,50 | 9,83 | 12,47 | 14,22 | 15,90 | 16,43 | 18,07 | 19,70 | 20,65 | 21,32 |
| **40** | 0,67 | 11,04 | 14,01 | 15,97 | 17,86 | 18,46 | 20,30 | 22,13 | 23,20 | 23,95 |
| **50** | 0,83 | 12,04 | 15,28 | 17,42 | 19,48 | 20,13 | 22,14 | 24,14 | 25,30 | 26,13 |
| **60** | 1 | 12,87 | 16,32 | 18,62 | 20,81 | 21,51 | 23,66 | 25,79 | 27,03 | 27,91 |
| **120** | 2 | 19,61 | 24,88 | 28,37 | 31,72 | 32,78 | 36,05 | 39,30 | 41,19 | 42,54 |
| **240** | 4 | 30,64 | 38,87 | 44,32 | 49,56 | 51,22 | 56,33 | 61,40 | 64,37 | 66,46 |
| **360** | 6 | 36,15 | 45,86 | 52,30 | 58,47 | 60,43 | 66,47 | 72,45 | 75,95 | 78,43 |
| **480** | 8 | 41,05 | 52,08 | 59,39 | 66,40 | 68,63 | 75,48 | 82,28 | 86,25 | 89,06 |
| **600** | 10 | 44,73 | 56,75 | 64,71 | 72,35 | 74,78 | 82,24 | 89,65 | 93,98 | 97,03 |
| **720** | 12 | 48,40 | 61,41 | 70,03 | 78,30 | 80,92 | 89,00 | 97,02 | 101,70 | 105,01 |
| **840** | 14 | 51,47 | 65,30 | 74,47 | 83,25 | 86,04 | 94,64 | 103,16 | 108,14 | 111,66 |
| **1080** | 18 | 55,76 | 70,74 | 80,67 | 90,19 | 93,21 | 102,52 | 111,75 | 117,15 | 120,96 |
| **1440** | 24 | 61,27 | 77,74 | 88,65 | 99,11 | 102,43 | 112,66 | 122,80 | 128,73 | 132,92 |

**Tabla 5.3.: Caudales pluviales áreas aportantes****

| Áreas<br>aportantes | Superficie | Coeficiente<br>Escorrentía | Caudal | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Áreas**<br>**aportantes** | **Superficie** | **Coeficiente**<br>**Escorrentía** | **Q = C*I*A/3,6 (m3/s)** | **Q = C*I*A/3,6 (m3/s)** | **Q = C*I*A/3,6 (m3/s)** | **Q = C*I*A/3,6 (m3/s)** |
| **AP** | **km2 ** | **C ** | **Q (T=2 años)** | **Q (T=5 años)** | **Q (T=10 años)** | **Q (T=100 años)** |
| A1.1 | 0,003 | 0,9 | 0,027 | 0,035 | 0,041 | 0,061 |
| A1.2 | 0,005 | 0,9 | 0,044 | 0,057 | 0,067 | 0,099 |
| A1.3 | 0,003 | 0,9 | 0,023 | 0,040 | 0,047 | 0,070 |
| A.2 | 0,010 | 0,87 | 0,079 | 0,102 | 0,119 | 0,176 |
| A.3 | 0,020 | 0,5 | 0,096 | 0,124 | 0,145 | 0,215 |
