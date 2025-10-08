---
title: Sin título
author: Ramón Valdivia
date: D:20230323152014-03'00'
language: es
type: report
pages: 25
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - X α,δ2 Valor teórico (tabulado) que toma la distribución Chi-Cuadrado para un nivel de
-->

|REV.|FECHA|RVIA|Col4|Col5|DESCRIPCIÓN|
|---|---|---|---|---|---|
|**REV.**|**FECHA**|**PREP.**|**REV.**|**APR.**||
|A|19-12-22|FMF|IVV|RVV|Revisión Interna|
|B|13-01-23|FMF|IVV|RVV|Revisión del Cliente|
|||||||
|||||||

2210323-00-HID-MCA-001 REV B Página 1 de 25

**ÍNDICE**

**1** **GENERAL .................................................................................................................... 4**
**1.1** **INTRODUCCIÓN ........................................................................................................................... 4**

**1.2** **OBJETIVOS ................................................................................................................................... 4**

**1.3** **ALCANCES ................................................................................................................................... 4**

**1.4** **REFERENCIAS ............................................................................................................................. 4**
**2** **DESCRIPCION DEL PROYECTO ................................................................................ 5**
**3** **REGISTROS PLUVIOMETRICOS ................................................................................ 6**

**4** **ANALISIS ESTADISTICO ............................................................................................ 6**

**4.1** **ANALISIS ESTADISTICO ............................................................................................................. 6**

**4.2** **ANALISIS DE FRECUENCIA DE PRECIPITACIONES MAXIMAS DIARIAS ............................. 9**

**4.2.1** **DISTRIBUCION NORMAL ............................................................................................................ 9**

**4.2.2** **DISTRIBUCION LOG - NORMAL ................................................................................................. 9**

**4.2.3** **DISTRIBUCION GUMBEL ...........................................................................................................10**

**4.2.4** **DISTRIBUCION LOG - PEARSON TIPO III ...............................................................................11**

**4.3** **PRECIPITACION MAXIMA DIARIA ............................................................................................13**

**4.4** **PRUEBA DE BONDAD DE AJUSTE ..........................................................................................14**
**4.5** **PRECIPITACION MAXIMA DIARIA ABSOLUTA .......................................................................15**
**5** **ESCORRENTIA SUPERFICIAL ................................................................................. 16**

**5.1** **DEFINICION DE CUENCAS........................................................................................................16**

**5.1.1** **DESCRIPCION MORMOMETRICA ............................................................................................16**

**5.1.2** **TIEMPO DE CONCENTRACION ................................................................................................17**

**5.2** **INTENSIDAD DE LA PRECIPITACION ......................................................................................18**

**5.2.1** **COEFICIENTE DE DURACION...................................................................................................19**

**5.2.2** **CURVA INTENSIDAD - DURACION - FRECUENCIA ................................................................19**

**5.3** **DETERMINACION DE LOS CAUDALES LIQUIDOS .................................................................22**
**5.3.1** **CUENCAS CON AREAS MENORES A 25 KM2 ........................................................................22**

**TABLAS**

Tabla 3-1 Estaciones Pluviométricas ..................................................................................... 6

Tabla 3-2 Precipitación Máxima Diarias en 24 horas - Estación Chacrilla ............................. 6

Tabla 4-1 Análisis de Datos Dudosos .................................................................................... 7

Tabla 4-2 Valores de _K_ _n_ para la Prueba de Datos Dudosos ................................................... 8

Tabla 4-3 Análisis de Datos Dudosos .................................................................................... 8

Tabla 4-4 Análisis de Datos Dudosos .................................................................................... 9

Tabla 4-5 Parámetros estadísticos (Log-Normal) ................................................................ 10

Tabla 4-6 Parámetros variable reducida (1989, Ayala et al) ................................................ 10

Tabla 4-7 Parámetros estadísticos (Gumbel) ...................................................................... 11

Tabla 4-8 Parámetros estadísticos (Log-Pearson III) .......................................................... 12

Tabla 4-9 Valores de k para la distribución Log-Pearson Tipo III ........................................ 13

Tabla 4-10 Test de Bondad................................................................................................. 15

Tabla 4-11 Precipitaciones Máximas Absolutas en 24 horas (mm) ..................................... 15

Tabla 5-1 Parámetros morfométricos de cuenca sin proyecto .............................................. 16

2210323-00-HID-MCA-001 REV B Página 2 de 25

Tabla 5-2 Tiempo de concentración - Escenario sin proyecto ............................................. 18

Tabla 5-3 Coeficiente de Duración - Estación Quillota ........................................................ 19

Tabla 5-4 Curva IDF (Duración t < 1 hora) ........................................................................... 20

Tabla 5-5 Curva IDF (Duración t > 1 hora) ........................................................................... 20

Tabla 5-6 Coeficiente de Escorrentía ................................................................................... 23

Tabla 5-7 Coeficiente de Escorrentía Adoptados ................................................................. 23

Tabla 5-8 Caudales Máximos Instantáneos ......................................................................... 24

**FIGURAS**

Figura 2-1. Trazado de línea de relaves.................................. **¡Error! Marcador no definido.**

Figura 5-1 Cuencas aportantes ............................................................................................ 16

Figura 5-2 Curva IDF (Duracion t < 1 hora) .......................................................................... 21

Figura 5-3 Curva IDF (Duracion t > 1 hora) .......................................................................... 21

2210323-00-HID-MCA-001 REV B Página 3 de 25

**1** **GENERAL**

**1.1** **INTRODUCCIÓN**

RVIA desarrolló para su cliente Minera Las Cenizas (“MLC”) el Proyecto de Disposición de
Relave en Pasta en Interior Mina Faena Cabildo, incluyendo la impulsión y líneas en superficie
e interior mina para el transporte de la pasta, así como información base para preparar la
Declaración de Impacto Ambiental (“DIA”).

Continuando con el desarrollo del proyecto, MLC ha solicitado una ingeniería complementaria
para el dimensionamiento de tapones, trazados de cañerías en interior mina y también la
incorporación de planos vendor de la nueva bomba de desplazamiento positivo ubicada en la
planta DEP.

En el contexto de la tramitación ambiental, MLC recibió el primer Informe Consolidado de
Solicitud de Aclaraciones, Rectificaciones y/o Ampliaciones (“ICSARA”) de acuerdo con Carta
N°202205103344 del 29 de junio del 2022 por parte de la directora regional del SEA de la
región de Valparaíso, para el cual este servicio incluye la elaboración de las respuestas de
algunas consultas seleccionadas.

**1.2** **OBJETIVOS**

El presente estudio hidrológico ha sido elaborado por RV Ingenieros para MLC, en el marco
de la elaboración de las respuestas al ICSARA del proyecto Disposición de Relaves en Pasta
Interior Mina (DEPIM), particularmente lo relacionado a la consulta 94.

**1.3** **ALCANCES**

El análisis desarrollado tiene como objetivo determinar los caudales máximos instantáneos
asociados a las quebradas en estudio, a fin de permitir el análisis hidráulico posterior de los

cauces.

El alcance de este documento considera un análisis estadístico de las precipitaciones
registradas en estaciones pluviométricas cercanas y la determinación del escurrimiento
superficial efectivo por medio de relaciones precipitación escorrentía conocidas.

**1.4** **REFERENCIAS**

Los presentes criterios de diseño son complementarios a los documentos indicados a
continuación:

Las referencias utilizadas para la realización del proyecto son las siguientes:

Ref. 1 Ministerio de Minería; Reglamento para la aprobación de proyectos de diseño,

construcción, operación y cierre de depósitos de relaves; DS N°248.

Ref. 2 SEA; Guía de Permisos Ambientales Sectoriales en el SEIA - Permisos para

Efectuar Modificaciones de Cauce (PAS - 156)

Ref. 3 SEA; Guía de Permisos Ambientales Sectoriales en el SEIA - Permiso Obras

de Regularización o Defensa de Cauces Naturales (PAS - 157)

Ref. 4 DGA 2016; Guías Metodológicas para Presentación y Revisión Técnica de

Proyectos - Modificación de Cauces Naturales y Artificiales

2210323-00-HID-MCA-001 REV B Página 4 de 25

**2** **DESCRIPCION DEL PROYECTO**

El Proyecto consiste en la construcción de un nuevo sistema para la disposición final de relave
en pasta producido en la Planta de Procesamiento de Minerales Cabildo de Minera Las
Cenizas. Este sistema estará compuesto por una nueva tubería de transporte de relave en
pasta, desde la actual planta de pasta (DEP), hasta la Boca Mina Farellones, desde donde
será distribuido el relave tipo pasta a los distintos caserones existentes al interior de la mina
subterránea.

Por otro lado, el proyecto DEPIM requiere la construcción de una nueva tubería Bypass de
transporte de relave espesado entre el tramo Bocamina Nueva Sauce y Bocamina soledad.
La tubería Bypass será soterrada, tendrá una extensión de 3 Km y su trazado rodeará el cerro
por el costado de un camino de servicios existente.

El propósito del Bypass es ser una línea alternativa al sistema de descarga de relave
espesado del proyecto DREIM (aprobado de acuerdo con RCA N°199/2005), en el caso que
el relaveducto que cruza por el interior de Mina Soledad sufra alguna contingencia.

En la figura Figura 2-1 se presenta la red hídrica del área de influencia del proyecto, basada
en la carta IGM escala 1:25.000 denominada Cabildo E-029-SE.

**Figura 2-2 Localización del Proyecto DEPIM**

2210323-00-HID-MCA-001 REV B Página 5 de 25

**3** **REGISTROS PLUVIOMETRICOS**

La zona del estudio presenta un régimen de precipitaciones netamente pluvial; por tal motivo,
el estudio hidrológico considera la pluviometría de la zona, con estadísticas de lluvias máximas
en 24 horas.

