---
title: Sin título
author: Desconocido
date: D:20220922182305-03'00'
language: es
type: report
pages: 26
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE INUNDABILIDAD
-->

# ESTUDIO DE INUNDABILIDAD

## PROYECTO PATIO LOS HALCONES

**REGIÓN METROPOLITANA**

SEPTIEMBRE - 2022

CURICÓ - CHILE

**Índice**

1. INTRODUCCIÓN ......................................................................................................................................................................... 4

2. ANTECEDENTES DEL PROYECTO ............................................................................................................................................ 5

2.1. UBICACIÓN DEL PROYECTO ........................................................................................................................................... 5

2.2. HIDROLOGÍA REGIONAL.................................................................................................................................................. 7

2.3. HIDROLOGÍA LOCAL ........................................................................................................................................................ 8

2.5. TOPOGRAFÍA DISPONIBLE ............................................................................................................................................ 11

2.5.1. Zona de análisis .......................................................................................................................................................... 11

2.6. PRECIPITACIONES DE DISEÑO ..................................................................................................................................... 12

2.6.1. Registros de precipitaciones ........................................................................................................................................ 12

2.6.2. Análisis de frecuencias ................................................................................................................................................ 15

2.6.3. Precipitaciones máximas ............................................................................................................................................. 15

2.7. CAUDALES MÁXIMOS A PARTIR DE ESTUDIOS PREVIOS EN LA ZONA ...................................................................... 16

2.7.1. Caudales máximos ...................................................................................................................................................... 17

3. METODOLOGÍA MODELACIÓN 1D ........................................................................................................................................... 18

3.1. Características geométricas del modelo ............................................................................................................................ 18

3.2. Estimación del coeficiente de rugosidad ........................................................................................................................... 19

3.3. Características de la modelación ...................................................................................................................................... 19

3.4. Caudales modelados........................................................................................................................................................ 19

4. RESULTADOS MODELACIÓN................................................................................................................................................... 20

5. CONCLUSIÓN Y COMENTARIOS ............................................................................................................................................. 25

Contacto : contacto@emergeingenieria.cl
**1**
Teléfono : 752313453

**Índice de figuras**

Figura 2.1 Ubicación del Proyecto ......................................................................................................................................................... 5

Figura 2.2 Ubicación local del proyecto ................................................................................................................................................. 6

Figura 2.3 Hidrología regional ............................................................................................................................................................... 7

Figura 2.4 Hidrología local - Cartas IGM E-058 Santiago y E-066 San Bernardo.................................................................................... 8

Figura 2.5 Zanjón de la aguada - Vista Av. Américo Vespucio .............................................................................................................. 9

Figura 2.6 Zanjón de la aguada - Vista Las Codornices ........................................................................................................................ 9

Figura 2.7 Áreas de riesgo de inundación - Plan Regulador Metropolitano de Santiago ....................................................................... 10

Figura 2.8 Topografía disponible ......................................................................................................................................................... 11

Figura 2.9 Estaciones meteorológicas cercanas al proyecto, isoyetas de prec. máxima diaria y clasificación de climas de Köppen ....... 12

Figura 3.1 Perfiles de modelación ....................................................................................................................................................... 18

Figura 4.1 Perfil Longitudinal Tramo Zanjón de la Aguada - Q (T=100 años) ....................................................................................... 21

Figura 4.2 Perfil Longitudinal Tramo Zanjón de la Aguada - Q (T=200 años) ....................................................................................... 21

Figura 4.3 Perfiles con desbordes Q(T=100 años) ............................................................................................................................... 21

Figura 4.4 Perfiles con desbordes Q (T=200 años) ............................................................................................................................. 22

Figura 4.5 Ubicación perfiles con desbordes respecto al proyecto........................................................................................................ 23

Figura 4.6 Áreas de inundación obtenidas ........................................................................................................................................... 24

Contacto : contacto@emergeingenieria.cl
**2**
Teléfono : 752313453

**Índice de tablas**

Tabla 2.1 Datos de la cuenca donde se ubica el Proyecto ..................................................................................................................... 7

Tabla 2.2 Datos estaciones meteorológicas cercanas .......................................................................................................................... 12

Tabla 2.3 Registro de precipitación máxima diaria, estación Terrazas oficinas centrales DGA .............................................................. 13

Tabla 2.4 Resultados prueba de bondad de ajuste Kolmogorov-Smirnov ............................................................................................. 15

Tabla 2.5 Precipitaciones máximas diarias .......................................................................................................................................... 15

Tabla 2.6 Precipitaciones máximas diaria para distintos periodos de retorno ........................................................................................ 15

Tabla 2.7 Resumen de Caudales Líquidos Quebrada de Macul ........................................................................................................... 16

Tabla 2.8 Caudales de aguas lluvias aportantes al Zanjón de la Aguada .............................................................................................. 17

Tabla 2.9 Caudales máximos (m [3] /s) .................................................................................................................................................... 17

Tabla 3.1 Rugosidad asignada al modelo ............................................................................................................................................ 19

Tabla 3.2 Parámetros de modelación utilizados ................................................................................................................................... 19

Tabla 3.3 Caudales de crecida ............................................................................................................................................................ 19

Tabla 4.1 Resultados modelación - Q (T=100 años) ........................................................................................................................... 20

Tabla 4.2 Resultados modelación - Q (T=200 años) ........................................................................................................................... 20

Tabla 4.3 Cota de agua perfiles con desbordes ................................................................................................................................... 23

Contacto : contacto@emergeingenieria.cl
**3**
Teléfono : 752313453

**1.** **INTRODUCCIÓN**

Este estudio se realiza en marco al proyecto “Patio Los Halcones” (en adelante “el Proyecto”) el cual consiste en la construcción de dos

edificios de 23 y 19 pisos de altura de uso residencial con 8 niveles subterráneos. Se contempla también locales comerciales en primer

piso y bodegaje de almacenamiento inofensivo en los pisos subterráneos. El proyecto se encuentra ubicado en la comuna de Macul,

región Metropolitana.

Al sur del área del proyecto se encuentra un importante cauce de la Región Metropolitana, conocido como “Zanjón de la Aguada” el cual

nace desde la Quebrada de Macul y descarga sus aguas al Río Mapocho. Este cauce se encuentra altamente intervenido y en la

actualidad se encuentra canalizado con recubrimiento de hormigón en la zona del proyecto.

En este informe se presentan los parámetros utilizados obtener la modelación 1D del Zanjón de la Aguada en la zona cercana al área del

proyecto, identificado según la carta IGM y la topografía, con el fin de determinar la cota de inundación en el área del proyecto. La

modelación fue realizada utilizando el software de libre acceso HEC-RAS (Hydraulic Engineering Center - River Analysis System),

desarrollado por el US Corp Engineers, el cual es aceptado en proyectos hidráulicos por la Dirección General de Aguas (DGA) y la

Dirección de Obras Hidráulicas (DOH).

