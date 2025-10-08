---
title: Sin título
author: Ricardo Martínez Villaseñor
date: D:20210415192738-04'00'
language: es
type: report
pages: 15
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 11 ANÁLISIS DE EFECTO POR SOMBRA INTERMITENTE PMGD EÓLICO CHARA
-->

# ANEXO 11 ANÁLISIS DE EFECTO POR SOMBRA INTERMITENTE PMGD EÓLICO CHARA

Documento preparado por:

**TEBAL, Estudios e ingeniería ambiental**
ANDRÉS DE FUENZALIDA 17, OFICINA 34, PROVIDENCIA, SANTIAGO DE CHILE

Teléfono +56 2 2222 7059

Email info@tebal.cl

[Website www.tebal.cl](http://www.tebal.cl/)

## REGISTRO DE CONTROL DE DOCUMENTO

|TÍTULO DEL DOCUMENTO|Col2|SHADOW FLICKER PROYECTO PMGD EÓLICO CHARA|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID de documento**|**ID de documento**||**Número de proyecto**|**Número de proyecto**|||
|**Versión**|**Fecha**|**Detalle/Estado**|**Autor**|**Revisión**<br>**TEBAL**|**Revisión**<br>**Cliente**|**Aprobado**<br>**por**|
|1|12-04-2021|Borrador|RMV||||
|2|12-04-2021|VF||MCF|||
||||||||

1-i

## CONTENIDOS

1. INTRODUCCIÓN ........................................................................................................... 3

2. OBJETIVOS ................................................................................................................... 3

3. DESCRIPCIÓN DEL PROYECTO...................................................................................... 4

3.1. ÁREA DE INFLUENCIA .................................................................................................. 4

4. ANTECEDENTES NORMATIVOS .................................................................................... 5

4.1. NORMA ALEMANA: INDICACIONES PARA LA DETERMINACIÓN DE LA APRECIACIÓN

DE EMISIONES ÓPTICAS DE INSTALACIONES EÓLICAS (WEA-SCHATTENWURF-HINWEISE, 2002) ..... 5
5. METODOLOGÍA DE MODELACIÓN ............................................................................... 8

5.1. ESCENARIO DE MODELACIÓN Y LÍMITES DE EXPOSICIÓN ........................................... 8

6. RESULTADOS ............................................................................................................. 10

7. CONCLUSIONES ......................................................................................................... 13

8. BIBLIOGRAFÍA ............................................................................................................ 14

## ÍNDICE DE FIGURAS

Figura 1. Plano Ubicación proyecto..................................................................................................... 4

## ÍNDICE DE TABLAS

Tabla 1. Promedio de horas diarias de sol Estación Meteorológica Puerto Montt. ........................... 9

Tabla 2. Datos modelación de Shadow flicker. ................................................................................. 10

1-ii

## 1. INTRODUCCIÓN

El presente informe corresponde a la evaluación de la eventual afectación por efecto de la sombra

intermitente o _shadow flicker_ en el proyecto **PMGD Eólico Chara**, en adelante, el Proyecto, que se

ubicará en la comuna de Calbuco, ubicada en la provincia de Llanquihue, Región de Los Lagos.

El Efecto sombra intermitente o _Shadow Flicker_ corresponde al sombreado repetitivo de la luz solar

directa provocado por las aspas del rotor de un aerogenerador sobre un receptor, pudiendo ser este

último, una vivienda u otra edificación. La proyección de sombras dependerá de las condiciones

atmosféricas, dirección del viento, posición del sol y las horas de operación del aerogenerador.

Para el cálculo de sombra intermitente o shadow flicker, se utiliza el programa especializado en la

evaluación de parques eólicos WindPRO. Por otro lado, en vista de que nuestro país no posee norma

con valores límites para la evaluación de esta componente, la evaluación de la afectación por

sombra se realiza en base a la norma alemana “ _Hinweise zur Ermittiung und Beurteilung der_

_optischen Inmissionen von Windenergieanlagen (WEA-Schattenwurf-Hinweise, 2020),”_ en español

“Indicaciones relativas a la investigación y evaluación de las emisiones ópticas de instalaciones de

energía eólica (Versión 13.03.2020)”.

## 2. OBJETIVOS

 - Evaluar las horas por año donde se produce el fenómeno _Shadow Flicker_ en los receptores

cercanos al proyecto.

 - Verificar el cumplimiento normativo, tomando como referencia la norma Alemana antes

mencionada

3

## 3. DESCRIPCIÓN DEL PROYECTO

El proyecto estará ubicado en las cercanías de la comuna de Calbuco, en la Región de Los Lagos. El

área específica corresponde a una zona rural de uso preferentemente agrícola y forestal.

**Figura 1. Plano Ubicación proyecto.**

Fuente: Elaboración propia.
### 3.1.ÁREA DE INFLUENCIA

Para determinar el área de influencia del efecto por sombra intermitente del Proyecto, se considera

un área con receptores donde, según la normativa de referencia, sea posible percibir el efecto por

sombra intermitente. La normativa alemana indica que para la extensión de la superficie de análisis,

el área de sombreado resulta de la distancia desde el aerogenerador en la cual el 20% de la superficie

del sol es ocultada por un aspa del rotor o bien un buffer de 2 [km] desde cada aerogenerador. Para

este estudio se consideró un área de influencia con radio de 2 [km] desde la base de cada

aerogenerador.

4

## 4. ANTECEDENTES NORMATIVOS

Actualmente, en Chile no existen normas que establezcan los niveles máximos para la exposición a

la sombra intermitente. Sin embargo, el Decreto Supremo N°40/12 del Ministerio del Medio

Ambiente, establece en su artículo 11 lo siguiente:

“ _Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos_

_de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados_

_en la letra b), ambas del artículo 11 de la ley, serán aquellas vigentes en los siguientes Estados:_