De acuerdo con la información disponible en la página de la Red Hidrométrica Nacional,
dependiente de la Dirección General de Aguas, las cuencas directamente comprometidas no
cuentan con registros de pluviometría, por lo tanto, para el caso específico del análisis
pluviométrico, se han seleccionado como estaciones representativas del área de estudio las
que se presentan en la tabla siguiente.

**Tabla 3-1 Estaciones Pluviométricas**

|Estación|Código BNA|Ubicación Geográfica|Col4|Col5|Col6|Administración|
|---|---|---|---|---|---|---|
|**Estación**|**Código BNA**|**Este**|**Norte**|**Altura**<br>**(msnm)**|**Cuenca**|**Cuenca**|
|La Viña|05210002-k|320.246|6.410.050|370|Rio Ligua|DGA|
|Chacrilla|05220006-7|306.249|6.410.346|290|Rio Ligua|DGA|
|Las Puertas|05211004-1|318.419|6.403.948|350|Rio Ligua|DGA|
|Alicahue|05200006-8|335.143|6.420.422|750|Rio Ligua|DGA|

Fuente: Elaboración Propia

La ubicación geográfica de cada estación Pluviométrica se presenta en la Tabla 3-1, mientras
que en la Tabla 3-2 Precipitación Máxima Diarias en 24 horas - Estación ChacrillaTabla 3-2
se muestra la precipitación Máxima diarias en 24 horas de la estación Chacrilla.

**Tabla 3-2 Precipitación Máxima Diarias en 24 horas - Estación Chacrilla**

**N°** **Año** **Fecha** **Pp** **N°** **Año** **Fecha** **Pp** **N°** **Año** **Fecha** **Pp**
**(mm)** **(mm)** **(mm)**

           

           

           

           

           

           

           

           

           

           

           

           

       

|N°|Año|Fecha|Pp<br>(mm)|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||

**4** **ANÁLISIS ESTADÍSTICO**

**4.1** **ANÁLISIS ESTADÍSTICO**

|N°|Año|Fecha|Pp<br>(mm)|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||

|N°|Año|Fecha|Pp<br>(mm)|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||

El método del Water Resources Council recomienda la realización de ajustes de datos
dudosos (Ven Te Chow, Hidrología aplicada 1987). Los datos dudosos (outliers) son puntos

2210323-00-HID-MCA-001 REV B Página 6 de 25

de la información que se alejan significativamente de la tendencia de la información restante.
La retención o eliminación de estos datos puede afectar significativamente la magnitud de los
parámetros estadísticos calculados para la información, especialmente en muestras
pequeñas.

De acuerdo con lo anterior, se realizó un análisis de datos dudosos a los registros
pluviométricos de la estación meteorológica Chacrilla, cuyos resultados se presenta en la
Tabla 4-1.

**Tabla 4-1 Análisis de Datos Dudosos**

|AÑO|X: Pp<br>max|Y∶log(X)|Y−Y|2<br>(Y−Y)|3<br>(Y−Y)|
|---|---|---|---|---|---|
|REGISTRO|(mm)|(mm)|(mm)|(mm)|(mm)|
|1983|51.60|1.7|0.1|0.01|0.00|
|1984|98.50|2.0|0.4|0.14|0.05|
|1985|39.40|1.6|0.0|0.00|0.00|
|1986|92.00|2.0|0.3|0.12|0.04|
|1987|77.20|1.9|0.3|0.07|0.02|
|1988|18.10|1.3|-0.4|0.13|-0.05|
|1989|40.50|1.6|0.0|0.00|0.00|
|1990|21.50|1.3|-0.3|0.08|-0.02|
|1991|41.00|1.6|0.0|0.00|0.00|
|1992|62.50|1.8|0.2|0.03|0.01|
|1993|54.20|1.7|0.1|0.01|0.00|
|1994|16.00|1.2|-0.4|0.17|-0.07|
|1995|45.50|1.7|0.0|0.00|0.00|
|1996|37.10|1.6|-0.1|0.00|0.00|
|1997|57.30|1.8|0.1|0.02|0.00|
|1998|11.10|1.0|-0.6|0.33|-0.19|
|1999|38.60|1.6|0.0|0.00|0.00|
|2000|37.20|1.6|0.0|0.00|0.00|
|2001|54.70|1.7|0.1|0.01|0.00|
|2002|125.30|2.1|0.5|0.23|0.11|
|2003|45.50|1.7|0.0|0.00|0.00|
|2004|47.00|1.7|0.1|0.00|0.00|
|2005|28.40|1.5|-0.2|0.03|0.00|
|2006|68.30|1.8|0.2|0.05|0.01|
|2007|64.20|1.8|0.2|0.04|0.01|
|2008|59.30|1.8|0.2|0.02|0.00|
|2009|40.00|1.6|0.0|0.00|0.00|
|2010|26.20|1.4|-0.2|0.04|-0.01|
|2011|34.20|1.5|-0.1|0.01|0.00|
|2012|40.00|1.6|0.0|0.00|0.00|
|2013|35.20|1.5|-0.1|0.01|0.00|
|2014|38.20|1.6|0.0|0.00|0.00|
|2015|60.50|1.8|0.2|0.03|0.00|
|2016|60.20|1.8|0.2|0.03|0.00|
|2017|50.00|1.7|0.1|0.01|0.00|

2210323-00-HID-MCA-001 REV B Página 7 de 25

|AÑO|X: Pp<br>max|Y∶log(X)|Y−Y|2<br>(Y−Y)|3<br>(Y−Y)|
|---|---|---|---|---|---|
|REGISTRO|(mm)|(mm)|(mm)|(mm)|(mm)|
|2018|22.20|1.3|-0.3|0.08|-0.02|
|2019|17.10|1.2|-0.4|0.15|-0.06|
|2020|33.70|1.5|-0.1|0.01|0.00|

Fuente: Elaboración Propia

El método consiste en determinar los valores de umbrales altos y bajos asociados para la
estadística en análisis, de acuerdo con las siguientes expresiones.

Umbral superior de datos dudosos.

Y H = Y+ K n ∗S y

Umbral inferior de datos dudosos.

Y L = Y− K n ∗S y

Donde:

Y : Promedio de los registros (mm)

S y : Desviación estándar (mm)

K n : Valores de datos dudosos asociados al tamaño de muestra.

Los valores de K n se obtienen de la tabla siguiente.

**Tabla 4-2 Valores de** _**K**_ _**n**_ **para la Prueba de Datos Dudosos**

|Tamaño<br>Muestra|K<br>n|
|---|---|
|10|2,036|
|15|2,247|
|20|2,385|
|25|2,486|
|30|2,563|
|35|2,628|
|40|2,682|

Fuente: Ven Te Chow, Hidrología Aplicada, 1987

Reemplazando los valores en las ecuaciones que representan los umbrales superior e inferior,
se obtienen los siguientes valores.

**Tabla 4-3 Análisis de Datos Dudosos**

|Variable|Item|Valor|
|---|---|---|
|Promedio|Y|1,62|
|Desviación Estándar|Sy|0,22|
|Numero de datos|N|38,00|
|Variable de datos dudosos|Kn|2,682|
|Umbral superior de datos dudosos|YH|2.20|
|Umbral inferior de datos dudosos|YL|1,02|

Fuente: Elaboración propia.

2210323-00-HID-MCA-001 REV B Página 8 de 25

De los resultados obtenidos, se observa que el valor del umbral superior de datos dudosos
( Y H = 2,20) resulta mayor al máximo valor de los registros de precipitación presentados en la

Tabla 4-3, por lo que, estos son validados por el umbral superior.

Para el caso del límite inferior, el valor de umbral inferior de datos dudosos, ( Y L = 1.02 ) resulta
menor al mínimo valor de los registros de precipitación presentados en la por lo que, estos
son validados por el umbral inferior.

**4.2** **ANÁLISIS DE FRECUENCIA DE PRECIPITACIONES MÁXIMAS DIARIAS**

El análisis probabilístico se realiza mediante el ajuste de las funciones de distribución de
Gumbel, Log-Normal, Log-Pearson III y Distribución Normal.

**4.2.1 DISTRIBUCION NORMAL**

El análisis probabilístico mediante el ajuste de la función de distribución Normal puede
presentarse en la siguiente forma:

P t = P+ Z∗σ p

Donde:

P t : Precipitación para un período de retorno T cualquiera mm

P : Valor medio del registro histórico mm

σ p : Desviación estándar del registro histórico mm

Z : Variable normal estándar de la distribución normal para cada período de
retorno.

La probabilidad acumulada de la distribución normal estándar se define como:

F(Z) = 1 − [1]

T r

**Tabla 4-4 Análisis de Datos Dudosos**

|Variable|Unidades|Chacrilla|
|---|---|---|
|N|No aplica|38|
|Mínimo|(mm)|11,1|
|Máximo|(mm)|125,0|
|Pm|(mm)|47,0|
|Sx|(mm)|23,6|

Fuente: Elaboración propia.

**4.2.2 DISTRIBUCION LOG - NORMAL**

El análisis probabilístico mediante el ajuste de distribución Log-Normal responde a la siguiente
función:

log(P t ) = log (P) + Z∗σ log(P)

Donde:
log(P t ) : Precipitación para un período de retorno T cualquiera, en mm
log (P) : Valor medio de los logaritmos del registro histórico, en mm

2210323-00-HID-MCA-001 REV B Página 9 de 25

σ log(P) : Desviación estándar de los logaritmos del registro histórico, en mm
Z : Variable normal estándar de la distribución normal para cada período de
retorno.
F(Z) : Probabilidad acumulada de la distribución normal estándar