Contacto : contacto@emergeingenieria.cl
**4**
Teléfono : 752313453

**2.** **ANTECEDENTES DEL PROYECTO**

**2.1.** **UBICACIÓN DEL PROYECTO**

El Proyecto se encuentra emplazado en la comuna de Macul, provincia de Santiago, Región Metropolitana.

En la Figura 2.1 se muestra la ubicación general y local del Proyecto.

**Figura 2.1 Ubicación del Proyecto**

Contacto : contacto@emergeingenieria.cl
**5**
Teléfono : 752313453

La ubicación local del proyecto junto con la red vial cercana se muestra en la Figura 2.2.

**Figura 2.2 Ubicación local del proyecto**

Contacto : contacto@emergeingenieria.cl
**6**
Teléfono : 752313453

**2.2.** **HIDROLOGÍA REGIONAL**

La zona de estudio se encuentra al centro de la cuenca Río Maipo (código DGA-BNA 057), específicamente en la subcuenca Mapocho

Bajo (código DGA-BNA 0573), en la subsubcuenca Río Mapocho entre Estero de Las Rosas y Estero Lampa y Bajo Zanjón de la Aguada.

El sistema de cuencas se aprecia en la Figura 2.3 y la información de las cuencas mencionadas anteriormente se presenta en la Tabla

2.1.

**Figura 2.3 Hidrología regional**

**Tabla 2.1 Datos de la cuenca donde se ubica el Proyecto**

|Unidad|Nombre|Código<br>DGA|Área<br>(km2)|
|---|---|---|---|
|~~Cuenca~~|~~Río Maipo~~|~~057~~|~~15274,14~~|
|Subcuenca|Mapocho Bajo|0573|3455,67|
|Subsubcuenca|Río Mapocho entre Estero de Las Rosas y Estero Lampa y Bajo Zanjón de la Aguada|05730|842,26|

Contacto : contacto@emergeingenieria.cl
**7**
Teléfono : 752313453

**2.3.** **HIDROLOGÍA LOCAL**

La caracterización hidrográfica local, se realizó con el fin de identificar los principales cursos de agua en la zona de estudio, lo cual se

llevó a cabo con las cartas IGM Santiago (E-058) y San Bernardo (E-066) complementando con la red hidrográfica e información satelital

disponible. De esta forma se identificó la red de drenaje local y el sentido del flujo (Figura 2.4).

**Figura 2.4 Hidrología local - Cartas IGM E-058 Santiago y E-066 San Bernardo**

El proyecto se ubica en las cercanías de un importante cauce que cruza Santiago de oriente a poniente, identificado como el Zanjón de

la Aguada. Este cauce capta sus escurrimientos desde la Quebrada de Macul y los descarga hacia el río Mapocho. En la actualidad, el

Zanjón de la Aguada se encuentra canalizado y recubierto de hormigón armado sin mantención en la zona de estudio, como se muestra

en la Figura 2.5 y Figura 2.6.

Contacto : contacto@emergeingenieria.cl
**8**
Teléfono : 752313453

**Figura 2.5 Zanjón de la aguada - Vista Av. Américo Vespucio**

_Fuente: Street view - Google Maps_

**Figura 2.6 Zanjón de la aguada - Vista Las Codornices**

_Fuente: Street view - Google Maps_

Se observa que el talud del canal es distinto en ambas riberas. Frente al área de estudio, el Zanjón de la Aguada presenta una sección

trapezoidal que cambia a talud vertical en la ribera norte.

Adicionalmente, de acuerdo al Artículo 8.2.1.4 del Plan Regulador Metropolitano de Santiago, el proyecto se encuentra localizado en un

área de riesgo de origen natural de tipo geofísico asociado a inundación debido a cauces naturales “recurrentemente inundables” producto

de crecidas y desbordes del Zanjón de la Aguada como se muestra en la Figura 2.7.

Contacto : contacto@emergeingenieria.cl
**9**
Teléfono : 752313453

**Figura 2.7 Áreas de riesgo de inundación - Plan Regulador Metropolitano de Santiago**

Cabe mencionar que el Zanjón de la Aguada es un cauce que históricamente ha presentado grandes crecidas e inundaciones, sin

embargo, se ha intervenido a lo largo de su todo su trazado mediante revestimientos, abovedamientos y parques inundables para aminorar

las posibles consecuencias de estas crecidas.

Contacto : contacto@emergeingenieria.cl
**10**
Teléfono : 752313453

**2.5.** **TOPOGRAFÍA DISPONIBLE**

**2.5.1.** **Zona de análisis**

Se trabajo con la topografía disponible en la zona del proyecto. Esta abarca exclusivamente la zona de la canalización del cauce, como

se muestra en la Figura 2.8. Por lo tanto, el estudio de inundación se limitará a la zona con información disponible.

**Figura 2.8 Topografía disponible**

Contacto : contacto@emergeingenieria.cl
**11**
Teléfono : 752313453

**2.6.** **PRECIPITACIONES DE DISEÑO**

**2.6.1.** **Registros de precipitaciones**

El cálculo de las precipitaciones máximas se realizó verificando las estaciones cercanas al lugar de estudio y que cumplieran con ciertas

características. Estas son: que se localicen en las proximidades del proyecto, que se encuentren en estado vigente y que posean una

altitud similar a la zona de estudio. En la Figura 2.9 se presentan las estaciones cercanas a la zona del proyecto que cumplen con estos

requerimientos, junto a las isoyetas de precipitación media anual y la clasificación climática de Köppen. En la Tabla 2.2 se presentan los

datos de las estaciones meteorológicas presentadas en el mapa.

**Figura 2.9 Estaciones meteorológicas cercanas al proyecto, isoyetas de prec. máxima diaria y clasificación de climas de**

**Köppen**

**Tabla 2.2 Datos estaciones meteorológicas cercanas**

|Código<br>estación|Nombre Estación|Institución|Coordenadas WGS 84<br>UTM19S|Col5|Altitud<br>(msnm)|Vigencia|Fecha<br>Inicio|
|---|---|---|---|---|---|---|---|
|**Código**<br>**estación**|**Nombre Estación**|**Institución**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|05730039-6|Quebrada de Macul|DGA|359320|6292012|950|Vigente|29/04/2003|
|05730013-2|Antupiren<br>|DGA|359149|6292612|904|Vigente|01/08/1979|
|05730016-7|~~Terrazas oficinas centrales~~<br>DGA|DGA|347173|6297768|560|Vigente|01/01/1960|

Contacto : contacto@emergeingenieria.cl
**12**
Teléfono : 752313453

Al observar la Tabla 2.2, es posible verificar que sólo la estación “Terrazas oficinas centrales DGA” presenta similar altitud respecto al

proyecto. Adicionalmente, del plano de isoyetas se observa que tanto la estación previamente mencionada como el proyecto se