_República Federal de Alemania, República de Argentina, Australia, República Federativa del Brasil,_

_Canadá, Reino de España, Estados Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia,_

_Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la_

_utilización de las normas de referencia, se priorizará aquel Estado que posea similitud en sus_

_componentes ambientales, con la situación nacional y/o local, lo que será justificado_

_razonablemente por el proponente”._

En base a este artículo, se toma como referencia la norma alemana “ _Hinweise zur Ermittiung und_

_Beurteilung der optischen Inmissionen von Windenergieanlagen (WEA-Schattenwurf-Hinweise,_

_2020),”_ en español “Indicaciones relativas a la investigación y evaluación de las emisiones ópticas

de instalaciones de energía eólica (Versión 2020)”, norma de calidad ambiental reconocida y vigente

dentro de los estados indicados en el artículo 11 del D.S. N°40/12 del MMA. Esta norma establece

dos escenarios de modelación: un límite de exposición temporal para la duración astronómicamente

posible (peor condición) de sombra anual de 30 horas/año y de 30 minutos/día, y un escenario

realista de exposición, en que se considera la meteorología y obstáculos existentes, con un límite de

8 horas/año y de 30 minutos/día de sombra.

### 4.1. NORMA ALEMANA: INDICACIONES PARA LA DETERMINACIÓN DE LA APRECIACIÓN DE EMISIONES ÓPTICAS DE INSTALACIONES EÓLICAS (WEA- SCHATTENWURF-HINWEISE, 2002)

La norma alemana de referencia define la proyección intermitente de sombras ( _shadow flicker_ )

como “el sombreado repetitivo de la luz solar directa provocado por las aspas del rotor de una

instalación de energía eólica (aerogenerador), en que la proyección de sombras dependerá de las

condiciones atmosféricas, la dirección del viento, la posición del sol y las horas de operación de la

instalación”.

Esta proyección intermitente de sombras puede hacer que las condiciones de iluminación de una

habitación con ventanas orientadas hacia el aerogenerador varíe a lo largo del día, situación que

5

puede resultar en una eventual molestia a las personas que viven en el área cercana a las sombras

proyectadas por las turbinas eólicas.

En este sentido, la superficie en la cual ocurre la proyección intermitente de sombras se denomina

área de sombreado y es en dicha área donde la norma de referencia a utilizar, tiene por objeto