La probabilidad acumulada de la distribución normal estándar se define como:

F(Z) = 1 − [1]

T r

**Tabla 4-5 Parámetros estadísticos (Log-Normal)**

|Variable|Unidades|Chacrilla|
|---|---|---|
|N|No aplica|38|
|Mínimo|(mm)|1,20|
|Máximo|(mm)|2,10|
|P log|(mm)|1,64|
|S log|(mm)|0,20|

Fuente: Elaboración propia

**4.2.3 DISTRIBUCION GUMBEL**

La distribución Gumbel responde a la siguiente expresión:

P t = P m − S [S] n [x]

∗(Y n + Ln(−Ln(1 − T [1] ~~[)]~~ [))]

Donde:

P t :Precipitación (mm) para Período de retorno T cualquiera

P m :Valor medio del registro histórico, en mm

S x :Desviación estándar del registro histórico, en mm

Y n :Valor medio de la variable reducida, es un parámetro de modelo función del tamaño de
la muestra

S n :Desviación estándar de la variable reducida función del tamaño de la serie, parámetro
del modelo

T :Período de retorno, en años

Ln :Logaritmo natural

**Tabla 4-6 Parámetros variable reducida (1989, Ayala et al)**

|Tamaño de la<br>Muestra<br>N|Valor Medio<br>Yn|Desviación<br>Estándar<br>Sn|
|---|---|---|
|10|0,50|0,95|
|15|0,51|1,01|

2210323-00-HID-MCA-001 REV B Página 10 de 25

|Tamaño de la<br>Muestra<br>N|Valor Medio<br>Yn|Desviación<br>Estándar<br>Sn|
|---|---|---|
|20|0,52|1,06|
|25|0,53|1,09|
|30|0,54|1,11|
|35|0,54|1,13|
|40|0,54|1,14|
|50|0,55|1,16|
|60|0,55|1,17|
|70|0,55|1,19|
|100|0,56|1,21|
||0,57|1,28|

Los parámetros para cada estación pluviométrica son los que se muestran en la tabla siguiente

**Tabla 4-7 Parámetros estadísticos (Gumbel)**

|Variable|Unidades|Chacrilla|
|---|---|---|
|N|No aplica|38|
|Mínimo|(mm)|11,1|
|Máximo|(mm)|125,3|
|Pm|(mm)|47,0|
|Sx|(mm)|23,6|
|Yn|(mm)|0,54|
|Sn|(mm)|1,14|

**4.2.4 DISTRIBUCION LOG - PEARSON TIPO III**

El análisis probabilístico se lleva a cabo mediante el ajuste de la función de distribución de
Log-Pearson Tipo III siguiente:

log(P t ) = log (P) + K∗σ log(P)

Donde:

P t : Precipitación para un período de retorno T cualquiera, en mm.

log (P) : Valor medio de los logaritmos del registro histórico, en mm.

σ log(P) : Desviación estándar de los logaritmos del registro histórico, en mm.

K : Factor de frecuencia del modelo en función del período de retorno T y el
coeficiente de asimetría (g) de los logaritmos de los valores de la serie.

n
g=
(n−1) ∗(n−2) ∗(σ log(Q) ) [∗∑(log(Q) − log (Q))]

2210323-00-HID-MCA-001 REV B Página 11 de 25

**Tabla 4-8 Parámetros estadísticos (Log-Pearson III)**

|Variable|Unidades|Chacrilla|
|---|---|---|
|N|No aplica|38|
|P log|(mm)|1,62|
|S log|(mm)|0,22|
|Coef. Asim|No aplica|-0,42|

2210323-00-HID-MCA-001 REV B Página 12 de 25

**Tabla 4-9 Valores de k para la distribución Log-Pearson Tipo III**

|Coeficiente<br>de<br>Asimetría|VALORES DE K PARA LA DISTRIBUCIÓN LOG-PEARSON TIPO III|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Coeficiente **<br>**de**<br>**Asimetría**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|**PERIODO DE RETORNO (AÑOS)**|
|**Coeficiente **<br>**de**<br>**Asimetría**|**1,0101**|**1,25**|**2 **|**5 **|**10**|**25**|**50**|**100**|
|**Coeficiente **<br>**de**<br>**Asimetría**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|**PROBABILIDAD DE NO EXCEDENCIA (%)**|
|**Coeficiente **<br>**de**<br>**Asimetría**|**1%**|**20%**|**50%**|**80%**|**90%**|**96%**|**98%**|**99%**|
|3,0|-0,667|-0,636|-0,396|0,420|1,180|2,278|3,152|4,051|
|2,8|-0,714|-0,666|-0,384|0,460|1,210|2,275|3,114|3,973|
|2,6|-0,769|-0,696|-0,368|0,499|1,238|2,267|3,071|3,889|
|2,4|-0,832|-0,725|-0,351|0,537|1,262|2,256|3,023|3,800|
|2,2|-0,905|-0,752|-0,330|0,574|1,284|2,240|2,970|3,705|
|2,0|-0,990|-0,777|-0,307|0,609|1,302|2,219|2,912|3,605|
|1,8|-1,087|-0,799|-0,282|0,643|1,318|2,193|2,848|3,499|
|1,6|-1,197|-0,817|-0,254|0,675|1,329|2,163|2,780|3,388|
|1,4|-1,318|-0,832|-0,225|0,705|1,337|2,128|2,706|3,271|
|1,2|-1,449|-0,844|-0,195|0,732|1,340|2,087|2,626|3,149|
|1,0|-1,588|-0,852|-0,164|0,758|1,340|2,043|2,542|3,022|
|0,8|-1,733|-0,856|-0,132|0,780|1,336|1,993|2,453|2,891|
|0,6|-1,880|-0,857|-0,099|0,800|1,328|1,939|2,359|2,755|
|-0,4|-2,615|-0,816|0,066|0,855|1,231|1,606|1,834|2,029|
|-0,6|-2,755|-0,800|0,099|0,857|1,200|1,528|1,720|1,880|
|-0,8|-2,891|-0,780|0,132|0,856|1,166|1,448|1,606|1,733|
|-1,0|-3,022|-0,758|0,164|0,852|1,128|1,366|1,492|1,588|
|-1,2|-3,149|-0,732|0,195|0,844|1,086|1,282|1,379|1,449|
|-1,4|-3,271|-0,705|0,225|0,832|1,041|1,198|1,270|1,318|
|-1,6|-3,388|-0,675|0,254|0,817|0,994|1,116|1,166|1,197|
|-1,8|-3,499|-0,643|0,282|0,799|0,945|1,035|1,069|1,087|
|-2,0|-3,605|-0,609|0,307|0,777|0,895|0,959|0,980|0,990|
|-2,2|-3,705|-0,574|0,330|0,752|0,844|0,888|0,900|0,905|
|-2,4|-3,800|-0,537|0,351|0,725|0,795|0,823|0,830|0,832|
|-2,6|-3,889|-0,499|0,368|0,696|0,747|0,764|0,768|0,769|
|-2,8|-3,973|-0,460|0,384|0,666|0,702|0,712|0,714|0,714|
|-3,0|-4,051|-0,420|0,396|0,636|0,660|0,666|0,666|0,667|

Fuente: Manual de Hidrología Básica para Estructuras de Drenagem, DNIT, pág. 45 y pág.
47. Ministerio dos Transportes 2005.

**4.3** **PRECIPITACION MAXIMA DIARIA**

|P ex|T|Normal|Log-Normal 2|Gumbel|Pearson III|Log-Pearson III|
|---|---|---|---|---|---|---|
|P ex|años|max inst anual|max inst anual|max inst anual|max inst anual|**max inst anual**|
|50.0%|2|47.1|43.2|43.4|42.4|**43.3**|
|20.0%|5|66.9|64.3|66.9|64.1|**64.8**|
|10.0%|10|77.3|79.2|82.5|78.5|**78.5**|
|5.0%|20|85.9|94.0|97.4|92.1|**91.1**|
|4.0%|25|88.3|98.8|102.2|96.4|**95.0**|
|2.0%|50|95.5|114.0|116.8|109.4|**106.6**|

2210323-00-HID-MCA-001 REV B Página 13 de 25

|P ex|T|Normal|Log-Normal 2|Gumbel|Pearson III|Log-Pearson III|
|---|---|---|---|---|---|---|
|P ex|años|max inst anual|max inst anual|max inst anual|max inst anual|**max inst anual**|
|1.0%|100|101.9|129.6|131.2|122.2|**117.8**|
|0.7%|150|105.4|139.0|139.7|129.6|**124.1**|
|0.5%|200|107.8|145.8|145.7|134.9|**128.4**|
|0.4%|250|109.6|151.2|150.3|138.9|**131.8**|
|0.2%|500|114.9|168.2|164.7|151.4|**142.0**|
|0.1%|1000|119.9|185.9|179.1|163.8|**151.9**|
|0.01%|10000|134.7|250.1|226.8|204.9|**182.7**|

**4.4** **PRUEBA DE BONDAD DE AJUSTE**

El método más usado para medir la bondad de ajuste de una distribución de probabilidad a
una serie de valores es el test Chi-Cuadrado. Este test consiste en comparar la frecuencia
observada en un intervalo, previamente definido, con la frecuencia teórica, que es función del
modelo probabilístico usado.

Llamando f s (x i ) al valor observado de la frecuencia relativa del intervalo i y p(x i ) al valor
teórico, se tiene:

f s (x i ) = [n] [i]

N

P(x i ) = F(x i ) −F(x i−1 )

Donde:

n i : Número de datos observados en el intervalo i .

N : Número total de datos de la serie.

F(x i ) : Frecuencia acumulada y teórica, calculada según el modelo, para el mayor valor del
intervalo.