encuentran entre los valores de precipitación máxima diaria de 70 y 80 mm. A diferencia de lo anterior, las estaciones “Antupiren” y

“Quebrada de Macul”, presentan mayores entre 80 y 90 mm diarios. En tanto, al contrastar esta información con la clasificación de clima

de Köppen, se concluye que las estaciones “Antupiren” y “Quebrada de Macul” se encuentran en la zona climática clasificada como clima

mediterráneo de lluvia invernal de altura (Csb (h)) mientras que la zona de estudio y la estación “Terrazas oficinas centrales DGA” se

encuentran en la misma zona climática la cual corresponde a clima mediterráneo de lluvia invernal (Csb).

Al verificar la disponibilidad de datos en las tres estaciones, la estación “Quebrada de Macul” presenta información disponible entre los

años 2003 y 2020 mientras que la estación “Antupiren” tiene un registro completo entre los años 1979 y 2020, completando 42 años de

información. Finalmente, la estación “Terrazas oficinas centrales DGA”, presenta un registro completo a partir del año 1960, siendo la que

posee más información disponible en la cercanía del proyecto con 61 años de información. Dado lo anterior, el análisis de precipitaciones

se realiza utilizando la estación “Terrazas oficinas centrales DGA” (Código BNA: 05730016-7).

Los registros de precipitación máxima diaria anual entre los años 1960 y 2020 en la estación seleccionada se presentan en la Tabla 2.3.

<!-- INICIO TABLA 2.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- se realiza utilizando la estación “Terrazas oficinas centrales DGA” (Código BNA: 05730016-7). Los registros de precipitación máxima diaria anual entre los años 1960 y 2020 en la estación seleccionada se presentan en la Tabla 2.3. -->

**Tabla 2.3: Registro de precipitación máxima diaria, estación Terrazas oficinas centrales DGA****

| Año | Fecha | Precipitación máxima diaria<br>(mm) |
| --- | --- | --- |
| ~~1960~~ | ~~20/06~~ | ~~35,00~~ |
| 1961 | 03/09 | 25,70 |
| 1962 | 23/06 | 61,00 |
| 1963 | 19/08 | 54,20 |
| 1964 | 02/06 | 43,10 |
| 1965 | 23/07 | 49,50 |
| 1966 | 10/07 | 45,50 |
| 1967 | 10/09 | 29,20 |
| 1968<br> | 08/09<br> | 14,20<br> |
| ~~1969~~ | ~~03/07~~ | ~~22,50~~ |
| 1970 | 14/07 | 51,90 |
| 1971 | 20/06 | 71,40 |
| 1972 | 06/05 | 66,90 |
| 1973 | 07/07 | 23,80 |
| 1974 | 29/06 | 81,50 |
| 1975 | 02/07 | 31,90 |
| 1976 | 04/06 | 26,80 |
| 1977 | 22/07 | 32,00 |
| 1978<br> | 16/11<br> | 49,80<br> |
| ~~1979~~ | ~~25/07~~ | ~~54,20~~ |
| 1980 | 18/07 | 34,80 |
| 1981 | 30/05 | 85,70 |
| 1981 | 26/06 | 58,30 |
| 1983 | 18/06 | 45,40 |
| 1984 | 04/07 | 69,70 |
| 1985 | 31/03 | 26,30 |
| 1986 | 15/06 | 44,50 |
| 1987<br> | 11/08<br> | 86,00<br> |
| ~~1988~~ | ~~18/08~~ | ~~20,30~~ |
| 1989 | 29/04 | 39,50 |

<!-- Estadísticas: 30 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- |Año|Fecha|Precipitación máxima diaria<br>(mm)| |---|---|---| |1990|30/08|53,00| |1991|19/07|39,00| -->
<!-- FIN TABLA 2.3 -->


**Tabla 2.3 Registro de precipitación máxima diaria, estación Terrazas oficinas centrales DGA**

Contacto : contacto@emergeingenieria.cl
**13**
Teléfono : 752313453

|Año|Fecha|Precipitación máxima diaria<br>(mm)|
|---|---|---|
|~~1960~~|~~20/06~~|~~35,00~~|
|1961|03/09|25,70|
|1962|23/06|61,00|
|1963|19/08|54,20|
|1964|02/06|43,10|
|1965|23/07|49,50|
|1966|10/07|45,50|
|1967|10/09|29,20|
|1968<br>|08/09<br>|14,20<br>|
|~~1969~~|~~03/07~~|~~22,50~~|
|1970|14/07|51,90|
|1971|20/06|71,40|
|1972|06/05|66,90|
|1973|07/07|23,80|
|1974|29/06|81,50|
|1975|02/07|31,90|
|1976|04/06|26,80|
|1977|22/07|32,00|
|1978<br>|16/11<br>|49,80<br>|
|~~1979~~|~~25/07~~|~~54,20~~|
|1980|18/07|34,80|
|1981|30/05|85,70|
|1981|26/06|58,30|
|1983|18/06|45,40|
|1984|04/07|69,70|
|1985|31/03|26,30|
|1986|15/06|44,50|
|1987<br>|11/08<br>|86,00<br>|
|~~1988~~|~~18/08~~|~~20,30~~|
|1989|29/04|39,50|

|Año|Fecha|Precipitación máxima diaria<br>(mm)|
|---|---|---|
|1990|30/08|53,00|
|1991|19/07|39,00|
|1992<br>|05/06<br>|46,90<br>|
|~~1993~~|~~14/04~~|~~34,40~~|
|1994|22/05|27,00|
|1995|13/08|29,40|
|1996|02/04|40,10|
|1997|16/08|58,00|
|1998|26/04|19,30|
|1999|07/09|32,70|
|2000|13/06|67,60|
|2001|18/07|58,00|
|2002<br>|03/06<br>|109,40<br>|
|~~2003~~|~~20/05~~|~~55,50~~|
|2004|12/11|46,20|
|2005|27/06|62,30|
|2006|07/06|62,50|
|2007|13/06|29,10|
|2008|15/08|77,70|
|2009|06/09|20,00|
|2010|07/11|44,00|
|2011<br>|29/06<br>|17,50<br>|
|~~2012~~|~~06/10~~|~~22,60~~|
|2013|27/05|34,30|
|2014|23/08|27,90|
|2015|06/08|45,50|
|2016|16/04|41,00|
|2017|16/06|52,90|
|2018|05/07|36,10|
|2019|21/07|12,30|
|2020|04/07|32,40|

Contacto : contacto@emergeingenieria.cl
**14**
Teléfono : 752313453

**2.6.2.** **Análisis de frecuencias**

Los datos de precipitación de la estación seleccionada fueron analizados a través del software Hydrognomon V.4, donde se realizó la

prueba de bondad de ajuste de Kolmogorov-Smirnov para las distribuciones recomendadas por la DGA según el documento “Guías

Metodológicas para Proyectos de Modificación de Cauces (2016)”, obteniendo los resultados mostrados en la Tabla 2.4.