evitar, de manera segura, las posibles molestias ocasionadas por la proyección intermitente de

sombras. Para la extensión de la superficie de análisis, según la normativa, el área de sombreado

resulta de la distancia desde el aerogenerador en la cual el 20% de la superficie del sol es ocultada

por un aspa del rotor o bien, una distancia de 2 kilómetros desde cada aerogenerador.

En forma complementaria, y de acuerdo a la Asociación Danesa de la Industria del Viento (Danish
Wind Industry Association [1] ), a distancias entre 500 y 1000 m, la proyección intermitente de sombra

no será observada, ya que la sombra de las turbinas se verá como un objeto fijo, y a una distancia

superior a los 1.000 m señalados, el efecto no será perceptible por los observadores y/o residentes

del sector.

Adicionalmente, la normativa de referencia alemana considera los siguientes lugares como

susceptibles de ser afectados por la proyección intermitente de sombras:

 - Espacios habitables, incluidos los pasillos habitables.

 - Dormitorios, incluidas las habitaciones en hoteles, hospitales y sanatorios.

 - Salas de clases de colegios, universidades y establecimientos similares.

 - Oficinas, consultas médicas, salas de trabajo, salas de capacitación y lugares de trabajo

similares.

 - Las superficies exteriores directamente adyacentes a edificios (por ejemplo, terrazas y

balcones) corresponden a espacios que deben protegerse durante el día, entre las 6:00 y las

22:00 hrs.

Para que se genere la proyección intermitente de sombras o efecto _shadow flicker_, se deben

combinar los siguientes factores.

 - **Día despejado** : ausencia de nubosidad, presencia de sol.

 - **Aerogenerador operando** : para esto se requiere una velocidad de viento superior a 3 m/s.

 - **Aerogenerador interpuesto entre el sol y observador** : en un momento determinado del

día, en función de la trayectoria del sol.

 - **Orientación de las aspas permitiendo proyectar sombras al observador** : rotor del

aerogenerador perpendicular al sol.

1 Danish Wind Industry Association” disponible en http://www.windpower.org

6

 - **Inexistencia de obstáculos entre aerogenerador y receptor** : vegetación, construcciones,

aleros, corredores techados y otros.

 **Ángulo de orientación de ventanas de receptores coincidente con orientación del sol y**

**posición de aerogenerador** .

 - **Vivienda habitada al momento de proyección de sombra** : existencia de observadores al

interior de vivienda.

La norma alemana considera dos escenarios posibles para la modelación:

a) **Duración máxima astronómicamente posible del sombreado (peor escenario)** : tiempo durante

el cual el sol teóricamente alumbra durante todo el periodo comprendido entre la salida y la puesta

de sol, con el cielo totalmente despejado. Por otro lado, la superficie del rotor se encuentra

perpendicular a los rayos del sol y la instalación de energía eólica está en operación. Los límites de

exposición para este modelo corresponden a: **30 horas al año y 30 minutos al día** .

b) **Duración del sombreado meteorológicamente probable (caso real, valores esperados):** período

para el cual se calcula la proyección de sombras considerando condiciones atmosféricas habituales

(nubosidad basada en estadística). Los límites de exposición para este modelo corresponden a: **8**

**horas al año y 30 minutos al día** .

En el Anexo 11-2 del presente informe se presenta la norma alemana de referencia utilizada, en su

idioma original y en su versión traducida y certificada por el Ministerio de Relaciones Exteriores de

Chile.

Considerando la norma revisada, el siguiente capítulo presenta la metodología utilizada para la

estimación del efecto sombra intermitente o _shadow flicker_ originado por el Proyecto.

7

## 5. METODOLOGÍA DE MODELACIÓN

### 5.1. ESCENARIO DE MODELACIÓN Y LÍMITES DE EXPOSICIÓN

Tal como se menciona en el punto anterior, los límites de exposición corresponden a 30 hrs/año y

30 minutos/día para el peor escenario y 8 hrs/año y 30 minutos/día para el caso real.

Para la estimación del fenómeno de _shadow flicker_, se utilizó el software especializado en parques

eólicos WindPRO versión 3.4, el que requiere de la incorporación de variables climáticas y