Una vez determinadas las frecuencias relativas para cada intervalo, se calcula el estadígrafo
Chi-Cuadrada, X α,δ2 con la siguiente ecuación

k

(X c ) [2]
= ∑N [(f] [x] [(x] [i] [) − P(x] [i] [))] [2]

i=1

P(x i )

En este tipo de análisis se recomienda que el número total de intervalos sea mayor que 5 y
menor que 20, siendo una alternativa calcularlo con la Regla de Sturges:

k= 1 + 3,3 ∗log (N)

Donde:

k : Número total de intervalos.

Para que el ajuste de la distribución de probabilidad a la serie de valores sea aceptable, se
requiere que el valor Chi-Cuadrado, X C2, sea menor que el valor teórico que toma la distribución

Chi-Cuadrado para un cierto nivel de confianza, es decir:

2210323-00-HID-MCA-001 REV B Página 14 de 25

2  _X_  2,

2

_X_ _c_  _X_  

Donde:

# X α,δ2 Valor teórico (tabulado) que toma la distribución Chi-Cuadrado para un nivel de

confianza  (comúnmente 95%) y  grados de libertad.

Dónde:

δ = k −m −1

m : Número de parámetros utilizados en el ajuste de la distribución propuesta.

**Tabla 4-10 Test de Bondad**

|Coeficiente|Normal|Log-Normal 2|Gumbel|Pearson III|Log-Pearson III|
|---|---|---|---|---|---|
|R2|0.9039|0.9753|0.9691|0.9691|**0.9761**|
|Chi2 Calculado<br>Chi2 Tabulado<br>Ajuste<br>Criterio|1.4037<br>7.8147<br>0.1796<br>Aceptado|9.0364<br>7.8147<br>1.1563<br>Rechazado|1.4049<br>7.8147<br>0.1798<br>Aceptado|5.8008<br>5.9915<br>0.9682<br>Aceptado|1.8895<br>5.9915<br>0.3154<br>Aceptado|
||||||**OK**|

Se observa que el análisis de regresión realizado empleando el modelo **Log-Pearson tipo III**
son los que arrojan los mejores resultados.

**4.5** **PRECIPITACION MAXIMA DIARIA ABSOLUTA**

Asumiendo las recomendaciones del Manual de Carreteras Vol. 3, y por tratarse de estaciones
pluviométricas, las precipitaciones calculadas se amplifican por el factor k = 1,1.

Estos nuevos valores de precipitaciones corregidas se muestran en la tabla siguiente.

**Tabla 4-11 Precipitaciones Máximas Absolutas en 24 horas (mm)**

|T|Chacrilla|
|---|---|
|2|**47.6**|
|5|**71.3**|
|10|**86.4**|
|20|**100.2**|
|25|**104.5**|
|50|**117.3**|
|**100 **|**129.5 **|
|150|**136.5**|
|200|**141.3**|
|250|**145.0**|
|500|**156.2**|
|1000|**167.1**|
|10000|**200.9**|

2210323-00-HID-MCA-001 REV B Página 15 de 25

**5** **ESCORRENTIA SUPERFICIAL**

**5.1** **DEFINICION DE CUENCAS**

Del análisis de interferencia entre el proyecto y los cauces naturales, se han detectado 22
puntos de análisis (ver Figura 5-1).

Las áreas aportantes para cada cauce interferido por el proyecto ha sido trazado por las
cumbres más altas de las cadenas montañosas, con punto de descarga la ubicación del
proyecto.

La delimitación de la superficie se realiza considerando como base la cartografía digital
correspondiente a Cabildo (carta IGM E029 SE).

|Col1|4|
|---|---|
|**5 **||

**Figura 5-1 Cuencas aportantes**

**5.1.1 DESCRIPCIÓN MORMOMÉTRICA**

En la Tabla 5-1 se presenta un resumen con las variables más importantes de las cuencas
aportantes según el escenario actual o proyectado.

**Tabla 5-1 Parámetros morfométricos de cuenca sin proyecto**

|Cuenca|Área|L(ppal)|H(max)|H(min)|H|Hg|Pendiente|
|---|---|---|---|---|---|---|---|
|Nombre|(Km2)|(Km)|(m)|(m)|(m)|(m)|(m/m)|
|1|0.103|0.358|727.5|516|211.5|105.8|0.59|
|2|0.027|0.265|650|508|142.0|71.0|0.54|
|3|0.017|0.117|637|512|125.0|62.5|1.07|
|4|0.011|0.098|550|512|38.0|19.0|0.39|

2210323-00-HID-MCA-001 REV B Página 16 de 25

|5|0.005|0.025|525|500|25.0|12.5|1.00|
|---|---|---|---|---|---|---|---|
|6|0.005|0.072|525|500|25.0|12.5|0.35|
|7|0.003|0.033|537|520|17.0|8.5|0.52|
|8|0.010|0.092|550|512|38.0|19.0|0.41|
|9|0.229|0.714|750|456|294.0|147.0|0.41|
|10|0.213|0.86|750|477|273.0|136.5|0.32|
|11|1.863|2.3|1225|477|748.0|374.0|0.33|
|12|2.541|2.536|1225|462|763.0|381.5|0.30|
|13|0.018|0.248|587|455|132.0|66.0|0.53|
|14|0.267|0.85|806|437|369.0|184.5|0.43|
|15|0.053|0.227|487|437|50.0|25.0|0.22|
|16|0.008|0.09|530|425|105.0|52.5|1.17|
|17|0.015|0.09|530|425|105.0|52.5|1.17|
|18|0.007|0.09|506|412|94.0|47.0|1.04|
|19|0.040|0.255|575|416|159.0|79.5|0.62|
|20|0.064|0.308|633|412|221.0|110.5|0.72|
|21|0.189|0.718|806|416|390.0|195.0|0.54|
|22|0.077|0.496|650|366|284.0|142.0|0.57|

**5.1.2 TIEMPO DE CONCENTRACION**

El tiempo de concentración se define como el tiempo que demora la gota de agua
hidráulicamente más alejada en llegar al punto de descarga o salida. Para determinar los
tiempos de concentración se utilizan fórmulas empíricas.

_**a)**_ _**Kirpich (1940)**_

T c = 3,98 ∗(S [L] [0,5][1] ~~[)]~~

T c = 3,98 ∗(S [L] [1]

0,77

_**b)**_ _**California Culverts Practice (1942)**_

3

0,385

T c H
= 60,0 ∗(0,87 ∗ [L] [1]

[1]

H [)]

_**c)**_ _**Giandotti,**_ Con restricción a cuencas con áreas menores a 200 ha

T c
= 60 ∗( [4 ∗] 0,8 ∗ ~~[√]~~ [A+ 1,5 ∗L] ~~√~~ H m [1]

)

condición:

4,5 _L_ 1  _T_ _c_  6,3 _L_ 1

En que:

T c : Tiempo de Concentración (min.)

S : Pendiente promedio de la cuenca (m/m)

L 1 : Longitud del Cauce principal (km)

2210323-00-HID-MCA-001 REV B Página 17 de 25

H : Diferencia de altura en cuenca (m).

H 1 : Desnivel entre la salida y el nivel medio de la cuenca (m).

Finalmente, en la adopción del tiempo de concentración de diseño se seleccionó aquel que
estuviese en el rango de valores del conjunto de métodos utilizados, relacionando siempre en
todo este proceso la experiencia obtenida en terreno.

**Tabla 5-2 Tiempo de concentración - Escenario sin proyecto**

|Cuenca<br>nombre|Área|Longitud<br>principal|Cotas|Col5|Desnivel|Col7|Pendiente|Tiempo de concentración|Col10|Col11|tc|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Cuenca<br>nombre|Área|Longitud<br>principal|H(max)|H(min)|H|Hg||Kirpich|C.C.P|Giandotti|adoptado|
|Cuenca<br>nombre|(km2)|(km)|m|m|(m)|(m)|(m/m)|(min)|(min)|(min)|(min)|

|1|0.103|0.358|727.5|516|211.5|105.8|0.59|2.21|2.21|***|2.21|
|---|---|---|---|---|---|---|---|---|---|---|---|
|2|0.027|0.265|650|508|142.0|71.0|0.54|1.82|1.82|***|1.82|
|3|0.017|0.117|637|512|125.0|62.5|1.07|0.74|0.74|***|0.74|
|4|0.011|0.098|550|512|38.0|19.0|0.39|0.96|0.96|***|0.96|
|5|0.005|0.025|525|500|25.0|12.5|1.00|0.23|0.23|***|0.23|
|6|0.005|0.072|525|500|25.0|12.5|0.35|0.79|0.79|***|0.79|
|7|0.003|0.033|537|520|17.0|8.5|0.52|0.37|0.37|***|0.37|
|8|0.010|0.092|550|512|38.0|19.0|0.41|0.89|0.89|***|0.89|
|9|0.229|0.714|750|456|294.0|147.0|0.41|4.32|4.32|***|4.32|
|10|0.213|0.86|750|477|273.0|136.5|0.32|5.51|5.51|***|5.51|
|11|1.863|2.3|1225|477|748.0|374.0|0.33|11.65|11.65|***|11.65|
|12|2.541|2.536|1225|462|763.0|381.5|0.30|12.94|12.94|***|12.94|
|13|0.018|0.248|587|455|132.0|66.0|0.53|1.73|1.73|***|1.73|
|14|0.267|0.85|806|437|369.0|184.5|0.43|4.84|4.84|***|4.84|
|15|0.053|0.227|487|437|50.0|25.0|0.22|2.28|2.27|***|2.27|
|16|0.008|0.09|530|425|105.0|52.5|1.17|0.59|0.59|***|0.59|
|17|0.015|0.09|530|425|105.0|52.5|1.17|0.59|0.59|***|0.59|
|18|0.007|0.09|506|412|94.0|47.0|1.04|0.61|0.61|***|0.61|
|19|0.040|0.255|575|416|159.0|79.5|0.62|1.67|1.67|***|1.67|
|20|0.064|0.308|633|412|221.0|110.5|0.72|1.83|1.83|***|1.83|
|21|0.189|0.718|806|416|390.0|195.0|0.54|3.90|3.90|***|3.90|
|22|0.077|0.496|650|366|284.0|142.0|0.57|2.87|2.87|***|2.87|

