---
title: Sin título
author: Eduardo Santibanez
date: D:20171107123553-03'00'
language: es
type: report
pages: 37
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - APÉNDICE 1
  - APÉNDICE 2
  - APÉNDICE 3
  - APÉNDICE 4
-->

#### ANEXO D ESTUDIO DE INUNDACIONES ADENDA I DECLARACIÓN DE IMPACTO AMBIENTAL ROMERAL

#### “ESTUDIO DE INUNDACIÓN EN LOTEO HIJUELA CHACRA EL RETIRO, DE LA COMUNA DE ROMERAL”, REGIÓN DEL MAULE

Preparado por:

_A_ luvial Consultoría en Recursos Hídricos

Agosto 2017

Rev.D

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

## Índice

##### 1.INTRODUCCIÓN ______________________________________________ 2 2.ANTECEDENTES _____________________________________________ 2 3.ESTUDIOS BÁSICOS __________________________________________ 3

3.1 L EVANTAMIENTO TOPOGRÁFICO _____________________________________________________ 3
3.2 E STUDIO H IDROLÓGICO ____________________________________________________________ 5
3.3 E STUDIO H IDRÁULICO _____________________________________________________________ 6
_3.3.1_ _Cálculo del Eje Hidráulico ____________________________________________________ 6_
_3.3.2_ _Descripción del programa HEC-RAS ____________________________________________ 6_
_3.3.3_ _Modelación ________________________________________________________________ 7_
_a)_ _Régimen de Escurrimiento y Condiciones de Borde del Flujo ____________________________ 7_
_b)_ _Coeficientes de Rugosidad _______________________________________________________ 8_
_c)_ _Antecedentes para la modelación __________________________________________________ 9_

##### 4.RESULTADOS ________________________________________________ 9

4.1 E JES H IDRÁULICOS _______________________________________________________________ 9
4.2 A NÁLISIS DE REVANCHA __________________________________________________________ 15
##### 5.IDEAS DE SOLUCIÓN _________________________________________ 16 6.CONCLUSIONES _____________________________________________ 16

APÉNDICES

Apéndice 1 : Resumen Plan Maestro Aguas Lluvias Curicó revisado.

Apéndice 2 : Fotografías cauce.

Apéndice 3 : Resultados eje Hidráulico T = 50, 25 años.

Apéndice 4 : Tabla revancha - desborde.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

1

### 1. INTRODUCCIÓN

Como producto de la evaluación ambiental a la que fue sometida el proyecto "EL

ROMERAL", en febrero de 2017, los servicios con competencia ambiental se han

pronunciado con observaciones en el proceso. La Consultora Ambiental Andalúe S.A ha

contactado a la consultora Aluvial para que ésta desarrolle los trabajos y labores

requeridas para dar cumplimiento a las exigencias de la DOH específicamente en el tema

relacionado con el estudio de inundabilidad del estero Guaiquillo, puesto que éste se

desarrolla muy cercano al proyecto “El Romeral” ubicado en Loteo Hijuela Chacra El

Retiro, de la comuna de Romeral, en la Región del Maule. La observación que debe ser

atendida, se encuentra contenida en el documento ICSARA, y que en específico es la

siguiente:

“Se solicita un estudio de inundaciones, dada la cercanía del loteo al Estero Guaiquillo, el

cual deberá basarse en los antecedentes que se muestran en el "Plan Maestro de

Evacuación y Drenaje de Aguas Lluvias de Curicó".

En el presente informe se presentan los trabajos desarrollados para determinar la zona de

inundación del estero Guaiquillo en el tramo frente al proyecto “El Romeral”.

### 2. ANTECEDENTES

Se revisaron los antecedentes contenidos en el Plan Maestro de Evacuación y Drenaje

Aguas lluvias de Curicó - Dirección de Obras Hidráulicas - MOP, obteniendo información

relativa a caudales de diseño y su respectivo periodo de retorno (T). Un resumen de los

antecedentes que aporta el mencionado estudio de la DOH y que permitieron obtener

algunos antecedentes requeridos para el análisis de inundación se presenta en el

Apéndice 1.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

2

### 3. ESTUDIOS BÁSICOS

##### 3.1 L EVANTAMIENTO TOPOGRÁFICO

Entre los días 07 y 10 de julio se realizó un levantamiento topobatimétrico de
aproximadamente 1255 m del estero Guaiquillo en el sector del proyecto “El Romeral”
(Latitud 34°59'0,70"S; Longitud 71°12'28,17"O). Este levantamiento consistió en la toma
de puntos de densidad suficiente que permitieran representar las condiciones del cauce y
obtener coordenadas con una precisión relativa horizontal de 1/166.000 Norte y 1/
142.000 Este, y una precisión altimétrica respecto al elipsoide del sistema geodésico
mundial WGS-84, del orden de ± (0,010 [m] + 3 a 4 [ppm]).

Así, se obtuvieron perfiles transversales cada 20 m, abarcando 100 metros hacia la ribera

izquierda y 100 metros hacia la derecha desde el eje principal del rio. Esto permitió

representar de manera adecuada la caja del cauce y sus planicies de inundación, frente al

terreno en análisis. El plano de planta con la ubicación de los perfiles se presenta en la

Figura 3.1.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

3

Figura 3.1. Ubicación perfiles transversales obtenidos en levantamiento topobatimétrico.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

4

Para verificar el comportamiento hidráulico en el terreno del proyecto, a solicitud del
mandante, se complementaron los perfiles transversales desde el kilometraje 480 hasta el
kilometraje 680 obtenidos por Aluvial, con la información contenida en el plano "Predio
con perfiles transversales hacia el rio (1)" proporcionada por el mandante, que cuenta con

curvas de nivel cada 0.5 metros

Dado que la topografía proporcionada por el mandante se encuentra en un sistema de
coordenadas con referencia altimétrica y sistema de coordenada desconocida fue
necesario realizar un calce de elementos singulares identificados en ambos planos (plano
Aluvial y plano mandante).

Con lo anterior, se determinó una diferencia de cota de 143 metros, entre uno y otro
sistema (estando las cotas de Aluvial 143 metros sobre las del plano "Predio con perfiles
transversales hacia el rio (1)", por lo que estas últimas fueron "levantadas" en ese valor. Al
realizar dicho paso, se aprecia coherencia entre ambos levantamientos, lo que es
apreciable en la continuidad de los perfiles que fueron extendidos. De todos modos, para
una mayor rigurosidad, Aluvial recomienda que ambas topografías estén referidas al

mismo sistema.

##### 3.2 E STUDIO H IDROLÓGICO

El presente estudio no consideró el desarrollo de una hidrología de la zona, puesto que la

autoridad competente solicita expresamente basarse en los antecedentes que se

muestran en el "Plan Maestro de Evacuación y Drenaje de Aguas Lluvias de Curicó”. La

información de caudales utilizada para el desarrollo del presente informe se obtuvo así del

Plan Maestro de Evacuación y Drenaje de Aguas Lluvias de Curicó, en el cual se entrega un

análisis de precipitaciones, un estudio de suelos y estimación de caudales en cauces

naturales para distintos periodos de retorno. En particular se indica que para el estero

Guaiquillo no existe control fluviométrico, por lo que los caudales fueron estimados

mediante tres métodos: el método regional propuesto en el “Manual de Cálculo de

Crecidas y Caudales Mínimos en Cuencas sin Información Fluviométrica”, DGA-AC, 1995; el

método racional modificado; y el método de transposición de crecidas. Los caudales

finalmente adoptados y su respectivo periodo de retorno (T) se presentan en la tabla 3.2.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

5

Tabla 3.2. Caudales estimados para estero Guaiquillo. Fuente: Plan Maestro de Aguas

Lluvias Curicó- MOP

|T [años]|Caudal [m3/s]|
|---|---|
|2|170|
|5|260|
|10|310|
|20|380|
|25|410|
|50|490|
|100|580|

Luego de una revisión de la metodología, criterios y análisis desarrollados en el Plan

Maestro, se ha considerado correcto adoptar los caudales indicados por la DOH.

##### 3.3 E STUDIO H IDRÁULICO

El estudio de inundación presentado en los capítulos siguientes se realizó para los

caudales de periodo de retorno 25, 50 y 100 años entregados para el estero Guaiquillo en

el Plan Maestro de Aguas Lluvias de Curicó.

3.3.1 Cálculo del Eje Hidráulico

El cálculo del eje hidráulico se realizó mediante la aplicación del software HEC-RAS (U.S.

Army Corps of Engineers River Analysis System), en su versión 5.0.3 de septiembre de

2016, desarrollado por el Hidrologic Engineering Center, este software de amplio uso en la

determinación de análisis hidráulicos entrega resultados confiables para este tipo de

estudios.

A continuación, se describen sus principales características y las condiciones de borde

incorporadas en la modelación.

3.3.2 Descripción del programa HEC-RAS

Este sistema de análisis resuelve el cálculo del eje hidráulico utilizando un modelo

numérico de flujo unidimensional para estimar las alturas de aguas, velocidades y demás

parámetros hidráulicos de interés, en las diferentes secciones transversales que deben ser

ingresadas por el usuario. Además, entre otras aplicaciones, HEC-RAS permite el cálculo

del eje hidráulico considerando la interferencia de puentes, alcantarillas y vertederos,

entre otras obras de arte emplazadas en el cauce.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

6

Como primer punto, HEC-RAS requiere la información topográfica del canal o cauce

natural, dada por una serie de perfiles transversales (distancia acumulada y cota) y las

distancias entre perfiles consecutivos. Junto con ello y para completar el archivo de datos

geométricos que HEC-RAS solicita, se debe determinar la sección principal del cauce y las

planicies de inundación contiguas, acompañadas de sus respectivos coeficientes de

rugosidad.

Por otra parte, HEC-RAS requiere de un archivo de datos donde se especifiquen las

condiciones de escurrimiento del flujo. En este archivo se deben ingresar los caudales de

crecidas para cada período de retorno considerado, dado que HEC-RAS tiene la facilidad

de ejecutar el modelo para diferentes caudales de manera simultánea; adicionalmente, se

tiene la opción de ir modificando dichos caudales, perfil a perfil, a lo largo del canal. Para

completar este archivo de datos, el programa requiere de una(s) condición(es) de borde

para la resolución del modelo; entre las alternativas que se tienen está imponer una altura

conocida, altura normal o altura crítica aguas arriba o aguas abajo del canal. Esta

condición se debe imponer en el primer perfil transversal de aguas abajo si el régimen de

escurrimiento es subcrítico, o en el primer perfil de aguas arriba si este es supercrítico. En

tanto que, si el régimen de escurrimiento es mixto, entonces, se debe ingresar una

condición de borde en ambos extremos.

El programa entrega como resultado para cada perfil transversal, los principales

parámetros que definen el escurrimiento, tales como: nivel del eje hidráulico, caudales y

velocidades por subsección, ancho superficial, nivel de energía, altura crítica, número de

Froude, etc.

3.3.3 Modelación

Con el objeto de asignar un kilometraje a cada perfil transversal tomado en el cauce, se

determinó la ubicación del eje longitudinal de éste. Luego, se asignó un kilometraje

comenzando desde aguas abajo hacia aguas arriba, donde el Km. 0,000 corresponde al

primer perfil considerado aguas abajo. El último perfil de aguas arriba finaliza en el perfil

transversal km 1,255 (perfil 64).

En los planos de planta del cauce (Figura 3.1), se muestra la ubicación de estos perfiles

transversales.

a) Régimen de Escurrimiento y Condiciones de Borde del Flujo

En el tramo analizado para los caudales considerados el régimen de escurrimiento es

subcrítico. En la zona de estudio, no existen obras de arte que obstaculicen el paso del

agua, en donde se pudiera producir un cambio en el régimen de escurrimiento. Por lo

indicado, la modelación se realizó considerando un escurrimiento en el cauce en régimen

subcrítico, considerando altura normal aguas abajo. La información considerada para el fin

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

7

de imponer dicha altura normal, corresponde a la pendiente media obtenida de la

tendencia establecida en los últimos 10 perfiles de aguas abajo. Así, se adoptó una
pendiente media de 0.00338 [m/m].

b) Coeficientes de Rugosidad