topográficas del sector. Los datos estadísticos de meteorología utilizados fueron los siguientes:

 - Probabilidad mensual de sol, específicamente la media diaria de horas de sol mensual.

 - Tiempo operacional anual de las turbinas en función de la dirección cardinal del viento.

La topografía del área de estudio considera los relieves y depresiones geográficas existentes. Cabe

señalar que bajo un escenario conservador, no se incorporó en la modelación las barreras vegetales

(alamedas, áreas boscosas), las cuales en la práctica permitirían la atenuación de la proyección

intermitente de sombras en los receptores.

En cuanto al peor escenario, el programa supone que el sol siempre brilla desde la salida a la puesta

de sol, el aerogenerador se mantiene siempre en movimiento y el rotor se encuentra orientado

perpendicularmente al receptor.

Para la extensión de la superficie de análisis se considera un buffer de 2000 [m] desde cada

aerogenerador.

Las variables incorporadas en el software windPRO para la modelación corresponden a las

siguientes:

 - Información del aerogenerador: la proyección de sombras se estimó a partir de las

dimensiones máximas definidas para los aerogeneradores del proyecto. Los

aerogeneradores a emplear corresponden al fabricante General Electrics Wind Energy,

referencial, con altura de buje de 140 [m] y 158[m] de diámetro de rotor

 - Ubicación geográfica de los aerogeneradores: comuna de Calbuco.

 - Ubicación de los receptores dentro de un radio de 2 [km] para cada aerogenerador,

considerando exclusivamente viviendas e infraestructura y/o equipamiento con flujos de

personas constante.

 - Para la topografía se consideró la visibilidad topográfica entre los aerogeneradores y los

receptores, así como las curvas de nivel del área de estudio.

 - Azimut y elevación del sol, las cuales corresponden a la traslación del sol en el día y a lo

largo del año según los cambios de estación.

8

 - Se consideró un ángulo de horizonte de 3° para el alba y el ocaso, en tanto las sombras son

bloqueadas por distintos obstáculos bajo dichos parámetros.

 - Para el cálculo promedio de horas de luz en periodo de un año corrido, se determinó la

estación de referencia más cercana al área del proyecto (Tabla 1), ubicada en la ciudad de

Puerto Montt.

 - Modo invernadero en los receptores: a modo de representar un escenario conservador, se

considera como “invernaderos”(Greenhouse) a todas las viviendas. Esto se traduce en que

basta que la sombra producida por los aerogeneradores alcance la vivienda para que se

considere la ocurrencia del efecto. En la realidad, solo podrá producirse el efecto si es que

existe una ventana orientada hacia los rayos del sol que se vean interrumpidos por el

aerogenerador.

**Tabla 1. Promedio de horas diarias de sol Estación Meteorológica Puerto Montt.**

|MES|PROMEDIO DE HORAS DIARIAS DE SOL|
|---|---|
|Enero|6.32|
|Febrero|6.58|
|Marzo|4.55|
|Abril|3.17|
|Mayo|2.40|
|Junio|1.73|
|Julio|2.63|
|Agosto|3.00|
|Septiembre|4.15|
|Octubre|5.40|
|Noviembre|5.72|
|Diciembre|5.52|

Fuente: Base de datos de EMD (Fabricante software WindPRO)

Cabe destacar que, dado que la modelación de sombras modo invernadero para los receptores, el

efecto se sobreestima tanto en las horas diarias como en la cantidad anual de horas de sombra que

recibe un receptor. En la práctica, la proyección de sombras se verá reducida respecto de los valores

estimados como consecuencia de atenuaciones y que los valores serán medidos dentro de las

viviendas.

9

## 6. RESULTADOS

Los Resultados obtenidos en cada receptor se muestran en la Tabla 2 [2], las coordenadas se presentan

en UTM datum WSG84 (18H):

**Tabla 2. Datos modelación de Shadow flicker.**