<!-- INICIO TABLA 2.4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- prueba de bondad de ajuste de Kolmogorov-Smirnov para las distribuciones recomendadas por la DGA según el documento “Guías Metodológicas para Proyectos de Modificación de Cauces (2016)”, obteniendo los resultados mostrados en la Tabla 2.4. -->

**Tabla 2.4: Resultados prueba de bondad de ajuste Kolmogorov-Smirnov****

| Test Kolmogorov-Smirnoff | a=1% | a=5% | a=10% | Porcentaje Alcanzado | Dmax |
| --- | --- | --- | --- | --- | --- |
| Normal<br> | Aceptado<br> | Aceptado<br> | Aceptado<br> | 75,11%<br> | 0,0865<br> |
| ~~Log Normal~~ | ~~Aceptado~~ | ~~Aceptado~~ | ~~Aceptado~~ | ~~98,65%~~ | ~~0,0580~~ |
| Pearson III | Aceptado | Aceptado | Aceptado | 99,89% | 0,0481 |
| Gumbel | Aceptado | Aceptado | Aceptado | **99,90%** | **0,0480** |
| Log Pearson III | Aceptado | Aceptado | Aceptado | 83,99% | 0,0791 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo con los resultados obtenidos mostrados en la Tabla 2.4, la distribución que presenta el mayor ajuste en comparación a las restantes es la Gumbel que se muestra en negrita. En la Tabla 2.5 se muestran las precipitaciones obtenidas para distintos periodos de -->
<!-- FIN TABLA 2.4 -->


**Tabla 2.4 Resultados prueba de bondad de ajuste Kolmogorov-Smirnov**

|Test Kolmogorov-Smirnoff|a=1%|a=5%|a=10%|Porcentaje Alcanzado|Dmax|
|---|---|---|---|---|---|
|Normal<br>|Aceptado<br>|Aceptado<br>|Aceptado<br>|75,11%<br>|0,0865<br>|
|~~Log Normal~~|~~Aceptado~~|~~Aceptado~~|~~Aceptado~~|~~98,65%~~|~~0,0580~~|
|Pearson III|Aceptado|Aceptado|Aceptado|99,89%|0,0481|
|Gumbel|Aceptado|Aceptado|Aceptado|**99,90%**|**0,0480**|
|Log Pearson III|Aceptado|Aceptado|Aceptado|83,99%|0,0791|

De acuerdo con los resultados obtenidos mostrados en la Tabla 2.4, la distribución que presenta el mayor ajuste en comparación a las

restantes es la Gumbel que se muestra en negrita. En la Tabla 2.5 se muestran las precipitaciones obtenidas para distintos periodos de

retorno en la estación “Terrazas oficinas centrales DGA” con la distribución seleccionada.

**Tabla 2.5 Precipitaciones máximas diarias**

|Periodo de retorno|Precipitación máxima diaria (mm)|
|---|---|
|**T (años)**|**T (años)**|
|2|41,23|
|5|58,87|
|10|70,54|
|20|81,74|
|25|85,29|
|50|96,23|
|100|107,09|
|150|113,42|
|200|117,91|

**2.6.3.** **Precipitaciones máximas**

A partir de las precipitaciones máximas diarias presentadas en la Tabla 2.6, se realizó un ajuste para obtener precipitaciones máximas

en 24 horas a través del coeficiente de corrección 1,1 según lo indicado en el “Manual de Carreteras Volumen N°3, MOP (2018)”.

**Tabla 2.6 Precipitaciones máximas diaria para distintos periodos de retorno**

|Periodo de retorno (años)|Precipitación máxima diaria (mm)|Precipitación máxima 24 horas (mm)|
|---|---|---|
|2|41,23|45,36|
|5|58,87|64,75|
|10|70,54|77,59|
|20|81,74|89,91|
|25|85,29|93,82|
|50|96,23|105,85|
|100|107,09|117,80|
|150|113,42|124,77|
|200|117,91|129,70|

Contacto : contacto@emergeingenieria.cl
**15**
Teléfono : 752313453

**2.7.** **CAUDALES MÁXIMOS A PARTIR DE ESTUDIOS PREVIOS EN LA ZONA**

El Zanjón de la Aguada es un importante cauce que recorre la ciudad de Santiago en dirección oriente a poniente. Este nace desde la

Quebrada de Macul, en el sector precordillerano y corresponde a una canalización que capta esos escurrimientos para su posterior

descarga en el río Mapocho. Los sectores aledaños al Zanjón de la Aguada son principalmente urbanos, y en el punto en estudio (por la

ubicación del proyecto), contiene aguas lluvias provenientes de las comunas de La Florida y Peñalolén. Dada su extensión y ubicación,

la estimación de caudales de crecida para este cauce urbano ha sido abarcado por una serie de estudios oficiales y realizados en el

contexto de proyectos previos localizados en sus cercanías y evaluados por el Servicio de Evaluación Ambiental. Esta información sirve

como antecedente para el estudio de inundación a realizar.

La línea de base del proyecto “Diseño de Obras para el Control de Aluviones y Arrastre de Sedimentos Quebrada de Macul - RM”

realizado en el año 2004 por SRK Consultores en conjunto con la Dirección de Obras Hidráulicas, realizó un catastro de estudios que

hayan estimado caudales de crecida para la Quebrada de Macul, principal afluente del Zanjón de la Aguada. En este estudio se revisaron

los métodos de estimación para cada caso, validando así su posible aplicación. La tabla resumen de la información proveniente de este

estudio se encuentra en la Tabla 2.7.

<!-- INICIO TABLA 2.7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- los métodos de estimación para cada caso, validando así su posible aplicación. La tabla resumen de la información proveniente de este estudio se encuentra en la Tabla 2.7. -->

**Tabla 2.7: Resumen de Caudales Líquidos Quebrada de Macul****

| Estudio | Qlíquido (m3/s) | Col3 | Col4 |
| --- | --- | --- | --- |
| **Estudio** | **T=50 años** | **T=100 años** | **T=200 años** |
| D.G.A - IPLA, 1974 | 50 | 54,7 | - |
| D.G.A - Roberto Aránguiz, 1978 | 40,1 | 42,2 | - |
| U. Católica de Chile, 1993 | 31 | 43 | 96 |
| Dirección de Vialidad - AC Consultores, 1996 | 51 | 75 | 94 |
| DOH - AC Ingenieros Consultores, 1997 | 51 | 80 | 118 |
| DOH - CADE IDEPE, 2001 | 44,82 | 53,68 | - |
| DOH - CADE IDEPE, 2001 | 29,43 | 34,67 | - |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo al estudio anteriormente mencionado, se considera que, de acuerdo a la metodología empleada, el estudio con mayor validez es el de la Dirección de Vialidad y AC consultores. Sin embargo, cabe destacar que este estudio corresponde al “Análisis de la -->
<!-- FIN TABLA 2.7 -->