De acuerdo con los antecedentes recopilados en los estudios desarrollados por la DOH, y a

las fotografías del cauce tomadas en terreno (apéndice 2), se estimaron coeficientes de

rugosidad para el canal natural por medio del procedimiento de Cowan (1956). De

acuerdo a éste, el valor del número de Manning “n” se obtiene como:

( )

donde:

: Valor de n para un canal recto, uniforme, suave en materiales naturales. Valor base de

n para el suelo descubierto natural de las planicies.

: Factor de corrección por efecto de irregularidades en la superficie.

: Valor para variaciones en forma y tamaño de la sección transversal (0 para planicies).

: Valor para las obstrucciones.

Valor para la vegetación y condiciones de flujo.

: Factor de corrección por meandros del cauce (1 para planicies).

Distintos autores han estudiado los valores y rangos de estos factores [Chow, 1959;

Benson y Dalrymple, 1967; Barnes, 1967; Aldridge and Garrett, 1973; Ree and Crow,

1977]. En el presente estudio, teniendo en cuenta las fotografías del estero (apéndice 2)

en el tramo en estudio, se determinó el valor de “n” de acuerdo a los valores de los

factores entregados por Aldridge and Garrett, 1973, obteniéndose un valor representativo
para las secciones de 0.1 [s/m [1/3] ], algo mayor a lo estimado en el Plan Maestro (Tabla 3.3).

Tabla 3.3. Manning obtenido mediante Cowan (1965)

|Valor de n|Col2|
|---|---|
|nb|0.035|
|n1|0.02|
|n2|0.005|
|n3|0.015|
|n4|0.025|
|m|1|
|**n **|**0.1**|

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

8

c) Antecedentes para la modelación

El tramo total en estudio tiene una longitud aproximada de 1255 m y para la modelación

del canal se utilizó un total de 64 perfiles transversales, con un ancho promedio de 200 m,

y separados 20 m entre sí. Como se señaló con anterioridad, para el tramo contenido

entre los perfiles 680 y 480 se extendieron los perfiles. Esta configuración permite una

precisa modelación del eje hidráulico del cauce, y asegura la correcta convergencia de los

resultados.

La numeración de estos perfiles se realizó desde aguas abajo hacia aguas arriba, tal como

lo establece el programa HEC-Ras, bajo el concepto de que el perfil ubicado más aguas

arriba es el perfil con mayor numeración. Así, la numeración adoptada equivale al

kilometraje longitudinal del eje del río conforme al levantamiento realizado por Aluvial,

por lo que el perfil de más aguas abajo corresponde al perfil 0, y el de más aguas arriba al

perfil 1,255.

La ubicación de los perfiles se muestra en los planos del levantamiento topográfico

realizado con motivo del presente estudio (Figura 3.1).

### 4. RESULTADOS

##### 4.1 E JES H IDRÁULICOS

Los ejes hidráulicos para los caudales asociados a los periodos de 25, 50 y 100 años se

presentan en las figuras siguientes. En los resultados presentados y considerando la

nomenclatura típica de la hidráulica los perfiles son siempre mirados hacia aguas abajo,

con lo cual la ribera derecha corresponde a la que enfrenta el proyecto “El Romeral”.

Estero Guaiquillo

252

250

248

246

244

242

240

238

236

234

232

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Legend|
|---|---|---|---|---|---|---|---|
||||||||EG 25 años<br>WS 25 años<br>Ground<br>LOB<br>ROB|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

0 200 400 600 800 1000 1200 1400

Distancia Cauce Principal (m)

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

9

Figura 4.1. Eje hidráulico T = 25 años. WS: Superficie de agua, E.G: Línea de energía LOB:

Elevación ribera izquierda, ROB: Elevación ribera derecha.

Estero Guaiquillo

252

250

248

246

244

242

240

238

236

234

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Legend<br>EG 50 años<br>WS 50 años<br>Ground<br>LOB<br>ROB|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||

232
0 200 400 600 800 1000 1200 1400

Distancia Cauce Principal (m)

Figura 4.2 Eje hidráulico T = 50 años. WS: Superficie de agua, E.G: Línea de energía LOB:

Elevación ribera izquierda, ROB: Elevación ribera derecha.

Estero Guaiquillo

252

250

248

246

244

242

240

238

236

234

232

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Legend|
|---|---|---|---|---|---|---|---|
||||||||EG 100 años<br>WS 100 años<br>Ground<br>LOB<br>ROB|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

0 200 400 600 800 1000 1200 1400

Distancia Cauce Principal (m)

Figura 4.3 Eje hidráulico T = 100 años. WS: Superficie de agua, E.G: Línea de energía LOB:

Elevación ribera izquierda, ROB: Elevación ribera derecha.

Al analizar el comportamiento hidráulico desde el punto de vista de las alturas de

escurrimiento, se verifica que para todos los periodos de retorno existen secciones con

desborde, siendo las secciones más restrictivas las desarrolladas entre los perfiles 320 y

360 hacia la ribera derecha. En la medida que aumenta el periodo de retorno en análisis

se van incorporando secciones que presentan desborde. Así, al analizar los resultados se

observa un aumento en la extensión de los tramos con desborde a medida que aumenta

el periodo de retorno. Estos se muestran en la tabla 4.1.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

10

Tabla 4.1. Desbordes (ribera izquierda - derecha) para los distintos periodos de retorno

simulados.

|Simulación|Tramo Desborde (perfil)|Col3|Longitud total [m]|Col5|
|---|---|---|---|---|
|**Simulación**|**Izquierda**|**Derecha**|**Izquierda**|**Derecha**|
|T = 25 años<br>(Q = 410 m3/s)|<br>-|320-340|-|20|
|T = 50 años<br>(Q = 490 m3/s)|-|280-420|-|140|
|T= 100 años<br>(Q = 580 m3/s)|-|0-80, 180-420|-|320|

A continuación, se presentan los resultados del análisis hidráulico para el caudal asociado

a un periodo de retorno de 100 años. Los resultados para los periodos de retorno de 25 y

50 años se presentan en el apéndice 3.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

11

Tabla 4.2. Eje Hidráulico T=100 años.

|Perfil|Q Total [m3/s]|LOB Elev [m]|ROB Elev [m]|Min Ch El [m]|W.S. Elev [m]|Vel Chnl [m]|Froude # Chl|
|---|---|---|---|---|---|---|---|
|1255.57|580|246.86|250.03|240.51|246|1.81|0.3|
|1240|580|246.84|249.82|240.57|245.9|1.85|0.31|
|1220|580|246.47|249.38|240.48|245.73|1.98|0.35|
|1200|580|246.29|249.24|240.36|245.67|1.59|0.25|
|1180|580|246.34|249.01|239.68|245.62|1.38|0.22|
|1160|580|246.05|248.92|239.92|245.53|1.47|0.26|
|1140|580|245.98|249.31|239.96|245.44|1.44|0.26|
|1120|580|246.05|248.07|239.67|245.39|1.28|0.21|
|1100|580|246.10|248.02|239.48|245.33|1.3|0.21|
|1080|580|246.15|247.73|239.66|245.29|1.21|0.18|
|1060|580|246.27|247.67|239.39|245.25|1.23|0.19|
|1040|580|245.43|247.73|239.27|245.2|1.21|0.21|
|1020|580|245.35|248.12|238.65|245.14|1.23|0.22|
|1000|580|245.17|247.54|238.55|245.06|1.25|0.23|
|980|580|245.30|247.14|238.2|244.98|1.3|0.24|
|960|580|245.22|247.29|237.51|244.87|1.38|0.27|
|940|580|245.10|247.06|237.18|244.74|1.48|0.29|
|920|580|244.82|246.92|237.22|244.62|1.49|0.29|
|900|580|244.51|246.95|237.61|244.47|1.56|0.32|
|880|580|244.44|246.62|237.72|244.27|1.71|0.35|
|860|580|244.45|246.31|237.56|244.08|1.78|0.35|
|840|580|244.41|246.11|237.38|243.93|1.68|0.32|
|820|580|244.27|246.07|237.73|243.78|1.65|0.33|
|800|580|244.26|246.03|237.99|243.64|1.65|0.31|
|780|580|244.37|245.99|237.88|243.51|1.6|0.29|
|760|580|244.02|246.06|237.97|243.39|1.55|0.31|
|740|580|243.92|246.09|237.71|243.29|1.46|0.26|
|720|580|244.00|245.17|237.74|243.21|1.38|0.25|
|700|580|243.95|244.87|237.55|243.14|1.27|0.23|
|680|580|243.77|244.83|237.57|243.08|1.19|0.22|
|660|580|243.69|244.65|237.68|243.01|1.23|0.22|
|640|580|243.72|244.74|237.22|242.93|1.29|0.23|
|620|580|243.45|244.31|236.89|242.83|1.39|0.26|
|600|580|243.27|244.34|236.67|242.76|1.22|0.22|
|580|580|243.21|243.51|237.02|242.68|1.26|0.25|
|560|580|243.37|243.52|237.1|242.56|1.37|0.28|
|540|580|243.31|243.54|236.66|242.48|1.29|0.23|
|520|580|243.30|243.59|236.74|242.44|1.17|0.2|
|500|580|242.96|243.49|236.16|242.4|1.06|0.17|
|480|580|242.76|243.41|235.79|242.37|1.01|0.17|
|460|580|242.72|242.55|235.59|242.29|1.19|0.22|
|440|580|242.69|242.41|235.12|242.23|1.14|0.2|
|420|580|243.17|241.54|235.02|242.17|1.18|0.21|
|400|580|243.50|241.42|234.92|242.1|1.24|0.22|
|380|580|243.31|241.50|234.75|242|1.4|0.25|
|360|580|243.24|241.13|234.79|241.9|1.46|0.26|
|340|580|242.76|240.38|234.7|241.83|1.37|0.23|
|320|580|242.68|240.45|234.93|241.75|1.47|0.24|
|300|580|242.84|240.87|235.07|241.69|1.32|0.23|
|280|580|242.65|240.84|235.35|241.6|1.39|0.25|
|260|580|242.22|241.37|234.4|241.48|1.52|0.28|
|240|580|242.47|240.85|234.78|241.36|1.56|0.29|
|220|580|242.45|241.10|235.07|241.24|1.55|0.29|
|200|580|242.42|240.66|234.97|241.1|1.59|0.31|
|180|580|243.04|240.94|234.67|240.96|1.58|0.31|
|160|580|245.64|241.01|234.49|240.87|1.45|0.25|
|140|580|245.90|241.17|234.16|240.79|1.41|0.24|
|120|580|245.60|241.09|234.01|240.72|1.43|0.24|
|100|580|245.15|240.66|233.87|240.66|1.35|0.22|
|80|580|245.02|240.23|234.16|240.61|1.25|0.21|
|60|580|244.71|240.02|234.2|240.57|1.17|0.18|
|40|580|244.39|240.27|234.47|240.5|1.35|0.22|
|20|580|243.98|240.32|234.23|240.42|1.42|0.23|
|0|580|243.90|240.29|234.31|240.37|1.28|0.22|