|RECEPTOR|COORDENADAS UTM<br>DATUM WSG84 (18H)|Col3|ALTURA|MODO<br>ANÁLISIS|CASO PEOR|Col7|CASO REAL|
|---|---|---|---|---|---|---|---|
|**RECEPTOR**|**ESTE**|**NORTE**|**(MSNM)**|**(MSNM)**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|**HRS**<br>**SOMBRA**<br>**MAX POR**<br>**DÍA [h/día]**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|
|A|649476|5389900|101,9|Invernadero|0:00|0:00|0:00|
|B|649518|5389930|102|Invernadero|0:00|0:00|0:00|
|C|649518|5389900|102|Invernadero|0:00|0:00|0:00|
|D|649587|5389917|102,1|Invernadero|0:00|0:00|0:00|
|E|649555|5389985|101,5|Invernadero|0:00|0:00|0:00|
|F|649580|5390007|102,2|Invernadero|0:00|0:00|0:00|
|G|649599|5389985|103|Invernadero|0:00|0:00|0:00|
|H|649679|5389970|102,8|Invernadero|0:00|0:00|0:00|
|I|649703|5389957|103,7|Invernadero|0:00|0:00|0:00|
|J|649730|5389956|105,8|Invernadero|0:00|0:00|0:00|
|K|649793|5389947|105,8|Invernadero|0:00|0:00|0:00|
|L|649814|5389939|105,2|Invernadero|0:00|0:00|0:00|
|M|649821|5389895|103,1|Invernadero|0:00|0:00|0:00|
|N|649863|5389892|102,9|Invernadero|0:00|0:00|0:00|
|O|649884|5389890|102,8|Invernadero|0:00|0:00|0:00|
|P|649920|5389885|102,3|Invernadero|0:00|0:00|0:00|
|Q|649855|5389966|103,8|Invernadero|0:00|0:00|0:00|
|R|649957|5389936|103,5|Invernadero|0:00|0:00|0:00|
|S|649988|5389914|102,9|Invernadero|0:00|0:00|0:00|
|T|649913|5389843|103,5|Invernadero|0:00|0:00|0:00|
|U|649906|5389784|104,3|Invernadero|0:00|0:00|0:00|
|V|650158|5389809|104,4|Invernadero|0:00|0:00|0:00|
|W|650185|5389851|103,9|Invernadero|0:00|0:00|0:00|
|X|650200|5389905|104,3|Invernadero|0:00|0:00|0:00|
|Y|650229|5389889|105,6|Invernadero|0:00|0:00|0:00|
|Z|650239|5389444|104,3|Invernadero|7:37|0:17|1:00|

2 Los resultados de la modelación, se presentan en el Anexo 11-1 del presente documento.

10