**Tabla 2.7 Resumen de Caudales Líquidos Quebrada de Macul**

_Fuente:_ _Anexo 3 Línea de Base “Diseño de Obras para el Control de Aluviones y Arrastre de Sedimentos Quebrada de Macul - RM”- Enero 2004_

|Estudio|Qlíquido (m3/s)|Col3|Col4|
|---|---|---|---|
|**Estudio**|**T=50 años**|**T=100 años**|**T=200 años**|
|D.G.A - IPLA, 1974|50|54,7|-|
|D.G.A - Roberto Aránguiz, 1978|40,1|42,2|-|
|U. Católica de Chile, 1993|31|43|96|
|Dirección de Vialidad - AC Consultores, 1996|51|75|94|
|DOH - AC Ingenieros Consultores, 1997|51|80|118|
|DOH - CADE IDEPE, 2001|44,82|53,68|-|
|DOH - CADE IDEPE, 2001|29,43|34,67|-|

De acuerdo al estudio anteriormente mencionado, se considera que, de acuerdo a la metodología empleada, el estudio con mayor validez

es el de la Dirección de Vialidad y AC consultores. Sin embargo, cabe destacar que este estudio corresponde al “Análisis de la

Vulnerabilidad del Sector Oriente de la Ciudad de Santiago ante Ocurrencia de Aluviones y Crecidas, R. Metropolitana” (1996) en el cual

se abarca la Quebrada de Macul y no considera al Zanjón de la Aguada.

El último de los estudios mencionados en la Tabla 2.7, corresponde al Plan Maestro de Aguas Lluvias de Santiago realizado por CADE

IDEPE y la Dirección de Obras Hidráulicas en el año 2001. En este estudio se abarca en específico el Zanjón de la Aguada, como un

cauce urbano y revestido, donde se destaca que el informe que ha estudiado en mayor detalle al cauce corresponde a la “Actualización

Estudio Plan Maestro Aguas Lluvias del Gran Santiago, Zanjón de La Aguada” de AC Consultores y la Dirección de Obras Hidráulicas en

Contacto : contacto@emergeingenieria.cl
**16**
Teléfono : 752313453

el año 1997. En este estudio se estimaron caudales a través del método de Hidrograma Unitario Sintético considerando distintas áreas

aportantes dentro de la cuenca donde en específico se consideró como cuenca aportante la Ex rotonda departamental, que es el punto

de inicio del presente estudio de inundación. Adicionalmente esta estimación de caudales consideró los cambios futuros en el tiempo

debido a las modificaciones en el Zanjón de la Aguada. Los caudales estimados con el área aportante respectiva se muestran en la Tabla

2.8.

**Tabla 2.8 Caudales de aguas lluvias aportantes al Zanjón de la Aguada**

_Fuente: “Actualización Estudio Plan Maestro Aguas Lluvias del Gran Santiago, Zanjón de La Aguada”_

|Subcuenca|Área (km2)|Caudal (m3/s)|Col4|Col5|
|---|---|---|---|---|
|**Subcuenca**|**Área (km2)**|**T= 50**|**T=100**|**T=200**|
|**Rotonda Departamental**|80,2|98|116|145|

Si bien el Plan Maestro de Aguas Lluvias de Santiago es un estudio más reciente y validado, no realiza una estimación de caudal específica

para el Zanjón de la Aguada considerando su tramo urbano (se evalúa el caudal de entrada proveniente de la Quebrada de Macul y otras

quebradas cercanas, sin considerar los aportes de la zona urbana) y valida los caudales obtenidos del estudio de AC Ingenieros, los

cuales adicionalmente son resultados conservadores en comparación a otras estimaciones. Por lo tanto, se optó por considerar para la

modelación los caudales obtenidos en este último estudio.

**2.7.1.** **Caudales máximos**

Finalmente, en base a la información presentada anteriormente, en la Tabla 2.9 se muestran los caudales máximos para un periodo de

retorno de 100 años y 200 años obtenidos para el Zanjón de la Aguada en la Ex rotonda Departamental obtenidos del estudio

“Actualización Estudio Plan Maestro Aguas Lluvias del Gran Santiago, Zanjón de La Aguada” de AC Consultores y la Dirección de Obras

Hidráulicas.

**Tabla 2.9 Caudales máximos (m** **[3]** **/s)**

|Periodo de retorno<br>(años)|Ex Rotonda<br>Departamental|
|---|---|
|**100**|116|
|**200**|145|

Contacto : contacto@emergeingenieria.cl
**17**
Teléfono : 752313453

**3.** **METODOLOGÍA MODELACIÓN 1D**

Para la modelación hidrológica del cauce identificado, se utilizó el software de libre acceso HEC-RAS (Hydraulic Engineering CenterRiver Analysis System), desarrollado por el US Corp Engineers, el cual resuelve la ecuación unidimensional del balance de energía, y en

situaciones donde la superficie del agua varía rápidamente se utiliza la ecuación de momento.

Los datos requeridos para la modelación son: (1) geometría del tramo en estudio, (2) rugosidad relativa del tramo a modelar (n de

Manning), (3) pendiente media aguas abajo y aguas arriba de la zona de interés, dependiendo del régimen del flujo.

**3.1.** **Características geométricas del modelo**

Se realizó un modelo, abarcando una longitud de 220 metros del cauce en estudio dentro de la limitación de la topografía disponible del

sector. En cuanto a la caracterización geométrica se utilizó el levantamiento topográfico disponible, caracterizado por medio de perfiles

transversales, los cuales fueron extraídos cada 20 metros, con un ancho de 17 metros. (Figura 3.1)

**Figura 3.1 Perfiles de modelación**

Contacto : contacto@emergeingenieria.cl
**18**
Teléfono : 752313453

**3.2.** **Estimación del coeficiente de rugosidad**

El coeficiente de rugosidad para el cauce en estudio se obtuvo según la recomendación de las “Guías Metodológicas para Proyectos de

Modificación de Cauces” de la Dirección General de Aguas para canales artificiales, al ser un cauce canalizado con revestimiento de

hormigón en la actualidad. El coeficiente de rugosidad se obtuvo del libro “Hidráulica de Canales” (Chow, 1994) y se muestra en la Tabla

3.1.

**Tabla 3.1 Rugosidad asignada al modelo**

|Materialidad|Mínimo|Normal|Máximo|
|---|---|---|---|
|Concreto terminado con llana metálica|0,011|0,013|0,015|

De lo observado en las fotografías del lugar, el cauce no se encuentra en buen estado de mantenimiento, por lo que se optó por el valor

máximo de 0,015.

**3.3.** **Características de la modelación**

Dado que no se observa la presencia de grandes obstrucciones ni cambios bruscos en el eje del flujo, se consideran los coeficientes de

contracción y expansión C CON = 0,1 y C EXP = 0,3 sugeridos por defecto en el software HEC-RAS según la guía “ _Flow Transitions in Bridge_