Es importante señalar, que, en la selección del tiempo de concentración, se ha adoptado el
tiempo de concentración menor, pues este valor maximiza el valor de la intensidad, acción
que entrega caudales mayores resultando en estructuras con un factor de seguridad adicional.

Como norma general, el Manual de Carreteras recomienda que el tiempo de concentración
no debe ser inferior a 10 minutos, salvo que se tengan mediciones en terreno que justifiquen
adoptar valores menores.

**5.2** **INTENSIDAD DE LA PRECIPITACION**

La intensidad de lluvia se define como la tasa temporal de precipitación, o la razón de
incremento de la altura que alcanza la lluvia respecto al tiempo.

 Duración mayor a 1 hora.

2210323-00-HID-MCA-001 REV B Página 18 de 25

De acuerdo con lo presentado en el libro, hidrología aplicada, Ven Te Chow, la intensidad
puede ser expresada en forma general como:

I(t, T) = [P(t, T)]

t d

- Duración menor a 1 hora.

Para aquellos casos con duraciones menores a 1 hora, es posible utilizar la expresión
desarrollada por Bell (Manual de Carreteras, volumen 3, 2008) que permite calcular

I(t, T) = [P(t, T)]

(60 ~~[t]~~ [d]

60 ~~[t]~~ [d] ~~[)]~~

Donde

I(t, T) : Intensidad de lluvia (mm/H) asociada a un periodo de retorno T (años), para
una duración t d (horas)

P(t, T) : Precipitación de lluvia (mm) asociada a un periodo de retorno T (años), para
una duración t d (horas)

t d : Duración de la precipitación (H)

**5.2.1 COEFICIENTE DE DURACIÓN**

El coeficiente de duración corresponde a la relación entre la lluvia caída en una determinada
duración y la lluvia caída en 24 horas, ambas para la misma frecuencia.

Duración mayor a 1 hora

Para precipitaciones con duración mayor a 1 hora, se han considerado los valores de la
estación Pluviométrica de Quillota (Tabla 3.702.403A, incluidas en el MC-V3), siendo la más
cercana al sector del proyecto. para duraciones comprendidas en el rango 1 a 24 horas.

**Tabla 5-3 Coeficiente de Duración - Estación Quillota**

|Estación<br>Meteorológica|Duración|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Estación<br>Meteorológica|1|2|4|6|8|10|12|14|18|24|
|Quillota|0,13|0,23|0,38|0,50|0,58|0,67|0,75|0,80|0,88|1,00|

**5.2.2 CURVA INTENSIDAD - DURACION - FRECUENCIA**

La familia de curvas que considera todos los períodos de retorno es la curva intensidadduración-frecuencia.

Éstas definen la intensidad de diseño dado un tiempo de concentración igual a la duración de
la lluvia para un cierto período de retorno.

Para cada período de retorno, es posible encontrar una curva determinada de intensidad duración.

2210323-00-HID-MCA-001 REV B Página 19 de 25

|Col1|Col2|INTENSIDAD (mm/Hr)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**T (años)**|2|6.2|5.5|4.5|4.0|3.5|3.2|3.0|2.7|2.3|1.98|
|**T (años)**|5|9.3|8.2|6.8|5.9|5.2|4.8|4.5|4.1|3.5|2.97|
|**T (años)**|10|11.2|9.9|8.2|7.2|6.3|5.8|5.4|4.9|4.2|3.60|
|**T (años)**|20|13.0|11.5|9.5|8.4|7.3|6.7|6.3|5.7|4.9|4.18|
|**T (años)**|25|13.6|12.0|9.9|8.7|7.6|7.0|6.5|6.0|5.1|4.35|
|**T (años)**|50|15.2|13.5|11.1|9.8|8.5|7.9|7.3|6.7|5.7|4.89|
|**T (años)**|100|16.8|14.9|12.3|10.8|9.4|8.7|8.1|7.4|6.3|5.40|
|**T (años)**|150|17.7|15.7|13.0|11.4|9.9|9.1|8.5|7.8|6.7|5.69|
|**T (años)**|200|18.4|16.2|13.4|11.8|10.2|9.5|8.8|8.1|6.9|5.89|
|**T (años)**|250|18.9|16.7|13.8|12.1|10.5|9.7|9.1|8.3|7.1|6.04|
|**T (años)**|500|20.3|18.0|14.8|13.0|11.3|10.5|9.8|8.9|7.6|6.51|
|**T (años)**|1000|21.7|19.2|15.9|13.9|12.1|11.2|10.4|9.5|8.2|6.96|
|**T (años)**|10000|26.1|23.1|19.1|16.7|14.6|13.5|12.6|11.5|9.8|8.37|

|Col1|Col2|INTENSIDAD (mm/Hr)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**T (años)**|2|21.5|17.1|14.1|11.9|9.8|7.9|7.0|6.2|
|**T (años)**|5|32.3|25.6|21.1|17.8|14.6|11.8|10.5|9.3|
|**T (años)**|10|39.1|31.0|25.6|21.6|17.7|14.3|12.7|11.2|
|**T (años)**|20|45.3|36.0|29.7|25.0|20.6|16.6|14.7|13.0|
|**T (años)**|25|47.3|37.5|31.0|26.1|21.5|17.3|15.3|13.6|
|**T (años)**|50|53.1|42.1|34.8|29.3|24.1|19.4|17.2|15.2|
|**T (años)**|100|58.6|46.5|38.4|32.3|26.6|21.5|19.0|16.8|
|**T (años)**|150|61.8|49.0|40.5|34.1|28.0|22.6|20.0|17.7|
|**T (años)**|200|63.9|50.7|41.9|35.3|29.0|23.4|20.7|18.4|
|**T (años)**|250|65.6|52.0|43.0|36.2|29.8|24.0|21.3|18.9|
|**T (años)**|500|70.7|56.0|46.3|39.0|32.1|25.9|22.9|20.3|
|**T (años)**|1000|75.6|60.0|49.5|41.7|34.3|27.7|24.5|21.7|
|**T (años)**|10000|90.9|72.1|59.5|50.1|41.3|33.3|29.5|26.1|

|abla 5-5 Curva IDF (Duración t > 1 hora)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|Duración en Horas|
|1|2|4|6|8|10|12|14|18|24|
|0.13|0.23|0.38|0.50|0.58|0.67|0.75|0.80|0.88|1.00|

|bla 5-4 Curva IDF (Duración t < 1 hora)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Duración en Minutos|Duración en Minutos|Duración en Minutos|Duración en Minutos|Duración en Minutos|Duración en Minutos|Duración en Minutos|Duración en Minutos|
|5|10|15|20|30|40|50|60|
|0.29|0.46|0.57|0.64|0.79|0.85|0.94|1.00|

2210323-00-HID-MCA-001 REV B Página 20 de 25

100

90

80

70

60

50

40

30

20

10

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||T=2 años|T=5 año|T=|0 años|T=20 años|T=25 años|||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||T= 50 años|T=100 a|os<br>T=|50 años|T=200 años|T=250 años|||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||T=500 años|T=1000|ños<br>T=|0.000 años|||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||

0 10 20 30 40 50 60

Tiempo de Concentracion (minutos)

**Figura 5-2 Curva IDF (Duracion t < 1 hora)**

30

25

20

15

10

5

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|Col45|Col46|Col47|Col48|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||=2 a|os|||||T=5|ños|||||T=1|año|||||T=2|año|s||||T=2|añ|s||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||= 50|ño|||||T=10|0 añ|s||||T=1|0 añ|s||||T=2|0 añ|os||||T=2|0 a|os||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||=500|añ|s||||T=10|00 a|os||||T=1|.000|año||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||

0 5 10 15 20

Tiempo de Concentracion (Horas)

**Figura 5-3 Curva IDF (Duracion t > 1 hora)**

2210323-00-HID-MCA-001 REV B Página 21 de 25

**5.3** **DETERMINACION DE LOS CAUDALES LIQUIDOS**

Para la determinación de los caudales líquidos, se han adoptado las recomendaciones
propuestas en la **Guías Metodológica para Proyectos de Modificación de Cauces**, en la
que se distingue entre cuencas con áreas aportantes menores y mayores a 25 Km2.

**5.3.1 CUENCAS CON AREAS MENORES A 25 KM2**

Los caudales máximos de crecida han sido estimados empleando el criterio del método
racional, que permite estimar el caudal de crecida en cuencas con áreas aportantes menores
a 25 Km [2] (Manual de Carreteras, volumen 3, 2008).

El método racional, propuesto por Mulvaney en 1850, es ampliamente utilizado para estimar
caudales de diseño en cuencas urbanas y rurales medianas y pequeñas debido a su
simplicidad y lógica. Su aplicación aparece descrita en el punto 2.402.8 del Manual de
Carreteras y en el “Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin
Información Fluviométricas” de la Dirección General de Aguas del Ministerio de Obras
Públicas.

El caudal máximo asociado a un determinado período de retorno, según el método racional,
se calcula con la siguiente expresión:

T ∗A

Q= [C∗I] [t]

3,6

Donde:

Q : Caudal en (m [3] /s).

A : Área aportante en (km [2] ).

C : Coeficiente de escorrentía.

I tT : Intensidad para t igual al tiempo de concentración y período de retorno T expresada