|RECEPTOR|COORDENADAS UTM<br>DATUM WSG84 (18H)|Col3|ALTURA|MODO<br>ANÁLISIS|CASO PEOR|Col7|CASO REAL|
|---|---|---|---|---|---|---|---|
|**RECEPTOR**|**ESTE**|**NORTE**|**(MSNM)**|**(MSNM)**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|**HRS**<br>**SOMBRA**<br>**MAX POR**<br>**DÍA [h/día]**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|
|AA|650254|5389424|103,9|Invernadero|11:18|0:20|1:31|
|AB|650205|5389452|103,9|Invernadero|4:09|0:12|0:32|
|AC|650223|5389334|102,2|Invernadero|21:24|0:25|3:00|
|AD|650263|5389274|103,1|Invernadero|18:52|0:21|2:46|
|AE|650367|5389162|102,8|Invernadero|9:53|0:22|1:35|
|AF|650403|5389093|100,7|Invernadero|8:07|0:21|1:22|
|AG|650641|5389069|88,3|Invernadero|0:00|0:00|0:00|
|AH|650661|5389051|85,5|Invernadero|0:00|0:00|0:00|
|AI|650615|5388954|95|Invernadero|0:00|0:00|0:00|
|AJ|650576|5388980|95,9|Invernadero|0:00|0:00|0:00|
|AK|650546|5388959|96,8|Invernadero|7:02|0:21|1:13|
|AL|650417|5388890|102,9|Invernadero|8:04|0:22|1:24|
|AM|650405|5388853|102,5|Invernadero|8:13|0:23|1:25|
|AN|650375|5388552|108,1|Invernadero|7:44|0:23|1:07|
|AO|649750|5389272|109|Invernadero|8:03|0:20|1:18|
|AP|649814|5389288|112,6|Invernadero|0:00|0:00|0:00|
|AQ|649923|5389284|110,1|Invernadero|8:55|0:20|1:10|
|AR|649943|5389270|108,9|Invernadero|13:55|0:25|1:52|
|AS|649987|5389169|116,7|Invernadero|0:00:00|0:00|0:00|
|AT|649946|5389140|115,2|Invernadero|0:00:00|0:00|0:00|
|AU|649948|5389100|118,1|Invernadero|0:00:00|0:00|0:00|
|AV|650037|5389035|126,6|Invernadero|16:23|0:29|2:40|
|AW|649987|5389026|124,7|Invernadero|18:41|0:30|3:02|
|AX|649977|5388990|123,3|Invernadero|18:16|0:29|3:02|
|AY|649954|5388978|120,7|Invernadero|19:19|0:29|3:13|
|AZ|649915|5389054|116,1|Invernadero|27:17:00|0:29|4:16|
|BA|649748|5389120|107,6|Invernadero|29:35:00|0:28|4:08|
|BB|649750|5389064|109|Invernadero|0:00:00|0:00|0:00|
|BC|649786|5388979|112,7|Invernadero|0:00:00|0:00|0:00|
|BD|649870|5388746|116,3|Invernadero|22:02|0:27|3:40|
|BE|649857|5388735|116,1|Invernadero|22:16|0:25|3:41|
|BF|649846|5388806|114,3|Invernadero|25:43:00|0:25|4:24|
|BG|649926|5388843|118,8|Invernadero|18:02|0:25|3:09|
|BH|649917|5388830|118,1|Invernadero|18:14|0:27|3:11|

11

|RECEPTOR|COORDENADAS UTM<br>DATUM WSG84 (18H)|Col3|ALTURA|MODO<br>ANÁLISIS|CASO PEOR|Col7|CASO REAL|
|---|---|---|---|---|---|---|---|
|**RECEPTOR**|**ESTE**|**NORTE**|**(MSNM)**|**(MSNM)**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|**HRS**<br>**SOMBRA**<br>**MAX POR**<br>**DÍA [h/día]**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|
|BI|649963|5388836|119|Invernadero|16:30|0:25|2:53|
|BJ|650059|5388802|121,5|Invernadero|13:13|0:29|2:16|
|BK|649923|5388776|117,8|Invernadero|17:21|0:29|2:58|
|BL|649948|5388771|118,1|Invernadero|16:24|0:28|2:47|
|BM|649968|5388760|118,8|Invernadero|15:42|0:29|2:38|
|BN|649946|5388736|117,2|Invernadero|16:21|0:28|2:42|
|BO|650021|5388701|121,4|Invernadero|13:30|0:29|2:08|
|BP|649881|5388637|114,8|Invernadero|18:40|0:28|2:50|
|BQ|649890|5388615|113,2|Invernadero|17:39|0:24|2:39|
|BR|649831|5388578|113,6|Invernadero|19:57|0:21|2:56|
|BS|649907|5388571|112|Invernadero|16:54|0:23|2:28|
|BT|649962|5388648|117,5|Invernadero|15:19|0:26|2:20|
|BU|650005|5388661|120|Invernadero|14:03|0:30|2:09|
|BV|650046|5388631|119,5|Invernadero|12:51|0:29|1:56|
|BW|650040|5388592|117,3|Invernadero|13:02|0:29|1:55|
|BX|649977|5388307|119|Invernadero|14:14|0:29|1:41|
|BY|649994|5388274|119,9|Invernadero|13:33|0:29|1:33|
|BZ|649967|5388247|119,6|Invernadero|14:34|0:30|1:37|
|CA|649974|5388228|119,9|Invernadero|14:15|0:29|1:34|
|CB|649932|5388234|120,4|Invernadero|15:25|0:30|1:41|
|CC|650013|5388250|120,6|Invernadero|13:08|0:28|1:29|
|CD|650037|5388214|121,1|Invernadero|12:31|0:27|1:23|
|CE|650096|5388279|121|Invernadero|11:13|0:26|1:19|
|CF|650169|5388231|121,3|Invernadero|9:48|0:25|1:08|
|CG|650127|5388214|124,5|Invernadero|10:21|0:26|1:10|
|CH|650130|5388189|126,1|Invernadero|10:10|0:25|1:07|
|CI|650117|5388157|126,8|Invernadero|10:31|0:25|1:07|
|CJ|650125|5388171|126,7|Invernadero|10:16|0:25|1:07|
|CK|650159|5388158|124,7|Invernadero|9:54|0:25|1:04|
|CL|650145|5388136|124,8|Invernadero|10:06|0:25|1:04|
|CM|650156|5388094|121,4|Invernadero|10:06|0:25|1:04|
|CN|650137|5388120|123,9|Invernadero|10:19|0:25|1:05|
|CO|650286|5388119|111,1|Invernadero|0:40|0:04|0:04|
|CP|650168|5388108|122|Invernadero|9:49|0:25|1:02|