_Backwater Analysis_, Hydrologic Engineering Center (HEC), 1995”.

En la Tabla 3.2 se aprecian las condiciones de borde ingresadas al modelo, las cuales se asignaron aguas arriba utilizando la pendiente

promedio a partir de la topografía utilizada, considerando un régimen de flujo supercrítico.

**Tabla 3.2 Parámetros de modelación utilizados**

|Cauce|Condición de borde|Tipo de régimen|
|---|---|---|
|**Cauce**|**Aguas arriba**|**Aguas arriba**|
|**Zanjón de la Aguada**|0,010|Supercrítico|

**3.4.** **Caudales modelados**

Como fue mencionado anteriormente, en vista de los antecedentes revisados, se seleccionaron los caudales obtenidos para la modelación

según se muestra en la Tabla 3.3

**Tabla 3.3 Caudales de crecida**

|Cauce|Q100 (m3/s)|Q200(m3/s)|
|---|---|---|
|**Zanjón de la Aguada**|116|145|

Contacto : contacto@emergeingenieria.cl
**19**
Teléfono : 752313453

**4.** **RESULTADOS MODELACIÓN**

A continuación, se presenta los resultados obtenidos para el caudal de crecida con periodo de retorno de 100 y 200 años, en los perfiles

analizados en la Tabla 4.1 y Tabla 4.2.

<!-- INICIO TABLA 4.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |160|Q(T=100)|116|581,92|583,48|0,01010|7,27|2,10| |180|Q(T=100)|116|582,13|583,57|0,01106|7,48|2,21| |200|Q(T=100)|116|582,34|583,63|0,01453|7,85|2,43| |220|Q(T=100)|116|582,55|584,28|0,01001|7,36|1,97| -->

**Tabla 4.2: Resultados modelación - Q (T=200 años)****

| Perfil | Periodo de<br>retorno | Q total<br>(m3/s) | Cota de fondo<br>(m.s.n.m.) | Cota de agua<br>(m.s.n.m.) | Pendiente de energía<br>(m/m) | Velocidad<br>(m/s) | Fr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Q(T=200) | 145 | 580,18 | 581,81 | 0,01149 | 7,83 | 2,21 |
| 20 | Q(T=200) | 145 | 580,40 | 582,32 | 0,00794 | 7,46 | 1,85 |
| 40 | Q(T=200) | 145 | 580,62 | 582,03 | 0,01371 | 8,33 | 2,39 |
| 60 | Q(T=200) | 145 | 580,84 | 582,76 | 0,00881 | 7,77 | 1,93 |
| 80 | Q(T=200) | 145 | 581,05 | 582,98 | 0,00863 | 7,71 | 1,92 |
| 100 | Q(T=200) | 145 | 581,28 | 583,20 | 0,00872 | 7,66 | 1,96 |
| 120 | Q(T=200) | 145 | 581,48 | 583,33 | 0,00930 | 7,84 | 1,99 |
| 140<br> | Q(T=200)<br> | 145 <br> | 581,69 <br> | 583,58 <br> | 0,00855 <br> | 7,67 <br> | 1,93 <br> |
| ~~160~~ | ~~Q(T=200)~~ | ~~145~~ | ~~581,92~~ | ~~583,66~~ | ~~0,01042~~ | ~~7,86~~ | ~~2,16~~ |
| 180 | Q(T=200) | 145 | 582,13 | 583,76 | 0,01127 | 8,07 | 2,26 |
| 200 | Q(T=200) | 145 | 582,34 | 583,80 | 0,01423 | 8,43 | 2,44 |
| 220 | Q(T=200) | 145 | 582,55 | 584,50 | 0,01001 | 7,94 | 2,01 |

<!-- Estadísticas: 12 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo a los resultados obtenidos, el cauce presenta escurrimiento supercrítico para las dos crecidas estudiadas en el tramo analizado, lo cual se verifica de acuerdo a lo indicado en el Plan Maestro de Aguas Lluvias de Santiago. De esta forma, se observa que -->
<!-- FIN TABLA 4.2 -->


**Tabla 4.1 Resultados modelación - Q (T=100 años)**

|Perfil|Periodo de<br>retorno|Q total<br>(m3/s)|Cota de fondo<br>(m.s.n.m.)|Cota de agua<br>(m.s.n.m.)|Pendiente de energía<br>(m/m)|Velocidad<br>(m/s)|Fr|
|---|---|---|---|---|---|---|---|
|0|Q(T=100)|116|580,18|581,62|0,01190|7,33|2,22|
|20|Q(T=100)|116|580,40|582,06|0,00816|7,02|1,85|
|40|Q(T=100)|116|580,62|581,85|0,01442|7,83|2,42|
|60|Q(T=100)|116|580,84|582,50|0,00912|7,33|1,95|
|80<br>|Q(T=100)<br>|116 <br>|581,05 <br>|582,72 <br>|0,00894 <br>|7,28 <br>|1,93 <br>|
|~~100~~|~~Q(T=100)~~|~~116~~|~~581,28~~|~~582,96~~|~~0,00890~~|~~7,20~~|~~1,95~~|
|120|Q(T=100)|116|581,48|583,16|0,00874|7,18|1,91|
|140|Q(T=100)|116|581,69|583,34|0,00861|7,16|1,92|
|160|Q(T=100)|116|581,92|583,48|0,01010|7,27|2,10|
|180|Q(T=100)|116|582,13|583,57|0,01106|7,48|2,21|
|200|Q(T=100)|116|582,34|583,63|0,01453|7,85|2,43|
|220|Q(T=100)|116|582,55|584,28|0,01001|7,36|1,97|

**Tabla 4.2 Resultados modelación - Q (T=200 años)**

|Perfil|Periodo de<br>retorno|Q total<br>(m3/s)|Cota de fondo<br>(m.s.n.m.)|Cota de agua<br>(m.s.n.m.)|Pendiente de energía<br>(m/m)|Velocidad<br>(m/s)|Fr|
|---|---|---|---|---|---|---|---|
|0|Q(T=200)|145|580,18|581,81|0,01149|7,83|2,21|
|20|Q(T=200)|145|580,40|582,32|0,00794|7,46|1,85|
|40|Q(T=200)|145|580,62|582,03|0,01371|8,33|2,39|
|60|Q(T=200)|145|580,84|582,76|0,00881|7,77|1,93|
|80|Q(T=200)|145|581,05|582,98|0,00863|7,71|1,92|
|100|Q(T=200)|145|581,28|583,20|0,00872|7,66|1,96|
|120|Q(T=200)|145|581,48|583,33|0,00930|7,84|1,99|
|140<br>|Q(T=200)<br>|145 <br>|581,69 <br>|583,58 <br>|0,00855 <br>|7,67 <br>|1,93 <br>|
|~~160~~|~~Q(T=200)~~|~~145~~|~~581,92~~|~~583,66~~|~~0,01042~~|~~7,86~~|~~2,16~~|
|180|Q(T=200)|145|582,13|583,76|0,01127|8,07|2,26|
|200|Q(T=200)|145|582,34|583,80|0,01423|8,43|2,44|
|220|Q(T=200)|145|582,55|584,50|0,01001|7,94|2,01|

