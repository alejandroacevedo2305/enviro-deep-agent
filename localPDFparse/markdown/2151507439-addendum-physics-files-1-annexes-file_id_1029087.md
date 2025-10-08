---
title: Sin título
author: Nicolas Martinez
date: D:20210924120641-03'00'
language: es
type: report
pages: 43
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIOS BÁSICOS MINICENTRAL EL PORTAL EJE HIDRÁULICO Eje Hidráulico Canal Matriz MEMORIA DE CÁLCULO HIDRÁULICA
-->

# ESTUDIOS BÁSICOS MINICENTRAL EL PORTAL EJE HIDRÁULICO Eje Hidráulico Canal Matriz MEMORIA DE CÁLCULO HIDRÁULICA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|14/09/2021|Coordinación Interna|JH|HRJ|ATR||
|_Versión_|_Fecha_|_Emitido para_|_Preparó_|_Revisó_|_Aprobado_<br>**HLT**|_Aprobado_<br>**Cliente**|
|_No del proyecto:_<br>**126 **|_No del proyecto:_<br>**126 **|_No del documento:_<br>**126-EB-00-HID-MCA-01**|_No del documento:_<br>**126-EB-00-HID-MCA-01**|_No del documento:_<br>**126-EB-00-HID-MCA-01**|_No del documento:_<br>**126-EB-00-HID-MCA-01**|_Revisión:_<br>**A**|

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**INDICE**

**ITEM** **CONTENIDO**

**PAGINA**

1. INTRODUCCIÓN ........................................................................................... 1

2. OBJETIVOS .................................................................................................... 4

3. ANTECEDENTES .......................................................................................... 4

4. DESCRIPCIÓN MODELO HIDRÁULICO ..................................................... 5

4.1 GENERALIDADES ........................................................................................ 5

4.2 DESCRIPCIÓN MODELO HEC-RAS ............................................................ 5

4.3 COEFICIENTE DE RUGOSIDAD .................................................................. 6

4.4 Caudal de Diseño ............................................................................................. 8

4.5 Condiciones de Borde ...................................................................................... 8

5. RESULTADOS EJES HIDRÁULICOS ......................................................... 10

5.1 Situación Sin Proyecto ................................................................................... 11

5.2 Situación Con Proyecto .................................................................................. 15

5.3 Comparación de los ejes hidráulcios obtenidos............................................... 19

6. CONCLUSIONES ......................................................................................... 25

**Anexo 1: Levantamiento Topográfico**

**Anexo 2: Eje Hidráulico Sin Proyecto**

**Anexo 3: Eje Hidráulico Con Proyecto**

126-EB-00-HID-MCA-01 **i**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**1.** **INTRODUCCIÓN**

La empresa El Atajo SpA se encuentra desarrollando el proyecto “Minicentral El Portal”,
ubicada en el sector denominado Pile, el cual se emplaza en la comuna de Mulchén, provincia
y Región del Biobío.

El proyecto consiste en aprovechar la descarga que se realiza desde el canal Biobío Sur, hacia
el canal Licura-Munilque, aprovechando un desnivel existente entre este punto y el sector de
compuertas y derivados ubicado unos 790 m aguas abajo. En la siguiente Figura se presenta un
esquema de lo descrito previamente, mientras que en el Anexo 1 se presenta el plano del
levantamiento topográfico realizado

126-EB-00-HID-MCA-01 **1**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

Zona de Compuertas
derivados

126-EB-00-HID-MCA-01 **2**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Figura 1.1 Disposición General de las Obras Existentes**

126-EB-00-HID-MCA-01 **3**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

En el marco de la Declaración de Impacto Ambiental, se ha solicitado aclarar si el proyecto
tendrá efectos sobre las condiciones de escurrimiento aguas abajo de la descarga de la central al
canal y aguas debajo de la bocatoma, en particular si esta modificación impactará en los puentes
públicos ubicados a unos 850 y 1600 [m] aguas abajo de las compuertas de regulación y 250

[m] aguas abajo de la bocatoma. En la siguiente Figura se presenta una ubicación general de las
obras y de los puentes existentes.

**Figura 1.2 Ubicación Puentes Públicos Existentes**

**2.** **OBJETIVOS**

El presente informe tiene como objetivo demostrar que la implantación de la central no tiene
efectos hidráulicos significativos hacia aguas abajo de la descarga y bocatoma, descartando
cualquier efecto de socavación retrograda sobre los pilares y/o estribitos del puente.

**3.** **ANTECEDENTES**

Para la realización de esta memoria se han tenido en consideración los siguientes antecedentes:

**Tabla 3.1 Antecedentes Disponibles**

|Ref|Titulo|Autor|
|---|---|---|
|1|Hidráulica|Francisco Domínguez|
|2|Levantamiento Topográfico escala 1:500|Quarzo Ingeniería|
|3|Layout de Proyecto|EIC Ingenieros|

126-EB-00-HID-MCA-01 **4**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**4.** **DESCRIPCIÓN MODELO HIDRÁULICO**

En el presente capítulo se describe la metodología de cálculo utilizada en el estudio hidráulico
del canal existente, que se realiza utilizando el software HEC-RAS 5.0.7, específicamente para
el caudal de diseño del canal, así como también considerando un caudal 15 y 20 % superior al
de diseño.

Para entregar un antecedente comparativo referente a la afección de las obras proyectadas sobre
el canal, se desarrollan simulaciones hidráulicas y presentan resultados para la situación actual
y un escenario con proyecto.

Para el modelo de la bocatoma, se uso el software Hcanales 3.0, así modelar la situación con y
sin proyecto.

**4.1** **GENERALIDADES**

El estudio hidráulico tiene por objetivo principal determinar los niveles de escurrimiento
máximos asociados a los caudales de crecidas antes mencionados, tanto para la situación natural
del cauce como considerando la modificación de este.

Para estudiar el eje hidráulico de un cauce se requiere del desarrollo de un modelo geométrico,
sobre el cual se posteriormente se desarrolla el análisis hidráulico respectivo. En el presente
estudio el análisis hidráulico se realiza en el software HEC-RAS 5.0.7.

El modelo geométrico de cada quebrada fue elaborado utilizando los antecedentes topográficos
disponibles, obteniendo perfiles transversales georreferenciados a base de un modelo de terreno
para ser trabajados en HEC-RAS.

Como metodología de cálculo Hec-Ras utiliza, básicamente, el balance de energía entre dos
secciones sucesivas, empleando como bases de cálculo las secciones transversales, que
representan la geometría del cauce en el tramo de interés, el caudal y el coeficiente de rugosidad.
Como resultado, en el software pueden obtenerse, para cada sección transversal, los niveles de
agua y parámetros hidráulicos tales como velocidad media del flujo, alturas máximas, radio
hidráulico, número de Froude, alturas críticas, etc.

Primeramente, se presenta una descripción general del modelo HEC-RAS, para luego ahondar
en los resultados y comparaciones de los escenarios con y sin proyecto.

Para la bocatoma, se desarrolla un modelo donde se verifica el nivel de agua y velocidades
adquiridas para la situación con y sin proyecto.

**4.2** **DESCRIPCIÓN MODELO**

El modelo hidráulico del canal Liucura-Munilque tiene una longitud aproximada de 797 [m], y
se han obtenido perfiles transversales cada 20 [m] tal como se presenta en la siguiente Figura:

126-EB-00-HID-MCA-01 **5**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Figura 4.1: Planta perfiles transversales modelo hidráulico**

Para el modelo de la bocatoma, obtuvieron los parámetros de los levantamientos realizados
en el canal mtriz donde arrojan que el canal tiene una pendiente del 1:5000 y un talud de
H:V 1:1

**4.3** **COEFICIENTE DE RUGOSIDAD**

Para definir el coeficiente de rugosidad de Manning se ha considerado el canal excavado en
tierra con algún grado de vegetación, el cual según la literatura varía entre 0,035 y 0,060 [m/s [1/3] ],
adoptando un valor medio de 0,042 [m/s [1/3] ]. Mientras que para las planicies de inundación se
consideró un valor de 0,052 [m/s [1/3] ]. En la siguiente imagen se puede apreciar un tramo típico
del canal:

126-EB-00-HID-MCA-01 **6**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Figura 4.2 Sección del Canal Aguas debajo de la Captación (perfil 680 aprox)**

Para la bocatoma, se asume un Manning de 0,028 dado que es un terreno natural en tierra con
poca vegetación.

**Figura 4.3 Sección del Canal Aguas debajo de la Captación (perfil 680 aprox)**

126-EB-00-HID-MCA-01 **7**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**4.4** **Caudal de Diseño**

Para las condiciones de borde se debe diferenciar las asumidas para la condición sin y con
proyecto, puesto que, para la primera, el caudal de entrada corresponde a la toma del canal
Biobío Sur (perfil 796.57), mientras que para la segunda se asume que el caudal de entrada
proviene del canal de descarga de la central (perfil 120). No obstante, para la condición con
proyecto se ha considerado que en la obra de toma (canal Biobío Sur), se dejará pasar un caudal
de 100 [l/s] para conservación ambiental.

Considerando que el caudal de diseño de la central corresponde al mismo caudal de diseño del
canal existente, es decir 10 [m3/s], se ha considerado como verificación las condiciones de 11,5
y 12 [m3/s] (15 y 20% por sobre el de diseño).

**4.5** **Condiciones de Borde**

Como condición de borde, se ha considerado que en la toma del existente se produce
escurrimiento crítico (condición de aguas arriba). Mientras que por aguas abajo se ha
considerado el efecto que tiene el vertedero existente en la obra de regulación y compuertas.

En efecto, tal como se aprecia en las siguientes figuras, existe un vertedero y un conjunto de
compuertas que distribuyen las aguas a los canales Liucura Muninque y Canal de Entrega:

**Figura 4.4 Detalle Obras de Regulación**

126-EB-00-HID-MCA-01 **8**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Figura 4.5 Vertedero Existente**

**Figura 4.6 Compuertas de Regulación Existentes.**

126-EB-00-HID-MCA-01 **9**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

En consecuencia, con lo anteriormente descrito, y asumiendo un criterio conservador, se ha
considerado como condición de borde de aguas abajo, el nivel de aguas igual a la cota del
vertedero existente (221 [msnm]), más la carga sobre este, es decir considerando que las
compuertas se mantienen cerradas.

Para determinar la carga sobre vertedero se consideró la siguiente ecuación:

Q= mLh ~~√~~ 2gh

En que:

Q Caudal que pasa por el vertedero [m3/s]

m Coeficiente de gasto del vertedero (=0,4)

L Longitud del vertedero (15 [m])

h Carga sobre el vertedero [m]