12

|RECEPTOR|COORDENADAS UTM<br>DATUM WSG84 (18H)|Col3|ALTURA|MODO<br>ANÁLISIS|CASO PEOR|Col7|CASO REAL|
|---|---|---|---|---|---|---|---|
|**RECEPTOR**|**ESTE**|**NORTE**|**(MSNM)**|**(MSNM)**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|**HRS**<br>**SOMBRA**<br>**MAX POR**<br>**DÍA [h/día]**|**HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]**|
|CQ|650233|5388073|122,2|Invernadero|8:47|0:23|0:56|
|CR|650138|5388080|123,6|Invernadero|10:27|0:25|1:05|
|CS|650151|5388066|124,3|Invernadero|10:06|0:24|1:03|
|CT|650174|5387999|127,5|Invernadero|9:43|0:23|0:58|
|CU|649940|5388169|120,6|Invernadero|15:23|0:30|1:36|
|CV|650046|5388175|121,9|Invernadero|12:19|0:27|1:19|
|CW|650001|5388164|122,7|Invernadero|13:31|0:28|1:25|
|CX|649976|5388147|122,9|Invernadero|14:17|0:28|1:29|
|CY|649998|5388058|124,9|Invernadero|13:58|0:28|1:22|
|CZ|649974|5388019|124,2|Invernadero|15:18|0:28|1:27|
|DA|650018|5387990|120,9|Invernadero|14:20|0:27|1:21|
|DB|650155|5387939|128,3|Invernadero|10:19|0:23|0:58|
|DC|650166|5387918|125,8|Invernadero|10:23|0:23|0:58|
|DD|650148|5387906|125,8|Invernadero|10:56|0:23|1:00|
|DE|648410|5388407|109,7|Invernadero|0:00|0:00|0:00|
|DF|649969|5387107|119,6|Invernadero|0:00|0:00|0:00|

Fuente: Elaboración propia Software WindPRO Anexo 11 .

## 7. CONCLUSIONES

A partir de los antecedentes entregados por el mandante acerca de las características del Proyecto,

en tanto a la ubicación de los aerogeneradores, altura de buje y diámetro del rotor, ubicación de

potenciales receptores de sombra a 2 km de cada aerogenerador y las condiciones ambientales y

meteorológicas de la zona, se concluye que el efecto sombra modelado para el proyecto **PMGD**

**Eólico Chara**, no producirá riesgo para la salud de la población, ni tampoco significará un impacto

adverso significativo sobre la comunidad circundante al proyecto.

Los resultados reflejados en la modelación del peor escenario y caso real demandado por la norma

alemana indican valores resultantes menores a los límites establecidos por dicha normativa, por lo

que se descarta la incorporación adicional de medidas de control de sombra en los aerogeneradores.

13

## 8. BIBLIOGRAFÍA

Hinweise zur Ermittiung und Beurteilung der optischen Inmissionen von Windenergieanlagen (WEA
Schattenwurf-Hinweise, 2002) o “Indicaciones relativas a la investigación y evaluación de las

emisiones ópticas de instalaciones de energía eólica.