en mm/H.

- Coeficiente de escorrentía

El coeficiente de escorrentía ha sido adoptado de acuerdo con las recomendaciones
presentadas en el Manual de Carreteras, volumen 3, que incluye los factores de relieve,
infiltración, cobertura vegetal y almacenamiento de agua en el suelo, adaptados desde
experiencias internacionales (Estado de California, 1995)

En la

2210323-00-HID-MCA-001 REV B Página 22 de 25

Tabla 5-6 se presenta un rango de valores, de los cuales, conservadoramente, se ha optado
por elegir el valor más alto, lo que se resultara en un caudal más conservador, aumentando
la seguridad de las obras proyectadas.

2210323-00-HID-MCA-001 REV B Página 23 de 25

**Tabla 5-6 Coeficiente de Escorrentía**

|Factor|Extremo|Alto|Normal|Bajo|
|---|---|---|---|---|
|**Relieve**|**0,28-0,35**<br>Escarpe con<br>pendientes<br>mayores que 30%|**0,20-0,28**<br>Montañoso con<br>pendientes entre 10 y<br>30%|**0,14-0,20**<br>Con cerros y<br>pendientes entre<br>5 y 10%|**0,08-0,14**<br>Relativamente plano<br>con pendientes<br>menores a 5%<br>|
|**Infiltración**|**0,12-0,16**<br>Suelo rocoso, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable|**0,08-0,12**<br>Suelos arcillosos o<br>limosos con baja<br>capacidad de<br>infiltración, mal<br>drenados|**0,06-0,08**<br>Normales, bien<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos|**0,04-0,06**<br>Suelos profundos de<br>arena u otros suelos<br>bien drenados con alta<br>capacidad de<br>infiltración|
|**Cobertura Vegetal**|**0,12-0,16**<br>Cobertura escasa,<br>terreno sin<br>vegetación o<br>escasa cobertura|**0,08-0,12**<br>Poca vegetación,<br>terrenos cultivados o<br>naturales, menos del<br>20% del área con<br>buena cobertura<br>vegetal|**0,06-0,08**<br>Regular a buena,<br>50% del área con<br>praderas o<br>bosques, no más<br>del 50% cultivado|**0,04-0,06**<br>Buena a excelente,<br>90% del área con<br>praderas, bosques o<br>cobertura equivalente.|
|**Almacenamiento**<br>**Superficial**|**0,10-0,12**<br>Despreciable,<br>pocas depresiones<br>superficiales, sin<br>zonas húmedas|**0,08-0,10**<br>Baja, sistema de<br>cauces superficiales<br>pequeños bien<br>definidos, sin zonas<br>húmedas.|**0,06-0,08**<br>Normal, posibilidad<br>de almacenamiento<br>buena, zonas<br>húmedas,<br>pantanos, lagunas<br>y lagos.|**0,04-0,06**<br>Capacidad alta,<br>sistema hidrográfico<br>poco definido, buenas<br>planicies de<br>inundación o gran<br>cantidad de zonas<br>húmedas, lagunas o<br>pantanos.|
|**Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25**|**Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25**|**Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25**|**Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25**|**Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25**|

Fuente: Tabla 3.702.503.B, Manual de Carreteras, volumen 3, año 2008

De esta forma, es posible afirmar que el valor del coeficiente de escorrentía que representa la
capacidad de infiltración del suelo alcanza un valor de 0,60 para un periodo de retorno de
menor o igual a 20 años.

**Tabla 5-7 Coeficiente de Escorrentía Adoptados**

|Periodo de Retorno|(T en años)|20 o menor|25|50|100 o mayor|
|---|---|---|---|---|---|
|Coeficiente Escorrentía|C|0,60|0,66|0,72|0,75|

Fuente: Elaboración propia

2210323-00-HID-MCA-001 REV B Página 24 de 25

**Tabla 5-8 Caudales Máximos Instantáneos**

|Cuenca|A|tc|C|Col5|Col6|I|Col8|Col9|Col10|Col11|Q|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Cuenca|A|tc|T = 20|T = 25|T ≥ 100|T=20|T=25|T=50|T=100|T=200|T=20|T=25|T=50|T=100|T=200|
|(N°)|(Km2)|(min)|(min)|(min)|(min)|<br>(mm/Hr)|<br>(mm/Hr)|<br>(mm/Hr)|<br>(mm/Hr)|<br>(mm/Hr)|(m3/s)|(m3/s)|(m3/s)|(m3/s)|(m3/s)|

|1|0.103|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.62|0.64|0.72|1.00|1.09|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2|0.027|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.16|0.17|0.19|0.26|0.29|
|3|0.017|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.10|0.11|0.12|0.17|0.18|
|4|0.011|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.07|0.07|0.08|0.11|0.12|
|5|0.005|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.03|0.03|0.03|0.05|0.05|
|6|0.005|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.03|0.03|0.04|0.05|0.06|
|7|0.003|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.02|0.02|0.02|0.03|0.03|
|8|0.010|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.06|0.06|0.07|0.10|0.10|
|9|0.229|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|1.37|1.43|1.60|2.21|2.41|
|10|0.213|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|1.28|1.33|1.50|2.06|2.25|
|11|1.863|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|11.18|11.64|13.07|18.05|19.68|
|12|2.541|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|15.24|15.88|17.83|24.61|26.84|
|13|0.018|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.11|0.11|0.13|0.18|0.19|
|14|0.267|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|1.60|1.67|1.88|2.59|2.82|
|15|0.053|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.32|0.33|0.37|0.52|0.56|
|16|0.008|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.05|0.05|0.06|0.08|0.08|
|17|0.015|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.09|0.09|0.10|0.14|0.15|
|18|0.007|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.04|0.04|0.05|0.07|0.07|
|19|0.040|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.24|0.25|0.28|0.39|0.43|
|20|0.064|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.38|0.40|0.45|0.62|0.68|
|21|0.189|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|1.13|1.18|1.33|1.83|2.00|
|22|0.077|10|0.60|0.66|0.75|36.00|37.50|42.10|46.50|50.70|0.46|0.48|0.54|0.74|0.81|

Fuente: Elaboración propia

**FIN DEL DOCUMENTO. -**

2210323-00-HID-MCA-001 REV B Página 25 de 25

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1: Estaciones Pluviométricas****

| Estación | Código BNA | Ubicación Geográfica | Col4 | Col5 | Col6 | Administración |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Código BNA** | **Este** | **Norte** | **Altura**<br>**(msnm)** | **Cuenca** | **Cuenca** |
| La Viña | 05210002-k | 320.246 | 6.410.050 | 370 | Rio Ligua | DGA |
| Chacrilla | 05220006-7 | 306.249 | 6.410.346 | 290 | Rio Ligua | DGA |
| Las Puertas | 05211004-1 | 318.419 | 6.403.948 | 350 | Rio Ligua | DGA |
| Alicahue | 05200006-8 | 335.143 | 6.420.422 | 750 | Rio Ligua | DGA |

**Tabla 4-1.**

| AÑO | X: Pp<br>max | Y∶log(X) | Y−Y | 2<br>(Y−Y) | 3<br>(Y−Y) |
| --- | --- | --- | --- | --- | --- |
| REGISTRO | (mm) | (mm) | (mm) | (mm) | (mm) |
| 1983 | 51.60 | 1.7 | 0.1 | 0.01 | 0.00 |
| 1984 | 98.50 | 2.0 | 0.4 | 0.14 | 0.05 |
| 1985 | 39.40 | 1.6 | 0.0 | 0.00 | 0.00 |
| 1986 | 92.00 | 2.0 | 0.3 | 0.12 | 0.04 |
| 1987 | 77.20 | 1.9 | 0.3 | 0.07 | 0.02 |
| 1988 | 18.10 | 1.3 | -0.4 | 0.13 | -0.05 |
| 1989 | 40.50 | 1.6 | 0.0 | 0.00 | 0.00 |
| 1990 | 21.50 | 1.3 | -0.3 | 0.08 | -0.02 |
| 1991 | 41.00 | 1.6 | 0.0 | 0.00 | 0.00 |
| 1992 | 62.50 | 1.8 | 0.2 | 0.03 | 0.01 |
| 1993 | 54.20 | 1.7 | 0.1 | 0.01 | 0.00 |
| 1994 | 16.00 | 1.2 | -0.4 | 0.17 | -0.07 |
| 1995 | 45.50 | 1.7 | 0.0 | 0.00 | 0.00 |
| 1996 | 37.10 | 1.6 | -0.1 | 0.00 | 0.00 |
| 1997 | 57.30 | 1.8 | 0.1 | 0.02 | 0.00 |
| 1998 | 11.10 | 1.0 | -0.6 | 0.33 | -0.19 |
| 1999 | 38.60 | 1.6 | 0.0 | 0.00 | 0.00 |
| 2000 | 37.20 | 1.6 | 0.0 | 0.00 | 0.00 |
| 2001 | 54.70 | 1.7 | 0.1 | 0.01 | 0.00 |
| 2002 | 125.30 | 2.1 | 0.5 | 0.23 | 0.11 |
| 2003 | 45.50 | 1.7 | 0.0 | 0.00 | 0.00 |
| 2004 | 47.00 | 1.7 | 0.1 | 0.00 | 0.00 |
| 2005 | 28.40 | 1.5 | -0.2 | 0.03 | 0.00 |
| 2006 | 68.30 | 1.8 | 0.2 | 0.05 | 0.01 |
| 2007 | 64.20 | 1.8 | 0.2 | 0.04 | 0.01 |
| 2008 | 59.30 | 1.8 | 0.2 | 0.02 | 0.00 |
| 2009 | 40.00 | 1.6 | 0.0 | 0.00 | 0.00 |
| 2010 | 26.20 | 1.4 | -0.2 | 0.04 | -0.01 |
| 2011 | 34.20 | 1.5 | -0.1 | 0.01 | 0.00 |
| 2012 | 40.00 | 1.6 | 0.0 | 0.00 | 0.00 |
| 2013 | 35.20 | 1.5 | -0.1 | 0.01 | 0.00 |
| 2014 | 38.20 | 1.6 | 0.0 | 0.00 | 0.00 |
| 2015 | 60.50 | 1.8 | 0.2 | 0.03 | 0.00 |
| 2016 | 60.20 | 1.8 | 0.2 | 0.03 | 0.00 |
| 2017 | 50.00 | 1.7 | 0.1 | 0.01 | 0.00 |