Dónde: Perfil: Denominación del perfil, Q Total: caudal, LOB Elev: elevación ribera

izquierda, ROB Elev: elevación ribera derecha, Min Ch El: Elevación mínima del cauce (cota
fondo), W.S Elev: Elevación del eje Hidráulico, Vel Chnl: Velocidad del canal (m/s), Froude

Chl: Número de Froude.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

12

La figura 4.4 muestra la zona inundada y los tramos con desborde para el caudal asociado

al periodo de retorno de 100 años.

A pesar de que las características topográficas del terreno del proyecto presentan una

cota inferior a la del eje hidráulico, la altura del pretil conformado en el lado derecho

contiene la crecida. Por ello, no se presenta desborde en los perfiles que enfrentan la zona

del proyecto.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

13

Figura 4.4. Zona de inundación y desbordes para caudal asociado a periodo de retorno T = 100 años.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

14

##### 4.2 A NÁLISIS DE REVANCHA

En cada simulación se identifican las zonas en las cuales la revancha no cumple con el

criterio de 1 m libre sobre la cota de agua. Los resultados se presentan en la tabla 4.3.

Tabla 4.3. Insuficiencia en la revancha para los distintos periodos de retorno simulados.

|Simulación|Tramo No cumple revancha (perfil)|Col3|Longitud total No cumple<br>revancha [m]|Col5|
|---|---|---|---|---|
|**Simulación**|**Izquierda**|**Derecha**|**Izquierda**|**Derecha**|
|T = 25 años<br>(Q = 410 m3/s)|<br>-|60-80, 200-300,<br>360-440|-|200|
|T = 50 años<br>(Q = 490 m3/s)|440-500, 580-<br>600, 860-920,<br>1000-1040|0-100, 160-260,<br>440-460|180|220|
|T= 100 años<br>(Q = 580 m3/s)|260, 320-340,<br>420-1040, 1080-<br>1255|100-160, 440-<br>460, 560-580|835|100|

Nota: En la tabla anterior solo se han considerado los tramos que no cumplen con la

revancha mínima de 1 metro, sin considerar los tramos con desborde identificados en la

tabla 4.1 presentada anteriormente.

El detalle de los tramos con desborde e insuficiencia en la revancha se presentan en el

apéndice 4.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

15

### 5. IDEAS DE SOLUCIÓN

Como se ha señalado en el capítulo anterior existen tramos con desborde e insuficiencia

de revancha, para dar solución a esto existen distintos tipos de solución ampliamente

utilizadas en la hidráulica fluvial, desde la mantención y eliminación de la vegetación del

cauce hasta la construcción de defensas fluviales.

En el caso en particular del tramo que enfrenta al Proyecto “El Romeral”, donde no se

observan sectores de desbordes, se estima conveniente la incorporación de u pretil

consolidado, resistente a la erosión, entre el perfil 820 y el 400, con una altura tal que

mantenga las cotas existente del pretil del terreno, o aquellas que permitan tener una

revancha de mínimo 1 m.

### 6. CONCLUSIONES

Se verifica que para los tres periodos de retorno en análisis las velocidades máximas son
del orden de 2 m/s, mientras que las mínimas son de aproximadamente 1 m/s. Así de

acuerdo a las alturas de escurrimiento obtenidas, se tienen valores de Froude menores a

1, lo cual indica que el escurrimiento se desarrolla en un régimen subcrítico.

Para todos los periodos de retorno se obtiene desbordes por la ribera derecha con una

longitud máxima de 320 m para el periodo de retorno 100 años. Los tramos con desborde

se comienzan a presentar a 160 m aguas abajo del proyecto “El Romeral”, donde el estero

Guaiquillo presenta una curva que se aleja del proyecto, por tanto, si bien estos desbordes

se producen no lo afectarían.

No obstante lo anterior, dado que las características topográficas del terreno del Proyecto

lo sitúan a una cota inferior a la del eje hidráulico, se sugiere verificar la conformación,

capacidad de soporte y resistencia del material del pretil que enfrenta al Proyecto, puesto

que si bien éste, por las crecidas simuladas no se ve superado, podría existir erosión por

insuficiencia en su compactación o consolidación como defensa.

De acuerdo a lo antes señalado, al análisis hidráulico realizado, y debido a que a lo largo
del tramo que enfrenta al proyecto se presentan perfiles en los que la revancha es menor
a 1 m, para asegurar el tránsito de la crecida de 100 años de periodo de retorno con un
mayor factor de seguridad y sin desbordes, se estima conveniente consolidar el pretil
existente de manera que permita tener una revancha de mínimo 1 m para el tramo
comprendido entre el perfil 600 y 400, salvo que el mandante estime conveniente
extender esta medida hacia aguas arriba a lo largo de todo el predio (abarcando desde el
perfil 820 a 400).

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

16

# APÉNDICE 1

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

17

**Revisión Plan Maestro de Aguas lluvias Curicó - Dirección de Obras**
**Hidráulicas - MOP**

Revisados los antecedentes del plan maestro a continuación se resume los antecedentes

relacionados con la estimación de caudales para el estero Guaiquillo y la determinación de

parámetros hidráulicos.

**A-** **Caudales sin Control Fluviométrico**

Se presentan los resultados del análisis de crecidas efectuado en cauces naturales sin

control fluviométrico. Para estimar los caudales en estos cauces se aplicaron tres

métodos, de amplio uso y aceptación en el medio: el método regional propuesto en el

“Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Información

Fluviométrica”, DGA-AC, 1995; el método racional modificado; y el método de

transposición de crecidas.

A continuación se presenta el cálculo de los parámetros morfométricos necesarios, tal

como el coeficiente de escorrentía y el tiempo de concentración de cada cuenca

aportante, una breve descripción de cada uno de los métodos elegidos y, finalmente, los

caudales estimados, asociados a períodos de retorno de 2, 5, 10, 20, 25, 50 y 100 años.

**a)** **Parámetros Morfométricos**

Los parámetros morfométricos de interés, para cada cuenca aportante a las secciones de

interés son la pendiente media de la cuenca, o índice de Mociornita, el tiempo de

concentración y el coeficiente de escorrentía ponderado.

La pendiente media o índice de Mociornita de la cuenca se estimó según la siguiente

expresión, extraída del Manual de Crecidas (1995).

 _h_  _lo_ ln 
### S     [li]   100
_A_  2 2 

_S_ : pendiente media de la cuenca (%)

_li_ : longitud de curva de nivel i (m)

_A_ : área aportante de la cuenca (m [2] )

###### N : no total de curvas de nivel consideradas  h : desnivel entre curvas de nivel adyacentes (m)

El tiempo de concentración de cada cuenca aportante se estimó en base a

las ecuaciones del California Highways and Public Works (CHPW) y del Soil Conservation

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

18

Service (SCS), de los EE.UU., las que se presentan a continuación, y al criterio y

experiencia de este Consultor.

CHPW :

 _L_ 3
_tc_  57



_H_

 _L_ 3 ,0385

57

 
 _H_ 

 _L_ 3 

 
 _H_ 

_tc_ : tiempo de concentración (min)

_L_ : longitud del cauce principal (km)

###### H : desnivel máximo de la cuenca (m)

,07

8,0

_L_
_tc_ ,01362 

,05

SCS :

,01362  _SL_ 8,0,05  1000 _CN_  9 

_tc_ : tiempo de concentración (min)

_L_ : longitud cauce principal (km)

###### CN : no de curva de la cuenca (SCS)

_S_ : Pendiente media de la cuenca (%)

Para el cálculo del tiempo de concentración, según esta última ecuación se

adoptó un valor de número de curva CN = 86, recomendado para la zona por el manual.

En la Tabla 1 se presentan los parámetros morfométricos de cada cuenca,

que se usarán en los métodos de estimación de crecidas.

Tabla 1. Parámetros Morfométricos de las Cuencas Aportantes

|Estero|A<br>(km2)|L<br>(m)|S<br>(%)|H<br>(M)|Tc (min)|Col7|Col8|Coeficiente<br>Escorrentía|
|---|---|---|---|---|---|---|---|---|
|Estero|A <br>(km2)|L <br>(m)|S <br>(%)|H <br>(M)|CHPW|SCS|Adoptado|Adoptado|
|Guaiquillo<br>Chequenlemo|334,77<br>191,49|48.849<br>36.572|33<br>18|1.725<br>1.100|289<br>246|263<br>282|270<br>270|0,33<br>0,35|

Puede observarse que el tiempo de concentración es similar en ambas

cuencas, de 270 minutos (4,5 horas); a su vez el coeficiente de escorrentía es levemente

mayor en la cuenca del estero Chequenlemo que en la del estero Guaiquillo.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

19

**b)** **Método Regional**

Este método precisa del cálculo del caudal máximo asociado a un período de retorno de

10 años, el que se estimó según la siguiente ecuación, válida en la zona de estudio,

recomendado por el manual.

#### Q 10  2  10  3  A p,0973   P 2410 horasaños ,1224