14

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Promedio de horas diarias de sol Estación Meteorológica Puerto Montt.****

| MES | PROMEDIO DE HORAS DIARIAS DE SOL |
| --- | --- |
| Enero | 6.32 |
| Febrero | 6.58 |
| Marzo | 4.55 |
| Abril | 3.17 |
| Mayo | 2.40 |
| Junio | 1.73 |
| Julio | 2.63 |
| Agosto | 3.00 |
| Septiembre | 4.15 |
| Octubre | 5.40 |
| Noviembre | 5.72 |
| Diciembre | 5.52 |

**Tabla 2.: Datos modelación de Shadow flicker.****

| RECEPTOR | COORDENADAS UTM<br>DATUM WSG84 (18H) | Col3 | ALTURA | MODO<br>ANÁLISIS | CASO PEOR | Col7 | CASO REAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **RECEPTOR** | **ESTE** | **NORTE** | **(MSNM)** | **(MSNM)** | **HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]** | **HRS**<br>**SOMBRA**<br>**MAX POR**<br>**DÍA [h/día]** | **HRS**<br>**SOMBRA**<br>**AL AÑO**<br>**[h/año]** |
| A | 649476 | 5389900 | 101,9 | Invernadero | 0:00 | 0:00 | 0:00 |
| B | 649518 | 5389930 | 102 | Invernadero | 0:00 | 0:00 | 0:00 |
| C | 649518 | 5389900 | 102 | Invernadero | 0:00 | 0:00 | 0:00 |
| D | 649587 | 5389917 | 102,1 | Invernadero | 0:00 | 0:00 | 0:00 |
| E | 649555 | 5389985 | 101,5 | Invernadero | 0:00 | 0:00 | 0:00 |
| F | 649580 | 5390007 | 102,2 | Invernadero | 0:00 | 0:00 | 0:00 |
| G | 649599 | 5389985 | 103 | Invernadero | 0:00 | 0:00 | 0:00 |
| H | 649679 | 5389970 | 102,8 | Invernadero | 0:00 | 0:00 | 0:00 |
| I | 649703 | 5389957 | 103,7 | Invernadero | 0:00 | 0:00 | 0:00 |
| J | 649730 | 5389956 | 105,8 | Invernadero | 0:00 | 0:00 | 0:00 |
| K | 649793 | 5389947 | 105,8 | Invernadero | 0:00 | 0:00 | 0:00 |
| L | 649814 | 5389939 | 105,2 | Invernadero | 0:00 | 0:00 | 0:00 |
| M | 649821 | 5389895 | 103,1 | Invernadero | 0:00 | 0:00 | 0:00 |
| N | 649863 | 5389892 | 102,9 | Invernadero | 0:00 | 0:00 | 0:00 |
| O | 649884 | 5389890 | 102,8 | Invernadero | 0:00 | 0:00 | 0:00 |
| P | 649920 | 5389885 | 102,3 | Invernadero | 0:00 | 0:00 | 0:00 |
| Q | 649855 | 5389966 | 103,8 | Invernadero | 0:00 | 0:00 | 0:00 |
| R | 649957 | 5389936 | 103,5 | Invernadero | 0:00 | 0:00 | 0:00 |
| S | 649988 | 5389914 | 102,9 | Invernadero | 0:00 | 0:00 | 0:00 |
| T | 649913 | 5389843 | 103,5 | Invernadero | 0:00 | 0:00 | 0:00 |
| U | 649906 | 5389784 | 104,3 | Invernadero | 0:00 | 0:00 | 0:00 |
| V | 650158 | 5389809 | 104,4 | Invernadero | 0:00 | 0:00 | 0:00 |
| W | 650185 | 5389851 | 103,9 | Invernadero | 0:00 | 0:00 | 0:00 |
| X | 650200 | 5389905 | 104,3 | Invernadero | 0:00 | 0:00 | 0:00 |
| Y | 650229 | 5389889 | 105,6 | Invernadero | 0:00 | 0:00 | 0:00 |
| Z | 650239 | 5389444 | 104,3 | Invernadero | 7:37 | 0:17 | 1:00 |