**Tabla 4-2: Valores de** _**K**_ _**n**_ **para la Prueba de Datos Dudosos****

| Tamaño<br>Muestra | K<br>n |
| --- | --- |
| 10 | 2,036 |
| 15 | 2,247 |
| 20 | 2,385 |
| 25 | 2,486 |
| 30 | 2,563 |
| 35 | 2,628 |
| 40 | 2,682 |

**Tabla 4-3: Análisis de Datos Dudosos****

| Variable | Item | Valor |
| --- | --- | --- |
| Promedio | Y | 1,62 |
| Desviación Estándar | Sy | 0,22 |
| Numero de datos | N | 38,00 |
| Variable de datos dudosos | Kn | 2,682 |
| Umbral superior de datos dudosos | YH | 2.20 |
| Umbral inferior de datos dudosos | YL | 1,02 |

**Tabla 4-4: Análisis de Datos Dudosos****

| Variable | Unidades | Chacrilla |
| --- | --- | --- |
| N | No aplica | 38 |
| Mínimo | (mm) | 11,1 |
| Máximo | (mm) | 125,0 |
| Pm | (mm) | 47,0 |
| Sx | (mm) | 23,6 |

**Tabla 4-5: Parámetros estadísticos (Log-Normal)****

| Variable | Unidades | Chacrilla |
| --- | --- | --- |
| N | No aplica | 38 |
| Mínimo | (mm) | 1,20 |
| Máximo | (mm) | 2,10 |
| P log | (mm) | 1,64 |
| S log | (mm) | 0,20 |

**Tabla 4-6: Parámetros variable reducida (1989, Ayala et al)****

| Tamaño de la<br>Muestra<br>N | Valor Medio<br>Yn | Desviación<br>Estándar<br>Sn |
| --- | --- | --- |
| 20 | 0,52 | 1,06 |
| 25 | 0,53 | 1,09 |
| 30 | 0,54 | 1,11 |
| 35 | 0,54 | 1,13 |
| 40 | 0,54 | 1,14 |
| 50 | 0,55 | 1,16 |
| 60 | 0,55 | 1,17 |
| 70 | 0,55 | 1,19 |
| 100 | 0,56 | 1,21 |
|  | 0,57 | 1,28 |

**Tabla 4-7: Parámetros estadísticos (Gumbel)****

| Variable | Unidades | Chacrilla |
| --- | --- | --- |
| N | No aplica | 38 |
| Mínimo | (mm) | 11,1 |
| Máximo | (mm) | 125,3 |
| Pm | (mm) | 47,0 |
| Sx | (mm) | 23,6 |
| Yn | (mm) | 0,54 |
| Sn | (mm) | 1,14 |

**Tabla 4-8: Parámetros estadísticos (Log-Pearson III)****

| Variable | Unidades | Chacrilla |
| --- | --- | --- |
| N | No aplica | 38 |
| P log | (mm) | 1,62 |
| S log | (mm) | 0,22 |
| Coef. Asim | No aplica | -0,42 |

**Tabla 4-9: Valores de k para la distribución Log-Pearson Tipo III****

| Coeficiente<br>de<br>Asimetría | VALORES DE K PARA LA DISTRIBUCIÓN LOG-PEARSON TIPO III | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Coeficiente **<br>**de**<br>**Asimetría** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** | **PERIODO DE RETORNO (AÑOS)** |
| **Coeficiente **<br>**de**<br>**Asimetría** | **1,0101** | **1,25** | **2 ** | **5 ** | **10** | **25** | **50** | **100** |
| **Coeficiente **<br>**de**<br>**Asimetría** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** | **PROBABILIDAD DE NO EXCEDENCIA (%)** |
| **Coeficiente **<br>**de**<br>**Asimetría** | **1%** | **20%** | **50%** | **80%** | **90%** | **96%** | **98%** | **99%** |
| 3,0 | -0,667 | -0,636 | -0,396 | 0,420 | 1,180 | 2,278 | 3,152 | 4,051 |
| 2,8 | -0,714 | -0,666 | -0,384 | 0,460 | 1,210 | 2,275 | 3,114 | 3,973 |
| 2,6 | -0,769 | -0,696 | -0,368 | 0,499 | 1,238 | 2,267 | 3,071 | 3,889 |
| 2,4 | -0,832 | -0,725 | -0,351 | 0,537 | 1,262 | 2,256 | 3,023 | 3,800 |
| 2,2 | -0,905 | -0,752 | -0,330 | 0,574 | 1,284 | 2,240 | 2,970 | 3,705 |
| 2,0 | -0,990 | -0,777 | -0,307 | 0,609 | 1,302 | 2,219 | 2,912 | 3,605 |
| 1,8 | -1,087 | -0,799 | -0,282 | 0,643 | 1,318 | 2,193 | 2,848 | 3,499 |
| 1,6 | -1,197 | -0,817 | -0,254 | 0,675 | 1,329 | 2,163 | 2,780 | 3,388 |
| 1,4 | -1,318 | -0,832 | -0,225 | 0,705 | 1,337 | 2,128 | 2,706 | 3,271 |
| 1,2 | -1,449 | -0,844 | -0,195 | 0,732 | 1,340 | 2,087 | 2,626 | 3,149 |
| 1,0 | -1,588 | -0,852 | -0,164 | 0,758 | 1,340 | 2,043 | 2,542 | 3,022 |
| 0,8 | -1,733 | -0,856 | -0,132 | 0,780 | 1,336 | 1,993 | 2,453 | 2,891 |
| 0,6 | -1,880 | -0,857 | -0,099 | 0,800 | 1,328 | 1,939 | 2,359 | 2,755 |
| -0,4 | -2,615 | -0,816 | 0,066 | 0,855 | 1,231 | 1,606 | 1,834 | 2,029 |
| -0,6 | -2,755 | -0,800 | 0,099 | 0,857 | 1,200 | 1,528 | 1,720 | 1,880 |
| -0,8 | -2,891 | -0,780 | 0,132 | 0,856 | 1,166 | 1,448 | 1,606 | 1,733 |
| -1,0 | -3,022 | -0,758 | 0,164 | 0,852 | 1,128 | 1,366 | 1,492 | 1,588 |
| -1,2 | -3,149 | -0,732 | 0,195 | 0,844 | 1,086 | 1,282 | 1,379 | 1,449 |
| -1,4 | -3,271 | -0,705 | 0,225 | 0,832 | 1,041 | 1,198 | 1,270 | 1,318 |
| -1,6 | -3,388 | -0,675 | 0,254 | 0,817 | 0,994 | 1,116 | 1,166 | 1,197 |
| -1,8 | -3,499 | -0,643 | 0,282 | 0,799 | 0,945 | 1,035 | 1,069 | 1,087 |
| -2,0 | -3,605 | -0,609 | 0,307 | 0,777 | 0,895 | 0,959 | 0,980 | 0,990 |
| -2,2 | -3,705 | -0,574 | 0,330 | 0,752 | 0,844 | 0,888 | 0,900 | 0,905 |
| -2,4 | -3,800 | -0,537 | 0,351 | 0,725 | 0,795 | 0,823 | 0,830 | 0,832 |
| -2,6 | -3,889 | -0,499 | 0,368 | 0,696 | 0,747 | 0,764 | 0,768 | 0,769 |
| -2,8 | -3,973 | -0,460 | 0,384 | 0,666 | 0,702 | 0,712 | 0,714 | 0,714 |
| -3,0 | -4,051 | -0,420 | 0,396 | 0,636 | 0,660 | 0,666 | 0,666 | 0,667 |

**Tabla 4-10: Test de Bondad****

| Coeficiente | Normal | Log-Normal 2 | Gumbel | Pearson III | Log-Pearson III |
| --- | --- | --- | --- | --- | --- |
| R2 | 0.9039 | 0.9753 | 0.9691 | 0.9691 | **0.9761** |
| Chi2 Calculado<br>Chi2 Tabulado<br>Ajuste<br>Criterio | 1.4037<br>7.8147<br>0.1796<br>Aceptado | 9.0364<br>7.8147<br>1.1563<br>Rechazado | 1.4049<br>7.8147<br>0.1798<br>Aceptado | 5.8008<br>5.9915<br>0.9682<br>Aceptado | 1.8895<br>5.9915<br>0.3154<br>Aceptado |
|  |  |  |  |  | **OK** |

**Tabla 4-11: Precipitaciones Máximas Absolutas en 24 horas (mm)****

| T | Chacrilla |
| --- | --- |
| 2 | **47.6** |
| 5 | **71.3** |
| 10 | **86.4** |
| 20 | **100.2** |
| 25 | **104.5** |
| 50 | **117.3** |
| **100 ** | **129.5 ** |
| 150 | **136.5** |
| 200 | **141.3** |
| 250 | **145.0** |
| 500 | **156.2** |
| 1000 | **167.1** |
| 10000 | **200.9** |

**Tabla 5-1: Parámetros morfométricos de cuenca sin proyecto****