_Q_ 10 : caudal medio diario máximo para T = 10 años (m [3] /s)

_A_ _p_ : área aportante (km [2] )

10 _años_
_P_ 24 _horas_ : precipitación diaria para T = 10 años, sobre la cuenca; de acuerdo al plano

de isoyetas se estimaron 140 mm para el estero Guaiquillo y 122 mm para el estero

Chequenlemo, correspondientes a las isoyetas medias de cada cuenca aportante.

Posteriormente, se estimó el caudal asociado a cada período de retorno,

según las relaciones que se presentan en la Tabla 2, las que fueron estimadas en base al

manual mencionado.

Tabla 2. Relación Q T /Q para el Area de Estudio (Zona homogénea Q p )

|Período de Retorno<br>(años)|2|5|10|20|25|50|100<br>1,62|
|---|---|---|---|---|---|---|---|
|Relación QT/Q|0,50|0,80|1,00|1,19|1,25|1,43|1,43|

Finalmente los caudales estimados se afectaron por un factor de conversión

de caudal medio diario máximo a caudal máximo instantáneo  = 1,51.

En la Tabla 3 se presentan los caudales de crecida estimados según el

método regional.

Tabla 3. Caudales de Crecida Estimados según el Método Regional, en m [3] /s

|T<br>(años)|Estero Guaiquillo|Estero Chequenlemo|
|---|---|---|
|2 <br>5 <br>10<br>20<br>25<br>50<br>100|182<br>293<br>365<br>436<br>457<br>523<br>592|90<br>144<br>180<br>214<br>224<br>257<br>291|

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

20

**c)** **Método Racional Modificado**

El método racional modificado precisa del conocimiento del área, el coeficiente de

escorrentía de la cuenca aportante, y de una lluvia de diseño para cada período de retorno

de interés, en este caso 2, 5, 10, 20, 25, 50 y 100 años.

Para cada cuenca aportante se adoptaron los parámetros calculados anteriormente. En

cuanto a la lluvia de diseño, se determinó la intensidad media de cada una de ellas, para

distintos períodos de retorno, en base a la isoyeta media y aplicando las relaciones

correspondientes, con los coeficientes de duración y frecuencia propuestos en el presente

estudio.

En la Tabla 4 se presentan estos valores de intensidad de precipitación, para cada cuenca

aportante y período de retorno de interés.

Tabla 4. Intensidades Medias estimadas en cada cuenca aportante, en mm/h.

|T<br>(años)|CF|Estero Guaiquillo<br>(P24 = 140 mm)<br>10|Estero Chequenlemo<br>P24<br>( 10 = 122 mm)|
|---|---|---|---|
|2 <br>5 <br>10<br>20<br>25<br>50<br>100|0,64<br>0,83<br>1,00<br>1,23<br>1,30<br>1,58<br>1,93|6,8<br>8,8<br>10,6<br>13,0<br>13,8<br>16,8<br>20,5|5,9<br>7,8<br>9,2<br>11,4<br>12,0<br>14,6<br>17,8|

- se adoptó el coeficiente de duración CD = 0,31, correspondiente a una duración de 4,5

hrs.

Posteriormente, se definieron lluvias de diseño en base a los hietogramas

determinados en este estudio (tipos I, II y III).

Para la aplicación del método se utilizó el modelo Caice SWMM, adoptando

como datos de entrada el área aportante de cada cuenca, su coeficiente de escorrentía

ponderado, y cada una de las lluvias de diseño definidas, dado que no se sabe

preliminarmente con cuál se obtendrían mayores caudales.

En la Tabla 5 se presentan los resultados obtenidos con este método, en

cada estero, y para distintos períodos de retorno.

Tabla 5. Caudales de Crecida, obtenidos con el Método Racional Modificado, en m [3] /s

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

21

|T<br>(años)|Estero Guaiquillo|Estero Chequenlemo|
|---|---|---|
|2 <br>5 <br>10<br>20<br>25<br>50<br>100|199<br>257<br>309<br>379<br>403<br>490<br>598|105<br>138<br>163<br>202<br>213<br>259<br>315|

**d)** **Método de Transposición de Crecidas**

Dado que se dispone de una estimación adecuada de crecidas en cuencas adyacentes, es

decir, en aquellas que poseen control fluviométrico, resulta apropiada la aplicación del

método de transposición de crecidas para estimar caudales asociados a distintos períodos

de retorno en los esteros Guaiquillo y Chequenlemo.

Este método se basa en considerar constante el rendimiento específico por

unidad de área y precipitación, en cuencas similares, de manera tal que en dos cuencas se

cumple la siguiente relación:

_Q_ 1 _Q_


_A_ _P_ _A_

_Q_ 1


1

2

1 1

_A_ _P_

2 2

En donde A i, Q i y P i corresponden al área aportante, al caudal y a la precipitación media en

cada una de las cuencas.

En la Tabla 6 se presentan los valores de área y precipitación media de cada

cuenca. Esta última correspondió a la precipitación media anual, y se estimó en base a las

figuras y tablas del Balance Hídrico de Chile, DGA, 1996.

Tabla 6. Areas Aportantes y Precipitaciones Medias de Cauces en el Area de Estudio

|Cauce|Control<br>Fluviométrico|Area<br>(Km2)|P media<br>p<br>(mm/año)|
|---|---|---|---|
|Río Teno después de Junta con Claro<br>Río Claro en Los Queñes<br>Estero Upeo en Upeo<br>Estero Guaiquillo<br>Estero Chequenlemo|si<br>si<br>si<br>no<br>no|1188<br>350<br>450<br>335<br>191|2100<br>2200<br>1500<br>1200<br>1200|

Dado que presenta características distintas al resto, no se tendrá en cuenta,

en este método, la cuenca aportante del río Teno después de Junta con Claro.

Para determinar los caudales de crecida en los esteros Guaiquillo y

Chequenlemo se aplicó el método con cada una de las otras cuencas, río Claro en Los

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

22

Queñes y Upeo en Upeo, adoptándose como valor final el promedio obtenido en cada

ocasión.

En la Tabla 7 se presentan los resultados obtenidos.

Tabla 7. Caudales de Crecida Obtenidos con el Método de Transposición, en m [3] /s

|T<br>(años<br>)|R.Claro en Los<br>Queñes<br>(A)|E.Upeo en<br>Upeo<br>(B)|Estero Guaiquillo|Col5|Col6|Estero Chequenlemo|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|T <br>(años<br>)|R.Claro<br>en<br>Los<br>Queñes<br>(A)|E.Upeo<br>en<br>Upeo<br>(B)|Con<br>(A)|Con<br>(B)|Promedi<br>o|Con<br>(A)|Con<br>(B)|Promedi<br>o|
|2 <br>5 <br>10<br>20<br>25<br>50<br>100|246<br>400<br>414<br>515<br>550<br>664<br>788|222<br>421<br>471<br>639<br>699<br>908<br>1151|128<br>209<br>216<br>269<br>287<br>347<br>411|132<br>251<br>281<br>381<br>417<br>541<br>686|130<br>230<br>248<br>325<br>352<br>444<br>549|73<br>119<br>123<br>153<br>164<br>198<br>235|75<br>143<br>160<br>217<br>238<br>309<br>391|74<br>131<br>142<br>185<br>201<br>253<br>313|

**e)** **Caudales Adoptados**

En base a cada uno de los métodos descritos precedentemente, se

estimaron los caudales de crecida asociados a cada período de retorno. Los valores

finalmente adoptados se estimaron en base a estos resultados y la experiencia y criterio

de este Consultor.

En las Tablas 8 y 9 se presentan los valores de crecida estimados en cada

estero, según cada método y los finalmente adoptados, para períodos de retorno de 2, 5,

10, 20, 25, 50 y 100 años.

Tabla 8. Caudales de Crecida Estimados para el Estero Guaiquillo, en m [3] /s

|T<br>(años)|Método|Col3|Col4|Promedio|Adoptado|
|---|---|---|---|---|---|
|T <br>(años)|Regional|Racional<br>Modificado|Transposici<br>ón|Transposici<br>ón|Transposici<br>ón|
|2 <br>5 <br>10<br>20<br>25<br>50<br>100|182<br>293<br>365<br>436<br>457<br>523<br>592|199<br>257<br>309<br>379<br>403<br>490<br>598|130<br>230<br>248<br>325<br>352<br>444<br>549|170<br>260<br>307<br>380<br>404<br>486<br>580|170<br>260<br>310<br>380<br>410<br>490<br>580|

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

23

Tabla 9. Caudales de Crecida Estimados para el Estero Chequenlemo, en m [3] /s

|T<br>(años)|Método|Col3|Col4|Promedio|Adoptado|
|---|---|---|---|---|---|
|T <br>(años)|Regional|Racional<br>Modificado|Transposició<br>n|Transposició<br>n|Transposició<br>n|
|2 <br>5 <br>10<br>20<br>25<br>50<br>100|90<br>144<br>180<br>214<br>224<br>257<br>291|105<br>138<br>163<br>202<br>213<br>259<br>315|74<br>131<br>142<br>182<br>201<br>253<br>313|90<br>138<br>162<br>200<br>213<br>256<br>306|90<br>140<br>160<br>200<br>220<br>260<br>310|

**A.1- Caudales de Estero Guaiquillo en Puntos de Interés**

A los fines del presente estudio, también es necesario conocer las estimaciones de

crecidas en otras secciones de interés, además de las ya presentadas.

Dichas secciones son dos, y se ubican en el cauce del estero Guaiquillo, en el sector

contiguo a la localidad de Romeral (entrada al área de estudio), e inmediatamente aguas

abajo de la confluencia con el estero Chequenlemo.

**a)** **Estero Guaiquillo en Romeral**

Esta sección, comprende un área aportante de 286,53 km [2] . Los caudales de crecida

asociados a períodos de retorno de 2, 5, 10, 20, 25, 50 y 100 años, fueron estimados

siguiendo la metodología expuesta para la estimación de caudales de crecida en cuencas

sin control fluviométrico.

En la Tabla 10 se presentan los caudales de crecida estimados en esta sección según los

distintos métodos aplicados, y el finalmente adoptado, en base al promedio de aquellos y

al criterio y experiencia de este Consultor.

Tabla 10. Caudales de Crecida Estimados en el Estero Guaiquillo en Romeral, en m [3] /s

|T<br>(años)|Método|Col3|Col4|Promedio|Caudal de Crecida<br>Adoptado|
|---|---|---|---|---|---|
|T <br>(años)|Regional|Racional<br>Modificado|Transposició<br>n|Transposició<br>n|Transposició<br>n|
|2 <br>5 <br>10<br>20<br>25<br>50|158<br>252<br>315<br>375<br>394<br>450|172<br>223<br>268<br>329<br>350<br>425|112<br>197<br>218<br>278<br>301<br>380|147<br>224<br>267<br>327<br>348<br>418|150<br>230<br>270<br>330<br>350<br>420|

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