g aceleración de gravedad (9,81 [m/s2]

De esta forma se tiene los siguientes niveles de agua como condición de borde:

**Tabla 4.1 Condición de Borde de Aguas Abajo (Carga sobre el Vertedero)**

|Variable|Qd|Qd+15%|Qd+20%|Unidad|Descripción|
|---|---|---|---|---|---|
|L|15|15|15|[m]|Longitud Vertedero|
|m|0,4|0,4|0,4|[-]|Coeficiente de Gasto|
|h|0,52|0,57|0,59|[m]|Carga sobre el Vertedero|
|Q|10,0|11,5|12,0|[m3/s]|Caudal|
|Z|221,52|221,57|221,59|[msnm[]|Condición de Borde|

**5.** **RESULTADOS EJES HIDRÁULICOS**

En adelante en el presente documento, los cuadros de resultados provenientes del modelo
hidráulico contienen parámetros abreviados de acuerdo con la siguiente nomenclatura:

km : Distancia acumulada según eje [m].

Q Total : Caudal total [m [3] /s].

Z Fondo : Cota de Fondo [m].

ZH : Cota eje hidráulico [m].

ZB : Cota Línea de energía [m].

ZHc : Cota crítica de escurrimiento [m].

126-EB-00-HID-MCA-01 **10**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

V : Velocidad media de escurrimiento [m/s].

J : Gradiente Hidráulico [m/m].

A : Área del flujo [m [2] ].

T : Ancho superficial del escurrimiento [m].

Fr : No de Froude [-].

**5.1** **Situación Sin Proyecto**

En la siguiente Tabla se presenta los resultados para la condición Sin Proyecto, considerando el
caudal de diseño:

**Tabla 5.1 Resultados Situación Sin Proyectos. Q diseño = 10 [m3/s]**

|Perfiles|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|796,57|10,0|230,37|231,42|231,12|231,61|0,00976|1,92|5,20|4,98|0,60|
|790|10,0|230,25|231,39|231,00|231,53|0,00640|1,66|6,01|5,61|0,51|
|780|10,0|229,97|231,36|230,78|231,45|0,00382|1,38|7,27|6,30|0,41|
|770|10,0|229,94|231,19|230,65|231,29|0,00408|1,41|7,09|6,31|0,42|
|760|10,0|229,79|230,46|230,62|231,04|0,05566|3,37|2,97|5,59|1,48|
|750|10,0|229,59|230,53|230,34|230,74|0,01107|2,01|4,97|5,84|0,70|
|740|10,0|229,43|230,34|230,17|230,56|0,01166|2,05|4,89|5,88|0,72|
|730|10,0|229,26|229,93|229,99|230,34|0,03150|2,84|3,52|5,66|1,15|
|720|10,0|229,08|229,74|229,81|230,16|0,03336|2,89|3,47|5,64|1,18|
|710|10,0|228,76|229,90|229,38|229,91|0,00102|0,57|17,54|26,16|0,22|
|700|10,0|228,18|229,90|229,22|229,90|0,00033|0,37|26,68|31,54|0,13|
|690|10,0|229,05|229,87|229,41|229,90|0,00114|0,64|15,55|21,05|0,24|
|680|10,0|228,96|229,70|229,66|229,84|0,02010|1,65|6,05|16,71|0,88|
|670|10,0|228,79|229,42|229,42|229,59|0,02535|1,82|5,49|16,04|0,99|
|660|10,0|228,54|229,26|229,06|229,36|0,00722|1,43|7,04|13,19|0,58|
|650|10,0|228,32|228,99|228,86|229,13|0,01074|1,64|6,10|10,75|0,69|
|640|10,0|228,24|228,88|228,77|229,01|0,01149|1,58|6,33|12,57|0,71|
|630|10,0|227,77|228,62|228,42|228,76|0,00870|1,67|5,98|8,21|0,63|
|620|10,0|227,50|228,56|228,19|228,69|0,00576|1,56|6,40|6,55|0,51|
|610|10,0|227,28|228,43|228,14|228,58|0,00807|1,74|5,75|6,29|0,58|
|600|10,0|226,43|228,40|227,79|228,51|0,00447|1,46|6,85|5,32|0,41|
|590|10,0|226,63|228,40|227,62|228,46|0,00227|1,14|8,79|6,91|0,31|

126-EB-00-HID-MCA-01 **11**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfiles|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|580|10,0|226,88|228,40|227,64|228,44|0,00137|0,88|12,47|25,57|0,26|
|570|10,0|227,42|228,35|228,01|228,41|0,00415|1,13|8,90|15,80|0,44|
|560|10,0|227,27|228,22|227,97|228,30|0,00528|1,22|8,49|17,19|0,50|
|550|10,0|226,93|228,19|227,82|228,24|0,00406|1,01|9,89|17,28|0,43|
|540|10,0|227,11|228,10|227,90|228,18|0,00860|1,31|7,63|16,27|0,61|
|530|10,0|227,01|227,58|227,68|227,95|0,04183|2,68|3,72|8,85|1,32|
|520|10,0|227,03|227,69|227,52|227,79|0,00802|1,41|7,08|12,77|0,61|
|510|10,0|226,98|227,56|227,44|227,68|0,01011|1,48|6,76|13,59|0,67|
|500|10,0|226,70|227,47|227,29|227,57|0,00763|1,39|7,20|12,78|0,59|
|490|10,0|226,32|227,41|227,14|227,50|0,00533|1,28|7,82|11,66|0,50|
|480|10,0|226,36|227,28|227,15|227,42|0,01162|1,65|6,12|13,27|0,71|
|470|10,0|226,41|227,21|227,02|227,30|0,00808|1,29|7,74|15,64|0,59|
|460|10,0|226,33|227,20|226,84|227,23|0,00291|0,86|11,63|20,45|0,36|
|450|10,0|226,20|227,15|226,68|227,19|0,00168|0,80|12,67|19,09|0,29|
|440|10,0|226,03|227,13|226,59|227,17|0,00203|0,93|11,56|18,22|0,32|
|430|10,0|225,97|227,10|226,69|227,15|0,00225|0,89|11,48|21,49|0,33|
|420|10,0|226,17|226,81|226,72|226,94|0,01344|1,58|6,32|13,85|0,75|
|410|10,0|225,91|226,57|226,57|226,78|0,02488|2,03|4,93|11,82|1,00|
|400|10,0|225,59|226,55|226,22|226,61|0,00373|1,09|9,15|13,25|0,42|
|390|10,0|225,32|226,55|225,89|226,58|0,00130|0,80|12,54|12,99|0,26|
|380|10,0|225,07|226,52|225,72|226,56|0,00140|0,88|12,04|15,76|0,27|
|370|10,0|225,42|226,49|226,11|226,54|0,00274|0,99|10,86|17,52|0,37|
|360|10,0|225,43|226,48|226,05|226,51|0,00185|0,79|13,66|21,72|0,30|
|350|10,0|225,74|226,40|226,12|226,44|0,00340|0,91|11,79|27,13|0,40|
|340|10,0|225,02|226,33|225,64|226,35|0,00114|0,68|15,13|20,53|0,24|
|330|10,0|224,96|226,29|225,77|226,33|0,00199|0,90|11,92|17,71|0,31|
|320|10,0|225,59|226,09|226,09|226,27|0,02348|1,86|5,55|16,67|0,98|
|310|10,0|225,08|226,09|225,65|226,12|0,00169|0,78|12,82|17,38|0,29|
|300|10,0|225,14|226,07|225,62|226,10|0,00166|0,77|13,53|22,47|0,29|
|290|10,0|225,19|225,81|225,70|225,93|0,01194|1,55|6,45|13,62|0,72|
|280|10,0|224,89|225,70|225,55|225,81|0,00985|1,51|6,63|12,35|0,66|
|270|10,0|224,67|225,71|225,15|225,75|0,00173|0,88|11,35|12,19|0,29|
|260|10,0|224,60|225,68|225,15|225,73|0,00194|0,92|10,85|12,55|0,31|
|250|10,0|224,59|225,05|225,17|225,48|0,06980|2,90|3,45|10,63|1,63|

126-EB-00-HID-MCA-01 **12**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfiles|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|240|10,0|224,38|225,30|224,91|225,36|0,00342|1,14|8,79|11,06|0,41|
|230|10,0|224,15|225,27|224,80|225,33|0,00263|1,06|9,41|10,70|0,36|
|220|10,0|224,11|225,25|224,71|225,30|0,00199|0,93|10,72|13,29|0,32|
|210|10,0|224,13|225,03|224,64|225,10|0,00343|1,12|8,93|11,47|0,41|
|200|10,0|223,80|225,01|224,53|225,06|0,00239|1,00|10,03|13,42|0,34|
|190|10,0|223,84|224,98|224,63|225,04|0,00328|1,05|9,74|17,83|0,40|
|180|10,0|223,93|224,93|224,65|225,00|0,00453|1,10|9,13|15,73|0,46|
|170|10,0|224,00|224,87|224,63|224,94|0,00564|1,22|8,22|13,67|0,50|
|160|10,0|224,00|224,83|224,48|224,89|0,00328|1,06|9,40|12,98|0,40|
|150|10,0|223,86|224,71|224,29|224,76|0,00265|1,00|10,04|12,98|0,36|
|140|10,0|223,77|224,69|224,25|224,73|0,00230|0,93|10,70|14,13|0,34|
|130|10,0|223,74|224,66|224,29|224,70|0,00261|0,93|10,80|15,68|0,36|
|120|10,0|223,67|224,66|224,15|224,68|0,00084|0,56|18,30|35,99|0,21|
|110|10,0|223,78|224,64|224,25|224,67|0,00165|0,72|13,93|22,05|0,28|
|100|10,0|223,71|224,52|224,35|224,63|0,00824|1,45|6,89|12,01|0,61|
|90|10,0|223,59|224,32|224,25|224,49|0,01532|1,83|5,46|10,80|0,82|
|80|10,0|223,42|224,13|224,13|224,34|0,02397|2,02|4,95|11,86|1,00|
|70|10,0|223,02|223,97|223,63|224,06|0,00499|1,28|7,83|11,18|0,49|
|60|10,0|222,62|223,97|223,32|224,01|0,00209|0,96|12,03|29,71|0,32|
|50|10,0|222,27|223,97|223,18|223,99|0,00135|0,72|19,25|44,46|0,26|
|40|10,0|222,56|223,97|223,29|223,97|0,00044|0,44|30,12|51,09|0,15|
|30|10,0|222,41|223,75|223,23|223,76|0,00187|0,56|18,04|44,70|0,27|
|20|10,0|221,70|222,42|222,62|223,03|0,08594|3,47|2,88|7,97|1,85|
|10|10,0|220,93|222,02|222,13|222,47|0,04408|2,97|3,36|6,17|1,29|
|0|10,0|220,67|221,52|221,12|221,54|0,00141|0,60|16,61|27,93|0,25|

En la siguiente figura se presenta un perfil longitudinal para la condición antes presentada:

126-EB-00-HID-MCA-01 **13**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

232

230

228

226

224

222

El Portal Plan: Sin Proyecto 13-10-2020

220

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Legend|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||EG PF 1<br>WS PF 1<br>Ground<br>Left Levee<br>Right Levee|
||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||
|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*||00*|00*|00*|00*|00*|00*<br>00*|00*||00*|00*|00*<br>00*|00*<br>00*|00*<br>00*<br>00*|00*<br>00*<br>00*|00*<br>00*|00*<br>00*|00*|00*<br>00*<br>|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*|00*|00*|00*|00*||00*|00*<br>00*|00*<br>00*<br>00*<br>00*<br>00*|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>|0*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>64*|00*<br>00*<br>00*<br>00*<br>00*<br>00*<br>64*|
|48.0<br>54.0<br>60<br>66.0<br>72.0<br>78.0<br>84.0<br>90<br>96.0<br>102.<br>108.<br>114.|120|126.|132.|138.|144.|150<br>156.|162.<br>168.|174.|180|186.|192.|198.<br>204.<br>210|216.<br>222.|228.<br>234.<br>240<br>246.|252.<br>258.<br>264.|270<br>276.<br>282.|288.<br>294.<br>300|306.|312.<br>318.<br>|324.<br>330<br>336.<br>342.<br>348.<br>354.<br>360<br>366.<br>372.<br>378.<br>384.<br>390|396.<br>402.<br>408.<br>414.<br>420<br>426.<br>432.<br>438.<br>444.|450<br>456.|462.|468.|474.|480|486.|492.<br>498.|504.<br>510<br>516.<br>522.<br>528.<br>534.<br>540|546.<br>552.<br>558.<br>564.<br>570<br>576.<br>582.<br>588.<br>594.<br>600<br>|606.<br>612.<br>618.<br>624.<br>630<br>636.<br>642.<br>648.<br>654.<br>660<br>666.|672.<br>678.<br>684.<br>690<br>696.<br>702.<br>708.<br>714.<br>720<br>726.<br>732.<br>738.<br>|744.<br>750<br>756.<br>762.<br>768.<br>774.<br>780<br>786.<br>791.|744.<br>750<br>756.<br>762.<br>768.<br>774.<br>780<br>786.<br>791.|

0 200 400 600 800

Main Channel Distance (m)

**Figura 5.1 Eje Hidráulico Canal. Situación Sin Proyecto. Qd = 10 [m3/s]**

126-EB-00-HID-MCA-01 **14**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

De los resultados anteriores se aprecia que el vertedero impone un nivel de aguas, que afecta los
últimos metros del canal, llegando a producir incluso un resalto hidráulico en la zona. En la
siguiente Figura se presenta un detalle del perfil hidráulico en su zona final:

**Figura 5.2 Detalle Eje Hidráulico.**

Los resultados de los otros caudales se presentan en el Anexo 2

**5.2** **Situación Con Proyecto**

Tal como se señaló anteriormente, para este caso se consideró un caudal de 100 [l/s] al inicio
del canal Liucura (entrega del caudal Biobio Sur) y la descarga de la central en el perfil 120
(Qd).

En la siguiente Tabla se presenta el eje hidráulico para esta condición, considerando el caudal
de diseño de 10 [m3/s]

126-EB-00-HID-MCA-01 **15**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Tabla 5.2 Resultados Situación Con Proyectos. Q diseño = 10 [m3/s]**

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|796,57|0,1|230,37|230,42|230,41|230,43|0,01313|0,38|0,26|4,95|0,53|
|790|0,1|230,25|230,33|230,32|230,34|0,01645|0,40|0,25|5,08|0,58|
|780|0,1|229,97|230,24|230,07|230,24|0,00024|0,11|0,91|5,24|0,08|
|770|0,1|229,94|230,09|229,98|230,09|0,00041|0,13|0,77|5,35|0,11|
|760|0,1|229,79|229,86|229,84|229,87|0,01763|0,52|0,19|2,77|0,63|
|750|0,1|229,59|229,66|229,63|229,67|0,00773|0,33|0,30|4,78|0,42|
|740|0,1|229,43|229,49|229,47|229,50|0,01304|0,39|0,26|4,75|0,53|
|730|0,1|229,26|229,31|229,29|229,32|0,01591|0,41|0,24|4,82|0,58|
|720|0,1|229,08|229,17|229,12|229,18|0,00289|0,24|0,42|5,05|0,27|
|710|0,1|228,76|229,17|228,87|229,17|0,00002|0,04|2,57|11,43|0,03|
|700|0,1|228,18|229,17|228,37|229,17|0,00001|0,02|5,10|25,76|0,01|
|690|0,1|229,05|229,17|229,08|229,17|0,00027|0,07|1,34|16,16|0,08|
|680|0,1|228,96|229,10|229,08|229,12|0,01745|0,54|0,19|2,53|0,64|
|670|0,1|228,79|228,92|228,91|228,94|0,02742|0,60|0,17|2,69|0,78|
|660|0,1|228,54|228,58|228,60|228,66|0,52628|1,25|0,08|4,14|2,86|
|650|0,1|228,32|228,42|228,39|228,42|0,00724|0,28|0,36|6,91|0,39|
|640|0,1|228,24|228,31|228,31|228,33|0,04391|0,57|0,17|4,43|0,93|
|630|0,1|227,77|227,84|227,85|227,88|0,09140|0,84|0,12|2,92|1,33|
|620|0,1|227,50|227,61|227,55|227,62|0,00163|0,19|0,52|5,77|0,20|
|610|0,1|227,28|227,60|227,49|227,60|0,00045|0,13|0,78|5,73|0,11|
|600|0,1|226,43|227,60|226,65|227,60|0,00001|0,04|2,78|4,73|0,02|
|590|0,1|226,63|227,60|226,75|227,60|0,00000|0,03|3,85|6,00|0,01|
|580|0,1|226,88|227,60|226,99|227,60|0,00000|0,02|4,07|8,60|0,01|
|570|0,1|227,42|227,60|227,55|227,60|0,01005|0,30|0,34|7,48|0,45|
|560|0,1|227,27|227,41|227,40|227,43|0,02769|0,67|0,15|2,13|0,80|
|550|0,1|226,93|227,31|227,06|227,31|0,00021|0,11|0,90|4,67|0,08|
|540|0,1|227,11|227,27|227,24|227,29|0,01329|0,51|0,19|2,36|0,57|
|530|0,1|227,01|227,16|227,09|227,16|0,00258|0,24|0,42|4,84|0,26|
|520|0,1|227,03|227,13|227,09|227,13|0,00427|0,21|0,47|9,43|0,30|
|510|0,1|226,98|227,07|227,06|227,07|0,01583|0,28|0,35|12,04|0,53|
|500|0,1|226,70|226,82|226,82|226,84|0,04149|0,61|0,17|3,72|0,92|
|490|0,1|226,32|226,60|226,44|226,60|0,00063|0,16|0,61|4,14|0,14|
|480|0,1|226,36|226,58|226,50|226,59|0,00357|0,31|0,32|2,91|0,30|
|470|0,1|226,41|226,53|226,50|226,54|0,00805|0,33|0,30|4,93|0,42|
|460|0,1|226,33|226,47|226,42|226,47|0,00529|0,24|0,42|8,00|0,34|
|450|0,1|226,20|226,34|226,27|226,34|0,00124|0,13|0,75|11,76|0,17|
|440|0,1|226,03|226,34|226,07|226,34|0,00003|0,05|2,18|9,39|0,03|
|430|0,1|225,97|226,34|226,12|226,34|0,00035|0,14|0,72|3,88|0,10|
|420|0,1|226,17|226,28|226,27|226,29|0,01817|0,44|0,22|4,21|0,61|
|410|0,1|225,91|226,02|226,02|226,04|0,03714|0,65|0,15|2,82|0,89|
|400|0,1|225,59|225,86|225,69|225,86|0,00028|0,10|0,97|7,34|0,09|
|390|0,1|225,32|225,86|225,40|225,86|0,00000|0,02|4,51|10,87|0,01|
|380|0,1|225,07|225,86|225,12|225,86|0,00000|0,02|5,26|7,77|0,01|
|370|0,1|225,42|225,86|225,51|225,86|0,00003|0,05|2,22|9,27|0,03|
|360|0,1|225,43|225,86|225,53|225,86|0,00002|0,04|2,67|13,21|0,03|

126-EB-00-HID-MCA-01 **16**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|350|0,1|225,74|225,81|225,77|225,81|0,00127|0,13|0,80|14,06|0,17|
|340|0,1|225,02|225,70|225,12|225,70|0,00000|0,02|5,85|13,10|0,01|
|330|0,1|224,96|225,70|225,08|225,70|0,00000|0,03|3,98|10,59|0,01|
|320|0,1|225,59|225,69|225,68|225,70|0,04368|0,45|0,22|8,30|0,87|
|310|0,1|225,08|225,32|225,17|225,32|0,00029|0,10|1,03|8,70|0,09|
|300|0,1|225,14|225,31|225,21|225,31|0,00047|0,11|0,95|10,23|0,11|
|290|0,1|225,19|225,27|225,25|225,28|0,02152|0,45|0,22|4,78|0,67|
|280|0,1|224,89|225,01|225,00|225,03|0,02472|0,56|0,18|2,98|0,73|
|270|0,1|224,67|224,83|224,73|224,83|0,00024|0,08|1,21|11,22|0,08|
|260|0,1|224,60|224,83|224,68|224,83|0,00015|0,07|1,37|10,63|0,07|
|250|0,1|224,59|224,70|224,68|224,71|0,01982|0,46|0,22|4,14|0,65|
|240|0,1|224,38|224,68|224,45|224,68|0,00002|0,04|2,33|10,15|0,03|
|230|0,1|224,15|224,68|224,22|224,68|0,00001|0,03|3,52|9,49|0,01|
|220|0,1|224,11|224,68|224,20|224,68|0,00000|0,02|4,41|10,42|0,01|
|210|0,1|224,13|224,68|224,19|224,68|0,00000|0,02|5,17|10,40|0,01|
|200|0,1|223,80|224,68|223,89|224,68|0,00000|0,02|6,36|10,70|0,01|
|190|0,1|223,84|224,68|223,97|224,68|0,00000|0,02|5,59|12,70|0,01|
|180|0,1|223,93|224,68|224,05|224,68|0,00000|0,02|5,54|13,24|0,01|
|170|0,1|224,00|224,68|224,13|224,68|0,00000|0,02|5,73|13,04|0,01|
|160|0,1|224,00|224,68|224,06|224,68|0,00000|0,01|7,46|12,67|0,01|
|150|0,1|223,86|224,68|223,88|224,68|0,00000|0,01|9,73|12,73|0,00|
|140|0,1|223,77|224,68|223,82|224,68|0,00000|0,01|10,65|14,08|0,00|
|130|0,1|223,74|224,68|223,83|224,68|0,00000|0,01|11,14|15,76|0,00|
|120|10,0|223,67|224,66|224,15|224,68|0,00084|0,56|18,30|35,99|0,21|
|110|10,0|223,78|224,64|224,25|224,67|0,00165|0,72|13,93|22,05|0,28|
|100|10,0|223,71|224,52|224,35|224,63|0,00824|1,45|6,89|12,01|0,61|
|90|10,0|223,59|224,32|224,25|224,49|0,01532|1,83|5,46|10,80|0,82|
|80|10,0|223,42|224,13|224,13|224,34|0,02397|2,02|4,95|11,86|1,00|
|70|10,0|223,02|223,97|223,63|224,06|0,00499|1,28|7,83|11,18|0,49|
|60|10,0|222,62|223,97|223,32|224,01|0,00209|0,96|12,03|29,71|0,32|
|50|10,0|222,27|223,97|223,18|223,99|0,00135|0,72|19,25|44,46|0,26|
|40|10,0|222,56|223,97|223,29|223,97|0,00044|0,44|30,12|51,09|0,15|
|30|10,0|222,41|223,75|223,23|223,76|0,00187|0,56|18,04|44,70|0,27|
|20|10,0|221,70|222,42|222,62|223,03|0,08594|3,47|2,88|7,97|1,85|
|10|10,0|220,93|222,02|222,13|222,47|0,04408|2,97|3,36|6,17|1,29|
|0|10,0|220,67|221,52|221,12|221,54|0,00141|0,60|16,61|27,93|0,25|

Al igual que en el caso anterior, en la siguiente Figura se presenta el perfil hidráulico para la
situación con Proyecto

126-EB-00-HID-MCA-01 **17**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Figura 5.3 Eje Hidráulico Canal. Situación Con Proyecto. Qd = 10 [m3/s]**

126-EB-00-HID-MCA-01 **18**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

Al igual que en el caso anterior, en la siguiente Figura se presenta el detalle del efecto del
vertedero sobre el nivel de escurrimiento de aguas arriba:

**Figura 5.4 Detalle Eje Hidráulico.**

Como se puede apreciar, el efecto es similar al obtenido en la situación sin proyecto.

Los resultados de los otros caudales se presentan en el Anexo 3.

**5.3** **Comparación de los ejes hidráulicos obtenidos**

En la siguiente Tabla se presenta una comparación numérica de las condiciones de escurrimiento
obtenidas para ambas condiciones (sin y con proyecto):

126-EB-00-HID-MCA-01 **19**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Tabla 5.3 Comparación Eje hidráulico**

|River Sta|Zfondo|ZH|Col4|Col5|ZB|Col7|Col8|Vel|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**River Sta**|**Zfondo**|**S.Proy**|**C Proy.**|**ZH**|**S.Proy**|**C Proy.**|**ZB**|**S.Proy**|**C Proy.**|**V **|
|**River Sta**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[m/s]**|**[m/s]**|**[m/s]**|
|796,57|230,37|231,42|230,42|-1,00|231,61|230,43|-1,18|1,92|0,38|-1,54|
|790|230,25|231,39|230,33|-1,06|231,53|230,34|-1,19|1,66|0,40|-1,26|
|780|229,97|231,36|230,24|-1,12|231,45|230,24|-1,21|1,38|0,11|-1,27|
|770|229,94|231,19|230,09|-1,10|231,29|230,09|-1,20|1,41|0,13|-1,28|
|760|229,79|230,46|229,86|-0,60|231,04|229,87|-1,17|3,37|0,52|-2,85|
|750|229,59|230,53|229,66|-0,87|230,74|229,67|-1,07|2,01|0,33|-1,68|
|740|229,43|230,34|229,49|-0,85|230,56|229,50|-1,06|2,05|0,39|-1,66|
|730|229,26|229,93|229,31|-0,62|230,34|229,32|-1,02|2,84|0,41|-2,43|
|720|229,08|229,74|229,17|-0,57|230,16|229,18|-0,98|2,89|0,24|-2,65|
|710|228,76|229,90|229,17|-0,73|229,91|229,17|-0,74|0,57|0,04|-0,53|
|700|228,18|229,90|229,17|-0,73|229,90|229,17|-0,73|0,37|0,02|-0,35|
|690|229,05|229,87|229,17|-0,70|229,90|229,17|-0,73|0,64|0,07|-0,57|
|680|228,96|229,70|229,10|-0,60|229,84|229,12|-0,72|1,65|0,54|-1,11|
|670|228,79|229,42|228,92|-0,50|229,59|228,94|-0,65|1,82|0,60|-1,22|
|660|228,54|229,26|228,58|-0,68|229,36|228,66|-0,70|1,43|1,25|-0,18|
|650|228,32|228,99|228,42|-0,57|229,13|228,42|-0,71|1,64|0,28|-1,36|
|640|228,24|228,88|228,31|-0,57|229,01|228,33|-0,68|1,58|0,57|-1,01|
|630|227,77|228,62|227,84|-0,78|228,76|227,88|-0,88|1,67|0,84|-0,83|
|620|227,5|228,56|227,61|-0,95|228,69|227,62|-1,07|1,56|0,19|-1,37|
|610|227,28|228,43|227,60|-0,83|228,58|227,60|-0,98|1,74|0,13|-1,61|
|600|226,43|228,40|227,60|-0,80|228,51|227,60|-0,91|1,46|0,04|-1,42|
|590|226,63|228,40|227,60|-0,80|228,46|227,60|-0,86|1,14|0,03|-1,11|
|580|226,88|228,40|227,60|-0,80|228,44|227,60|-0,84|0,88|0,02|-0,86|
|570|227,42|228,35|227,60|-0,75|228,41|227,60|-0,81|1,13|0,30|-0,83|
|560|227,27|228,22|227,41|-0,81|228,30|227,43|-0,87|1,22|0,67|-0,55|
|550|226,93|228,19|227,31|-0,88|228,24|227,31|-0,93|1,01|0,11|-0,90|
|540|227,11|228,10|227,27|-0,83|228,18|227,29|-0,89|1,31|0,51|-0,80|
|530|227,01|227,58|227,16|-0,42|227,95|227,16|-0,79|2,68|0,24|-2,44|
|520|227,03|227,69|227,13|-0,56|227,79|227,13|-0,66|1,41|0,21|-1,20|
|510|226,98|227,56|227,07|-0,49|227,68|227,07|-0,61|1,48|0,28|-1,20|
|500|226,7|227,47|226,82|-0,65|227,57|226,84|-0,73|1,39|0,61|-0,78|
|490|226,32|227,41|226,60|-0,81|227,50|226,60|-0,90|1,28|0,16|-1,12|
|480|226,36|227,28|226,58|-0,70|227,42|226,59|-0,83|1,65|0,31|-1,34|
|470|226,41|227,21|226,53|-0,68|227,30|226,54|-0,76|1,29|0,33|-0,96|
|460|226,33|227,20|226,47|-0,73|227,23|226,47|-0,76|0,86|0,24|-0,62|

126-EB-00-HID-MCA-01 **20**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|River Sta|Zfondo|ZH|Col4|Col5|ZB|Col7|Col8|Vel|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**River Sta**|**Zfondo**|**S.Proy**|**C Proy.**|**ZH**|**S.Proy**|**C Proy.**|**ZB**|**S.Proy**|**C Proy.**|**V **|
|**River Sta**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[m/s]**|**[m/s]**|**[m/s]**|
|450|226,2|227,15|226,34|-0,81|227,19|226,34|-0,85|0,80|0,13|-0,67|
|440|226,03|227,13|226,34|-0,79|227,17|226,34|-0,83|0,93|0,05|-0,88|
|430|225,97|227,10|226,34|-0,76|227,15|226,34|-0,81|0,89|0,14|-0,75|
|420|226,17|226,81|226,28|-0,53|226,94|226,29|-0,65|1,58|0,44|-1,14|
|410|225,91|226,57|226,02|-0,55|226,78|226,04|-0,74|2,03|0,65|-1,38|
|400|225,59|226,55|225,86|-0,69|226,61|225,86|-0,75|1,09|0,10|-0,99|
|390|225,32|226,55|225,86|-0,69|226,58|225,86|-0,72|0,80|0,02|-0,78|
|380|225,07|226,52|225,86|-0,66|226,56|225,86|-0,70|0,88|0,02|-0,86|
|370|225,42|226,49|225,86|-0,63|226,54|225,86|-0,68|0,99|0,05|-0,94|
|360|225,43|226,48|225,86|-0,62|226,51|225,86|-0,65|0,79|0,04|-0,75|
|350|225,74|226,40|225,81|-0,59|226,44|225,81|-0,63|0,91|0,13|-0,78|
|340|225,02|226,33|225,70|-0,63|226,35|225,70|-0,65|0,68|0,02|-0,66|
|330|224,96|226,29|225,70|-0,59|226,33|225,70|-0,63|0,90|0,03|-0,87|
|320|225,59|226,09|225,69|-0,40|226,27|225,70|-0,57|1,86|0,45|-1,41|
|310|225,08|226,09|225,32|-0,77|226,12|225,32|-0,80|0,78|0,10|-0,68|
|300|225,14|226,07|225,31|-0,76|226,10|225,31|-0,79|0,77|0,11|-0,66|
|290|225,19|225,81|225,27|-0,54|225,93|225,28|-0,65|1,55|0,45|-1,10|
|280|224,89|225,70|225,01|-0,69|225,81|225,03|-0,78|1,51|0,56|-0,95|
|270|224,67|225,71|224,83|-0,88|225,75|224,83|-0,92|0,88|0,08|-0,80|
|260|224,6|225,68|224,83|-0,85|225,73|224,83|-0,90|0,92|0,07|-0,85|
|250|224,59|225,05|224,70|-0,35|225,48|224,71|-0,77|2,90|0,46|-2,44|
|240|224,38|225,30|224,68|-0,62|225,36|224,68|-0,68|1,14|0,04|-1,10|
|230|224,15|225,27|224,68|-0,59|225,33|224,68|-0,65|1,06|0,03|-1,03|
|220|224,11|225,25|224,68|-0,57|225,30|224,68|-0,62|0,93|0,02|-0,91|
|210|224,13|225,03|224,68|-0,35|225,10|224,68|-0,42|1,12|0,02|-1,10|
|200|223,8|225,01|224,68|-0,33|225,06|224,68|-0,38|1,00|0,02|-0,98|
|190|223,84|224,98|224,68|-0,30|225,04|224,68|-0,36|1,05|0,02|-1,03|
|180|223,93|224,93|224,68|-0,25|225,00|224,68|-0,32|1,10|0,02|-1,08|
|170|224|224,87|224,68|-0,19|224,94|224,68|-0,26|1,22|0,02|-1,20|
|160|224|224,83|224,68|-0,15|224,89|224,68|-0,21|1,06|0,01|-1,05|
|150|223,86|224,71|224,68|-0,03|224,76|224,68|-0,08|1,00|0,01|-0,99|
|140|223,77|224,69|224,68|-0,01|224,73|224,68|-0,05|0,93|0,01|-0,92|
|130|223,74|224,66|224,68|0,02|224,70|224,68|-0,02|0,93|0,01|-0,92|
|**120**|**223,67**|**224,66**|**224,66**|**0,00**|**224,68**|**224,68**|**0,00**|**0,56**|**0,56**|**0,00**|
|110|223,78|224,64|224,64|0,00|224,67|224,67|0,00|0,72|0,72|0,00|
|100|223,71|224,52|224,52|0,00|224,63|224,63|0,00|1,45|1,45|0,00|
|90|223,59|224,32|224,32|0,00|224,49|224,49|0,00|1,83|1,83|0,00|
|80|223,42|224,13|224,13|0,00|224,34|224,34|0,00|2,02|2,02|0,00|

126-EB-00-HID-MCA-01 **21**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|River Sta|Zfondo|ZH|Col4|Col5|ZB|Col7|Col8|Vel|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**River Sta**|**Zfondo**|**S.Proy**|**C Proy.**|**ZH**|**S.Proy**|**C Proy.**|**ZB**|**S.Proy**|**C Proy.**|**V **|
|**River Sta**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[m/s]**|**[m/s]**|**[m/s]**|
|70|223,02|223,97|223,97|0,00|224,06|224,06|0,00|1,28|1,28|0,00|
|60|222,62|223,97|223,97|0,00|224,01|224,01|0,00|0,96|0,96|0,00|
|50|222,27|223,97|223,97|0,00|223,99|223,99|0,00|0,72|0,72|0,00|
|40|222,56|223,97|223,97|0,00|223,97|223,97|0,00|0,44|0,44|0,00|
|30|222,41|223,75|223,75|0,00|223,76|223,76|0,00|0,56|0,56|0,00|
|20|221,7|222,42|222,42|0,00|223,03|223,03|0,00|3,47|3,47|0,00|
|10|220,93|222,02|222,02|0,00|222,47|222,47|0,00|2,97|2,97|0,00|
|0|220,67|221,52|221,52|0,00|221,54|221,54|0,00|0,60|0,60|0,00|

Como es evidente, entre el perfil 796,57 y el 120 (descarga de la futura central), existe una
diferencia notoria en las condiciones de escurrimiento, debido al cambio de caudal que será
conducido en dicha zona, pasando de 10 [m3/s] a solo 0,1 [m3/s].

Sin embargo, a partir del perfil 120, lugar donde ocurrirá la descarga de la central, los caudales
son similares en ambas condiciones y las condiciones de escurrimiento son iguales. Esto se debe
a que en el perfil 80 se produce un escurrimiento crítico, lo cual independiza las condiciones de
escurrimiento entre aguas arriba y aguas abajo. De tal manera que para aguas arriba, donde
existe una condición sub crítica el perfil hidráulico es controlado por dicha crisis, mientras que
hacía aguas abajo, se produce un régimen super crítico y posterior resalto.

126-EB-00-HID-MCA-01 **22**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

Régimen Sub Crítico

**Figura 5.5 Detalle Escurrimiento en la Descarga de la Central**

Al realizar la misma comparación para los otros caudales simulados (11,5 y 12 [m3/s]), en el
tramo final se tiene:

126-EB-00-HID-MCA-01 **23**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**Tabla 5.4 Comparación Situación Sin y Con Proyecto. Q = 11,5 [m3/s]**

|Perfil|Zfondo|ZH|Col4|Col5|ZB|Col7|Col8|Vel|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**Zfondo**|**SP**|**CP**|**ZH**|**SP**|**CP**|**ZB**|**SP**|**CP**|**V **|
|**Perfil**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[m/s]**|**[m/s]**|**[m/s]**|
|140|223,77|224,75|224,74|-0,01|224,80|224,74|-0,06|1,00|0,01|-0,99|
|130|223,74|224,72|224,74|0,02|224,77|224,74|-0,03|0,98|0,01|-0,97|
|**120**|**223,67**|**224,73**|**224,72**|**-0,01**|**224,74**|**224,74**|**0,00**|**0,59**|**0,59**|**0,00**|
|110|223,78|224,70|224,70|0,00|224,73|224,73|0,00|0,76|0,76|0,00|
|100|223,71|224,57|224,56|-0,01|224,69|224,68|-0,01|1,54|1,53|-0,01|
|90|223,59|224,36|224,36|0,00|224,55|224,55|0,00|1,93|1,93|0,00|
|80|223,42|224,17|224,17|0,00|224,40|224,39|-0,01|2,10|2,10|0,00|
|70|223,02|223,90|223,89|-0,01|224,03|224,03|0,00|1,65|1,64|-0,01|
|60|222,62|223,88|223,87|-0,01|223,96|223,95|-0,01|1,27|1,26|-0,01|
|50|222,27|223,85|223,85|0,00|223,90|223,90|0,00|1,10|1,09|-0,01|
|40|222,56|223,82|223,82|0,00|223,87|223,86|-0,01|0,92|0,91|-0,01|
|30|222,41|223,80|223,79|-0,01|223,81|223,81|0,00|0,57|0,57|0,00|
|20|221,7|222,46|222,46|0,00|223,11|223,11|0,00|3,58|3,57|-0,01|
|10|220,93|222,08|222,08|0,00|222,55|222,55|0,00|3,04|3,04|0,00|
|0|220,67|221,57|221,57|0,00|221,59|221,59|0,00|0,64|0,63|-0,01|

**Tabla 5.5 Comparación Situación Sin y Con Proyecto. Q = 11,5 [m3/s]**

|Perfil|Zfondo|ZH|Col4|Col5|ZB|Col7|Col8|Vel|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**Zfondo**|**SP**|**CP**|**ZH**|**SP**|**CP**|**ZB**|**SP**|**CP**|**V **|
|**Perfil**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[msnm]**|**[msnm]**|**[m]**|**[m/s]**|**[m/s]**|**[m/s]**|
|140|223,77|224,77|224,76|-0,01|224,82|224,76|-0,06|1,02|0,01|-1,01|
|130|223,74|224,74|224,76|0,02|224,79|224,76|-0,03|0,99|0,01|-0,98|
|**120**|**223,67**|**224,75**|**224,74**|**-0,01**|**224,76**|**224,76**|**0,00**|**0,60**|**0,59**|**-0,01**|
|110|223,78|224,72|224,72|0,00|224,75|224,75|0,00|0,77|0,77|0,00|
|100|223,71|224,58|224,58|0,00|224,71|224,70|-0,01|1,56|1,56|0,00|
|90|223,59|224,38|224,37|-0,01|224,57|224,57|0,00|1,97|1,96|-0,01|
|80|223,42|224,18|224,18|0,00|224,42|224,41|-0,01|2,13|2,13|0,00|
|70|223,02|223,91|223,91|0,00|224,05|224,05|0,00|1,68|1,68|0,00|
|60|222,62|223,89|223,89|0,00|223,97|223,97|0,00|1,30|1,29|-0,01|
|50|222,27|223,86|223,86|0,00|223,91|223,91|0,00|1,11|1,11|0,00|
|40|222,56|223,84|223,83|-0,01|223,88|223,88|0,00|0,94|0,94|0,00|
|30|222,41|223,81|223,81|0,00|223,83|223,83|0,00|0,58|0,58|0,00|
|20|221,7|222,47|222,47|0,00|223,14|223,13|-0,01|3,61|3,61|0,00|
|10|220,93|222,10|222,10|0,00|222,58|222,57|-0,01|3,06|3,05|-0,01|
|0|220,67|221,59|221,59|0,00|221,61|221,61|0,00|0,65|0,64|-0,01|

Como se puede apreciar, para los caudales mayores simulados, se observa que la alteración de
las condiciones de escurrimiento también es despreciable, y es producida por el mismo efecto
del escurrimiento crítico en el perfil 80, tal como se puede ver en los resultados expuestos en
los anexos 2 y 3.

126-EB-00-HID-MCA-01 **24**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**5.4** **Situación eje hidráulico Bocatoma con y sin proyecto**

En la actualidad, existe una revancha suficiente para que el puente no se vea afectado por alguna
crecida controlada del canal matriz, siendo el nivel de agua con proyecto el siguiente, según el
software H-canales:

Con una velocidad de 0.79 m/s que no permite socavación de la zona del puente. Con proyecto,
esta situación mejora, ya que el caudal del canal matriz bajaría en 10 m3/s (caudal de diseño de
la central) y por lo tanto, la velocidad de escurrimiento y el nivel de agua serian menores,

Con una velocidad de 0,74 m/s

126-EB-00-HID-MCA-01 **25**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

**6.** **CONCLUSIONES**

En consecuencia, se descarta que hacía aguas abajo la descarga de la central hidroeléctrica El
Portal altere las condiciones de escurrimiento actuales, y menos que pueda afectar a los puentes
ubicados más aguas abajo.

Si a lo anterior se suma el hecho de que actualmente existe una obra de regulación, la cual
controla los caudales, independizando los flujos entre aguas arriaba y aguas debajo de esta obra
(compuertas y vertedero existente), se puede descartar algún efecto sobre obras de
infraestructura hacia aguas abajo.

En la zona de la bocatoma, se observa que no existe posibilidad de afectación de la obra al
puente que lo precede, ya que con y sin proyecto, el régimen de escurrimiento no cambia y
además, con proyecto, baja el caudal y disminuye la velocidad y nivel de agua en la zona del
puente, imposibilitando así, su deterioro.

126-EB-00-HID-MCA-01 **26**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### ANEXO 1 LEVANTAMIENTO TOPOGRÁFICO

126-EB-00-HID-MCA-01 **27**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### ANEXO 2 EJE HIDRÁULICO SIN PROYECTO

126-EB-00-HID-MCA-01 **28**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### Eje hidráulico Sin Proyecto. Q = 11,5 [m3/s]

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|796,57|11,5|230,37|231,50|231,19|231,72|0,01031|2,05|5,62|4,98|0,62|
|790|11,5|230,25|231,47|231,07|231,63|0,00677|1,77|6,49|5,62|0,53|
|780|11,5|229,97|231,44|230,85|231,55|0,00412|1,47|7,80|6,40|0,43|
|770|11,5|229,94|231,27|230,72|231,39|0,00437|1,51|7,63|6,39|0,44|
|760|11,5|229,79|230,52|230,69|231,14|0,05329|3,49|3,30|5,64|1,46|
|750|11,5|229,59|230,61|230,41|230,84|0,01130|2,12|5,42|5,92|0,71|
|740|11,5|229,43|230,42|230,24|230,66|0,01184|2,15|5,34|5,96|0,73|
|730|11,5|229,26|229,99|230,06|230,44|0,03095|2,96|3,88|5,72|1,15|
|720|11,5|229,08|229,81|229,88|230,26|0,03127|2,96|3,88|5,72|1,15|
|710|11,5|228,76|229,94|229,42|229,96|0,00107|0,61|18,83|26,26|0,23|
|700|11,5|228,18|229,95|229,24|229,95|0,00036|0,41|28,25|31,57|0,14|
|690|11,5|229,05|229,92|229,44|229,95|0,00124|0,70|16,53|21,11|0,25|
|680|11,5|228,96|229,73|229,70|229,89|0,01973|1,72|6,68|17,14|0,88|
|670|11,5|228,79|229,47|229,45|229,64|0,02288|1,86|6,18|16,12|0,96|
|660|11,5|228,54|229,31|229,10|229,43|0,00724|1,50|7,83|15,47|0,58|
|650|11,5|228,32|229,04|228,91|229,19|0,01075|1,73|6,66|10,79|0,70|
|640|11,5|228,24|228,94|228,81|229,08|0,01071|1,63|7,08|12,75|0,70|
|630|11,5|227,77|228,70|228,47|228,85|0,00834|1,73|6,64|8,26|0,62|
|620|11,5|227,50|228,64|228,25|228,78|0,00615|1,67|6,88|6,63|0,52|
|610|11,5|227,28|228,49|228,20|228,67|0,00880|1,87|6,14|6,36|0,61|
|600|11,5|226,43|228,46|227,86|228,59|0,00528|1,61|7,14|5,39|0,45|
|590|11,5|226,63|228,45|227,68|228,53|0,00268|1,26|9,19|8,23|0,34|
|580|11,5|226,88|228,45|227,70|228,50|0,00151|0,94|13,99|27,42|0,27|
|570|11,5|227,42|228,40|228,06|228,47|0,00445|1,20|9,76|19,07|0,46|
|560|11,5|227,27|228,27|228,02|228,35|0,00535|1,28|9,36|17,42|0,51|
|550|11,5|226,93|228,24|227,86|228,30|0,00423|1,07|10,78|17,91|0,44|
|540|11,5|227,11|228,14|227,95|228,24|0,00840|1,36|8,46|17,86|0,61|
|530|11,5|227,01|227,64|227,73|228,02|0,03676|2,70|4,26|9,06|1,26|
|520|11,5|227,03|227,74|227,56|227,85|0,00828|1,50|7,68|12,97|0,62|
|510|11,5|226,98|227,62|227,48|227,74|0,00981|1,54|7,46|13,73|0,67|
|500|11,5|226,70|227,53|227,33|227,63|0,00740|1,45|7,94|12,89|0,59|

126-EB-00-HID-MCA-01 **29**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|490|11,5|226,32|227,47|227,18|227,56|0,00557|1,36|8,46|11,90|0,51|
|480|11,5|226,36|227,33|227,20|227,48|0,01192|1,74|6,77|14,77|0,73|
|470|11,5|226,41|227,27|227,07|227,36|0,00807|1,34|8,60|16,47|0,59|
|460|11,5|226,33|227,25|226,88|227,29|0,00290|0,90|12,77|20,89|0,37|
|450|11,5|226,20|227,21|226,71|227,25|0,00180|0,86|13,76|21,56|0,30|
|440|11,5|226,03|227,18|226,64|227,23|0,00220|1,00|12,52|20,43|0,34|
|430|11,5|225,97|227,15|226,74|227,20|0,00239|0,95|12,57|22,94|0,35|
|420|11,5|226,17|226,85|226,76|226,99|0,01307|1,65|6,95|14,15|0,75|
|410|11,5|225,91|226,61|226,61|226,84|0,02466|2,12|5,43|12,15|1,01|
|400|11,5|225,59|226,60|226,26|226,67|0,00397|1,17|9,82|13,38|0,44|
|390|11,5|225,32|226,60|225,93|226,64|0,00150|0,87|13,20|14,84|0,28|
|380|11,5|225,07|226,57|225,78|226,62|0,00160|0,97|12,77|16,41|0,29|
|370|11,5|225,42|226,54|226,15|226,59|0,00301|1,07|11,65|18,27|0,39|
|360|11,5|225,43|226,53|226,08|226,56|0,00206|0,86|14,63|23,87|0,32|
|350|11,5|225,74|226,45|226,15|226,49|0,00343|0,96|13,01|27,76|0,40|
|340|11,5|225,02|226,38|225,68|226,41|0,00123|0,73|16,43|29,72|0,25|
|330|11,5|224,96|226,34|225,82|226,39|0,00234|0,97|12,81|19,27|0,34|
|320|11,5|225,59|226,13|226,13|226,32|0,02292|1,93|6,21|17,53|0,98|
|310|11,5|225,08|226,14|225,68|226,17|0,00188|0,85|13,60|17,70|0,31|
|300|11,5|225,14|226,12|225,65|226,15|0,00190|0,83|14,52|23,67|0,31|
|290|11,5|225,19|225,86|225,74|225,99|0,01172|1,60|7,19|14,29|0,72|
|280|11,5|224,89|225,76|225,59|225,88|0,00945|1,56|7,38|12,71|0,65|
|270|11,5|224,67|225,77|225,20|225,81|0,00191|0,95|12,10|13,30|0,31|
|260|11,5|224,60|225,74|225,19|225,79|0,00213|1,00|11,67|16,54|0,33|
|250|11,5|224,59|225,09|225,22|225,55|0,06646|3,01|3,82|10,68|1,61|
|240|11,5|224,38|225,36|224,96|225,43|0,00358|1,21|9,48|11,19|0,42|
|230|11,5|224,15|225,33|224,84|225,40|0,00284|1,14|10,07|10,83|0,38|
|220|11,5|224,11|225,31|224,76|225,36|0,00218|1,00|11,60|16,04|0,33|
|210|11,5|224,13|225,09|224,68|225,16|0,00368|1,20|9,62|11,80|0,42|
|200|11,5|223,80|225,07|224,57|225,13|0,00254|1,07|10,85|14,69|0,36|
|190|11,5|223,84|225,04|224,67|225,10|0,00329|1,10|10,85|19,65|0,41|
|180|11,5|223,93|224,99|224,68|225,06|0,00458|1,14|10,08|16,50|0,46|
|170|11,5|224,00|224,93|224,67|225,01|0,00566|1,28|9,00|13,83|0,51|
|160|11,5|224,00|224,89|224,52|224,95|0,00361|1,13|10,14|13,67|0,42|

126-EB-00-HID-MCA-01 **30**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|150|11,5|223,86|224,77|224,33|224,83|0,00290|1,06|10,87|14,01|0,38|
|140|11,5|223,77|224,75|224,29|224,80|0,00236|1,00|11,59|15,17|0,35|
|130|11,5|223,74|224,72|224,32|224,77|0,00274|0,98|11,76|16,33|0,37|
|120|11,5|223,67|224,73|224,18|224,74|0,00088|0,59|20,97|48,55|0,21|
|110|11,5|223,78|224,70|224,28|224,73|0,00164|0,76|15,29|22,37|0,29|
|100|11,5|223,71|224,57|224,39|224,69|0,00836|1,54|7,49|12,11|0,62|
|90|11,5|223,59|224,36|224,30|224,55|0,01548|1,93|5,95|10,94|0,84|
|80|11,5|223,42|224,17|224,17|224,40|0,02335|2,10|5,47|12,08|1,00|
|70|11,5|223,02|223,90|223,68|224,03|0,00890|1,65|6,98|10,51|0,65|
|60|11,5|222,62|223,88|223,38|223,96|0,00408|1,27|9,60|22,49|0,45|
|50|11,5|222,27|223,85|223,25|223,90|0,00330|1,10|14,06|40,67|0,39|
|40|11,5|222,56|223,82|223,33|223,87|0,00240|0,92|12,73|19,13|0,35|
|30|11,5|222,41|223,80|223,27|223,81|0,00173|0,57|20,43|46,51|0,27|
|20|11,5|221,70|222,46|222,67|223,11|0,08475|3,58|3,21|8,42|1,85|
|10|11,5|220,93|222,08|222,20|222,55|0,04273|3,04|3,78|6,54|1,28|
|0|11,5|220,67|221,57|221,15|221,59|0,00145|0,64|18,01|28,31|0,26|

126-EB-00-HID-MCA-01 **31**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### Eje hidráulico Sin Proyecto. Q = 12 [m3/s]

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|796,57|12,0|230,37|231,53|231,21|231,75|0,01045|2,08|5,76|4,98|0,62|
|790|12,0|230,25|231,50|231,09|231,67|0,00688|1,81|6,64|5,63|0,53|
|780|12,0|229,97|231,47|230,87|231,59|0,00421|1,50|7,98|6,43|0,43|
|770|12,0|229,94|231,30|230,75|231,42|0,00446|1,54|7,80|6,42|0,45|
|760|12,0|229,79|230,54|230,71|231,17|0,05240|3,52|3,41|5,66|1,45|
|750|12,0|229,59|230,63|230,43|230,87|0,01137|2,16|5,57|5,94|0,71|
|740|12,0|229,43|230,45|230,26|230,69|0,01190|2,19|5,49|5,98|0,73|
|730|12,0|229,26|230,01|230,08|230,47|0,03080|3,00|4,00|5,74|1,15|
|720|12,0|229,08|229,82|229,90|230,30|0,03263|3,05|3,94|5,73|1,17|
|710|12,0|228,76|229,96|229,43|229,98|0,00109|0,62|19,25|26,29|0,23|
|700|12,0|228,18|229,96|229,25|229,97|0,00037|0,42|28,75|31,58|0,14|
|690|12,0|229,05|229,94|229,45|229,96|0,00127|0,71|16,85|21,13|0,25|
|680|12,0|228,96|229,75|229,71|229,90|0,01975|1,75|6,87|17,26|0,88|
|670|12,0|228,79|229,48|229,46|229,66|0,02203|1,87|6,42|16,15|0,95|
|660|12,0|228,54|229,33|229,12|229,45|0,00723|1,53|8,12|16,17|0,58|
|650|12,0|228,32|229,06|228,92|229,21|0,01077|1,76|6,84|10,80|0,70|
|640|12,0|228,24|228,96|228,83|229,10|0,01052|1,64|7,31|12,79|0,69|
|630|12,0|227,77|228,73|228,49|228,88|0,00824|1,75|6,85|8,27|0,62|
|620|12,0|227,50|228,66|228,27|228,81|0,00627|1,71|7,03|6,65|0,53|
|610|12,0|227,28|228,51|228,22|228,70|0,00905|1,92|6,26|6,38|0,62|
|600|12,0|226,43|228,47|227,89|228,61|0,00555|1,66|7,22|5,42|0,46|
|590|12,0|226,63|228,47|227,70|228,55|0,00282|1,30|9,35|9,83|0,35|
|580|12,0|226,88|228,47|227,71|228,52|0,00155|0,96|14,49|27,53|0,28|
|570|12,0|227,42|228,41|228,07|228,49|0,00446|1,22|10,08|19,32|0,46|
|560|12,0|227,27|228,29|228,03|228,37|0,00535|1,30|9,65|17,50|0,51|
|550|12,0|226,93|228,26|227,88|228,32|0,00436|1,08|11,08|18,46|0,45|
|540|12,0|227,11|228,16|227,97|228,26|0,00833|1,38|8,75|18,39|0,61|
|530|12,0|227,01|227,66|227,78|228,04|0,03568|2,72|4,42|9,13|1,25|
|520|12,0|227,03|227,75|227,58|227,87|0,00837|1,53|7,87|13,03|0,63|
|510|12,0|226,98|227,63|227,49|227,76|0,00973|1,56|7,68|13,77|0,67|
|500|12,0|226,70|227,54|227,35|227,65|0,00738|1,47|8,16|12,93|0,59|

126-EB-00-HID-MCA-01 **32**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|490|12,0|226,32|227,48|227,20|227,58|0,00566|1,39|8,66|11,97|0,52|
|480|12,0|226,36|227,34|227,22|227,50|0,01195|1,76|7,00|14,95|0,73|
|470|12,0|226,41|227,29|227,08|227,38|0,00806|1,35|8,89|16,76|0,59|
|460|12,0|226,33|227,27|226,89|227,31|0,00296|0,91|13,14|21,35|0,37|
|450|12,0|226,20|227,23|226,73|227,26|0,00182|0,88|14,13|22,78|0,31|
|440|12,0|226,03|227,19|226,66|227,24|0,00225|1,03|12,85|21,46|0,34|
|430|12,0|225,97|227,17|226,75|227,22|0,00243|0,97|12,93|23,38|0,35|
|420|12,0|226,17|226,87|226,77|227,01|0,01298|1,68|7,15|14,63|0,75|
|410|12,0|225,91|226,63|226,63|226,86|0,02455|2,14|5,60|12,26|1,01|
|400|12,0|225,59|226,61|226,27|226,69|0,00405|1,20|10,03|13,42|0,44|
|390|12,0|225,32|226,61|225,94|226,65|0,00155|0,90|13,45|16,09|0,29|
|380|12,0|225,07|226,58|225,80|226,63|0,00166|1,00|13,02|16,65|0,30|
|370|12,0|225,42|226,55|226,17|226,61|0,00307|1,09|11,91|18,34|0,39|
|360|12,0|225,43|226,54|226,10|226,58|0,00214|0,88|14,97|24,66|0,33|
|350|12,0|225,74|226,46|226,16|226,51|0,00346|0,98|13,43|28,22|0,41|
|340|12,0|225,02|226,40|225,69|226,42|0,00126|0,75|16,93|31,09|0,25|
|330|12,0|224,96|226,36|225,84|226,40|0,00244|0,99|13,10|19,64|0,35|
|320|12,0|225,59|226,14|226,14|226,33|0,02313|1,96|6,39|17,75|0,98|
|310|12,0|225,08|226,15|225,69|226,19|0,00195|0,87|13,85|17,80|0,31|
|300|12,0|225,14|226,13|225,66|226,17|0,00202|0,85|14,84|24,34|0,32|
|290|12,0|225,19|225,88|225,75|226,01|0,01157|1,61|7,45|14,52|0,72|
|280|12,0|224,89|225,77|225,61|225,90|0,00931|1,57|7,63|12,81|0,65|
|270|12,0|224,67|225,79|225,21|225,83|0,00196|0,97|12,37|15,33|0,31|
|260|12,0|224,60|225,76|225,20|225,81|0,00220|1,02|12,00|19,72|0,33|
|250|12,0|224,59|225,10|225,23|225,57|0,06535|3,05|3,94|10,69|1,60|
|240|12,0|224,38|225,38|224,97|225,46|0,00363|1,24|9,71|11,24|0,42|
|230|12,0|224,15|225,35|224,86|225,42|0,00291|1,17|10,28|10,90|0,38|
|220|12,0|224,11|225,33|224,77|225,39|0,00224|1,02|11,93|16,91|0,34|
|210|12,0|224,13|225,11|224,70|225,19|0,00375|1,22|9,85|12,95|0,43|
|200|12,0|223,80|225,09|224,59|225,15|0,00257|1,10|11,13|15,11|0,36|
|190|12,0|223,84|225,06|224,69|225,12|0,00329|1,12|11,23|20,25|0,41|
|180|12,0|223,93|225,01|224,70|225,08|0,00457|1,16|10,40|16,76|0,46|
|170|12,0|224,00|224,94|224,68|225,03|0,00568|1,30|9,26|13,94|0,51|
|160|12,0|224,00|224,91|224,54|224,97|0,00371|1,16|10,39|13,90|0,43|

126-EB-00-HID-MCA-01 **33**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|150|12,0|223,86|224,79|224,35|224,85|0,00293|1,08|11,15|14,79|0,38|
|140|12,0|223,77|224,77|224,30|224,82|0,00238|1,02|11,89|15,50|0,35|
|130|12,0|223,74|224,74|224,34|224,79|0,00281|0,99|12,08|16,68|0,37|
|120|12,0|223,67|224,75|224,19|224,76|0,00088|0,60|21,96|49,82|0,21|
|110|12,0|223,78|224,72|224,29|224,75|0,00164|0,77|15,73|22,48|0,29|
|100|12,0|223,71|224,58|224,41|224,71|0,00844|1,56|7,68|12,16|0,63|
|90|12,0|223,59|224,38|224,31|224,57|0,01557|1,97|6,11|10,99|0,84|
|80|12,0|223,42|224,18|224,18|224,42|0,02325|2,13|5,63|12,14|1,00|
|70|12,0|223,02|223,91|223,70|224,05|0,00919|1,68|7,13|10,63|0,66|
|60|12,0|222,62|223,89|223,40|223,97|0,00427|1,30|9,87|23,87|0,46|
|50|12,0|222,27|223,86|223,27|223,91|0,00336|1,11|14,64|41,72|0,40|
|40|12,0|222,56|223,84|223,35|223,88|0,00255|0,94|12,96|19,58|0,36|
|30|12,0|222,41|223,81|223,29|223,83|0,00168|0,58|21,22|46,97|0,26|
|20|12,0|221,70|222,47|222,69|223,14|0,08443|3,61|3,32|8,56|1,85|
|10|12,0|220,93|222,10|222,22|222,58|0,04206|3,06|3,92|6,67|1,27|
|0|12,0|220,67|221,59|221,16|221,61|0,00144|0,65|18,57|28,45|0,26|

126-EB-00-HID-MCA-01 **34**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### ANEXO 3 EJE HIDRÁULICO CON PROYECTO

126-EB-00-HID-MCA-01 **35**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### Eje hidráulico Con Proyecto. Q = 11,5 [m3/s]

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|796,57|0,1|230,37|230,42|230,41|230,43|0,01313|0,38|0,26|4,95|0,53|
|790|0,1|230,25|230,33|230,32|230,34|0,01645|0,40|0,25|5,08|0,58|
|780|0,1|229,97|230,24|230,07|230,24|0,00024|0,11|0,91|5,24|0,08|
|770|0,1|229,94|230,09|229,98|230,09|0,00041|0,13|0,77|5,35|0,11|
|760|0,1|229,79|229,86|229,84|229,87|0,01763|0,52|0,19|2,77|0,63|
|750|0,1|229,59|229,66|229,63|229,67|0,00773|0,33|0,30|4,78|0,42|
|740|0,1|229,43|229,49|229,47|229,50|0,01304|0,39|0,26|4,75|0,53|
|730|0,1|229,26|229,31|229,29|229,32|0,01591|0,41|0,24|4,82|0,58|
|720|0,1|229,08|229,17|229,12|229,18|0,00289|0,24|0,42|5,05|0,27|
|710|0,1|228,76|229,17|228,87|229,17|0,00002|0,04|2,57|11,43|0,03|
|700|0,1|228,18|229,17|228,37|229,17|0,00001|0,02|5,10|25,76|0,01|
|690|0,1|229,05|229,17|229,08|229,17|0,00027|0,07|1,34|16,16|0,08|
|680|0,1|228,96|229,10|229,08|229,12|0,01745|0,54|0,19|2,53|0,64|
|670|0,1|228,79|228,92|228,91|228,94|0,02742|0,60|0,17|2,69|0,78|
|660|0,1|228,54|228,58|228,60|228,66|0,52628|1,25|0,08|4,14|2,86|
|650|0,1|228,32|228,42|228,39|228,42|0,00724|0,28|0,36|6,91|0,39|
|640|0,1|228,24|228,31|228,31|228,33|0,04391|0,57|0,17|4,43|0,93|
|630|0,1|227,77|227,84|227,85|227,88|0,09140|0,84|0,12|2,92|1,33|
|620|0,1|227,50|227,61|227,55|227,62|0,00163|0,19|0,52|5,77|0,20|
|610|0,1|227,28|227,60|227,49|227,60|0,00045|0,13|0,78|5,73|0,11|
|600|0,1|226,43|227,60|226,65|227,60|0,00001|0,04|2,78|4,73|0,02|
|590|0,1|226,63|227,60|226,75|227,60|0,00000|0,03|3,85|6,00|0,01|
|580|0,1|226,88|227,60|226,99|227,60|0,00000|0,02|4,07|8,60|0,01|
|570|0,1|227,42|227,60|227,55|227,60|0,01005|0,30|0,34|7,48|0,45|
|560|0,1|227,27|227,41|227,40|227,43|0,02769|0,67|0,15|2,13|0,80|
|550|0,1|226,93|227,31|227,06|227,31|0,00021|0,11|0,90|4,67|0,08|
|540|0,1|227,11|227,27|227,24|227,29|0,01329|0,51|0,19|2,36|0,57|
|530|0,1|227,01|227,16|227,09|227,16|0,00258|0,24|0,42|4,84|0,26|
|520|0,1|227,03|227,13|227,09|227,13|0,00427|0,21|0,47|9,43|0,30|
|510|0,1|226,98|227,07|227,06|227,07|0,01583|0,28|0,35|12,04|0,53|
|500|0,1|226,70|226,82|226,82|226,84|0,04149|0,61|0,17|3,72|0,92|
|490|0,1|226,32|226,60|226,44|226,60|0,00063|0,16|0,61|4,14|0,14|
|480|0,1|226,36|226,58|226,50|226,59|0,00357|0,31|0,32|2,91|0,30|

126-EB-00-HID-MCA-01 **36**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|470|0,1|226,41|226,53|226,50|226,54|0,00805|0,33|0,30|4,93|0,42|
|460|0,1|226,33|226,47|226,42|226,47|0,00529|0,24|0,42|8,00|0,34|
|450|0,1|226,20|226,34|226,27|226,34|0,00124|0,13|0,75|11,76|0,17|
|440|0,1|226,03|226,34|226,07|226,34|0,00003|0,05|2,18|9,39|0,03|
|430|0,1|225,97|226,34|226,12|226,34|0,00035|0,14|0,72|3,88|0,10|
|420|0,1|226,17|226,28|226,27|226,29|0,01817|0,44|0,22|4,21|0,61|
|410|0,1|225,91|226,02|226,02|226,04|0,03714|0,65|0,15|2,82|0,89|
|400|0,1|225,59|225,86|225,69|225,86|0,00028|0,10|0,97|7,34|0,09|
|390|0,1|225,32|225,86|225,40|225,86|0,00000|0,02|4,51|10,87|0,01|
|380|0,1|225,07|225,86|225,12|225,86|0,00000|0,02|5,26|7,77|0,01|
|370|0,1|225,42|225,86|225,51|225,86|0,00003|0,05|2,22|9,27|0,03|
|360|0,1|225,43|225,86|225,53|225,86|0,00002|0,04|2,67|13,21|0,03|
|350|0,1|225,74|225,81|225,77|225,81|0,00127|0,13|0,80|14,06|0,17|
|340|0,1|225,02|225,70|225,12|225,70|0,00000|0,02|5,85|13,10|0,01|
|330|0,1|224,96|225,70|225,08|225,70|0,00000|0,03|3,98|10,59|0,01|
|320|0,1|225,59|225,69|225,68|225,70|0,04368|0,45|0,22|8,30|0,87|
|310|0,1|225,08|225,32|225,17|225,32|0,00029|0,10|1,03|8,70|0,09|
|300|0,1|225,14|225,31|225,21|225,31|0,00047|0,11|0,95|10,23|0,11|
|290|0,1|225,19|225,27|225,25|225,28|0,02152|0,45|0,22|4,78|0,67|
|280|0,1|224,89|225,01|225,00|225,03|0,02472|0,56|0,18|2,98|0,73|
|270|0,1|224,67|224,83|224,73|224,83|0,00024|0,08|1,21|11,22|0,08|
|260|0,1|224,60|224,83|224,68|224,83|0,00015|0,07|1,37|10,63|0,07|
|250|0,1|224,59|224,74|224,68|224,75|0,00254|0,21|0,47|6,09|0,25|
|240|0,1|224,38|224,74|224,45|224,74|0,00001|0,03|2,94|10,23|0,02|
|230|0,1|224,15|224,74|224,22|224,74|0,00000|0,02|4,09|9,59|0,01|
|220|0,1|224,11|224,74|224,20|224,74|0,00000|0,02|5,03|10,52|0,01|
|210|0,1|224,13|224,74|224,19|224,74|0,00000|0,02|5,79|10,47|0,01|
|200|0,1|223,80|224,74|223,89|224,74|0,00000|0,01|7,01|10,76|0,01|
|190|0,1|223,84|224,74|223,97|224,74|0,00000|0,02|6,36|12,88|0,01|
|180|0,1|223,93|224,74|224,05|224,74|0,00000|0,02|6,35|13,57|0,01|
|170|0,1|224,00|224,74|224,13|224,74|0,00000|0,02|6,52|13,24|0,01|
|160|0,1|224,00|224,74|224,06|224,74|0,00000|0,01|8,23|12,81|0,00|
|150|0,1|223,86|224,74|223,88|224,74|0,00000|0,01|10,52|13,48|0,00|
|140|0,1|223,77|224,74|223,82|224,74|0,00000|0,01|11,53|15,10|0,00|
|130|0,1|223,74|224,74|223,83|224,74|0,00000|0,01|12,11|16,71|0,00|
|120|11,4|223,67|224,72|224,18|224,74|0,00087|0,59|20,78|48,29|0,21|

126-EB-00-HID-MCA-01 **37**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|110|11,4|223,78|224,70|224,28|224,73|0,00164|0,76|15,20|22,34|0,29|
|100|11,4|223,71|224,56|224,39|224,68|0,00835|1,53|7,45|12,10|0,62|
|90|11,4|223,59|224,36|224,30|224,55|0,01545|1,93|5,92|10,93|0,84|
|80|11,4|223,42|224,17|224,17|224,39|0,02352|2,10|5,42|12,06|1,00|
|70|11,4|223,02|223,89|223,68|224,03|0,00881|1,64|6,96|10,50|0,64|
|60|11,4|222,62|223,87|223,38|223,95|0,00403|1,26|9,56|22,28|0,44|
|50|11,4|222,27|223,85|223,25|223,90|0,00326|1,09|14,03|40,62|0,39|
|40|11,4|222,56|223,82|223,33|223,86|0,00236|0,91|12,72|19,11|0,34|
|30|11,4|222,41|223,79|223,27|223,81|0,00174|0,57|20,26|46,41|0,27|
|20|11,4|221,70|222,46|222,67|223,11|0,08483|3,57|3,19|8,39|1,85|
|10|11,4|220,93|222,08|222,20|222,55|0,04281|3,04|3,75|6,52|1,28|
|0|11,4|220,67|221,57|221,15|221,59|0,00143|0,63|18,01|28,31|0,25|

126-EB-00-HID-MCA-01 **38**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

### Eje hidráulico Con Proyecto. Q = 12 [m3/s]

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|796,57|0,1|230,37|230,42|230,41|230,43|0,01313|0,38|0,26|4,95|0,53|
|790|0,1|230,25|230,33|230,32|230,34|0,01645|0,40|0,25|5,08|0,58|
|780|0,1|229,97|230,24|230,07|230,24|0,00024|0,11|0,91|5,24|0,08|
|770|0,1|229,94|230,09|229,98|230,09|0,00041|0,13|0,77|5,35|0,11|
|760|0,1|229,79|229,86|229,84|229,87|0,01763|0,52|0,19|2,77|0,63|
|750|0,1|229,59|229,66|229,63|229,67|0,00773|0,33|0,30|4,78|0,42|
|740|0,1|229,43|229,49|229,47|229,50|0,01304|0,39|0,26|4,75|0,53|
|730|0,1|229,26|229,31|229,29|229,32|0,01591|0,41|0,24|4,82|0,58|
|720|0,1|229,08|229,17|229,12|229,18|0,00289|0,24|0,42|5,05|0,27|
|710|0,1|228,76|229,17|228,87|229,17|0,00002|0,04|2,57|11,43|0,03|
|700|0,1|228,18|229,17|228,37|229,17|0,00001|0,02|5,10|25,76|0,01|
|690|0,1|229,05|229,17|229,08|229,17|0,00027|0,07|1,34|16,16|0,08|
|680|0,1|228,96|229,10|229,08|229,12|0,01745|0,54|0,19|2,53|0,64|
|670|0,1|228,79|228,92|228,91|228,94|0,02742|0,60|0,17|2,69|0,78|
|660|0,1|228,54|228,58|228,60|228,66|0,52628|1,25|0,08|4,14|2,86|
|650|0,1|228,32|228,42|228,39|228,42|0,00724|0,28|0,36|6,91|0,39|
|640|0,1|228,24|228,31|228,31|228,33|0,04391|0,57|0,17|4,43|0,93|
|630|0,1|227,77|227,84|227,85|227,88|0,09140|0,84|0,12|2,92|1,33|
|620|0,1|227,50|227,61|227,55|227,62|0,00163|0,19|0,52|5,77|0,20|
|610|0,1|227,28|227,60|227,49|227,60|0,00045|0,13|0,78|5,73|0,11|
|600|0,1|226,43|227,60|226,65|227,60|0,00001|0,04|2,78|4,73|0,02|
|590|0,1|226,63|227,60|226,75|227,60|0,00000|0,03|3,85|6,00|0,01|
|580|0,1|226,88|227,60|226,99|227,60|0,00000|0,02|4,07|8,60|0,01|
|570|0,1|227,42|227,60|227,55|227,60|0,01005|0,30|0,34|7,48|0,45|
|560|0,1|227,27|227,41|227,40|227,43|0,02769|0,67|0,15|2,13|0,80|
|550|0,1|226,93|227,31|227,06|227,31|0,00021|0,11|0,90|4,67|0,08|
|540|0,1|227,11|227,27|227,24|227,29|0,01329|0,51|0,19|2,36|0,57|
|530|0,1|227,01|227,16|227,09|227,16|0,00258|0,24|0,42|4,84|0,26|
|520|0,1|227,03|227,13|227,09|227,13|0,00427|0,21|0,47|9,43|0,30|
|510|0,1|226,98|227,07|227,06|227,07|0,01583|0,28|0,35|12,04|0,53|
|500|0,1|226,70|226,82|226,82|226,84|0,04149|0,61|0,17|3,72|0,92|
|490|0,1|226,32|226,60|226,44|226,60|0,00063|0,16|0,61|4,14|0,14|
|480|0,1|226,36|226,58|226,50|226,59|0,00357|0,31|0,32|2,91|0,30|
|470|0,1|226,41|226,53|226,50|226,54|0,00805|0,33|0,30|4,93|0,42|
|460|0,1|226,33|226,47|226,42|226,47|0,00529|0,24|0,42|8,00|0,34|
|450|0,1|226,20|226,34|226,27|226,34|0,00124|0,13|0,75|11,76|0,17|

126-EB-00-HID-MCA-01 **39**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|440|0,1|226,03|226,34|226,07|226,34|0,00003|0,05|2,18|9,39|0,03|
|430|0,1|225,97|226,34|226,12|226,34|0,00035|0,14|0,72|3,88|0,10|
|420|0,1|226,17|226,28|226,27|226,29|0,01817|0,44|0,22|4,21|0,61|
|410|0,1|225,91|226,02|226,02|226,04|0,03714|0,65|0,15|2,82|0,89|
|400|0,1|225,59|225,86|225,69|225,86|0,00028|0,10|0,97|7,34|0,09|
|390|0,1|225,32|225,86|225,40|225,86|0,00000|0,02|4,51|10,87|0,01|
|380|0,1|225,07|225,86|225,12|225,86|0,00000|0,02|5,26|7,77|0,01|
|370|0,1|225,42|225,86|225,51|225,86|0,00003|0,05|2,22|9,27|0,03|
|360|0,1|225,43|225,86|225,53|225,86|0,00002|0,04|2,67|13,21|0,03|
|350|0,1|225,74|225,81|225,77|225,81|0,00127|0,13|0,80|14,06|0,17|
|340|0,1|225,02|225,70|225,12|225,70|0,00000|0,02|5,85|13,10|0,01|
|330|0,1|224,96|225,70|225,08|225,70|0,00000|0,03|3,98|10,59|0,01|
|320|0,1|225,59|225,69|225,68|225,70|0,04368|0,45|0,22|8,30|0,87|
|310|0,1|225,08|225,32|225,17|225,32|0,00029|0,10|1,03|8,70|0,09|
|300|0,1|225,14|225,31|225,21|225,31|0,00047|0,11|0,95|10,23|0,11|
|290|0,1|225,19|225,27|225,25|225,28|0,02152|0,45|0,22|4,78|0,67|
|280|0,1|224,89|225,01|225,00|225,03|0,02472|0,56|0,18|2,98|0,73|
|270|0,1|224,67|224,83|224,73|224,83|0,00024|0,08|1,21|11,22|0,08|
|260|0,1|224,60|224,83|224,68|224,83|0,00015|0,07|1,37|10,63|0,07|
|250|0,1|224,59|224,76|224,68|224,77|0,00133|0,17|0,59|6,87|0,18|
|240|0,1|224,38|224,76|224,45|224,76|0,00001|0,03|3,15|10,25|0,02|
|230|0,1|224,15|224,76|224,22|224,76|0,00000|0,02|4,28|9,63|0,01|
|220|0,1|224,11|224,76|224,20|224,76|0,00000|0,02|5,25|10,56|0,01|
|210|0,1|224,13|224,76|224,19|224,76|0,00000|0,02|6,01|10,50|0,01|
|200|0,1|223,80|224,76|223,89|224,76|0,00000|0,01|7,23|10,78|0,01|
|190|0,1|223,84|224,76|223,97|224,76|0,00000|0,02|6,62|12,95|0,01|
|180|0,1|223,93|224,76|224,05|224,76|0,00000|0,02|6,62|13,71|0,01|
|170|0,1|224,00|224,76|224,13|224,76|0,00000|0,01|6,79|13,31|0,01|
|160|0,1|224,00|224,76|224,06|224,76|0,00000|0,01|8,49|12,84|0,00|
|150|0,1|223,86|224,76|223,88|224,76|0,00000|0,01|10,80|13,78|0,00|
|140|0,1|223,77|224,76|223,82|224,76|0,00000|0,01|11,84|15,44|0,00|
|130|0,1|223,74|224,76|223,83|224,76|0,00000|0,01|12,46|18,14|0,00|
|120|11,9|223,67|224,74|224,19|224,76|0,00088|0,59|21,76|49,57|0,21|
|110|11,9|223,78|224,72|224,29|224,75|0,00164|0,77|15,64|22,45|0,29|
|100|11,9|223,71|224,58|224,41|224,70|0,00842|1,56|7,64|12,15|0,63|
|90|11,9|223,59|224,37|224,31|224,57|0,01555|1,96|6,07|10,98|0,84|
|80|11,9|223,42|224,18|224,18|224,41|0,02331|2,13|5,59|12,13|1,00|
|70|11,9|223,02|223,91|223,70|224,05|0,00914|1,68|7,10|10,60|0,65|
|60|11,9|222,62|223,89|223,40|223,97|0,00424|1,29|9,80|23,53|0,46|

126-EB-00-HID-MCA-01 **40**

MEMORIA DE CÁLCULO HIDRÁULICA
ESTUDIOS BÁSICOS

|Perfil|Q Total|Zfondo|ZH|ZHc|ZB|J|V|A|T|Fr|
|---|---|---|---|---|---|---|---|---|---|---|
||**[m3/s]**|**[msnm]**|**[msnm]**|**[msnm]**|**[msnm]**|**[m/m]**|**[m/s]**|**[m2]**|**[m]**|**[-]**|
|50|11,9|222,27|223,86|223,27|223,91|0,00336|1,11|14,49|41,46|0,40|
|40|11,9|222,56|223,83|223,35|223,88|0,00253|0,94|12,90|19,48|0,35|
|30|11,9|222,41|223,81|223,28|223,83|0,00169|0,58|21,07|46,88|0,26|
|20|11,9|221,70|222,47|222,68|223,13|0,08450|3,61|3,30|8,53|1,85|
|10|11,9|220,93|222,10|222,22|222,57|0,04215|3,05|3,90|6,64|1,27|
|0|11,9|220,67|221,59|221,16|221,61|0,00142|0,64|18,57|28,45|0,25|

126-EB-00-HID-MCA-01 **41**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3.1: Antecedentes Disponibles****

| Ref | Titulo | Autor |
| --- | --- | --- |
| 1 | Hidráulica | Francisco Domínguez |
| 2 | Levantamiento Topográfico escala 1:500 | Quarzo Ingeniería |
| 3 | Layout de Proyecto | EIC Ingenieros |

**Tabla 4.1: Condición de Borde de Aguas Abajo (Carga sobre el Vertedero)****

| Variable | Qd | Qd+15% | Qd+20% | Unidad | Descripción |
| --- | --- | --- | --- | --- | --- |
| L | 15 | 15 | 15 | [m] | Longitud Vertedero |
| m | 0,4 | 0,4 | 0,4 | [-] | Coeficiente de Gasto |
| h | 0,52 | 0,57 | 0,59 | [m] | Carga sobre el Vertedero |
| Q | 10,0 | 11,5 | 12,0 | [m3/s] | Caudal |
| Z | 221,52 | 221,57 | 221,59 | [msnm[] | Condición de Borde |

**Tabla 5.1: Resultados Situación Sin Proyectos. Q diseño = 10 [m3/s]****

| Perfiles | Q Total | Zfondo | ZH | ZHc | ZB | J | V | A | T | Fr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **[m3/s]** | **[msnm]** | **[msnm]** | **[msnm]** | **[msnm]** | **[m/m]** | **[m/s]** | **[m2]** | **[m]** | **[-]** |
| 796,57 | 10,0 | 230,37 | 231,42 | 231,12 | 231,61 | 0,00976 | 1,92 | 5,20 | 4,98 | 0,60 |
| 790 | 10,0 | 230,25 | 231,39 | 231,00 | 231,53 | 0,00640 | 1,66 | 6,01 | 5,61 | 0,51 |
| 780 | 10,0 | 229,97 | 231,36 | 230,78 | 231,45 | 0,00382 | 1,38 | 7,27 | 6,30 | 0,41 |
| 770 | 10,0 | 229,94 | 231,19 | 230,65 | 231,29 | 0,00408 | 1,41 | 7,09 | 6,31 | 0,42 |
| 760 | 10,0 | 229,79 | 230,46 | 230,62 | 231,04 | 0,05566 | 3,37 | 2,97 | 5,59 | 1,48 |
| 750 | 10,0 | 229,59 | 230,53 | 230,34 | 230,74 | 0,01107 | 2,01 | 4,97 | 5,84 | 0,70 |
| 740 | 10,0 | 229,43 | 230,34 | 230,17 | 230,56 | 0,01166 | 2,05 | 4,89 | 5,88 | 0,72 |
| 730 | 10,0 | 229,26 | 229,93 | 229,99 | 230,34 | 0,03150 | 2,84 | 3,52 | 5,66 | 1,15 |
| 720 | 10,0 | 229,08 | 229,74 | 229,81 | 230,16 | 0,03336 | 2,89 | 3,47 | 5,64 | 1,18 |
| 710 | 10,0 | 228,76 | 229,90 | 229,38 | 229,91 | 0,00102 | 0,57 | 17,54 | 26,16 | 0,22 |
| 700 | 10,0 | 228,18 | 229,90 | 229,22 | 229,90 | 0,00033 | 0,37 | 26,68 | 31,54 | 0,13 |
| 690 | 10,0 | 229,05 | 229,87 | 229,41 | 229,90 | 0,00114 | 0,64 | 15,55 | 21,05 | 0,24 |
| 680 | 10,0 | 228,96 | 229,70 | 229,66 | 229,84 | 0,02010 | 1,65 | 6,05 | 16,71 | 0,88 |
| 670 | 10,0 | 228,79 | 229,42 | 229,42 | 229,59 | 0,02535 | 1,82 | 5,49 | 16,04 | 0,99 |
| 660 | 10,0 | 228,54 | 229,26 | 229,06 | 229,36 | 0,00722 | 1,43 | 7,04 | 13,19 | 0,58 |
| 650 | 10,0 | 228,32 | 228,99 | 228,86 | 229,13 | 0,01074 | 1,64 | 6,10 | 10,75 | 0,69 |
| 640 | 10,0 | 228,24 | 228,88 | 228,77 | 229,01 | 0,01149 | 1,58 | 6,33 | 12,57 | 0,71 |
| 630 | 10,0 | 227,77 | 228,62 | 228,42 | 228,76 | 0,00870 | 1,67 | 5,98 | 8,21 | 0,63 |
| 620 | 10,0 | 227,50 | 228,56 | 228,19 | 228,69 | 0,00576 | 1,56 | 6,40 | 6,55 | 0,51 |
| 610 | 10,0 | 227,28 | 228,43 | 228,14 | 228,58 | 0,00807 | 1,74 | 5,75 | 6,29 | 0,58 |
| 600 | 10,0 | 226,43 | 228,40 | 227,79 | 228,51 | 0,00447 | 1,46 | 6,85 | 5,32 | 0,41 |
| 590 | 10,0 | 226,63 | 228,40 | 227,62 | 228,46 | 0,00227 | 1,14 | 8,79 | 6,91 | 0,31 |

**Tabla 5.2: Resultados Situación Con Proyectos. Q diseño = 10 [m3/s]****

| Perfil | Q Total | Zfondo | ZH | ZHc | ZB | J | V | A | T | Fr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **[m3/s]** | **[msnm]** | **[msnm]** | **[msnm]** | **[msnm]** | **[m/m]** | **[m/s]** | **[m2]** | **[m]** | **[-]** |
| 796,57 | 0,1 | 230,37 | 230,42 | 230,41 | 230,43 | 0,01313 | 0,38 | 0,26 | 4,95 | 0,53 |
| 790 | 0,1 | 230,25 | 230,33 | 230,32 | 230,34 | 0,01645 | 0,40 | 0,25 | 5,08 | 0,58 |
| 780 | 0,1 | 229,97 | 230,24 | 230,07 | 230,24 | 0,00024 | 0,11 | 0,91 | 5,24 | 0,08 |
| 770 | 0,1 | 229,94 | 230,09 | 229,98 | 230,09 | 0,00041 | 0,13 | 0,77 | 5,35 | 0,11 |
| 760 | 0,1 | 229,79 | 229,86 | 229,84 | 229,87 | 0,01763 | 0,52 | 0,19 | 2,77 | 0,63 |
| 750 | 0,1 | 229,59 | 229,66 | 229,63 | 229,67 | 0,00773 | 0,33 | 0,30 | 4,78 | 0,42 |
| 740 | 0,1 | 229,43 | 229,49 | 229,47 | 229,50 | 0,01304 | 0,39 | 0,26 | 4,75 | 0,53 |
| 730 | 0,1 | 229,26 | 229,31 | 229,29 | 229,32 | 0,01591 | 0,41 | 0,24 | 4,82 | 0,58 |
| 720 | 0,1 | 229,08 | 229,17 | 229,12 | 229,18 | 0,00289 | 0,24 | 0,42 | 5,05 | 0,27 |
| 710 | 0,1 | 228,76 | 229,17 | 228,87 | 229,17 | 0,00002 | 0,04 | 2,57 | 11,43 | 0,03 |
| 700 | 0,1 | 228,18 | 229,17 | 228,37 | 229,17 | 0,00001 | 0,02 | 5,10 | 25,76 | 0,01 |
| 690 | 0,1 | 229,05 | 229,17 | 229,08 | 229,17 | 0,00027 | 0,07 | 1,34 | 16,16 | 0,08 |
| 680 | 0,1 | 228,96 | 229,10 | 229,08 | 229,12 | 0,01745 | 0,54 | 0,19 | 2,53 | 0,64 |
| 670 | 0,1 | 228,79 | 228,92 | 228,91 | 228,94 | 0,02742 | 0,60 | 0,17 | 2,69 | 0,78 |
| 660 | 0,1 | 228,54 | 228,58 | 228,60 | 228,66 | 0,52628 | 1,25 | 0,08 | 4,14 | 2,86 |
| 650 | 0,1 | 228,32 | 228,42 | 228,39 | 228,42 | 0,00724 | 0,28 | 0,36 | 6,91 | 0,39 |
| 640 | 0,1 | 228,24 | 228,31 | 228,31 | 228,33 | 0,04391 | 0,57 | 0,17 | 4,43 | 0,93 |
| 630 | 0,1 | 227,77 | 227,84 | 227,85 | 227,88 | 0,09140 | 0,84 | 0,12 | 2,92 | 1,33 |
| 620 | 0,1 | 227,50 | 227,61 | 227,55 | 227,62 | 0,00163 | 0,19 | 0,52 | 5,77 | 0,20 |
| 610 | 0,1 | 227,28 | 227,60 | 227,49 | 227,60 | 0,00045 | 0,13 | 0,78 | 5,73 | 0,11 |
| 600 | 0,1 | 226,43 | 227,60 | 226,65 | 227,60 | 0,00001 | 0,04 | 2,78 | 4,73 | 0,02 |
| 590 | 0,1 | 226,63 | 227,60 | 226,75 | 227,60 | 0,00000 | 0,03 | 3,85 | 6,00 | 0,01 |
| 580 | 0,1 | 226,88 | 227,60 | 226,99 | 227,60 | 0,00000 | 0,02 | 4,07 | 8,60 | 0,01 |
| 570 | 0,1 | 227,42 | 227,60 | 227,55 | 227,60 | 0,01005 | 0,30 | 0,34 | 7,48 | 0,45 |
| 560 | 0,1 | 227,27 | 227,41 | 227,40 | 227,43 | 0,02769 | 0,67 | 0,15 | 2,13 | 0,80 |
| 550 | 0,1 | 226,93 | 227,31 | 227,06 | 227,31 | 0,00021 | 0,11 | 0,90 | 4,67 | 0,08 |
| 540 | 0,1 | 227,11 | 227,27 | 227,24 | 227,29 | 0,01329 | 0,51 | 0,19 | 2,36 | 0,57 |
| 530 | 0,1 | 227,01 | 227,16 | 227,09 | 227,16 | 0,00258 | 0,24 | 0,42 | 4,84 | 0,26 |
| 520 | 0,1 | 227,03 | 227,13 | 227,09 | 227,13 | 0,00427 | 0,21 | 0,47 | 9,43 | 0,30 |
| 510 | 0,1 | 226,98 | 227,07 | 227,06 | 227,07 | 0,01583 | 0,28 | 0,35 | 12,04 | 0,53 |
| 500 | 0,1 | 226,70 | 226,82 | 226,82 | 226,84 | 0,04149 | 0,61 | 0,17 | 3,72 | 0,92 |
| 490 | 0,1 | 226,32 | 226,60 | 226,44 | 226,60 | 0,00063 | 0,16 | 0,61 | 4,14 | 0,14 |
| 480 | 0,1 | 226,36 | 226,58 | 226,50 | 226,59 | 0,00357 | 0,31 | 0,32 | 2,91 | 0,30 |
| 470 | 0,1 | 226,41 | 226,53 | 226,50 | 226,54 | 0,00805 | 0,33 | 0,30 | 4,93 | 0,42 |
| 460 | 0,1 | 226,33 | 226,47 | 226,42 | 226,47 | 0,00529 | 0,24 | 0,42 | 8,00 | 0,34 |
| 450 | 0,1 | 226,20 | 226,34 | 226,27 | 226,34 | 0,00124 | 0,13 | 0,75 | 11,76 | 0,17 |
| 440 | 0,1 | 226,03 | 226,34 | 226,07 | 226,34 | 0,00003 | 0,05 | 2,18 | 9,39 | 0,03 |
| 430 | 0,1 | 225,97 | 226,34 | 226,12 | 226,34 | 0,00035 | 0,14 | 0,72 | 3,88 | 0,10 |
| 420 | 0,1 | 226,17 | 226,28 | 226,27 | 226,29 | 0,01817 | 0,44 | 0,22 | 4,21 | 0,61 |
| 410 | 0,1 | 225,91 | 226,02 | 226,02 | 226,04 | 0,03714 | 0,65 | 0,15 | 2,82 | 0,89 |
| 400 | 0,1 | 225,59 | 225,86 | 225,69 | 225,86 | 0,00028 | 0,10 | 0,97 | 7,34 | 0,09 |
| 390 | 0,1 | 225,32 | 225,86 | 225,40 | 225,86 | 0,00000 | 0,02 | 4,51 | 10,87 | 0,01 |
| 380 | 0,1 | 225,07 | 225,86 | 225,12 | 225,86 | 0,00000 | 0,02 | 5,26 | 7,77 | 0,01 |
| 370 | 0,1 | 225,42 | 225,86 | 225,51 | 225,86 | 0,00003 | 0,05 | 2,22 | 9,27 | 0,03 |
| 360 | 0,1 | 225,43 | 225,86 | 225,53 | 225,86 | 0,00002 | 0,04 | 2,67 | 13,21 | 0,03 |

**Tabla 5.3: Comparación Eje hidráulico****

| River Sta | Zfondo | ZH | Col4 | Col5 | ZB | Col7 | Col8 | Vel | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **River Sta** | **Zfondo** | **S.Proy** | **C Proy.** | **ZH** | **S.Proy** | **C Proy.** | **ZB** | **S.Proy** | **C Proy.** | **V ** |
| **River Sta** | **[m]** | **[msnm]** | **[msnm]** | **[m]** | **[msnm]** | **[msnm]** | **[m]** | **[m/s]** | **[m/s]** | **[m/s]** |
| 796,57 | 230,37 | 231,42 | 230,42 | -1,00 | 231,61 | 230,43 | -1,18 | 1,92 | 0,38 | -1,54 |
| 790 | 230,25 | 231,39 | 230,33 | -1,06 | 231,53 | 230,34 | -1,19 | 1,66 | 0,40 | -1,26 |
| 780 | 229,97 | 231,36 | 230,24 | -1,12 | 231,45 | 230,24 | -1,21 | 1,38 | 0,11 | -1,27 |
| 770 | 229,94 | 231,19 | 230,09 | -1,10 | 231,29 | 230,09 | -1,20 | 1,41 | 0,13 | -1,28 |
| 760 | 229,79 | 230,46 | 229,86 | -0,60 | 231,04 | 229,87 | -1,17 | 3,37 | 0,52 | -2,85 |
| 750 | 229,59 | 230,53 | 229,66 | -0,87 | 230,74 | 229,67 | -1,07 | 2,01 | 0,33 | -1,68 |
| 740 | 229,43 | 230,34 | 229,49 | -0,85 | 230,56 | 229,50 | -1,06 | 2,05 | 0,39 | -1,66 |
| 730 | 229,26 | 229,93 | 229,31 | -0,62 | 230,34 | 229,32 | -1,02 | 2,84 | 0,41 | -2,43 |
| 720 | 229,08 | 229,74 | 229,17 | -0,57 | 230,16 | 229,18 | -0,98 | 2,89 | 0,24 | -2,65 |
| 710 | 228,76 | 229,90 | 229,17 | -0,73 | 229,91 | 229,17 | -0,74 | 0,57 | 0,04 | -0,53 |
| 700 | 228,18 | 229,90 | 229,17 | -0,73 | 229,90 | 229,17 | -0,73 | 0,37 | 0,02 | -0,35 |
| 690 | 229,05 | 229,87 | 229,17 | -0,70 | 229,90 | 229,17 | -0,73 | 0,64 | 0,07 | -0,57 |
| 680 | 228,96 | 229,70 | 229,10 | -0,60 | 229,84 | 229,12 | -0,72 | 1,65 | 0,54 | -1,11 |
| 670 | 228,79 | 229,42 | 228,92 | -0,50 | 229,59 | 228,94 | -0,65 | 1,82 | 0,60 | -1,22 |
| 660 | 228,54 | 229,26 | 228,58 | -0,68 | 229,36 | 228,66 | -0,70 | 1,43 | 1,25 | -0,18 |
| 650 | 228,32 | 228,99 | 228,42 | -0,57 | 229,13 | 228,42 | -0,71 | 1,64 | 0,28 | -1,36 |
| 640 | 228,24 | 228,88 | 228,31 | -0,57 | 229,01 | 228,33 | -0,68 | 1,58 | 0,57 | -1,01 |
| 630 | 227,77 | 228,62 | 227,84 | -0,78 | 228,76 | 227,88 | -0,88 | 1,67 | 0,84 | -0,83 |
| 620 | 227,5 | 228,56 | 227,61 | -0,95 | 228,69 | 227,62 | -1,07 | 1,56 | 0,19 | -1,37 |
| 610 | 227,28 | 228,43 | 227,60 | -0,83 | 228,58 | 227,60 | -0,98 | 1,74 | 0,13 | -1,61 |
| 600 | 226,43 | 228,40 | 227,60 | -0,80 | 228,51 | 227,60 | -0,91 | 1,46 | 0,04 | -1,42 |
| 590 | 226,63 | 228,40 | 227,60 | -0,80 | 228,46 | 227,60 | -0,86 | 1,14 | 0,03 | -1,11 |
| 580 | 226,88 | 228,40 | 227,60 | -0,80 | 228,44 | 227,60 | -0,84 | 0,88 | 0,02 | -0,86 |
| 570 | 227,42 | 228,35 | 227,60 | -0,75 | 228,41 | 227,60 | -0,81 | 1,13 | 0,30 | -0,83 |
| 560 | 227,27 | 228,22 | 227,41 | -0,81 | 228,30 | 227,43 | -0,87 | 1,22 | 0,67 | -0,55 |
| 550 | 226,93 | 228,19 | 227,31 | -0,88 | 228,24 | 227,31 | -0,93 | 1,01 | 0,11 | -0,90 |
| 540 | 227,11 | 228,10 | 227,27 | -0,83 | 228,18 | 227,29 | -0,89 | 1,31 | 0,51 | -0,80 |
| 530 | 227,01 | 227,58 | 227,16 | -0,42 | 227,95 | 227,16 | -0,79 | 2,68 | 0,24 | -2,44 |
| 520 | 227,03 | 227,69 | 227,13 | -0,56 | 227,79 | 227,13 | -0,66 | 1,41 | 0,21 | -1,20 |
| 510 | 226,98 | 227,56 | 227,07 | -0,49 | 227,68 | 227,07 | -0,61 | 1,48 | 0,28 | -1,20 |
| 500 | 226,7 | 227,47 | 226,82 | -0,65 | 227,57 | 226,84 | -0,73 | 1,39 | 0,61 | -0,78 |
| 490 | 226,32 | 227,41 | 226,60 | -0,81 | 227,50 | 226,60 | -0,90 | 1,28 | 0,16 | -1,12 |
| 480 | 226,36 | 227,28 | 226,58 | -0,70 | 227,42 | 226,59 | -0,83 | 1,65 | 0,31 | -1,34 |
| 470 | 226,41 | 227,21 | 226,53 | -0,68 | 227,30 | 226,54 | -0,76 | 1,29 | 0,33 | -0,96 |
| 460 | 226,33 | 227,20 | 226,47 | -0,73 | 227,23 | 226,47 | -0,76 | 0,86 | 0,24 | -0,62 |

**Tabla 5.4: Comparación Situación Sin y Con Proyecto. Q = 11,5 [m3/s]****

| Perfil | Zfondo | ZH | Col4 | Col5 | ZB | Col7 | Col8 | Vel | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **Zfondo** | **SP** | **CP** | **ZH** | **SP** | **CP** | **ZB** | **SP** | **CP** | **V ** |
| **Perfil** | **[m]** | **[msnm]** | **[msnm]** | **[m]** | **[msnm]** | **[msnm]** | **[m]** | **[m/s]** | **[m/s]** | **[m/s]** |
| 140 | 223,77 | 224,75 | 224,74 | -0,01 | 224,80 | 224,74 | -0,06 | 1,00 | 0,01 | -0,99 |
| 130 | 223,74 | 224,72 | 224,74 | 0,02 | 224,77 | 224,74 | -0,03 | 0,98 | 0,01 | -0,97 |
| **120** | **223,67** | **224,73** | **224,72** | **-0,01** | **224,74** | **224,74** | **0,00** | **0,59** | **0,59** | **0,00** |
| 110 | 223,78 | 224,70 | 224,70 | 0,00 | 224,73 | 224,73 | 0,00 | 0,76 | 0,76 | 0,00 |
| 100 | 223,71 | 224,57 | 224,56 | -0,01 | 224,69 | 224,68 | -0,01 | 1,54 | 1,53 | -0,01 |
| 90 | 223,59 | 224,36 | 224,36 | 0,00 | 224,55 | 224,55 | 0,00 | 1,93 | 1,93 | 0,00 |
| 80 | 223,42 | 224,17 | 224,17 | 0,00 | 224,40 | 224,39 | -0,01 | 2,10 | 2,10 | 0,00 |
| 70 | 223,02 | 223,90 | 223,89 | -0,01 | 224,03 | 224,03 | 0,00 | 1,65 | 1,64 | -0,01 |
| 60 | 222,62 | 223,88 | 223,87 | -0,01 | 223,96 | 223,95 | -0,01 | 1,27 | 1,26 | -0,01 |
| 50 | 222,27 | 223,85 | 223,85 | 0,00 | 223,90 | 223,90 | 0,00 | 1,10 | 1,09 | -0,01 |
| 40 | 222,56 | 223,82 | 223,82 | 0,00 | 223,87 | 223,86 | -0,01 | 0,92 | 0,91 | -0,01 |
| 30 | 222,41 | 223,80 | 223,79 | -0,01 | 223,81 | 223,81 | 0,00 | 0,57 | 0,57 | 0,00 |
| 20 | 221,7 | 222,46 | 222,46 | 0,00 | 223,11 | 223,11 | 0,00 | 3,58 | 3,57 | -0,01 |
| 10 | 220,93 | 222,08 | 222,08 | 0,00 | 222,55 | 222,55 | 0,00 | 3,04 | 3,04 | 0,00 |
| 0 | 220,67 | 221,57 | 221,57 | 0,00 | 221,59 | 221,59 | 0,00 | 0,64 | 0,63 | -0,01 |

**Tabla 5.5: Comparación Situación Sin y Con Proyecto. Q = 11,5 [m3/s]****

| Perfil | Zfondo | ZH | Col4 | Col5 | ZB | Col7 | Col8 | Vel | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **Zfondo** | **SP** | **CP** | **ZH** | **SP** | **CP** | **ZB** | **SP** | **CP** | **V ** |
| **Perfil** | **[m]** | **[msnm]** | **[msnm]** | **[m]** | **[msnm]** | **[msnm]** | **[m]** | **[m/s]** | **[m/s]** | **[m/s]** |
| 140 | 223,77 | 224,77 | 224,76 | -0,01 | 224,82 | 224,76 | -0,06 | 1,02 | 0,01 | -1,01 |
| 130 | 223,74 | 224,74 | 224,76 | 0,02 | 224,79 | 224,76 | -0,03 | 0,99 | 0,01 | -0,98 |
| **120** | **223,67** | **224,75** | **224,74** | **-0,01** | **224,76** | **224,76** | **0,00** | **0,60** | **0,59** | **-0,01** |
| 110 | 223,78 | 224,72 | 224,72 | 0,00 | 224,75 | 224,75 | 0,00 | 0,77 | 0,77 | 0,00 |
| 100 | 223,71 | 224,58 | 224,58 | 0,00 | 224,71 | 224,70 | -0,01 | 1,56 | 1,56 | 0,00 |
| 90 | 223,59 | 224,38 | 224,37 | -0,01 | 224,57 | 224,57 | 0,00 | 1,97 | 1,96 | -0,01 |
| 80 | 223,42 | 224,18 | 224,18 | 0,00 | 224,42 | 224,41 | -0,01 | 2,13 | 2,13 | 0,00 |
| 70 | 223,02 | 223,91 | 223,91 | 0,00 | 224,05 | 224,05 | 0,00 | 1,68 | 1,68 | 0,00 |
| 60 | 222,62 | 223,89 | 223,89 | 0,00 | 223,97 | 223,97 | 0,00 | 1,30 | 1,29 | -0,01 |
| 50 | 222,27 | 223,86 | 223,86 | 0,00 | 223,91 | 223,91 | 0,00 | 1,11 | 1,11 | 0,00 |
| 40 | 222,56 | 223,84 | 223,83 | -0,01 | 223,88 | 223,88 | 0,00 | 0,94 | 0,94 | 0,00 |
| 30 | 222,41 | 223,81 | 223,81 | 0,00 | 223,83 | 223,83 | 0,00 | 0,58 | 0,58 | 0,00 |
| 20 | 221,7 | 222,47 | 222,47 | 0,00 | 223,14 | 223,13 | -0,01 | 3,61 | 3,61 | 0,00 |
| 10 | 220,93 | 222,10 | 222,10 | 0,00 | 222,58 | 222,57 | -0,01 | 3,06 | 3,05 | -0,01 |
| 0 | 220,67 | 221,59 | 221,59 | 0,00 | 221,61 | 221,61 | 0,00 | 0,65 | 0,64 | -0,01 |