| Cuenca | Área | L(ppal) | H(max) | H(min) | H | Hg | Pendiente |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nombre | (Km2) | (Km) | (m) | (m) | (m) | (m) | (m/m) |
| 1 | 0.103 | 0.358 | 727.5 | 516 | 211.5 | 105.8 | 0.59 |
| 2 | 0.027 | 0.265 | 650 | 508 | 142.0 | 71.0 | 0.54 |
| 3 | 0.017 | 0.117 | 637 | 512 | 125.0 | 62.5 | 1.07 |
| 4 | 0.011 | 0.098 | 550 | 512 | 38.0 | 19.0 | 0.39 |

**Tabla 5-2: Tiempo de concentración - Escenario sin proyecto****

| 1 | 0.103 | 0.358 | 727.5 | 516 | 211.5 | 105.8 | 0.59 | 2.21 | 2.21 | *** | 2.21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.027 | 0.265 | 650 | 508 | 142.0 | 71.0 | 0.54 | 1.82 | 1.82 | *** | 1.82 |
| 3 | 0.017 | 0.117 | 637 | 512 | 125.0 | 62.5 | 1.07 | 0.74 | 0.74 | *** | 0.74 |
| 4 | 0.011 | 0.098 | 550 | 512 | 38.0 | 19.0 | 0.39 | 0.96 | 0.96 | *** | 0.96 |
| 5 | 0.005 | 0.025 | 525 | 500 | 25.0 | 12.5 | 1.00 | 0.23 | 0.23 | *** | 0.23 |
| 6 | 0.005 | 0.072 | 525 | 500 | 25.0 | 12.5 | 0.35 | 0.79 | 0.79 | *** | 0.79 |
| 7 | 0.003 | 0.033 | 537 | 520 | 17.0 | 8.5 | 0.52 | 0.37 | 0.37 | *** | 0.37 |
| 8 | 0.010 | 0.092 | 550 | 512 | 38.0 | 19.0 | 0.41 | 0.89 | 0.89 | *** | 0.89 |
| 9 | 0.229 | 0.714 | 750 | 456 | 294.0 | 147.0 | 0.41 | 4.32 | 4.32 | *** | 4.32 |
| 10 | 0.213 | 0.86 | 750 | 477 | 273.0 | 136.5 | 0.32 | 5.51 | 5.51 | *** | 5.51 |
| 11 | 1.863 | 2.3 | 1225 | 477 | 748.0 | 374.0 | 0.33 | 11.65 | 11.65 | *** | 11.65 |
| 12 | 2.541 | 2.536 | 1225 | 462 | 763.0 | 381.5 | 0.30 | 12.94 | 12.94 | *** | 12.94 |
| 13 | 0.018 | 0.248 | 587 | 455 | 132.0 | 66.0 | 0.53 | 1.73 | 1.73 | *** | 1.73 |
| 14 | 0.267 | 0.85 | 806 | 437 | 369.0 | 184.5 | 0.43 | 4.84 | 4.84 | *** | 4.84 |
| 15 | 0.053 | 0.227 | 487 | 437 | 50.0 | 25.0 | 0.22 | 2.28 | 2.27 | *** | 2.27 |
| 16 | 0.008 | 0.09 | 530 | 425 | 105.0 | 52.5 | 1.17 | 0.59 | 0.59 | *** | 0.59 |
| 17 | 0.015 | 0.09 | 530 | 425 | 105.0 | 52.5 | 1.17 | 0.59 | 0.59 | *** | 0.59 |
| 18 | 0.007 | 0.09 | 506 | 412 | 94.0 | 47.0 | 1.04 | 0.61 | 0.61 | *** | 0.61 |
| 19 | 0.040 | 0.255 | 575 | 416 | 159.0 | 79.5 | 0.62 | 1.67 | 1.67 | *** | 1.67 |
| 20 | 0.064 | 0.308 | 633 | 412 | 221.0 | 110.5 | 0.72 | 1.83 | 1.83 | *** | 1.83 |
| 21 | 0.189 | 0.718 | 806 | 416 | 390.0 | 195.0 | 0.54 | 3.90 | 3.90 | *** | 3.90 |
| 22 | 0.077 | 0.496 | 650 | 366 | 284.0 | 142.0 | 0.57 | 2.87 | 2.87 | *** | 2.87 |

**Tabla 5-3: Coeficiente de Duración - Estación Quillota****

| Estación<br>Meteorológica | Duración | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estación<br>Meteorológica | 1 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 18 | 24 |
| Quillota | 0,13 | 0,23 | 0,38 | 0,50 | 0,58 | 0,67 | 0,75 | 0,80 | 0,88 | 1,00 |

**Tabla 5-6: se presenta un rango de valores, de los cuales, conservadoramente, se ha optado**

| Factor | Extremo | Alto | Normal | Bajo |
| --- | --- | --- | --- | --- |
| **Relieve** | **0,28-0,35**<br>Escarpe con<br>pendientes<br>mayores que 30% | **0,20-0,28**<br>Montañoso con<br>pendientes entre 10 y<br>30% | **0,14-0,20**<br>Con cerros y<br>pendientes entre<br>5 y 10% | **0,08-0,14**<br>Relativamente plano<br>con pendientes<br>menores a 5%<br> |
| **Infiltración** | **0,12-0,16**<br>Suelo rocoso, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable | **0,08-0,12**<br>Suelos arcillosos o<br>limosos con baja<br>capacidad de<br>infiltración, mal<br>drenados | **0,06-0,08**<br>Normales, bien<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos | **0,04-0,06**<br>Suelos profundos de<br>arena u otros suelos<br>bien drenados con alta<br>capacidad de<br>infiltración |
| **Cobertura Vegetal** | **0,12-0,16**<br>Cobertura escasa,<br>terreno sin<br>vegetación o<br>escasa cobertura | **0,08-0,12**<br>Poca vegetación,<br>terrenos cultivados o<br>naturales, menos del<br>20% del área con<br>buena cobertura<br>vegetal | **0,06-0,08**<br>Regular a buena,<br>50% del área con<br>praderas o<br>bosques, no más<br>del 50% cultivado | **0,04-0,06**<br>Buena a excelente,<br>90% del área con<br>praderas, bosques o<br>cobertura equivalente. |
| **Almacenamiento**<br>**Superficial** | **0,10-0,12**<br>Despreciable,<br>pocas depresiones<br>superficiales, sin<br>zonas húmedas | **0,08-0,10**<br>Baja, sistema de<br>cauces superficiales<br>pequeños bien<br>definidos, sin zonas<br>húmedas. | **0,06-0,08**<br>Normal, posibilidad<br>de almacenamiento<br>buena, zonas<br>húmedas,<br>pantanos, lagunas<br>y lagos. | **0,04-0,06**<br>Capacidad alta,<br>sistema hidrográfico<br>poco definido, buenas<br>planicies de<br>inundación o gran<br>cantidad de zonas<br>húmedas, lagunas o<br>pantanos. |
| **Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25** | **Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25** | **Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25** | **Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25** | **Si T>10 años, amplificar resultados**<br>**T:25; C*1,10**<br>**T:50; C*1,20**<br>**T=100; C*1,25** |

**Tabla 5-7: Coeficiente de Escorrentía Adoptados****

| Periodo de Retorno | (T en años) | 20 o menor | 25 | 50 | 100 o mayor |
| --- | --- | --- | --- | --- | --- |
| Coeficiente Escorrentía | C | 0,60 | 0,66 | 0,72 | 0,75 |

**Tabla 5-8: Caudales Máximos Instantáneos****

| 1 | 0.103 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.62 | 0.64 | 0.72 | 1.00 | 1.09 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.027 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.16 | 0.17 | 0.19 | 0.26 | 0.29 |
| 3 | 0.017 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.10 | 0.11 | 0.12 | 0.17 | 0.18 |
| 4 | 0.011 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.07 | 0.07 | 0.08 | 0.11 | 0.12 |
| 5 | 0.005 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.03 | 0.03 | 0.03 | 0.05 | 0.05 |
| 6 | 0.005 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.03 | 0.03 | 0.04 | 0.05 | 0.06 |
| 7 | 0.003 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.02 | 0.02 | 0.02 | 0.03 | 0.03 |
| 8 | 0.010 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.06 | 0.06 | 0.07 | 0.10 | 0.10 |
| 9 | 0.229 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 1.37 | 1.43 | 1.60 | 2.21 | 2.41 |
| 10 | 0.213 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 1.28 | 1.33 | 1.50 | 2.06 | 2.25 |
| 11 | 1.863 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 11.18 | 11.64 | 13.07 | 18.05 | 19.68 |
| 12 | 2.541 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 15.24 | 15.88 | 17.83 | 24.61 | 26.84 |
| 13 | 0.018 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.11 | 0.11 | 0.13 | 0.18 | 0.19 |
| 14 | 0.267 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 1.60 | 1.67 | 1.88 | 2.59 | 2.82 |
| 15 | 0.053 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.32 | 0.33 | 0.37 | 0.52 | 0.56 |
| 16 | 0.008 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.05 | 0.05 | 0.06 | 0.08 | 0.08 |
| 17 | 0.015 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.09 | 0.09 | 0.10 | 0.14 | 0.15 |
| 18 | 0.007 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.04 | 0.04 | 0.05 | 0.07 | 0.07 |
| 19 | 0.040 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.24 | 0.25 | 0.28 | 0.39 | 0.43 |
| 20 | 0.064 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.38 | 0.40 | 0.45 | 0.62 | 0.68 |
| 21 | 0.189 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 1.13 | 1.18 | 1.33 | 1.83 | 2.00 |
| 22 | 0.077 | 10 | 0.60 | 0.66 | 0.75 | 36.00 | 37.50 | 42.10 | 46.50 | 50.70 | 0.46 | 0.48 | 0.54 | 0.74 | 0.81 |