24

100 510 520 469 500 500

**b)** **Estero Guaiquillo Aguas Abajo de la Confluencia con el Estero Chequenlemo**

Esta sección, se encuentra dentro del área de estudio, en el extremo SurOeste. Su área aportante es la suma de las de los esteros Guaiquillo (334,77 km [2] ) y
Chequenlemo (191,49 km [2] ) abarcando un área aportante total de 526,26 km [2] .

En este caso, los caudales de crecida se estimaron como la suma, para cada

período de retorno seleccionado, de los caudales de crecida ya estimados para cada

estero. Según este Consultor, este procedimiento es válido, dada la similaridad, en cuanto

a características hidrológicas, de ambas cuencas aportantes.

En la Tabla 11 se presentan los caudales de crecidas estimados en cada

estero, y los adoptados aguas abajo de su confluencia, en base a la suma de éstos y al

criterio de este Consultor, para períodos de retorno de 2, 5, 10, 20, 25, 50 y 100 años.

Tabla 11. Caudales de Crecida Estimados en el Estero Guaiquillo,

Aguas Abajo de su Confluencia con el Estero Chequenlemo, en m [3] /s

|T<br>(años)|Estero Guaiquillo<br>(s/Tabla 3.51)|Estero Chequenlemo<br>(s/Tabla 3.52)|Caudal de Crecida<br>Adoptado|
|---|---|---|---|
|2|170|90|260|
|5|260|140|400|
|10|310|160|470|
|20|380|200|580|
|25|410|220|630|
|50|490|260|750|
|100|580|310|890|

**B- Determinación de Capacidad Hidráulica de Cauces**

**a)** **Metodología**

La determinación de la capacidad hidráulica de los cauces naturales se hizo

con la misma metodología usada para los canales urbanos.

Sin embargo, sólo se consideró un mejoramiento en las quebradas que

consiste básicamente en la limpieza de su fondo y riberas.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

25

Tabla 12 Cantidades de Perfiles Transversales Generados y Obras de Arte Catastradas en el

|Area de Estudio|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Cauce|Perfiles Transversales|Perfiles Transversales|Obras de Arte|Obras de Arte|Cantidad<br>Total|Pendient<br>e <br>Promedi<br>o <br>(%)|Longitud<br>Catastra<br>da (m)|
|Cauce|Código|Cantidad|Código|Cantidad|Cantidad|Cantidad|Cantidad|
|Estero Guaiquillo<br>Estero<br>Chequenlemo<br>Estero<br>Los<br>Cristales<br>Estero<br>Quetequete<br>Quebrada<br>El<br>Litre<br>Quebrada<br>Mataquito|PT EG-n<br>PT ECH-<br>n <br>PT ELC-<br>n <br>PT EQ-n<br>PT QL-n<br>PT QM-n|60<br>8 <br>10<br>29<br>21<br>4|OA EG-n<br>OA ECH-n<br>OA ELC-n<br>OA EQ-n<br>OA QL-n<br>OA QM-n|3 <br>0<br>2 <br>3 <br>11<br>1|63<br>8 <br>12<br>32<br>32<br>5|0,48<br>0,36<br>0,43<br>0,36<br>0,82<br>1,75|14.045<br>1.530<br>2.348<br>4.952<br>3.228<br>300|
|Total||132||20|152|-|26.403|

Para el estero Guaiquillo se supuso un coeficiente de rugosidad compuesto

para cada uno de los perfiles transversales, con un coeficiente de Manning n=0,040 para el

cauce principal y para las áreas de inundación n= 0,060.

Para los restantes cauces naturales se estimó un coeficiente de rugosidad

único para cada sección según los recorridos de terreno realizados por el Consultor.

En la quebrada El Litre, además de la limpieza de su cauce, se supuso la

ejecución de actividades de limpieza y desembanque de obras de arte. La quebrada

Mataquito solo tiene una obra de arte la cual corresponde al cruce bajo el colector

interceptor de aguas servidas, la cual se encuentra en excelente estado.

**b)** **Capacidades Determinadas**

Las capacidades hidráulicas para la situación actual y situación mejorada se

detallan en el Apéndice V.5 “Capacidad Hidráulica de Cauces Naturales”, para cada cauce

y cada tramo de capacidad homogénea. Un resumen de estas capacidades se indica en la

Tabla 13.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

26

Tabla 13. Capacidades de Cauces Naturales

|Cauce|Capacidades (m3/s)|Col3|Col4|Col5|
|---|---|---|---|---|
|Cauce|Situación Actual|Situación Actual|Situación Mejorada|Situación Mejorada|
|Cauce|Mínima|Máxima|Mínima|Máxima|
|Estero Guaiquillo<br>Estero Chequenlemo<br>Estero Los Cristales<br>Estero Quetequete<br>Quebrada El Litre<br>Quebrada<br>Mataquito|300<br>38<br>3 <br>7 <br>1 <br>5|1.300<br>400<br>50<br>100<br>20<br>10|300<br>38<br>3 <br>9 <br>2 <br>6|1.300<br>450<br>50<br>120<br>22<br>15|

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

27

# APÉNDICE 2

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

28

**Fotografías estero Guaiquillo en zona de estudio**

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

29

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

30

# APÉNDICE 3

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

31

Tabla A 3.1: Eje Hidráulico T=50 años.

|Perfil|Q Total [m3/s]|LOB Elev [m]|ROB Elev [m]|Min Ch El [m]|W.S. Elev [m]|Vel Chnl [m]|Froude # Chl|
|---|---|---|---|---|---|---|---|
|1255.57|490|246.86|250.03|240.51|245.41|1.8|0.31|
|1240|490|246.84|249.82|240.57|245.28|1.88|0.34|
|1220|490|246.47|249.38|240.48|245.06|2.07|0.38|
|1200|490|246.29|249.24|240.36|244.98|1.61|0.28|
|1180|490|246.34|249.01|239.68|244.92|1.39|0.23|
|1160|490|246.05|248.92|239.92|244.82|1.51|0.26|
|1140|490|245.98|249.31|239.96|244.73|1.51|0.27|
|1120|490|246.05|248.07|239.67|244.66|1.31|0.23|
|1100|490|246.10|248.02|239.48|244.59|1.33|0.22|
|1080|490|246.15|247.73|239.66|244.55|1.22|0.2|
|1060|490|246.27|247.67|239.39|244.49|1.25|0.21|
|1040|490|245.43|247.73|239.27|244.43|1.26|0.21|
|1020|490|245.35|248.12|238.65|244.37|1.28|0.22|
|1000|490|245.17|247.54|238.55|244.3|1.32|0.23|
|980|490|245.30|247.14|238.2|244.21|1.4|0.26|
|960|490|245.22|247.29|237.51|244.1|1.5|0.25|
|940|490|245.10|247.06|237.18|243.98|1.62|0.28|
|920|490|244.82|246.92|237.22|243.87|1.63|0.29|
|900|490|244.51|246.95|237.61|243.75|1.7|0.29|
|880|490|244.44|246.62|237.72|243.6|1.83|0.32|
|860|490|244.45|246.31|237.56|243.46|1.85|0.32|
|840|490|244.41|246.11|237.38|243.35|1.71|0.3|
|820|490|244.27|246.07|237.73|243.23|1.69|0.3|
|800|490|244.26|246.03|237.99|243.12|1.64|0.29|
|780|490|244.37|245.99|237.88|243|1.58|0.29|
|760|490|244.02|246.06|237.97|242.9|1.54|0.28|
|740|490|243.92|246.09|237.71|242.82|1.42|0.25|
|720|490|244.00|245.17|237.74|242.75|1.34|0.24|
|700|490|243.95|244.87|237.55|242.69|1.23|0.21|
|680|490|243.77|244.83|237.57|242.64|1.15|0.21|
|660|490|243.69|244.65|237.68|242.58|1.19|0.21|
|640|490|243.72|244.74|237.22|242.5|1.25|0.23|
|620|490|243.45|244.31|236.89|242.4|1.36|0.26|
|600|490|243.27|244.34|236.67|242.33|1.19|0.23|
|580|490|243.21|243.51|237.02|242.24|1.27|0.25|
|560|490|243.37|243.52|237.1|242.13|1.36|0.27|
|540|490|243.31|243.54|236.66|242.06|1.24|0.22|
|520|490|243.30|243.59|236.74|242.02|1.11|0.19|
|500|490|242.96|243.49|236.16|241.98|1|0.17|
|480|490|242.76|243.41|235.79|241.95|0.96|0.17|
|460|490|242.72|242.55|235.59|241.87|1.16|0.22|
|440|490|242.69|242.41|235.12|241.82|1.1|0.2|
|420|490|243.17|241.54|235.02|241.75|1.14|0.21|
|400|490|243.50|241.42|234.92|241.67|1.21|0.23|
|380|490|243.31|241.50|234.75|241.56|1.38|0.27|
|360|490|243.24|241.13|234.79|241.44|1.44|0.28|
|340|490|242.76|240.38|234.7|241.36|1.35|0.24|
|320|490|242.68|240.45|234.93|241.27|1.47|0.25|
|300|490|242.84|240.87|235.07|241.19|1.31|0.25|
|280|490|242.65|240.84|235.35|241.08|1.39|0.27|
|260|490|242.22|241.37|234.4|240.93|1.57|0.32|
|240|490|242.47|240.85|234.78|240.74|1.67|0.35|
|220|490|242.45|241.10|235.07|240.56|1.69|0.35|
|200|490|242.42|240.66|234.97|240.31|1.87|0.4|
|180|490|243.04|240.94|234.67|240.12|1.8|0.34|
|160|490|245.64|241.01|234.49|240.02|1.58|0.29|
|140|490|245.90|241.17|234.16|239.91|1.55|0.28|
|120|490|245.60|241.09|234.01|239.82|1.54|0.25|
|100|490|245.15|240.66|233.87|239.76|1.44|0.23|
|80|490|245.02|240.23|234.16|239.69|1.39|0.23|
|60|490|244.71|240.02|234.2|239.64|1.26|0.21|
|40|490|244.39|240.27|234.47|239.54|1.49|0.25|
|20|490|243.98|240.32|234.23|239.44|1.58|0.28|
|0|490|243.90|240.29|234.31|239.37|1.42|0.23|

Donde: Perfil: Denominación del perfil, Q Total: caudal, LOB Elev :elevación ribera izquierda, ROB

Elev : elevación ribera derecha, Min Ch El: Elevación mínima del cauce (cota fondo), W.S Elev:
Elevación del eje Hidráulico, Vel Chnl: Velocidad del canal (m/s), Froude Chl: Número de Froude.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