De acuerdo a los resultados obtenidos, el cauce presenta escurrimiento supercrítico para las dos crecidas estudiadas en el tramo

analizado, lo cual se verifica de acuerdo a lo indicado en el Plan Maestro de Aguas Lluvias de Santiago. De esta forma, se observa que

el flujo posee alta velocidad, y que la crecida puede ser un riesgo más allá del alcance de inundación, sino por la energía del flujo.

Sin embargo, el canal tiene la capacidad para contener los caudales en la mayoría del tramo analizado, a excepción de perfiles donde se

evidencia que existe una diferencia de terreno entre la ribera izquierda y derecha del cauce. Cabe destacar que la modelación se limita a

la topografía disponible, por lo tanto, no es posible determinar el alcance de la inundación respecto a la zona urbanizada próxima al lugar

del cauce. El eje hidráulico junto con la elevación de la ribera izquierda (LOB) y derecha (ROB) se observa en la Figura 4.1 y Figura 4.2.

Contacto : contacto@emergeingenieria.cl
**20**
Teléfono : 752313453

**Figura 4.1 Perfil Longitudinal Tramo Zanjón de la Aguada - Q (T=100 años)**

**Figura 4.2 Perfil Longitudinal Tramo Zanjón de la Aguada - Q (T=200 años)**

A partir de las figuras anteriormente mostradas, se evidencian los perfiles que presentan desbordes hacia la ribera izquierda (en dirección

al norte) del cauce. Los perfiles con desbordes para el caudal modelado se muestran en la Figura 4.3

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>580.0<br>580.5<br>581.0<br>581.5<br>582.0<br>582.5<br>583.0<br>583.5<br>584.0<br> RS = 0<br>Distancia (m)<br>Elevación (m)<br>.015|0<br>2<br>580.5<br>581.0<br>581.5<br>582.0<br>582.5<br>583.0<br>583.5<br>584.0<br>584.5<br>Elevación (m)|<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br> RS = 40<br>Distancia (m)<br>.015|0<br><br>582.0<br>582.5<br>583.0<br>583.5<br>584.0<br>584.5<br>585.0<br>585.5<br>Elevación (m)|<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br> RS = 200<br>Distancia (m)<br>.015<br>.<br>~~0~~<br>1<br>~~5~~||
|||||||

**Figura 4.3 Perfiles con desbordes Q(T=100 años)**

Contacto : contacto@emergeingenieria.cl
**21**
Teléfono : 752313453

**Figura 4.4 Perfiles con desbordes Q (T=200 años)**

A partir de los perfiles con desbordes, se observa que estos se encuentran distanciados entre sí y que los desbordes se presentan en

ribera izquierda, en dirección al proyecto. Se observa que, en esta dirección, desde el Zanjón de la Aguada hasta la ubicación del

proyecto hay una distancia de aproximadamente 360 metros la cual se encuentra completamente urbanizada. La ubicación de los

desbordes para las crecidas estudiadas, se muestran en la Figura 4.5.

Contacto : contacto@emergeingenieria.cl
**22**
Teléfono : 752313453

**Figura 4.5 Ubicación perfiles con desbordes respecto al proyecto**

De esta forma, la cota de agua para los perfiles que presentan desbordes en la modelación para ambas situaciones analizadas se

muestran en la Tabla 4.3.

<!-- INICIO TABLA 4.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- De esta forma, la cota de agua para los perfiles que presentan desbordes en la modelación para ambas situaciones analizadas se muestran en la Tabla 4.3. -->

**Tabla 4.3: Cota de agua perfiles con desbordes****

| Q(T=100 años) | Col2 |
| --- | --- |
| **Perfi**l | **Cota de agua (m.s.n.m.)** |
| 0 | 581,62 |
| 40 | 581,85 |
| 220 | 584,28<br> |
| **Q(T=200 años)** <br> | **Q(T=200 años)** <br> |
| **Perfil** | **Cota de agua (m.s.n.m.)** |
| 0 | 581,81 |
| 40 | 582,03 |
| 200 | 583,80 |
| 220 | 584,50 |

<!-- Estadísticas: 10 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Finalmente, las áreas de inundación obtenidas se muestran en la Figura 4.6. **Figura 4.6 Áreas de inundación obtenidas** -->
<!-- FIN TABLA 4.3 -->


**Tabla 4.3 Cota de agua perfiles con desbordes**

Contacto : contacto@emergeingenieria.cl
**23**
Teléfono : 752313453

|Q(T=100 años)|Col2|
|---|---|
|**Perfi**l|**Cota de agua (m.s.n.m.)**|
|0|581,62|
|40|581,85|
|220|584,28<br>|
|**Q(T=200 años)** <br>|**Q(T=200 años)** <br>|
|**Perfil**|**Cota de agua (m.s.n.m.)**|
|0|581,81|
|40|582,03|
|200|583,80|
|220|584,50|

Finalmente, las áreas de inundación obtenidas se muestran en la Figura 4.6.

**Figura 4.6 Áreas de inundación obtenidas**

Contacto : contacto@emergeingenieria.cl
**24**
Teléfono : 752313453

**5.** **CONCLUSIÓN Y COMENTARIOS**

 - El proyecto “Patio Los Halcones” es un proyecto habitacional que consiste en dos edificios de 23 y 19 pisos de altura de uso

residencial con 8 niveles subterráneos ubicado en la comuna de Macul, región Metropolitana.

 - La hidrología a nivel local se caracterizó según la información obtenida de las Cartas IGM San Bernardo y Santiago

complementando con imágenes satelitales actualizadas e informes de la zona de estudio. Se identifica que el cauce más

cercano al proyecto se encuentra a aproximadamente 360 metros de este y corresponde al Zanjón de la Aguada.

 - Al tratarse de un cauce urbano y canalizado, se revisaron estudios previos y proyectos realizados en la zona para obtener una

estimación validada de los caudales máximos en la zona, utilizando aquellos presentados en el Plan Maestro de Aguas Lluvias

de Santiago (DOH-CADE IDEPE, 2001), que corresponden a los calculados en el estudio “Actualización Estudio Plan Maestro

Aguas Lluvias del Gran Santiago, Zanjón de La Aguada” (DOH- AC Consultores, 1997) que considera como área aportante la

ex Rotonda Departamental, punto de inicio del tramo del cauce en estudio. Los caudales modelados fueron de 116 m [3] /s para

un periodo de retorno de 100 años y 145 m [3] /s para 200 años.

 - Se desarrollo un modelo unidimensional considerando caudales para dos periodos de retorno (100 y 200 años) utilizando el