32

Tabla A 3.2: Eje Hidráulico T=25 años.

|Perfil|Q Total [m3/s]|LOB Elev [m]|ROB Elev [m]|Min Ch El [m]|W.S. Elev [m]|Vel Chnl [m]|Froude # Chl|
|---|---|---|---|---|---|---|---|
|1255.57|410|246.86|250.03|240.51|245.02|1.7|0.31|
|1240|410|246.84|249.82|240.57|244.89|1.79|0.34|
|1220|410|246.47|249.38|240.48|244.66|1.99|0.39|
|1200|410|246.29|249.24|240.36|244.58|1.53|0.27|
|1180|410|246.34|249.01|239.68|244.52|1.3|0.22|
|1160|410|246.05|248.92|239.92|244.42|1.44|0.27|
|1140|410|245.98|249.31|239.96|244.31|1.45|0.28|
|1120|410|246.05|248.07|239.67|244.25|1.25|0.22|
|1100|410|246.10|248.02|239.48|244.18|1.26|0.22|
|1080|410|246.15|247.73|239.66|244.13|1.14|0.19|
|1060|410|246.27|247.67|239.39|244.08|1.18|0.2|
|1040|410|245.43|247.73|239.27|244.02|1.19|0.21|
|1020|410|245.35|248.12|238.65|243.95|1.21|0.22|
|1000|410|245.17|247.54|238.55|243.88|1.25|0.22|
|980|410|245.30|247.14|238.2|243.8|1.33|0.24|
|960|410|245.22|247.29|237.51|243.7|1.41|0.24|
|940|410|245.10|247.06|237.18|243.59|1.53|0.28|
|920|410|244.82|246.92|237.22|243.48|1.54|0.28|
|900|410|244.51|246.95|237.61|243.37|1.59|0.28|
|880|410|244.44|246.62|237.72|243.22|1.72|0.31|
|860|410|244.45|246.31|237.56|243.08|1.74|0.31|
|840|410|244.41|246.11|237.38|242.98|1.6|0.29|
|820|410|244.27|246.07|237.73|242.86|1.59|0.3|
|800|410|244.26|246.03|237.99|242.74|1.55|0.29|
|780|410|244.37|245.99|237.88|242.62|1.52|0.29|
|760|410|244.02|246.06|237.97|242.51|1.47|0.28|
|740|410|243.92|246.09|237.71|242.43|1.34|0.24|
|720|410|244.00|245.17|237.74|242.36|1.28|0.24|
|700|410|243.95|244.87|237.55|242.3|1.16|0.21|
|680|410|243.77|244.83|237.57|242.25|1.09|0.2|
|660|410|243.69|244.65|237.68|242.19|1.13|0.21|
|640|410|243.72|244.74|237.22|242.12|1.19|0.22|
|620|410|243.45|244.31|236.89|242.02|1.31|0.25|
|600|410|243.27|244.34|236.67|241.96|1.15|0.22|
|580|410|243.21|243.51|237.02|241.86|1.24|0.25|
|560|410|243.37|243.52|237.1|241.77|1.3|0.24|
|540|410|243.31|243.54|236.66|241.71|1.16|0.21|
|520|410|243.30|243.59|236.74|241.67|1.03|0.18|
|500|410|242.96|243.49|236.16|241.64|0.93|0.17|
|480|410|242.76|243.41|235.79|241.6|0.89|0.16|
|460|410|242.72|242.55|235.59|241.53|1.11|0.22|
|440|410|242.69|242.41|235.12|241.47|1.04|0.2|
|420|410|243.17|241.54|235.02|241.4|1.08|0.21|
|400|410|243.50|241.42|234.92|241.32|1.15|0.23|
|380|410|243.31|241.50|234.75|241.21|1.31|0.26|
|360|410|243.24|241.13|234.79|241.09|1.39|0.28|
|340|410|242.76|240.38|234.7|241.01|1.29|0.24|
|320|410|242.68|240.45|234.93|240.9|1.41|0.26|
|300|410|242.84|240.87|235.07|240.82|1.26|0.25|
|280|410|242.65|240.84|235.35|240.7|1.35|0.28|
|260|410|242.22|241.37|234.4|240.54|1.55|0.32|
|240|410|242.47|240.85|234.78|240.33|1.68|0.37|
|220|410|242.45|241.10|235.07|240.11|1.72|0.37|
|200|410|242.42|240.66|234.97|239.85|1.93|0.4|
|180|410|243.04|240.94|234.67|239.67|1.76|0.34|
|160|410|245.64|241.01|234.49|239.56|1.55|0.29|
|140|410|245.90|241.17|234.16|239.45|1.5|0.27|
|120|410|245.60|241.09|234.01|239.37|1.46|0.25|
|100|410|245.15|240.66|233.87|239.3|1.35|0.22|
|80|410|245.02|240.23|234.16|239.24|1.32|0.23|
|60|410|244.71|240.02|234.2|239.19|1.19|0.2|
|40|410|244.39|240.27|234.47|239.09|1.42|0.25|
|20|410|243.98|240.32|234.23|238.98|1.52|0.28|
|0|410|243.90|240.29|234.31|238.91|1.34|0.23|

Donde: Perfil: Denominación del perfil, Q Total: caudal, LOB Elev :elevación ribera izquierda, ROB Elev :

elevación ribera derecha, Min Ch El: Elevación mínima del cauce (cota fondo), W.S Elev: Elevación del eje
Hidráulico, Vel Chnl: Velocidad del canal (m/s), Froude Chl: Número de Froude.

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

33

# APÉNDICE 4

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

34

Tabla A.4.1 Revancha en cada perfil para los tres periodos de retorno simulados.

Amarillo: insuficiencia de revancha (<1m), Rojo: desborde.

|Perfil|Revancha|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Perfil**|**T = 100 años**|**T = 100 años**|**T = 50 años**|**T = 50 años**|**T = 25 años**|**T = 25 años**|
|**Perfil**|**Izquierda**|**Derecha**|**Izquierda**|**Derecha**|**Izquierda**|**Derecha**|
|1255.57|0.86<br>0.94<br>0.74<br>0.62<br>0.72<br>0.52<br>0.54<br>0.66<br>0.77<br>0.86<br>1.02<br>0.23<br>0.21<br>0.11<br>0.32<br>0.35<br>0.36<br>0.2<br>0.04<br>0.17<br>0.37<br>0.48<br>0.49<br>0.62<br>0.86<br>0.63<br>0.63<br>0.79<br>0.81<br>0.69<br>0.68<br>0.79<br>0.62<br>0.51<br>0.53<br>0.81<br>0.83<br>0.86<br>0.56<br>0.39<br>0.43<br>0.46<br>1<br>1.4|4.03|1.45|4.62|1.84|5.01|
|1240|1240|3.92|1.56|4.54|1.95|4.93|
|1220|1220|3.65|1.41|4.32|1.81|4.72|
|1200|1200|3.57|1.31|4.26|1.71|4.66|
|1180|1180|3.39|1.42|4.09|1.82|4.49|
|1160|1160|3.39|1.23|4.1|1.63|4.5|
|1140|1140|3.87|1.25|4.58|1.67|5|
|1120|1120|2.68|1.39|3.41|1.8|3.82|
|1100|1100|2.69|1.51|3.43|1.92|3.84|
|1080|1080|2.44|1.6|3.18|2.02|3.6|
|1060|1060|2.42|1.78<br>1<br>0.98<br>0.87<br>1.09|3.18|2.19|3.59|
|1040|1040|2.53|2.53|3.3|1.41|3.71|
|1020|1020|2.98|2.98|3.75|1.4|4.17|
|1000|1000|2.48|2.48|3.24|1.29|3.66|
|980|980|2.16|2.16|2.93|1.5|3.34|
|960|960|2.42|1.12|3.19|1.52|3.59|
|940|940|2.32|1.12<br>0.95<br>0.76<br>0.84<br>0.99<br>1.06|3.08|1.51|3.47|
|920|920|2.3|2.3|3.05|1.34|3.44|
|900|900|2.48|2.48|3.2|1.14|3.58|
|880|880|2.35|2.35|3.02|1.22|3.4|
|860|860|2.23|2.23|2.85|1.37|3.23|
|840|840|2.18|2.18|2.76|1.43|3.13|
|820|820|2.29|1.04|2.84|1.41|3.21|
|800|800|2.39|1.14|2.91|1.52|3.29|
|780|780|2.48|1.37|2.99|1.75|3.37|
|760|760|2.67|1.12|3.16|1.51|3.55|
|740|740|2.8|1.1|3.27|1.49|3.66|
|720|720|1.96|1.25|2.42|1.64|2.81|
|700|700|1.73|1.26|2.18|1.65|2.57|
|680|680|1.75|1.13|2.19|1.52|2.58|
|660|660|1.64|1.11|2.07|1.5|2.46|
|640|640|1.81|1.22|2.24|1.6|2.62|
|620|620|1.48|1.05<br>0.94<br>0.97<br>1.24|1.91|1.43|2.29|
|600|600|1.58<br>0.83<br>0.96<br>1.06|1.58<br>0.83<br>0.96<br>1.06|2.01|1.31|2.38|
|580|580|580|580|1.27|1.35|1.65|
|560|560|560|560|1.39|1.6|1.75|
|540|540|540|1.25|1.48|1.6|1.83|
|520|520|1.15|1.28<br>0.98<br>0.81<br>0.85<br>0.87<br>1.42|1.57|1.63|1.92|
|500|500|1.09|1.09|1.51|1.32|1.85|
|480|480|1.04<br>0.26<br>0.18<br>-0.63<br>-0.68<br>-0.5<br>-0.77<br>-1.45<br>-1.3<br>-0.82<br>-0.76<br>-0.11<br>-0.51<br>-0.14<br>-0.44<br>-0.02<br>0.14<br>0.38<br>0.37<br>0<br>-0.38<br>-0.55<br>-0.23<br>-0.1<br>-0.08|1.04<br>0.26<br>0.18<br>-0.63<br>-0.68<br>-0.5<br>-0.77<br>-1.45<br>-1.3<br>-0.82<br>-0.76<br>-0.11<br>-0.51<br>-0.14<br>-0.44<br>-0.02<br>0.14<br>0.38<br>0.37<br>0<br>-0.38<br>-0.55<br>-0.23<br>-0.1<br>-0.08|1.46<br>0.68<br>0.59<br>-0.21<br>-0.25<br>-0.06<br>-0.31<br>-0.98<br>-0.82<br>-0.32<br>-0.24<br>0.44<br>0.11<br>0.54<br>0.35<br>0.82<br>0.99<br>1.26|1.16|1.81|
|460|460|460|460|460|1.19|1.02<br>0.94<br>0.14<br>0.1<br>0.29<br>0.04<br>-0.63<br>-0.45<br>0.05<br>0.14<br>0.83<br>0.52<br>0.99<br>0.81<br>1.27|
|440|440|440|440|440|1.22|1.22|
|420|420|420|420|420|1.77|1.77|
|400|400|400|1.83|1.83|2.18|2.18|
|380|1.31|1.31|1.75|1.75|2.1|2.1|
|360|1.34<br>0.93<br>0.93<br>1.15|1.34<br>0.93<br>0.93<br>1.15|1.8|1.8|2.15|2.15|
|340|340|340|1.4|1.4|1.75|1.75|
|320|320|320|1.41|1.41|1.78|1.78|
|300|300|300|1.65|1.65|2.02|2.02|
|280|1.05<br>0.74<br>1.11|1.05<br>0.74<br>1.11|1.57|1.57|1.95|1.95|
|260|260|260|1.29|1.29|1.68|1.68|
|240|240|240|1.73|1.73|2.14|2.14|
|220|1.21|1.21|1.89|1.89|2.34|2.34|
|200|1.32|1.32|2.11|2.11|2.57|2.57|
|180|2.08|2.08|2.92|2.92|3.37|3.37|
|160|4.77|4.77|5.62|5.62|6.08|1.45|
|140|5.11|5.11|5.99|5.99|6.45|1.72|
|120|4.88|4.88|5.78|1.27<br>0.9<br>0.54<br>0.38<br>0.73<br>0.88<br>0.92|6.23|1.72|
|100|4.49|4.49|5.39|5.39|5.85|1.36<br>0.99<br>0.83<br>1.18|
|80|4.41|4.41|5.33|5.33|5.78|5.78|
|60|4.14|4.14|5.07|5.07|5.52|5.52|
|40|3.89|3.89|4.85|4.85|5.3|5.3|
|20|3.56|3.56|4.54|4.54|5|1.34|
|0|3.53|3.53|4.53|4.53|4.99|1.38|

_A_ luvial Consultoría en Recursos Hídricos - Pedro de Valdivia 1215, Of. 504, Providencia, Santiago de Chile

Tel. +56 2 2673 9225 - www.aluvial.net - info@aluvial.net

35

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3.2.: Caudales estimados para estero Guaiquillo. Fuente: Plan Maestro de Aguas**

| T [años] | Caudal [m3/s] |
| --- | --- |
| 2 | 170 |
| 5 | 260 |
| 10 | 310 |
| 20 | 380 |
| 25 | 410 |
| 50 | 490 |
| 100 | 580 |

**Tabla 3.3.: Manning obtenido mediante Cowan (1965)**

| Valor de n | Col2 |
| --- | --- |
| nb | 0.035 |
| n1 | 0.02 |
| n2 | 0.005 |
| n3 | 0.015 |
| n4 | 0.025 |
| m | 1 |
| **n ** | **0.1** |

**Tabla 4.1.: Desbordes (ribera izquierda - derecha) para los distintos periodos de retorno**

| Simulación | Tramo Desborde (perfil) | Col3 | Longitud total [m] | Col5 |
| --- | --- | --- | --- | --- |
| **Simulación** | **Izquierda** | **Derecha** | **Izquierda** | **Derecha** |
| T = 25 años<br>(Q = 410 m3/s) | <br>- | 320-340 | - | 20 |
| T = 50 años<br>(Q = 490 m3/s) | - | 280-420 | - | 140 |
| T= 100 años<br>(Q = 580 m3/s) | - | 0-80, 180-420 | - | 320 |

**Tabla 4.2.: Eje Hidráulico T=100 años.**

| Perfil | Q Total [m3/s] | LOB Elev [m] | ROB Elev [m] | Min Ch El [m] | W.S. Elev [m] | Vel Chnl [m] | Froude # Chl |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1255.57 | 580 | 246.86 | 250.03 | 240.51 | 246 | 1.81 | 0.3 |
| 1240 | 580 | 246.84 | 249.82 | 240.57 | 245.9 | 1.85 | 0.31 |
| 1220 | 580 | 246.47 | 249.38 | 240.48 | 245.73 | 1.98 | 0.35 |
| 1200 | 580 | 246.29 | 249.24 | 240.36 | 245.67 | 1.59 | 0.25 |
| 1180 | 580 | 246.34 | 249.01 | 239.68 | 245.62 | 1.38 | 0.22 |
| 1160 | 580 | 246.05 | 248.92 | 239.92 | 245.53 | 1.47 | 0.26 |
| 1140 | 580 | 245.98 | 249.31 | 239.96 | 245.44 | 1.44 | 0.26 |
| 1120 | 580 | 246.05 | 248.07 | 239.67 | 245.39 | 1.28 | 0.21 |
| 1100 | 580 | 246.10 | 248.02 | 239.48 | 245.33 | 1.3 | 0.21 |
| 1080 | 580 | 246.15 | 247.73 | 239.66 | 245.29 | 1.21 | 0.18 |
| 1060 | 580 | 246.27 | 247.67 | 239.39 | 245.25 | 1.23 | 0.19 |
| 1040 | 580 | 245.43 | 247.73 | 239.27 | 245.2 | 1.21 | 0.21 |
| 1020 | 580 | 245.35 | 248.12 | 238.65 | 245.14 | 1.23 | 0.22 |
| 1000 | 580 | 245.17 | 247.54 | 238.55 | 245.06 | 1.25 | 0.23 |
| 980 | 580 | 245.30 | 247.14 | 238.2 | 244.98 | 1.3 | 0.24 |
| 960 | 580 | 245.22 | 247.29 | 237.51 | 244.87 | 1.38 | 0.27 |
| 940 | 580 | 245.10 | 247.06 | 237.18 | 244.74 | 1.48 | 0.29 |
| 920 | 580 | 244.82 | 246.92 | 237.22 | 244.62 | 1.49 | 0.29 |
| 900 | 580 | 244.51 | 246.95 | 237.61 | 244.47 | 1.56 | 0.32 |
| 880 | 580 | 244.44 | 246.62 | 237.72 | 244.27 | 1.71 | 0.35 |
| 860 | 580 | 244.45 | 246.31 | 237.56 | 244.08 | 1.78 | 0.35 |
| 840 | 580 | 244.41 | 246.11 | 237.38 | 243.93 | 1.68 | 0.32 |
| 820 | 580 | 244.27 | 246.07 | 237.73 | 243.78 | 1.65 | 0.33 |
| 800 | 580 | 244.26 | 246.03 | 237.99 | 243.64 | 1.65 | 0.31 |
| 780 | 580 | 244.37 | 245.99 | 237.88 | 243.51 | 1.6 | 0.29 |
| 760 | 580 | 244.02 | 246.06 | 237.97 | 243.39 | 1.55 | 0.31 |
| 740 | 580 | 243.92 | 246.09 | 237.71 | 243.29 | 1.46 | 0.26 |
| 720 | 580 | 244.00 | 245.17 | 237.74 | 243.21 | 1.38 | 0.25 |
| 700 | 580 | 243.95 | 244.87 | 237.55 | 243.14 | 1.27 | 0.23 |
| 680 | 580 | 243.77 | 244.83 | 237.57 | 243.08 | 1.19 | 0.22 |
| 660 | 580 | 243.69 | 244.65 | 237.68 | 243.01 | 1.23 | 0.22 |
| 640 | 580 | 243.72 | 244.74 | 237.22 | 242.93 | 1.29 | 0.23 |
| 620 | 580 | 243.45 | 244.31 | 236.89 | 242.83 | 1.39 | 0.26 |
| 600 | 580 | 243.27 | 244.34 | 236.67 | 242.76 | 1.22 | 0.22 |
| 580 | 580 | 243.21 | 243.51 | 237.02 | 242.68 | 1.26 | 0.25 |
| 560 | 580 | 243.37 | 243.52 | 237.1 | 242.56 | 1.37 | 0.28 |
| 540 | 580 | 243.31 | 243.54 | 236.66 | 242.48 | 1.29 | 0.23 |
| 520 | 580 | 243.30 | 243.59 | 236.74 | 242.44 | 1.17 | 0.2 |
| 500 | 580 | 242.96 | 243.49 | 236.16 | 242.4 | 1.06 | 0.17 |
| 480 | 580 | 242.76 | 243.41 | 235.79 | 242.37 | 1.01 | 0.17 |
| 460 | 580 | 242.72 | 242.55 | 235.59 | 242.29 | 1.19 | 0.22 |
| 440 | 580 | 242.69 | 242.41 | 235.12 | 242.23 | 1.14 | 0.2 |
| 420 | 580 | 243.17 | 241.54 | 235.02 | 242.17 | 1.18 | 0.21 |
| 400 | 580 | 243.50 | 241.42 | 234.92 | 242.1 | 1.24 | 0.22 |
| 380 | 580 | 243.31 | 241.50 | 234.75 | 242 | 1.4 | 0.25 |
| 360 | 580 | 243.24 | 241.13 | 234.79 | 241.9 | 1.46 | 0.26 |
| 340 | 580 | 242.76 | 240.38 | 234.7 | 241.83 | 1.37 | 0.23 |
| 320 | 580 | 242.68 | 240.45 | 234.93 | 241.75 | 1.47 | 0.24 |
| 300 | 580 | 242.84 | 240.87 | 235.07 | 241.69 | 1.32 | 0.23 |
| 280 | 580 | 242.65 | 240.84 | 235.35 | 241.6 | 1.39 | 0.25 |
| 260 | 580 | 242.22 | 241.37 | 234.4 | 241.48 | 1.52 | 0.28 |
| 240 | 580 | 242.47 | 240.85 | 234.78 | 241.36 | 1.56 | 0.29 |
| 220 | 580 | 242.45 | 241.10 | 235.07 | 241.24 | 1.55 | 0.29 |
| 200 | 580 | 242.42 | 240.66 | 234.97 | 241.1 | 1.59 | 0.31 |
| 180 | 580 | 243.04 | 240.94 | 234.67 | 240.96 | 1.58 | 0.31 |
| 160 | 580 | 245.64 | 241.01 | 234.49 | 240.87 | 1.45 | 0.25 |
| 140 | 580 | 245.90 | 241.17 | 234.16 | 240.79 | 1.41 | 0.24 |
| 120 | 580 | 245.60 | 241.09 | 234.01 | 240.72 | 1.43 | 0.24 |
| 100 | 580 | 245.15 | 240.66 | 233.87 | 240.66 | 1.35 | 0.22 |
| 80 | 580 | 245.02 | 240.23 | 234.16 | 240.61 | 1.25 | 0.21 |
| 60 | 580 | 244.71 | 240.02 | 234.2 | 240.57 | 1.17 | 0.18 |
| 40 | 580 | 244.39 | 240.27 | 234.47 | 240.5 | 1.35 | 0.22 |
| 20 | 580 | 243.98 | 240.32 | 234.23 | 240.42 | 1.42 | 0.23 |
| 0 | 580 | 243.90 | 240.29 | 234.31 | 240.37 | 1.28 | 0.22 |