software de libre acceso HEC-RAS (Hydraulic Engineering Center - River Analysis System), desarrollado por el US Corp

Engineers a partir de la información hidrológica del área en estudio y la topografía disponible del sector.

 - De acuerdo a los resultados obtenidos en la modelación, para ambos caudales evaluados, el cauce en su mayoría posee

capacidad de contener las aguas sin presentar desbordes. Sin embargo, el escurrimiento es de tipo supercrítico, con una

velocidad alta para los caudales evaluados. Existen perfiles en los que se presentan desbordes, no obstante, la evaluación del

alcance de la inundación está limitada por la topografía disponible del sector.

 - Finalmente, según los resultados obtenidos en la modelación hidráulica del tramo del Zanjón de la Aguada, la cota máxima

alcanzada por inundación es de 584,28 m.s.n.m y 584,50 m.s.n.m para los caudales con periodo de retorno 100 y 200 años

respectivamente, las cuales deben ser verificadas con la cota del área del proyecto para evaluar la posible afectación de este.

**JORGE SMITH IRAZABAL**

**INGENIERO CIVIL**
**EMERGE INGENIERÍA**

**CURICÓ, 21 DE SEPTIEMBRE DE 2022**

Contacto : contacto@emergeingenieria.cl
**25**
Teléfono : 752313453

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1: Datos de la cuenca donde se ubica el Proyecto****

| Unidad | Nombre | Código<br>DGA | Área<br>(km2) |
| --- | --- | --- | --- |
| ~~Cuenca~~ | ~~Río Maipo~~ | ~~057~~ | ~~15274,14~~ |
| Subcuenca | Mapocho Bajo | 0573 | 3455,67 |
| Subsubcuenca | Río Mapocho entre Estero de Las Rosas y Estero Lampa y Bajo Zanjón de la Aguada | 05730 | 842,26 |

**Tabla 2.2: Datos estaciones meteorológicas cercanas****

| Código<br>estación | Nombre Estación | Institución | Coordenadas WGS 84<br>UTM19S | Col5 | Altitud<br>(msnm) | Vigencia | Fecha<br>Inicio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Código**<br>**estación** | **Nombre Estación** | **Institución** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| 05730039-6 | Quebrada de Macul | DGA | 359320 | 6292012 | 950 | Vigente | 29/04/2003 |
| 05730013-2 | Antupiren<br> | DGA | 359149 | 6292612 | 904 | Vigente | 01/08/1979 |
| 05730016-7 | ~~Terrazas oficinas centrales~~<br>DGA | DGA | 347173 | 6297768 | 560 | Vigente | 01/01/1960 |

**Tabla 2.5: Precipitaciones máximas diarias****

| Periodo de retorno | Precipitación máxima diaria (mm) |
| --- | --- |
| **T (años)** | **T (años)** |
| 2 | 41,23 |
| 5 | 58,87 |
| 10 | 70,54 |
| 20 | 81,74 |
| 25 | 85,29 |
| 50 | 96,23 |
| 100 | 107,09 |
| 150 | 113,42 |
| 200 | 117,91 |

**Tabla 2.6: Precipitaciones máximas diaria para distintos periodos de retorno****

| Periodo de retorno (años) | Precipitación máxima diaria (mm) | Precipitación máxima 24 horas (mm) |
| --- | --- | --- |
| 2 | 41,23 | 45,36 |
| 5 | 58,87 | 64,75 |
| 10 | 70,54 | 77,59 |
| 20 | 81,74 | 89,91 |
| 25 | 85,29 | 93,82 |
| 50 | 96,23 | 105,85 |
| 100 | 107,09 | 117,80 |
| 150 | 113,42 | 124,77 |
| 200 | 117,91 | 129,70 |

**Tabla 2.8: Caudales de aguas lluvias aportantes al Zanjón de la Aguada****

| Subcuenca | Área (km2) | Caudal (m3/s) | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Subcuenca** | **Área (km2)** | **T= 50** | **T=100** | **T=200** |
| **Rotonda Departamental** | 80,2 | 98 | 116 | 145 |

**Tabla 2.9: Caudales máximos (m** **[3]** **/s)****

| Periodo de retorno<br>(años) | Ex Rotonda<br>Departamental |
| --- | --- |
| **100** | 116 |
| **200** | 145 |

**Tabla 3.1: Rugosidad asignada al modelo****

| Materialidad | Mínimo | Normal | Máximo |
| --- | --- | --- | --- |
| Concreto terminado con llana metálica | 0,011 | 0,013 | 0,015 |

**Tabla 3.2: Parámetros de modelación utilizados****

| Cauce | Condición de borde | Tipo de régimen |
| --- | --- | --- |
| **Cauce** | **Aguas arriba** | **Aguas arriba** |
| **Zanjón de la Aguada** | 0,010 | Supercrítico |

**Tabla 3.3: Caudales de crecida****

| Cauce | Q100 (m3/s) | Q200(m3/s) |
| --- | --- | --- |
| **Zanjón de la Aguada** | 116 | 145 |

**Tabla 4.1: Resultados modelación - Q (T=100 años)****

| Perfil | Periodo de<br>retorno | Q total<br>(m3/s) | Cota de fondo<br>(m.s.n.m.) | Cota de agua<br>(m.s.n.m.) | Pendiente de energía<br>(m/m) | Velocidad<br>(m/s) | Fr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Q(T=100) | 116 | 580,18 | 581,62 | 0,01190 | 7,33 | 2,22 |
| 20 | Q(T=100) | 116 | 580,40 | 582,06 | 0,00816 | 7,02 | 1,85 |
| 40 | Q(T=100) | 116 | 580,62 | 581,85 | 0,01442 | 7,83 | 2,42 |
| 60 | Q(T=100) | 116 | 580,84 | 582,50 | 0,00912 | 7,33 | 1,95 |
| 80<br> | Q(T=100)<br> | 116 <br> | 581,05 <br> | 582,72 <br> | 0,00894 <br> | 7,28 <br> | 1,93 <br> |
| ~~100~~ | ~~Q(T=100)~~ | ~~116~~ | ~~581,28~~ | ~~582,96~~ | ~~0,00890~~ | ~~7,20~~ | ~~1,95~~ |
| 120 | Q(T=100) | 116 | 581,48 | 583,16 | 0,00874 | 7,18 | 1,91 |
| 140 | Q(T=100) | 116 | 581,69 | 583,34 | 0,00861 | 7,16 | 1,92 |
| 160 | Q(T=100) | 116 | 581,92 | 583,48 | 0,01010 | 7,27 | 2,10 |
| 180 | Q(T=100) | 116 | 582,13 | 583,57 | 0,01106 | 7,48 | 2,21 |
| 200 | Q(T=100) | 116 | 582,34 | 583,63 | 0,01453 | 7,85 | 2,43 |
| 220 | Q(T=100) | 116 | 582,55 | 584,28 | 0,01001 | 7,36 | 1,97 |