**Tabla 4.3.: Insuficiencia en la revancha para los distintos periodos de retorno simulados.**

| Simulación | Tramo No cumple revancha (perfil) | Col3 | Longitud total No cumple<br>revancha [m] | Col5 |
| --- | --- | --- | --- | --- |
| **Simulación** | **Izquierda** | **Derecha** | **Izquierda** | **Derecha** |
| T = 25 años<br>(Q = 410 m3/s) | <br>- | 60-80, 200-300,<br>360-440 | - | 200 |
| T = 50 años<br>(Q = 490 m3/s) | 440-500, 580-<br>600, 860-920,<br>1000-1040 | 0-100, 160-260,<br>440-460 | 180 | 220 |
| T= 100 años<br>(Q = 580 m3/s) | 260, 320-340,<br>420-1040, 1080-<br>1255 | 100-160, 440-<br>460, 560-580 | 835 | 100 |

**Tabla 1.: Parámetros Morfométricos de las Cuencas Aportantes**

| Estero | A<br>(km2) | L<br>(m) | S<br>(%) | H<br>(M) | Tc (min) | Col7 | Col8 | Coeficiente<br>Escorrentía |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estero | A <br>(km2) | L <br>(m) | S <br>(%) | H <br>(M) | CHPW | SCS | Adoptado | Adoptado |
| Guaiquillo<br>Chequenlemo | 334,77<br>191,49 | 48.849<br>36.572 | 33<br>18 | 1.725<br>1.100 | 289<br>246 | 263<br>282 | 270<br>270 | 0,33<br>0,35 |

**Tabla 2.: Relación Q T /Q para el Area de Estudio (Zona homogénea Q p )**

| Período de Retorno<br>(años) | 2 | 5 | 10 | 20 | 25 | 50 | 100<br>1,62 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Relación QT/Q | 0,50 | 0,80 | 1,00 | 1,19 | 1,25 | 1,43 | 1,43 |

**Tabla 3.: Caudales de Crecida Estimados según el Método Regional, en m [3] /s**

| T<br>(años) | Estero Guaiquillo | Estero Chequenlemo |
| --- | --- | --- |
| 2 <br>5 <br>10<br>20<br>25<br>50<br>100 | 182<br>293<br>365<br>436<br>457<br>523<br>592 | 90<br>144<br>180<br>214<br>224<br>257<br>291 |

**Tabla 4.: Intensidades Medias estimadas en cada cuenca aportante, en mm/h.**

| T<br>(años) | CF | Estero Guaiquillo<br>(P24 = 140 mm)<br>10 | Estero Chequenlemo<br>P24<br>( 10 = 122 mm) |
| --- | --- | --- | --- |
| 2 <br>5 <br>10<br>20<br>25<br>50<br>100 | 0,64<br>0,83<br>1,00<br>1,23<br>1,30<br>1,58<br>1,93 | 6,8<br>8,8<br>10,6<br>13,0<br>13,8<br>16,8<br>20,5 | 5,9<br>7,8<br>9,2<br>11,4<br>12,0<br>14,6<br>17,8 |

**Tabla 5.: Caudales de Crecida, obtenidos con el Método Racional Modificado, en m [3] /s**

| T<br>(años) | Estero Guaiquillo | Estero Chequenlemo |
| --- | --- | --- |
| 2 <br>5 <br>10<br>20<br>25<br>50<br>100 | 199<br>257<br>309<br>379<br>403<br>490<br>598 | 105<br>138<br>163<br>202<br>213<br>259<br>315 |

**Tabla 6.: Areas Aportantes y Precipitaciones Medias de Cauces en el Area de Estudio**

| Cauce | Control<br>Fluviométrico | Area<br>(Km2) | P media<br>p<br>(mm/año) |
| --- | --- | --- | --- |
| Río Teno después de Junta con Claro<br>Río Claro en Los Queñes<br>Estero Upeo en Upeo<br>Estero Guaiquillo<br>Estero Chequenlemo | si<br>si<br>si<br>no<br>no | 1188<br>350<br>450<br>335<br>191 | 2100<br>2200<br>1500<br>1200<br>1200 |

**Tabla 7.: Caudales de Crecida Obtenidos con el Método de Transposición, en m [3] /s**

| T<br>(años<br>) | R.Claro en Los<br>Queñes<br>(A) | E.Upeo en<br>Upeo<br>(B) | Estero Guaiquillo | Col5 | Col6 | Estero Chequenlemo | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T <br>(años<br>) | R.Claro<br>en<br>Los<br>Queñes<br>(A) | E.Upeo<br>en<br>Upeo<br>(B) | Con<br>(A) | Con<br>(B) | Promedi<br>o | Con<br>(A) | Con<br>(B) | Promedi<br>o |
| 2 <br>5 <br>10<br>20<br>25<br>50<br>100 | 246<br>400<br>414<br>515<br>550<br>664<br>788 | 222<br>421<br>471<br>639<br>699<br>908<br>1151 | 128<br>209<br>216<br>269<br>287<br>347<br>411 | 132<br>251<br>281<br>381<br>417<br>541<br>686 | 130<br>230<br>248<br>325<br>352<br>444<br>549 | 73<br>119<br>123<br>153<br>164<br>198<br>235 | 75<br>143<br>160<br>217<br>238<br>309<br>391 | 74<br>131<br>142<br>185<br>201<br>253<br>313 |

**Tabla 8.: Caudales de Crecida Estimados para el Estero Guaiquillo, en m [3] /s**

| T<br>(años) | Método | Col3 | Col4 | Promedio | Adoptado |
| --- | --- | --- | --- | --- | --- |
| T <br>(años) | Regional | Racional<br>Modificado | Transposici<br>ón | Transposici<br>ón | Transposici<br>ón |
| 2 <br>5 <br>10<br>20<br>25<br>50<br>100 | 182<br>293<br>365<br>436<br>457<br>523<br>592 | 199<br>257<br>309<br>379<br>403<br>490<br>598 | 130<br>230<br>248<br>325<br>352<br>444<br>549 | 170<br>260<br>307<br>380<br>404<br>486<br>580 | 170<br>260<br>310<br>380<br>410<br>490<br>580 |

**Tabla 9.: Caudales de Crecida Estimados para el Estero Chequenlemo, en m [3] /s**

| T<br>(años) | Método | Col3 | Col4 | Promedio | Adoptado |
| --- | --- | --- | --- | --- | --- |
| T <br>(años) | Regional | Racional<br>Modificado | Transposició<br>n | Transposició<br>n | Transposició<br>n |
| 2 <br>5 <br>10<br>20<br>25<br>50<br>100 | 90<br>144<br>180<br>214<br>224<br>257<br>291 | 105<br>138<br>163<br>202<br>213<br>259<br>315 | 74<br>131<br>142<br>182<br>201<br>253<br>313 | 90<br>138<br>162<br>200<br>213<br>256<br>306 | 90<br>140<br>160<br>200<br>220<br>260<br>310 |

**Tabla 10.: Caudales de Crecida Estimados en el Estero Guaiquillo en Romeral, en m [3] /s**

| T<br>(años) | Método | Col3 | Col4 | Promedio | Caudal de Crecida<br>Adoptado |
| --- | --- | --- | --- | --- | --- |
| T <br>(años) | Regional | Racional<br>Modificado | Transposició<br>n | Transposició<br>n | Transposició<br>n |
| 2 <br>5 <br>10<br>20<br>25<br>50 | 158<br>252<br>315<br>375<br>394<br>450 | 172<br>223<br>268<br>329<br>350<br>425 | 112<br>197<br>218<br>278<br>301<br>380 | 147<br>224<br>267<br>327<br>348<br>418 | 150<br>230<br>270<br>330<br>350<br>420 |

**Tabla 11.: Caudales de Crecida Estimados en el Estero Guaiquillo,**

| T<br>(años) | Estero Guaiquillo<br>(s/Tabla 3.51) | Estero Chequenlemo<br>(s/Tabla 3.52) | Caudal de Crecida<br>Adoptado |
| --- | --- | --- | --- |
| 2 | 170 | 90 | 260 |
| 5 | 260 | 140 | 400 |
| 10 | 310 | 160 | 470 |
| 20 | 380 | 200 | 580 |
| 25 | 410 | 220 | 630 |
| 50 | 490 | 260 | 750 |
| 100 | 580 | 310 | 890 |

**Tabla 12: Cantidades de Perfiles Transversales Generados y Obras de Arte Catastradas en el**

| Area de Estudio | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cauce | Perfiles Transversales | Perfiles Transversales | Obras de Arte | Obras de Arte | Cantidad<br>Total | Pendient<br>e <br>Promedi<br>o <br>(%) | Longitud<br>Catastra<br>da (m) |
| Cauce | Código | Cantidad | Código | Cantidad | Cantidad | Cantidad | Cantidad |
| Estero Guaiquillo<br>Estero<br>Chequenlemo<br>Estero<br>Los<br>Cristales<br>Estero<br>Quetequete<br>Quebrada<br>El<br>Litre<br>Quebrada<br>Mataquito | PT EG-n<br>PT ECH-<br>n <br>PT ELC-<br>n <br>PT EQ-n<br>PT QL-n<br>PT QM-n | 60<br>8 <br>10<br>29<br>21<br>4 | OA EG-n<br>OA ECH-n<br>OA ELC-n<br>OA EQ-n<br>OA QL-n<br>OA QM-n | 3 <br>0<br>2 <br>3 <br>11<br>1 | 63<br>8 <br>12<br>32<br>32<br>5 | 0,48<br>0,36<br>0,43<br>0,36<br>0,82<br>1,75 | 14.045<br>1.530<br>2.348<br>4.952<br>3.228<br>300 |
| Total |  | 132 |  | 20 | 152 | - | 26.403 |

**Tabla 13.: Capacidades de Cauces Naturales**

| Cauce | Capacidades (m3/s) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| Cauce | Situación Actual | Situación Actual | Situación Mejorada | Situación Mejorada |
| Cauce | Mínima | Máxima | Mínima | Máxima |
| Estero Guaiquillo<br>Estero Chequenlemo<br>Estero Los Cristales<br>Estero Quetequete<br>Quebrada El Litre<br>Quebrada<br>Mataquito | 300<br>38<br>3 <br>7 <br>1 <br>5 | 1.300<br>400<br>50<br>100<br>20<br>10 | 300<br>38<br>3 <br>9 <br>2 <br>6 | 1.300<br>450<br>50<br>120<br>22<br>15 |
