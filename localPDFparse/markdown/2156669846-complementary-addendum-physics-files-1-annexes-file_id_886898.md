---
title: Sin título
author: Alvaro  Gonzalez Vasquez
date: D:20240731190558-04'00'
language: es
type: report
pages: 93
has_toc: False
has_tables: True
extraction_quality: high
---

|Código interno|Col2|P-2023-136 PTAS Buin|Col4|Col5|
|---|---|---|---|---|
|Revisión / Versión|Fecha|Elaborado por|Revisado por|Aprobado por|
|RevA/Ver2|10-01-2024|TCO/FAM/MPP|MPP||
|RevB/Ver0|14-01-2024|MPP|MPP||
|RevC/Ver1|25-07-2024|TCO/FAM/MPP|MPP||
|RevD.Ver0|30-07-2024|TCO/FAM/MPP|MPP||
|RevD.Ver3|31-07-2024|TCO/FAM/MPP|MPP/DBQ||

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## Tabla de contenido

**1** **INTRODUCCIÓN .................................................................................................................................. 4**

**2** **OBJETIVOS .......................................................................................................................................... 4**

2.1 OBJETIVO GENERAL .............................................................................................................................. 4

2.2 O BJETIVOS ESPECÍFICOS .............................................................................................................................. 4

**3** **ZONA DE ESTUDIO .............................................................................................................................. 6**

**4** **ANTECEDENTES ................................................................................................................................... 8**

4.1 CALIDAD DEL AGUA .............................................................................................................................. 8

4.2 CARACTERIZACIÓN HIDRÁULICA ........................................................................................................ 12

_4.2.1_ _Topobatimetría ......................................................................................................................... 12_

_4.2.2_ _Aforos ....................................................................................................................................... 13_

**5** **CARACTERIZACIÓN HIDROLÓGICA .................................................................................................... 17**

5.1 DATOS HISTÓRICOS .............................................................................................................................. 1

5.2 CAUDALES ANUALES............................................................................................................................. 2

5.3 CAUDALES MEDIOS MENSUALES .......................................................................................................... 3

5.4 VARIACIÓN ESTACIONAL ...................................................................................................................... 4

**6** **ASPECTOS NORMATIVOS .................................................................................................................... 7**

**7** **MODELO DE DISPERSIÓN DE LA PLUMA CONTAMINANTE .................................................................. 9**

7.1 METODOLOGÍA GENERAL ..................................................................................................................... 9

7.2 IMPLEMENTACIÓN DEL MODELO QUAL2KW ....................................................................................... 9

_7.2.1_ _Estructura del modelo ............................................................................................................... 10_

_7.2.2_ _Datos fisicoquímicos ................................................................................................................. 13_

_7.2.3_ _Calibración ................................................................................................................................ 17_

_7.2.4_ _DEFINICIÓN DE ESCENARIOS DE SIMULACIÓN.......................................................................... 19_

7.3 MODELO DE DISPERSIÓN DE METALES ............................................................................................... 23

_7.3.1_ _Estructura de modelo de dispersión ......................................................................................... 23_

_7.3.2_ _Calibración ................................................................................................................................ 26_

_7.3.3_ _Escenarios simulados ................................................................................................................ 27_

7.4 MODELO DE DISPERSIÓN DE IONES .................................................................................................... 29

_7.4.1_ _Implementación del modelo ..................................................................................................... 29_

_7.4.2_ _Calibración ................................................................................................................................ 31_

_7.4.3_ _Generación de escenarios ......................................................................................................... 31_

**8** **RESULTADOS MODELACIÓN DE DISPERSIÓN..................................................................................... 33**

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

2

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

8.1 MODELO DE NUTRIENTES ................................................................................................................... 33

_8.1.1_ _Calibración ................................................................................................................................ 33_

_8.1.2_ _Simulación de escenarios de modelación ................................................................................. 41_

_8.1.3_ _Áreas de influencia ................................................................................................................... 48_

_8.1.4_ _Comentarios.............................................................................................................................. 49_

8.2 MODELO DE METALES ........................................................................................................................ 50

_8.2.1_ _Calibración ................................................................................................................................ 50_

_8.2.2_ _Simulación de escenarios .......................................................................................................... 52_

_8.2.3_ _Comentarios.............................................................................................................................. 56_

8.3 MODELO DE IONES ............................................................................................................................. 57

_8.3.1_ _Calibración ................................................................................................................................ 57_

_8.3.2_ _Simulación de escenarios .......................................................................................................... 59_

**9** **SITUACIÓN ACTUAL VS SITUACIÓN FUTURA ..................................................................................... 63**

9.1 CONCENTRACIÓN MÁXIMA ................................................................................................................ 63

9.2 LONGITUD DEL ÁREA DE INFLUENCIA ................................................................................................. 65

**10** **CONCLUSIONES ................................................................................................................................. 67**

**REFERENCIAS ............................................................................................................................................. 69**

**ANEXOS ..................................................................................................................................................... 70**

**ANEXO A - FICHAS TÉCNICAS DE AFORO .................................................................................................... 70**

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

3

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 1 INTRODUCCIÓN

La Planta de Tratamiento de Aguas Servidas Buin (en adelante PTAS Buin), propiedad de Aguas
Andina S.A. actualmente en evaluación ambiental solicita el estudio de dispersión para responder
las observaciones emitidas por autoridad en el ICSARA.

El presente informe tiene como finalidad presentar la metodología y los resultados de las campañas
de terreno, análisis fisicoquímico de los parámetros muestreados en campañas, el estudio
hidrológico de la zona de estudio y el modelo de dispersión implementado para determinar el área
de influencia de la PTAS en el río Maipo.

Se implementaron tres modelos. El primero se implementó para modelación de nutrientes y
parámetros fisicoquímicos in situ; el segundo para modelación de metales y el tercero para
modelación de cloruro y sulfato. De esta forma, se abordan la totalidad de los parámetros
fisicoquímicos establecidos en la Norma Secundaria de Calidad Ambiental.

## 2 OBJETIVOS

2.1 OBJETIVO GENERAL

Implementar modelos matemáticos para la simulación de nutrientes, metales y iones de la calidad
del agua en el canal de descarga y río Maipo, con el fin de evaluar el comportamiento actual y bajo

escenarios futuros.

2.2 Objetivos específicos

 - Desarrollar un estudio hidrológico realizado para caracterizar los cauces en estudio,

específicamente el río Maipo.

 - Analizar la fisicoquímica de la calidad de agua en el canal desagüe, en donde la PTAS realiza

la descarga del efluente y en el río Maipo.

 - Construir un modelo de dispersión mediante el modelo QUAL2Kw que simule la descarga

de la PTAS en el río Maipo y el comportamiento de los parámetros fisicoquímicos a lo largo

del Canal desagüe y el río Maipo. Los principales parámetros a modelar corresponden a los
nutrientes nitrógeno, nitrato, fósforo orgánico e inorgánico, oxígeno disuelto (OD),

demanda bioquímica de oxígeno (DBO 5 ) y coliformes fecales. Parámetros necesarios para

estudiar el desarrollo microbiológico y estado trófico del río Maipo.

 - Implementar el modelo matemático de simulación de la calidad del agua en WASP en el

Canal desagüe y río Maipo con el objetivo de identificar el efecto de los metales establecidos

en la Norma Secundaría de Calidad del Agua de la cuenca del río Maipo sobre el río Maipo

producto de la descarga de la PTAS Buin.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

4

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

 - Implementar un modelo matemático de los iones Cloruro (Cl-) y Sulfato (SO4) producto de

la descarga del efluente de la PTAS de Buin sobre el Canal desagüe y posteriormente sobre

el río Maipo.

 - Determinar las áreas de influencia que tiene la PTAS Buin sobre el río Maipo.

 - Comparar la situación actual con la situación futura de descarga de la PTAS Buin sobre el río

Maipo.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

5

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 3 ZONA DE ESTUDIO

El proyecto se ubica en la Región Metropolitana, específicamente en la comuna de Buin. En la Figura
3-1 se observa el área de estudio, detallando la ubicación de la PTAS Buin Maipo y su respectiva red
de descarga. La PTAS Buin descarga sus aguas al río Maipo mediante un canal acueducto soterrado.
Cuando el río Maipo presenta un caudal bajo, la salida de la descarga se conecta al cauce vivo
(sección del cauce cubierto de agua), mediante un canal desagüe que se forma sobre el cauce del
mismo río, el cual se ha denominado como Canal desagüe efluente (ver Figura 3-1).

**Figura 3-1. Zona de estudio de la PTAS Buin Maipo.**

Fuente: elaboración propia.

En la Figura 3-2 se presenta la descarga de la PTAS en el canal desagüe efluente, este es un canal
que transporta las aguas de la PTAS Buin y las descarga en el río Maipo y no corresponde a un canal
de riego, es parte de la caja del río. La zona muestra estancamiento del agua ante la nula descarga
de la PTAS, pero al momento de enviar pulsos de descarga la PTAS Buin, se ve un incremento en el
flujo del canal generando un incremento del caudal. Se debe destacar que el canal de desagüe
presenta un efluente cuyo uso de riego se verifico in situ al cual se le denominará “Canal de regadío”
para el resto del documento, este se muestra en la Figura 3-2 imagen de la derecha. Al momento de
funcionar la descarga, gran parte del caudal fluye por el canal de regadío, por lo que para el caso de
este estudio ambos canales fueron aforados. En el punto P2 el suelo está compuesto principalmente
por limo y grava, a diferencia de los taludes que están integrados mayoritariamente por vegetación.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

6

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 3-2. Fotografía en terreno punto P2 (aforo) - Canal descarga efluente PTAS Buin Maipo.**

Fuente: elaboración propia, basado en salidas a terreno.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

7

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 4 ANTECEDENTES

Se realizaron 4 campañas de terreno con el objetivo de inspeccionar la zona de estudio, realizar la
topobatimetría del área de interés, aforar caudal en tramos específicos del sistema y realizar
muestreos de calidad del agua y sedimentos, se debe destacar que la medición de caudal y calidad
del agua se realizan simultáneamente. En la Tabla 4-1 se presenta el detalle de las salidas a terreno
y en la Tabla 4-2 se indican los profesionales participantes de las campañas.

**Tabla 4-1. Detalles de las salidas a terreno.**

|Campaña|Fecha|Descripción|
|---|---|---|
|C1|Marzo 2022|Muestreo de calidad del agua|
|C2|Julio 2023|Determinación de batimetría, aforos y calidad del agua|
|C3|Abril 2024|Muestreo de calidad del agua|
|C4|Junio 2024|Muestreo de calidad del agua|

Fuente: elaboración propia.

**Tabla 4-2. Detalle de los profesionales participantes en las diferentes campañas.**

|Profesional|Nombre|Cargo|
|---|---|---|
|1|Luis Abrigo|Especialista de limnología y calidad del agua|
|2|Felipe Aguilar|Ingeniero de Proyecto|
|3|Tomás Cabrera|Ingeniero de Proyecto|

Fuente: elaboración propia.

4.1 CALIDAD DEL AGUA

Para efectos del proyecto y la caracterización de la zona de estudio se han realizado 4 campañas de
calidad del agua, la primera realizada en marzo del 2022, la segunda en julio del 2023, luego en abril
del 2024 y finalmente, en junio del 2024, como parte de la caracterización del ecosistema acuático.

Se definieron un total de 6 puntos de muestreos en la campaña de marzo de 2022, 8 puntos para la
campaña de julio 2023, y 7 puntos para las últimas dos campañas, los cuales se presentan en la Tabla
4-3 y en la Figura 4-1 se presenta la ubicación del total de estaciones de calidad del agua
muestreadas en las campañas.

**Tabla 4-3. Campañas y sus puntos de muestreo.**

|Punto|Campañas|Col3|Col4|Col5|Curso de agua|
|---|---|---|---|---|---|
|**Punto**|**Marzo 2022**|**Julio 2023**|**Abril 2024**|**Junio 2024**|**Junio 2024**|
|P1|X|X|X|X|Río Maipo|
|P1a|*|X|X|X|Río Maipo|
|P2|X|X|X|X|Canal desagüe efluente|
|P3|X|X|X|X|Canal desagüe efluente|
|P4|X|X|X|X|Canal desagüe efluente|
|P5|X|X|*|*|Río Maipo|
|P6|*|X|X|X|Río Maipo|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

8

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Punto|Campañas|Col3|Col4|Col5|Curso de agua|
|---|---|---|---|---|---|
|**Punto**|**Marzo 2022**|**Julio 2023**|**Abril 2024**|**Junio 2024**|**Junio 2024**|
|P7|*|X|X|X|Río Maipo|

(*) Sin muestreo.

Fuente: elaboración propia.

**Figura 4-1. Total de puntos de muestreo de calidad del agua y sedimentos para la campaña de julio del**

**2023.**

Fuente: elaboración propia.

En las campañas se midieron parámetros _in situ_ mediante sondas multiparamétricas y se tomaron
muestras de agua y sedimentos que luego fueron analizadas en laboratorio. Los parámetros
corresponden a los siguientes, los cuales se obtuvieron de aquellos muestreados para la LB de
limnología (Caracterización limnológica proyecto “Ampliación de la PTAS Buin”):

 - In situ: conductividad eléctrica, oxígeno disuelto, temperatura y pH.

 - Analizados en laboratorio: temperatura, conductividad eléctrica, demanda biológica de
oxígeno, nitrógeno orgánico, nitrógeno amoniacal, nitrato, nitrógeno total, nitrógeno total
Kjeldahl, fósforo orgánico, ortofosfato, coliformes fecales totales, pH y alcalinidad.

 - En campaña de julio de 2023, se incluyeron los metales Cromo total, plomo disuelto, zinc

disuelto y níquel disuelto. Además, se incluyó cloruros y sulfatos.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

9

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Por último, en la Tabla 4-4, Tabla 4-5, Tabla 4-6 y Tabla 4-7 se presentan los resultados del muestreo

de calidad del agua para las 4 campañas.

**Tabla 4-4. Resultados muestreo puntos P1 y P1a.**

|Parámetros|Unidad|P1|Col4|Col5|Col6|P1a|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Parámetros**|**Unidad**|**C1**|**C2**|**C3**|**C4**|**C1**|**C2**|**C3**|**C4**|
|Alcalinidad|mg/l|145|110|112|109|*|110|109|110|
|Temperatura|°C|14,5|6,41|9,1|9,92|*|7,59|10,6|9,79|
|Clorofila a|mg/l|*|27,9|1,36|0,8|*|57|0,32|0,92|
|Conductividad|us/cm|1597|1894|1549|1399|*|1939|1575|1402|
|Coliformes fecales|NMP/100ml|1,8|4900|640|490|*|1,8|230|230|
|OD|mg/l|6,99|14,67|9,03|5,25|*|14,8|10,6|5,27|
|pH|-|8,02|7,65|8,54|8,28|*|7,5|8,7|6,95|
|Nitrato|mg/l|1,2|3,8|1,9|2|*|2,9|1,8|1,5|
|Ortofosfato|mg/l|0,2|1,5|0,5|0,5|*|2,6|0,5|0,5|
|DBO5|mg/l|2|15,1|1|1|*|14,9|1|1|
|Nitrito|mg/l|0,03|0,05|0,039|0,039|*|0,03|0,039|0,028|
|Nitrógeno amoniacal|mg/l|*|0,58|0,16|0,02|*|1,52|0,02|0,02|
|NTK|mg/l|0,867|1,23|2,3|0,58|*|2,36|0,6|0,55|
|NT|mg/l|2,067|5,08|2,73|1,09|*|5,26|1,01|1,13|
|PT|mg/l|0,2|2,6|0,66|0,43|*|2,7|0,17|0,48|
|Fosfato|mg/l|*|0,13|0,05|0,05|*|0,13|0,05|0,05|
|Norg|mg/l|*|0,65|2,17|0,7|*|0,84|0,7|0,7|
|Porg|mg/l|*|1,1|*|*|*|0,2|*|*|

(*) Sin muestreo.

Fuente: elaboración propia.

**Tabla 4-5. Resultados muestreo puntos P2 y P3.**

|Parámetros|Unidad|P2|Col4|Col5|Col6|P3|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Parámetros**|**Unidad**|**C1**|**C2**|**C3**|**C4**|**C1**|**C2**|**C3**|**C4**|
|Alcalinidad|mg/l|145|144|2|155|175|146|2|115|
|Temperatura|°C|15,1|15,73|17,4|18,3|16,4|14,15|11|9,57|
|Clorofila a|mg/l|*|10|0,02|0,02|*|10|0,47|0,47|
|Conductividad|us/cm|1666|1753|1659|1545|1680|1752|1572|1413|
|Coliformes fecales|NMP/100ml|1,8|3300|640|2|1,8|1,8|240|23|
|OD|mg/l|5,36|9,61|7,26|3,63|5,45|10,23|11|5,05|
|pH|-|7,61|7,23|7,69|8,95|7,8|7,48|8,7|8,11|
|Nitrato|mg/l|14,4|11,6|27,1|8,86|7,3|11,7|0,203|1,5|
|Ortofosfato|mg/l|0,2|4,1|4,2|0,006|0,2|4|0,05|0,05|
|DBO5|mg/l|2,54|10,4|1|1|4,5|11,9|1|1|
|Nitrito|mg/l|0,03|0,03|0,039|0,005|0,23|0,03|0,039|0,039|
|Nitrógeno amoniacal|mg/l|*|0,98|0,02|0,02|*|0,58|0,02|0,02|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

10

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetros|Unidad|P2|Col4|Col5|Col6|P3|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Parámetros**|**Unidad**|**C1**|**C2**|**C3**|**C4**|**C1**|**C2**|**C3**|**C4**|
|NTK|mg/l|1,3|2,47|0,23|0,88|1,4|2,14|0,23|0,63|
|NT|mg/l|15,7|14,1|6,12|9,74|8,93|13,9|0,23|1,26|
|PT|mg/l|0,2|2,2|2,53|2,78|0,2|1,6|0,17|0,08|
|Fosfato|mg/l|*|0,13|4,235|8,002|*|0,13|0,05|0,05|
|Norg|mg/l|*|1,5|0,7|0,875|*|1,6|0,7|0,7|
|Porg|mg/l|*|0,2|*|*|*|0,2|*|*|

(*) Sin muestreo.

Fuente: elaboración propia.

**Tabla 4-6. Resultados muestreo puntos P4 y P5.**

|Parámetros|Unidad|P4|Col4|Col5|Col6|P5|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Parámetros**|**Unidad**|**C1**|**C2**|**C3**|**C4**|**C1**|**C2**|**C3**|**C4**|
|Alcalinidad|mg/l|167|151|2|111|162|110|*|*|
|Temperatura|°C|24,02|14,28|10,6|9,6|20,3|7,22|*|*|
|Clorofila a|mg/l|*|10,7|0,02|1,06||59,9|*|*|
|Conductividad|us/cm|1685|1752|1570|1410|1665|1944|*|*|
|Coliformes fecales|NMP/100ml|1,8|4900|330|330|1,8|35000|*|*|
|OD|mg/l|5,01|11,17|8,93|5,05|5,55|14,64|*|*|
|pH|-|7,95|7,55|8,72|8,28|8,32|7,36|*|*|
|Nitrato|mg/l|7,4|10,7|2,1|1,6|8,1|3,2|*|*|
|Ortofosfato|mg/l|0,2|4,2|0,06|0,5|0,2|2,6|*|*|
|DBO5|mg/l|2|19|1|1|2,47|14,4|*|*|
|Nitrito|mg/l|0,08|0,04|0,039|0,039|0,06|0,03|*|*|
|Nitrógeno amoniacal|mg/l||0,96|0,02|0,02||0,98|*|*|
|NTK|mg/l|1,7|1,97|0,23|0,5|1,2|1,57|*|*|
|NT|mg/l|9,18|12,7|0,47|0,9|9,36|4,77|*|*|
|PT|mg/l|0,2|2,3|0,35|0,2|0,2|4,1|*|*|
|Fosfato|mg/l|*|0,13|0,02|0,02|*|0,13|*|*|
|Norg|mg/l|*|1|0,7|0,7|*|0,59|*|*|
|Porg|mg/l|*|0,2|*|*|*|1,5|*|*|

(*) Sin muestreo.

Fuente: elaboración propia.

**Tabla 4-7. Resultados muestreo puntos P6 y P7.**

|Parámetros|Unidad|P6|Col4|Col5|Col6|P7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Parámetros**|**Unidad**|**C1**|**C2**|**C3**|**C4**|**C1**|**C2**|**C3**|**C4**|
|Alcalinidad|mg/l|*|112|111|111|*|110|113|110|
|Temperatura|°C|*|7,8|9,2|9,96|*|7,7|9,3|9,98|
|Clorofila a|mg/l|*|51,3|73|58|*|63,3|36|64|
|Conductividad|us/cm|*|1950|1575|1405|*|1945|1579|1404|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

11

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetros|Unidad|P6|Col4|Col5|Col6|P7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Parámetros**|**Unidad**|**C1**|**C2**|**C3**|**C4**|**C1**|**C2**|**C3**|**C4**|
|Coliformes fecales|NMP/100ml|*|35000|790|220|*|2000|490|960|
|OD|mg/l|*|14,37|9,04|5,5|*|14,45|9,18|5,47|
|pH|-|*|7,65|8,71|8,19|*|7,63|8,68|8,34|
|Nitrato|mg/l|*|3,2|0,203|1,4|*|2,8|1,9|1,1|
|Ortofosfato|mg/l|*|1,5|0,5|0,5|*|1,6|0,5|0,5|
|DBO5|mg/l|*|12,9|1|1|*|12,4|1|1|
|Nitrito|mg/l|*|0,03|0,039|0,039|*|0,03|0,039|0,015|
|Nitrógeno amoniacal|mg/l|*|0,96|0,02|0,02|*|1,02|0,02|0,02|
|NTK|mg/l|*|1,42|0,23|0,5|*|2,36|0,23|0,5|
|NT|mg/l|*|4,62|0,23|0,95|*|5,16|0,43|0,91|
|PT|mg/l|*|2|0,4|0,43|*|2,1|0,65|0,06|
|Fosfato|mg/l|*|0,13|0,05|0,05|*|0,13|0,05|0,05|
|Norg|mg/l|*|0,46|0,7|0,7|*|1,3|0,7|0,7|
|Porg|mg/l|*|0,5|*|*|*|0,5|*|*|

(*) Sin muestreo.

Fuente: elaboración propia.

4.2 CARACTERIZACIÓN HIDRÁULICA

_4.2.1_ _Topobatimetría_

En primera instancia, se realizó una inspección de la zona de estudio, definiendo los tramos a
modelar y sus respectivos afluentes y efluentes. La modelación incluye el canal efluente de la PTAS
Buin Maipo, el canal desagüe y el río Maipo. Por lo tanto, la batimetría tiene por objetivo caracterizar

dichos sectores.

Para el levantamiento batimétrico se utilizó un equipo Receptores GNSS Base y Móvil, el cual cuenta
con un GPS RTK base que permite corregir en tiempo real las coordenadas de un GPS RTK móvil, con
el cual se van tomando puntos en terreno de precisión milimétrica. Para esto se utilizó un equipo
Geomax Zenith 35 pro.

La metodología del terreno consistió en fijar un punto de referencia en la zona de la PTAS Buin
Maipo. En uno de esos puntos se fija el GPS RTK base y luego, con el GPS RTK móvil se van tomando
los puntos donde se requiera, considerando un rango máximo de 5 km. La tarea tuvo una duración
de una campaña.

En la Tabla 4-8 se presentan los detalles del punto de referencia, sus respectivas cotas y

coordenadas.

**Tabla 4-8. Coordenadas y cotas de los puntos de referencia.**

|PUNTO|UTM N [m]|UTM E [m]|COTA [msnm]|
|---|---|---|---|
|PR1|6.264.075|332.529|445|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

12

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

En la Figura 4-2 se presentan los resultados de la topobatimetría, los puntos medidos corresponden
a 440. Del total de los perfiles transversales medidos, 4 se ubican en el río Maipo y los demás se
ubican en el canal desagüe. Es relevante tener en cuenta que la imagen satelital no concuerda con
la fecha de la campaña de terreno, lo cual explica la presencia de puntos en áreas del río donde no
hay agua.

**Figura 4-2. Ubicación de los puntos medidos mediante topobatimetría.**

Fuente: elaboración propia.

_4.2.2_ _Aforos_

Al igual que para la batimetría, el objetivo de los aforos es caracterizar todos los tramos de interés
para la modelación, por lo que se planeó el aforo en 5 puntos: 3 sobre el canal desagüe (P2, P3 y
P4), uno sobre el canal de regadío (PA) y el último en el río Maipo (P5-1 y P5-2). En la Figura 4-3 se
presentan los puntos ubicados en el mapa, se debe destacar que en el río Maipo se midió en dos
puntos, ya que en la zona del punto P5, el río estaba dividido en dos brazos, por lo que se aforó cada
uno por separado y el caudal total corresponde a la suma de los dos. Producto de las condiciones
del río Maipo en la fecha de terreno no se logró realizar un aforo aguas arriba de la confluencia del
canal de desagüe con el río Maipo, no obstante, este valor se determina a partir de la diferencia
entre el aforo en el punto P5 y el P4 en el canal de desagüe dado que no existen afluentes entre
estas dos mediciones y cumplen con desfase de tiempo de 10 min para ser utilizados en el cálculo.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

13

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 4-3. Ubicación de los puntos de aforo.**

Fuente: elaboración propia.

Para la medición de velocidades del flujo, se utilizó un aforador tipo molinete electromagnético, el
cual mide velocidad en el punto específico donde se ubique. Como ya se mencionó, se aforó en 6
secciones transversales, en cada una de ellas se definió un perfil transversal donde se realizaron
mediciones cada 20, 30, 50 y 100 centímetros, dependiendo de su longitud y se realizaron dos
pasadas en cada uno. Los datos recopilados en cada punto son: velocidad, altura del sensor, altura
de escurrimiento y distancia en el perfil transversal, y así, teniendo características hidráulicas y
geométricas, estimar el caudal en cada tramo.

Para obtener la velocidad media en la vertical se determina mediante el método de los puntos, el
cual consiste en realizar distintas observaciones de velocidad en la vertical dependiendo de la altura

de escurrimiento. Para secciones donde la altura es menor a 50 cm se realiza una observación

colocando el molinete a un 60% de la profundidad total por debajo de la superficie libre. Para
profundidades superiores se toman dos observaciones, a un 20% y a un 80% de la profundidad de
la superficie libre y se usa el promedio de las dos medidas como la velocidad media en la vertical.

Para cada sección entre dos verticales, el área se calcula como el producto del promedio del alto
por el ancho, y la velocidad media como el promedio de las velocidades medidas en los puntos de
la vertical. El caudal se estima como el producto del área y la velocidad media, por lo tanto, el caudal
total corresponde a la suma de los caudales entre las verticales.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

14

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

A continuación, se presentan los resultados de los aforos y estimaciones de caudal siguiendo la
metodología expuesta. Además, en la Figura 4-4 se presenta el diagrama unifilar del sistema,
detallando las conexiones de sus diferentes componentes. En la sección de Anexos se presentan las
fichas técnicas de los aforos realizados. Se debe destacar que no se obtuvo el promedio de caudal
para un mismo punto, ya que los caudales difieren considerablemente debido a que entre las
mediciones aumentos de caudal del efluente de la PTAS Buin Maipo debido al funcionamiento de
pulso que presenta la PTAS.

En este sentido, se considerarán como caudales horarios, los cuales serán tenidos en cuenta al

momento de la calibración del modelo.

**Tabla 4-9. Resultados de los aforos.**

|Punto|Caudal [m3/s]|Hora|Caudal [L/s]|Detalle|
|---|---|---|---|---|
|P2|0,0008|10:05|0,8|Canal desagüe|
|P2|0,0005|10:25|0,5|Canal desagüe|
|P2|0,0177|10:51|17,7|Canal desagüe|
|PA|0,1673|10:30|167,3|Canal regadío|
|PA|0,0735|10:40|73,5|Canal regadío|
|P3|0,0242|11:20|24,2|Canal desagüe|
|P3|0,0173|11:40|17,3|Canal desagüe|
|P4'|0,0105|12:15|10,5|Canal desagüe|
|P4'|0,0088|12:40|8,8|Canal desagüe|
|P5 - 1|1,3769|13:00|1376,9|Río Maipo|
|P5 - 2|4,0279|13:30|4027,9|Río Maipo|

Fuente: elaboración propia a partir de ficha de terreno (ver Anexo A).

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

15

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

**Figura 4-4. Diagrama unifilar.**

Fuente: elaboración propia.

16

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 5 CARACTERIZACIÓN HIDROLÓGICA

El río Maipo a la altura de la descarga de la PTAS Buin es un río altamente modificado, tanto en su
régimen hidrológico, como la morfología fluvial. El régimen hidrológico se ve modificado. Entre la
estación fluviométrica El Manzano y la descarga, existen X extracciones de agua para agua potable,
riego y generación hidroeléctrica.

Entre las principales bocatomas existentes se distinguen la Plata de tratamiento de agua potable de
Aguas Andinas (La Vizcachas) y las captaciones de uso para las plantas de agua potable para La
Florida, Padre Hurtado y Chamisero. Entre los usos para riegos, destacan la Sociedad Canal De Maipo
(SCM), Asociación Canales del Maipo (ACM), Asociación Canal Unidos de Buin (ACUB), Asociación
Canal Huidobro (ACH), Asociación Canalistas Lo Herrera (ACLH), Asociación Canalistas Lonquén - La
Isla (ACIL), Asociación Canalistas Canal de Pirque (ACCP). Y finalmente las centrales hidroeléctricas
Florida, Puntilla y CARBOMET-CAEMSA. En la fig se muestra un diagrama unifilar de las extracciones
y usuarios del río Maipo entre la estación fluviométrica El Manzano y la descarga del efluente de la

PTAS Buin

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

17

**Figura 5-1 Diagrama unifilar de la primera sección del río Maipo**

Fuente: información entregada por el Titular

Entre los usos consuntivos, existen porcentajes de participación, los cuales son equivalentes a las
acciones de riego (ver Tabla 5-1). A partir del caudal estimado en el río Maipo y a dichos porcentajes,

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Entre los usos consuntivos, existen porcentajes de participación, los cuales son equivalentes a las acciones de riego (ver Tabla 5-1). A partir del caudal estimado en el río Maipo y a dichos porcentajes, se estima que el caudal de extracción de cada usuario y por tanto el remanente sobre el río Maipo -->

**Tabla 5-1: Porcentaje de participación de los principales usuarios aguas arriba de la descarga de la PTAS Buin.****

| Col1 | ACCP | SCM | ACM | ACH | ACUB | ACIL | ACLH | Aguas<br>Andinas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Acciones** | 650,535 | 1845,475 | 1584,858 | 647,737 | 1042,265 | 30,253 | 53,739 | 2250,770 |
| % de<br>participación | 8,0% | 22,8% | 19,6% | 8,0% | 12,9% | 0,4% | 0,7% | 27,8% |

<!-- Estadísticas: 2 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: información entregada por el Titular Por otra parte, Aguas Andinas también es uno de los usuarios y debe satisfacer la demanda de agua potable para Santiago. Las estimaciones de demanda se muestran en la Tabla 5-2. -->
<!-- FIN TABLA 5-1 -->

se estima que el caudal de extracción de cada usuario y por tanto el remanente sobre el río Maipo

**Tabla 5-1 Porcentaje de participación de los principales usuarios aguas arriba de la descarga de la PTAS Buin.**

|Col1|ACCP|SCM|ACM|ACH|ACUB|ACIL|ACLH|Aguas<br>Andinas|
|---|---|---|---|---|---|---|---|---|
|**Acciones**|650,535|1845,475|1584,858|647,737|1042,265|30,253|53,739|2250,770|
|% de<br>participación|8,0%|22,8%|19,6%|8,0%|12,9%|0,4%|0,7%|27,8%|

Fuente: información entregada por el Titular

Por otra parte, Aguas Andinas también es uno de los usuarios y debe satisfacer la demanda de agua
potable para Santiago. Las estimaciones de demanda se muestran en la Tabla 5-2.

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: información entregada por el Titular Por otra parte, Aguas Andinas también es uno de los usuarios y debe satisfacer la demanda de agua potable para Santiago. Las estimaciones de demanda se muestran en la Tabla 5-2. -->

**Tabla 5-2: promedio mensual demanda de Captación Aguas Andinas****

| Mes | Caudal [m3/s] |
| --- | --- |
| Enero | 21,2 |
| Febrero | 21,1 |
| Marzo | 21,2 |
| Abril | 20,6 |
| Mayo | 18,5 |
| Junio | 18,0 |
| Julio | 15,9 |
| Agosto | 18,2 |
| Septiembre | 18,8 |
| Octubre | 19,2 |
| Noviembre | 19,3 |
| Diciembre | 21,4 |

<!-- Estadísticas: 12 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: información entregada por el titular 5.1 DATOS HISTÓRICOS -->
<!-- FIN TABLA 5-2 -->


**Tabla 5-2 promedio mensual demanda de Captación Aguas Andinas**

|Mes|Caudal [m3/s]|
|---|---|
|Enero|21,2|
|Febrero|21,1|
|Marzo|21,2|
|Abril|20,6|
|Mayo|18,5|
|Junio|18,0|
|Julio|15,9|
|Agosto|18,2|
|Septiembre|18,8|
|Octubre|19,2|
|Noviembre|19,3|
|Diciembre|21,4|

Fuente: información entregada por el titular

5.1 DATOS HISTÓRICOS

Aguas Andinas realiza estimaciones del caudal sobre el río Maipo aguas arriba del canal La Sirena,
Considerando este caudal, los porcentajes de participación de los usuarios aguas arriba de la
descarga de la PTAS Buin y la demanda promedio de agua potable, se determinó el caudal medio
mensual remanente aguas abajo de las extracciones indicadas, y por tanto, en el río Maipo a la altura
de la descarga de la PTAS Buin. Los caudales medios mensuales se muestran en la Tabla 5-3.

**Tabla 5-3. Caudales mensuales.**

|Año|Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sept|Oct|Nov|Dic|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2009|35,2|20,1|3,2|0,0|0,8|0,0|0,0|0,0|7,9|1,9|9,5|38,8|
|2010|39,1|24,8|8,0|0,7|0,0|0,0|0,0|0,0|0,0|0,2|1,3|1,3|
|2011|0,1|0,2|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|2,7|5,1|

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Año|Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sept|Oct|Nov|Dic|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2012|3,9|1,0|0,0|0,0|8,6|0,4|0,3|0,0|0,0|0,0|10,0|10,1|
|2013|15,6|6,2|0,0|0,0|0,0|0,0|0,0|0,0|0,3|0,0|5,7|14,5|
|2014|5,8|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,4|1,8|2,2|
|2015|1,3|0,1|0,0|0,0|0,0|0,0|0,0|1,2|0,0|0,0|7,6|21,0|
|2016|21,6|9,2|0,5|12,5|1,8|2,0|0,1|0,0|1,5|2,3|17,3|24,4|
|2017|28,9|11,4|0,4|2,3|0,0|0,2|0,0|0,0|0,0|0,3|7,5|11,4|
|2018|3,2|2,9|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|1,5|4,0|
|2019|3,2|1,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|
|2020|1,0|0,1|0,1|0,0|0,0|0,0|0,0|0,0|0,0|0,8|3,0|1,5|
|2021|4,6|0,8|0,0|0,0|0,0|0,0|0,0|0,1|0,0|0,2|0,1|0,3|
|2022|1,0|0,2|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|2,2|0,8|
|2023|0,2|0,4|0,0|0,0|0,0|14,7|0,0|3,3|1,2|3,4|14,3|40,7|

Fuente: elaboración propia en funcion de informacion entregada por el cliente

Se aprecia que el caudal sobre el río Maipo resulta ser nulo principalmente en el invierno, mientras
que en la época de deshielo existe un remanente. En resumen, es posible indicar que la hidrología
del río está altamente intervenida en esta zona, dejando al río con caudal nulo en todos los inviernos

desde el año 2009 en adelante.

5.2 CAUDALES ANUALES

A continuación, en la Tabla 5-4 se presentan los caudales anuales para analizar las variaciones
interanuales, y en la Figura 5-2 se muestran los resultados gráficamente. Analizando el gráfico de
caudales anuales no se ve una tendencia clara al aumento o disminución de caudales, se evidencian
4 años con caudales superiores a los 6 m [3] /s (2009, 2010, 2016 y 2023), y el promedio de todos los
años con registros es de 3,2 m [3] /s. El valor máximo corresponde a 9,8 m [3] /s en el año 2009 y el mínimo
corresponde a 0,3 m [3] /s el año 2022.

Además, se presenta la ecuación lineal que representa la tendencia de la muestra de datos, la cual
indica una pendiente negativa, es decir, una disminución del caudal medio anual.

**Tabla 5-4. Caudales anuales.**

|Año|Promedio anual [m3/s]|
|---|---|
|2009|9,8|
|2010|6,3|
|2011|0,7|
|2012|2,8|
|2013|3,5|
|2014|0,9|
|2015|2,6|
|2016|7,8|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

2

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

12

10

8

6

4

2

0

|Año|Promedio anual [m3/s]|
|---|---|
|2017|5,2|
|2018|1,0|
|2019|0,3|
|2020|0,5|
|2021|0,5|
|2022|0,3|
|2023|6,5|

Fuente: elaboración propia en función de .

**Figura 5-2. Caudales medios anuales.**

Caudal medio anual

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
||||||||||y|y||||961||
||||||||||y|y|= -0,2|684x|+ 5,3|961|961|
|||||||||||||||||
|||||||||||||||||

2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023

Año

Fuente: elaboración propia.

5.3 CAUDALES MEDIOS MENSUALES

A continuación, en la Tabla 5-5 se presentan los caudales medios mensuales para analizar la
estacionalidad de la cuenca en estudio, y en la Figura 5-3 se muestran los resultados gráficamente.
Analizando el gráfico de caudales medios mensuales se concluye la estacionalidad de la cuenca, la
cual posee un régimen nival, es decir, se perciben aumentos en el periodo de verano producto del
derretimiento nival. Por lo tanto, el periodo de estiaje se da en los meses de marzo a octubre,
momento en el cual los aportes por el derretimiento de nieve se acaba.

**Tabla 5-5. Caudales medios mensuales.**

|Mes|Caudal [m3/s]|
|---|---|
|abr|1,03|
|may|0,74|
|jun|1,16|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

3

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Mes|Caudal [m3/s]|
|---|---|
|jul|0,03|
|ago|0,31|
|sept|0,72|
|oct|0,63|
|nov|5,62|
|dic|11,74|
|ene|10,98|
|feb|5,21|
|mar|0,82|

Fuente: elaboración propia en función de .

**Figura 5-3. Caudales medios mensuales.**

Fuente: elaboración propia.

5.4 VARIACIÓN ESTACIONAL

Para el cálculo de la curva de variación estacional (CVE) del Río Maipo en el punto de descarga de la
PTAS Buin, se realiza un análisis de frecuencia de los caudales para cada mes, analizando las
siguientes distribuciones: Normal, Log-Normal, Pearson III, Log-Pearson, Gumbel, Gamma y LogGamma. Para cada mes se analizó qué distribución se ajusta mejor a los datos, para esto se evaluó
el coeficiente de correlación, el error cuadrático medio y prueba de bondad de ajuste Chi Cuadrado.
En la Tabla 5-6 se presentan los resultados del análisis de frecuencia para el Río Maipo en función
de los datos históricos. Se debe destacar que las distribuciones que mejor ajuste presentan en
función de los datos observados son: Gamma y Log-Pearson III. Solo enero y febrero se ajustan en
base a Log-Pearson II, y todos los demás meses de marzo a diciembre se ajustan mediante Gamma.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

4

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 5-6. Variación estacional.**

|Mes|Caudales asociados a probabilidades de excedencia [m3/s]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Mes**|**1%**|**5%**|**10%**|**25%**|**50%**|**80%**|**90%**|**95%**|
|Abril|16,2|6,0|2,8|0,4|0,0|0,0|0,0|0,0|
|Mayo|11,2|4,3|2,1|0,3|0,0|0,0|0,0|0,0|
|Junio|19,0|6,8|3,0|0,4|0,0|0,0|0,0|0,0|
|Julio|0,4|0,1|0,1|0,0|0,0|0,0|0,0|0,0|
|Agosto|4,4|1,8|0,9|0,2|0,0|0,0|0,0|0,0|
|Septiembre|10,2|4,1|2,1|0,4|0,0|0,0|0,0|0,0|
|Octubre|5,0|2,7|1,8|0,8|0,2|0,0|0,0|0,0|
|Noviembre|24,3|16,1|12,6|7,8|4,1|1,4|0,7|0,4|
|Diciembre|63,3|39,3|29,1|16,2|7,0|1,7|0,6|0,2|
|Enero|471,9|92,0|40,9|11,6|3,2|0,8|0,4|0,3|
|Febrero|144,6|36,7|17,7|5,2|1,3|0,2|0,1|0,0|
|Marzo|10,8|4,5|2,4|0,5|0,0|0,0|0,0|0,0|

Fuente: elaboración propia en función de informacion entregada por el titular.

En la Figura 5-4 se muestra gráficamente la variación estacional para las 8 probabilidades de
excedencia estimadas, además, en la Figura 5-5 se presenta la variación estacional solo con las tres
probabilidades de excedencia más ocurrentes (80%, 90% y 95%). Analizando los caudales asociados
a la probabilidad de excedencia de un 95%, el menor, sin considerar los caudales nulos, corresponde
a 0,2 m [3] /s en el mes de diciembre.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

5

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 5-4. Variación estacional.**

Fuente: elaboración propia.

**Figura 5-5. Variación estacional.**

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

6

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

El régimen hidrológico resultante sugiere desarrollar un escenario asociado a los meses de octubre
a marzo, pues es en donde existe un caudal en el río Maipo. Este escenario debiera representar las
épocas de bajo caudal en dichos meses, es decir, asociados a condiciones de bajo caudal (estiaje).

Entre los meses de abril y septiembre, el caudal es nulo en el río Maipo, y si bien, es una condición
puede ser interesante para ser modelada, no es una condición más desfavorable para ser modelada.
Esto debido a que en estos casos de caudal nulo del río Maipo, el ecosistema acuático existente se
mantiene exclusivamente por el aporte de caudal que proviene de la descarga del efluente de la
PTAS Buin, por tanto, la PTAS es un elemento positivo actualmente en dicho ecosistema. Por tal
motivo, la condición más desfavorable para modelar es una condición de estiaje en los meses con
caudal pasante en el río, ya que el ecosistema presente no se sustenta exclusivamente a partir del
caudal de descarga de la PTAS Buin.

## 6 ASPECTOS NORMATIVOS

En este capítulo se describen los aspectos normativos que tienen incidencia en el estudio de
contaminantes, respecto a límites de emisión por parte de la PTAS Buin y límites máximos definidos
para el río Maipo en la zona de estudio.

Por lo tanto, en la tabla 1 del D.S. N°90 se establecen los límites máximos permitidos para la descarga
de residuos líquidos a cuerpos de agua fluviales, es decir, los límites máximos que podría descargar
la PTAS Buin. En la Tabla 6-1 se detallan los parámetros que se van a modelar que están descritos
en la tabla 1 del D.S. N°90 con sus respectivos límites máximos permitidos. Se incluyen los
parámetros fisicoquímicos para la modelación de nutrientes (Temperatura, DBO 5, NTK, fósforo,
coliformes fecales y pH), los metales (cromo, plomo, zinc y níquel) y los iones (cloruro y sulfato).

**Tabla 6-1. Límites máximos permitidos para la descarga de residuos líquidos a cuerpos de agua fluviales**

**(Tabla 1 D.S. N°90).**

|Parámetro|Unidad|Límite máximo permitido|
|---|---|---|
|Temperatura|°C|35|
|DBO5|mg/L|35,0|
|Nitrógeno total Kjeldahl|mg N/L|50,0|
|Fósforo|mg P/L|0,2|
|Coliformes totales fecales|NMP/100ml|1000|
|pH|-|8,5|
|Sulfatos|mg/L|1000|
|Cloruros|mg/L|400|
|Cromo|mg/L|0,05|
|Plomo|mg/L|0,05|
|Zinc|mg/L|3|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

7

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetro|Unidad|Límite máximo permitido|
|---|---|---|
|Níquel|mg/L|0,2|

Fuente: elaboración propia.

Por otro lado, la NSCA del Río Maipo considera el límite máximo que pueden tener los cuerpos de
agua naturales que pertenecen a la red hidrográfica del río Maipo. El río Maipo a la altura de la
descarga de la PTAS Buin pertenece al área de vigilancia Ambiental asociada a la cuenca del río
Maipo, denotada como MA-4. En la tabla C de la normativa se muestran los valores límites de esta
área de vigilancia (Tabla 6-2), la cual incluye los parámetros fisicoquímicos para la modelación de
nutrientes (OD, CE, pH, DBO 5, nitrato y ortofosfato), los metales (cromo total, plomo disuelto, zinc
disuelto y níquel disuelto) y los iones (cloruro y sulfato).

**Tabla 6-2. Concentraciones máximas permitidas en el área de vigilancia MA-4 de la NSCA del Río Maipo.**

|Parámetro|Unidad|MA-4|
|---|---|---|
|Oxígeno Disuelto|mg/l|8|
|Conductividad Eléctrica|S/cm|1600|
|pH|-|6,5 - 8,7|
|DBO5|mg/l|8|
|Nitrato|mg/l|4|
|Ortofosfato|mg/l|0,15|
|Cromo total|mg/l|0,05|
|Níquel disuelto|mg/l|0,02|
|Plomo disuelto|mg/l|0,007|
|Zinc disuelto|mg/l|0,03|
|Cloruro|mg/l|180|
|Sulfato|mg/l|380|

Fuente: Decreto 53 (BCN, 2023).

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

8

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 7 MODELO DE DISPERSIÓN DE LA PLUMA CONTAMINANTE

7.1 METODOLOGÍA GENERAL

Para poder modelar la totalidad de los parámetros fiscoquímicos abordados en la NSCA del río
Maipo, fue necesario implementar 3 modelos, cada uno de ellos especializados en un grupo de
parámetros en particular.

Así, se modelaron los parámetros nitrógeno orgánico, nitrato, fósforo orgánico e inorgánico,
oxígeno disuelto, pH, conductividad eléctrica, DBO 5, temperatura y coliformes fecales con el modelo
Qual 2K, los metales cromo total, níquel disuelto, plomo disuelto y cinc disuelto con el modelo WASP
(toxic module) y se realizó un modelo conservativo para los iones cloruro y sulfatos.

Se buscó que para estos tres modelos, los escenarios generados sean similares, los cuales tuvieron
que adaptarse a la información disponible y a los límites de vertimiento dados por el DS 90 cuando
corresponde.

En términos generales, se simularon 4 escenarios: 2 bajo condiciones actuales máximas permitida,
y 2 bajo condición futura de operación.

7.2 IMPLEMENTACIÓN DEL MODELO QUAL2KW

Para simular la calidad de agua se utilizó el modelo QUAL2Kw, software respaldado por el
Departamento de Ecología del Estado de Washington y la US-EPA. El modelo QUAL2KW ha sido
ampliamente utilizado para el modelamiento de la calidad de agua. Como caso especial, se
menciona a Pelletier et al. (2006) quienes desarrollaron su modelo modificando la versión original
(QUAL2K) incluyendo el AG PIKAIA para la calibración de los parámetros cinéticos de la corriente.

El modelo unidimensional QUAL2Kw simula el impacto de cargas de parámetros físico químicos
puntuales y distribuidas en un flujo permanente, no uniforme, segmentando el sistema en tramos
que pueden ser de longitud variable. El balance hidrológico se representa a través del flujo; el
balance de calor, a través de la temperatura, y el balance de material, a través de la concentración
de especies constituyentes. Los procesos cinéticos que se incluyen en el modelo son disolución,
hidrólisis, oxidación, nitrificación, desnitrificación, muerte y respiración/excreción y fotosíntesis. Los
procesos de transferencia de masa incluidos son reaireación, sedimentación, demanda béntica de
oxígeno y flujo de carbono orgánico de los sedimentos. Considerando estos procesos, el modelo
QUAL2Kw simula el transporte de la temperatura, la demanda bioquímica de oxígeno carbonácea
(DBOC), el fitoplancton, el oxígeno disuelto (OD), el material orgánico particulado, las diferentes
formas de nitrógeno y fósforo, el pH, la alcalinidad, los sólidos suspendidos inorgánicos (SSI), los
patógenos, las algas en el fondo de la columna de agua y en la zona hiporréica (estas dos últimas
son simuladas para ríos poco profundos). La DBOC se representa de dos formas: la DBOC rápida que
es la materia orgánica fácilmente oxidada por los microorganismos y la DBOC lenta que es la materia
orgánica difícilmente biodegradable por la población bacteriana.

EL procedimiento de modelación se divide en 3 pasos: 1) la construcción y configuración del modelo,
2) la calibración y finalmente, 3) la simulación de escenarios.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

9

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

1. Construcción del modelo: como se mencionó anteriormente, para la modelación se utilizó

el modelo QUAL2KW, el cual necesita para su configuración las siguientes entradas: datos
de topografía, meteorológicos, hidráulicos y fisicoquímicos del sistema. Todos los datos son
obtenidos en las campañas de terreno, a excepción de la meteorología, la cual se obtiene a
partir de estaciones meteorológicas.

2. Calibración: una vez configurado el modelo se ajustan los parámetros del modelo a partir

de datos obtenidos en el muestreo (datos observados). con el objetivo de obtener una
simulación lo más parecida posible a los datos observados. La forma de evaluar la similitud
es mediante estadísticos, como el error cuadrático medio y normalizado (RMSE y NRMSE),
el coeficiente de determinación (R2) y el sesgo o PBIAS.

3. Simulación de escenarios: finalmente, una vez ya calibrado y validado el modelo, se simulan

los escenarios que se alinean con el objetivo del estudio.

_7.2.1_ _Estructura del modelo_

Los datos hidráulicos necesarios para la construcción del modelo en QUAL2Kw corresponden a
información geométrica para definir las propiedades hidráulicas del canal de desagüe efluente de la
PTAS Buin y del río Maipo agua abajo de la descarga del canal mencionado.

En la Figura 7-1 se aprecia un modelo conceptual idealizado que explica cómo se abordó la
segmentación del cuerpo de agua y la distribución de las fuentes puntuales y sus tributarios.

**Figura 7-1. Modelo conceptual de la segmentación de un río utilizada por QUAL2Kw.**

Fuente: Pelletier & Chapra (2008).

El modelo QUAL2Kw discretiza el cuerpo fluvial en pequeños tramos denominados “reach”, donde
cada sección “i“ tiene un balance de masa propio y se rige por ecuaciones de advección-dispersiónreacción. El modelo conceptual consiste en conectar estas secciones, generando una gran cadena
de flujos aguas abajo. Internamente, el software determina la velocidad y la profundidad medias del

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

10

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

flujo para cada tramo de la corriente usando una ecuación para flujo uniforme de Manning
empleando una sección transversal regular de forma trapezoidal.

Los reach del modelo se definen en función de la red hídrica y del diagrama unifilar presentado
(Figura 4-4). La configuración de los Reach se muestra en la Figura 7-2 detallando el diagrama unifilar
y la ubicación de los reach. El reach 1 corresponde a la ubicación de la PTAS Buin Maipo, la cual
descarga al canal de desagüe efluente, compuesto por los reach del 1 al 17. Posterior, dicho canal
se une al río Maipo, el cual se representa con los reach del 17 al 26.

**Figura 7-2. Estructura del modelo y sus afluentes.**

Fuente: Elaboración propia.

Para determinar las elevaciones, largos y pendientes de cada reach se utilizaron los datos levantados
en la campaña de topobatimetría la que tuvo como objetivo medir perfiles transversales mediante
un equipo Geomax Zenith 35 pro.

Todos los reach se modelaron como canales trapezoidales con pendientes laterales 1:1. El modelo
calcula las velocidades en cada segmento para medir el tiempo de residencia. Estas velocidades las
computa por medio de la ecuación de Manning bajo condiciones estacionarias.

En la Tabla 7-1 se detallan los 26 reach definidos, con sus respectivas distancias, pendientes, número
de Manning y anchos representativos.

**Tabla 7-1. Reach definidos para la modelación en QUAL2Kw.**

|Reach|Distancia ac.<br>[km]|Cuerpo de agua|Pendiente [-]|Manning [-]|Ancho [m]|
|---|---|---|---|---|---|
|Reach 0|0,00|Canal de desagüe|0,005|0,039|1,6|
|Reach 1|0,020|Canal de desagüe|0,006|0,039|2,1|
|Reach 2|0,102|Canal de desagüe|0,012|0,039|1,5|
|Reach 3|0,147|Canal de desagüe|0,003|0,039|3,1|
|Reach 4|0,174|Canal de desagüe|0,000|0,039|3,0|
|Reach 5|0,230|Canal de desagüe|0,003|0,039|3,5|
|Reach 6|0,261|Canal de desagüe|0,005|0,039|2,6|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

11

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Reach|Distancia ac.<br>[km]|Cuerpo de agua|Pendiente [-]|Manning [-]|Ancho [m]|
|---|---|---|---|---|---|
|Reach 7|0,291|Canal de desagüe|0,005|0,039|4,4|
|Reach 8|0,334|Canal de desagüe|0,005|0,025|2,4|
|Reach 9|0,385|Canal de desagüe|0,000|0,025|1,4|
|Reach 10|0,406|Canal de desagüe|0,004|0,025|2,0|
|Reach 11|0,462|Canal de desagüe|0,001|0,025|7,4|
|Reach 12|0,544|Canal de desagüe|0,001|0,025|0,6|
|Reach 13|0,585|Canal de desagüe|0,001|0,025|8,7|
|Reach 14|0,617|Canal de desagüe|0,002|0,049|6,1|
|Reach 15|0,649|Canal de desagüe|0,003|0,049|2,8|
|Reach 16|0,668|Canal de desagüe|0,000|0,049|2,7|
|Reach 17|0,775|Río Maipo|0,008|0,053|29,6|
|Reach 18|0,879|Río Maipo|0,008|0,053|29,6|
|Reach 19|1,117|Río Maipo|0,007|0,053|47,1|
|Reach 20|1,300|Río Maipo|0,007|0,053|47,1|
|Reach 21|1,500|Río Maipo|0,007|0,053|47,1|
|Reach 22|1,700|Río Maipo|0,007|0,053|47,1|
|Reach 23|1,900|Río Maipo|0,007|0,053|47,1|
|Reach 24|2,100|Río Maipo|0,007|0,053|47,1|
|Reach 25|2,300|Río Maipo|0,007|0,053|47,1|
|Reach 26|2,500|Río Maipo|0,007|0,053|47,1|

Fuente: Elaboración propia.

El coeficiente de Manning se calculó a través del método de Cowan diferenciando la zona en 4
tramos en función de lo visto en terreno. El eje principal del modelo, comprendido entre el punto
de descarga y el punto más aguas abajo en el río Maipo, tiene una extensión de 2,5 kilómetros,
fijando en el modelo de dispersión el kilómetro 0 como el punto más aguas arriba (P2), y el kilómetro
2,5 como el punto más aguas abajo.

Los tramos se definieron basándose en la cantidad de vegetación en el cauce y en las laderas, el tipo
de granulometría de cauce y la exposición al sol, relacionado al tamaño de la vegetación de los
tramos. En la Tabla 7-2 se presenta el detalle de los tramos.

**Tabla 7-2. Tramos representativos para la estimación del número de manning.**

|Tramo|Kilómetros|Rango de Reach del<br>modelo|
|---|---|---|
|1|0,00 - 0,29|Reach 0 - 7|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

12

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Tramo|Kilómetros|Rango de Reach del<br>modelo|
|---|---|---|
|2|0,29 - 0,59|Reach 7 - 13|
|3|0,59 - 0,70|Reach 13 -17|
|4|0,70 - 2,50|Reach 17 - 26|

Fuente: elaboración propia.

En la Tabla 7-3 se presentan los factores utilizados para la determinación del número de Manning
utilizado en el tramo aguas arriba de la descarga y el resultado de este.

**Tabla 7-3. Valores número de Manning** **por tramos.**

|Parámetro|Col2|Valor por tramo|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Parámetro**|**1 **|**2 **|**3 **|**4 **|
|Material involucrado|n0|0,024|0,020|0,024|0,028|
|Grado de irregularidad|n1|0,005|0,000|0,005|0,020|
|Variaciones en la sección transversal|n2|0,005|0,005|0,005|0,005|
|Efecto relativo de las obstrucciones|n3|0,000|0,000|0,010|0,000|
|Vegetación|n4|0,005|0,000|0,005|0,000|
|Grado sinuosidad|m|1,000|1,000|1,000|1,000|
|Manning adoptado|n|0,039|0,025|0,049|0,053|

Fuente: basado en Acrement y Schneider, 1989.

Finalmente, en la Tabla 7-4 se presentan los caudales estimados para la campaña julio del 2023, en
el canal de desagüe de la PTAS Buin y en el río Maipo. Como se menciona anteriormente estos
valores son utilizados para la calibración del modelo de dispersión.

**Tabla 7-4. Caudales definidos para las calibraciones del modelo.**

|Punto|Curso de agua|Caudal [m3/s]|
|---|---|---|
|**Punto**|**Curso de agua**|**Julio 2023**|
|P3|Canal de desagüe|0,021|
|P5|Río Maipo|5,401|

Fuente: elaboración propia.

_7.2.2_ _Datos fisicoquímicos_

Para el análisis se incorporan principalmente los parámetros fisicoquímicos que mayor nivel de
contaminación provienen de aguas servidas domiciliarias y que deben ser tratadas por las PTAS, y
los parámetros que son afectados indirectamente por ellos, tal como lo es el nitrógeno orgánico,
nitrato, fosforo orgánico e inorgánico, oxígeno disuelto, coliformes fecales, pH y temperatura.

Para el caso de este estudio se optó por modelar el nitrógeno orgánico, nitrato, fósforo orgánico e
inorgánico, oxígeno disuelto, pH, conductividad eléctrica, DBO 5, temperatura y coliformes fecales.
Se utilizaron estos parámetros debido a la incidencia e importancia que presentan en los procesos

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

13

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

biológicos y químicos en la columna de agua. El fósforo, al aumentar sus concentraciones, causa la
eutrofización del ambiente, reduciendo la producción primaria y esto lleva a que el río pierda sus
funciones ecológicas a largo plazo cuando está sometido a una exposición constante a este
elemento. El nitrógeno juega un rol importante al ser el que define si el ambiente se encuentra
eutrofizado y genera las bases para variados procesos biogeoquímicos, que dependen de la
capacidad de los microorganismos para poder ocupar y procesar de forma correcta este elemento.

Al agregar también el Oxígeno Disuelto (OD) al modelo de dispersión nos permite evaluar cómo
varía la calidad fisicoquímica del agua abajo de la descarga, es un parámetro importante de modelar
por el rol que cumple en los sistemas dulceacuícolas, siendo un parámetro clave en el

funcionamiento de los ecosistemas.

Las coliformes fecales es un parámetro fundamental para estudiar aguas abajo de la planta de
tratamiento, y así analizar la influencia que tiene la PTAS Buin sobre el río Maipo. El estudio se
compara con la Norma Secundaria de Calidad Ambiental para la protección de las aguas
continentales superficiales de la cuenca del Río Maipo (NSCA Maipo), lo que permite evidenciar si
la descarga se encuentra sobre o bajo la norma.

Al comparar estos parámetros, podemos obtener de manera clara el área de influencia de la
descarga sobre el objeto de protección calidad del agua, al ser los parámetros que se encuentran
con mayor alteración post integración al sistema, de esta manera si se sabe cuál es su
comportamiento o concentración a lo largo del sistema, es posible evidenciar de manera clara y
definida cual es el área de influencia sobre este objeto de protección.

En la Tabla 7-5 se presentan los parámetros a estudiar con sus respectivas unidades y abreviaciones,
y además, se detallan los parámetros que se ingresan como entradas en el modelo de calidad de
agua para los distintos afluentes. Los parámetros que no se ingresan corresponden al nitrito,
nitrógeno total Kjeldahl, nitrógeno total y fósforo total, ya que estos son estimados internamente
por el modelo.

**Tabla 7-5. Parámetros fisicoquímicos modelados.**

|Parámetros modelados|Unidad|Abreviación|Parámetros de<br>entrada|
|---|---|---|---|
|Conductividad eléctrica|us/cm|CE|X|
|Demanda Biológica de Oxígeno|mg/l|DBO5|X|
|Coliformes Fecales Totales|NMP/100ml|CFT|X|
|Nitrato|mg/l|Nn|X|
|Nitrito|mg/l|Ni|-|
|Nitrógeno Amoniacal|mg/l|Na|X|
|Nitrógeno Total Kjeldahl|mg/l|NTK|-|
|Nitrógeno orgánico|mg/l|Norg|X|
|Nitrógeno Total|mg/l|NT|-|
|Fósforo orgánico|mg/l|Porg|X|
|Fósforo Inorgánico|mg/l|Pinorg|X|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

14

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetros modelados|Unidad|Abreviación|Parámetros de<br>entrada|
|---|---|---|---|
|Fósforo Total|mg/l|PT|-|
|pH|-|pH|X|
|Oxígeno disuelto|mg/l|OD|X|
|Temperatura|°C|T°|X|

Fuente: elaboración propia.

7.2.2.1 Condiciones aguas arriba

Recordando la configuración del modelo, este comienza en la descarga de la PTAS Buin hacia el canal
de desagüe y luego este desemboca en el río Maipo. Por lo tanto, la condición aguas arriba del
modelo está impuesta por la calidad fisicoquímica del agua y caudal en el punto de descarga de la
PTAS Buin (P2). A continuación, en la Tabla 7-6 se presentan los valores de los parámetros
fisicoquímicos ingresados como condiciones aguas arriba para la campaña de julio del 2023, los
cuales corresponden a las mediciones tomadas en el punto más cercano a la descarga de la PTAS
Buin en el canal de desagüe.

**Tabla 7-6. Condiciones fisicoquímicas aguas arribas.**

|Parámetro|Unidad|Julio 2023|
|---|---|---|
|CE|s/cm|1753|
|DBO5|mg/L|10,4|
|CT|NMP/100 mL|4900|
|Nn|mg N/L|11,60|
|Na|mg N/L|0,98|
|Norg|mg N/L|1,5|
|NTK|mg N/L|1,35|
|Pinorg|mg P/L|4,1|
|pH|-|7,23|
|OD|mg/l|9,61|
|T°|°C|20,6|

Fuente: elaboración propia.

7.2.2.2 Datos fisicoquímicos en el eje principal

El eje principal del modelo está compuesto en su inicio por el punto más cercano a la descarga de la
PTAS Buin (P2), luego en el mismo canal de desagüe se ubican los puntos P3 y P4. Posterior al punto
P4, el canal de desagüe desemboca en el río Maipo, y en este se encuentran los puntos P5, P6 y P7.
Por lo tanto, el eje principal del modelo se compone por los puntos P2, P3, P4, P5, P6 y P7. En la

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

15

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Tabla 7-7 se presentan los valores de los parámetros fisicoquímicos de los puntos de muestreo
ubicados en el eje central del modelo.

**Tabla 7-7. Parámetros fisicoquímicos de los puntos dentro del eje principal del modelo en julio del 2023.**

<!-- INICIO TABLA 7-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Descarga PTAS BUIN Modelación de dispersión Río Maipo Elaborado para: Aguas Andinas 31 de julio de 2024 -->

**Tabla 7-7: se presentan los valores de los parámetros fisicoquímicos de los puntos de muestreo**

| Parámetro | Unidad | P2 | P3 | P4 | P5 | P6 | P7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CE | us/cm | 1753 | 1752 | 1752 | 1944 | 1950 | 1945 |
| DBO5 | mg/L | 10,4 | 11,9 | 19 | 14,4 | 12,9 | 12,4 |
| CT | NMP/100 mL | 4900 | 1,8 | 7900 | 54000 | 54000 | 4500 |
| Nn | mg N/L | 11,6 | 11,7 | 10,7 | 3,2 | 3,2 | 2,8 |
| Na | mg N/L | 0,98 | 0,58 | 0,96 | 0,98 | 0,96 | 1,02 |
| pH | unidad de pH | 7,23 | 7,48 | 7,55 | 7,36 | 7,65 | 7,63 |
| Pinorg | mg P/L | 4,1 | 4 | 4,2 | 2,6 | 1,5 | 1,6 |
| Porg | mg P/L | 0,2 | 0,2 | 0,2 | 1,5 | 0,5 | 0,5 |
| Norg | mg N/L | 1,5 | 1,6 | 1 | 0,59 | 0,46 | 1,3 |
| OD | mg/l | 9,61 | 10,23 | 11,17 | 14,64 | 14,37 | 14,45 |
| T° | °C | 20,6 | 20,7 | 20,6 | 20,7 | 20,6 | 20,7 |

<!-- Estadísticas: 11 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: elaboración propia. 7.2.2.3 Fuentes puntuales -->
<!-- FIN TABLA 7-7 -->


|Parámetro|Unidad|P2|P3|P4|P5|P6|P7|
|---|---|---|---|---|---|---|---|
|CE|us/cm|1753|1752|1752|1944|1950|1945|
|DBO5|mg/L|10,4|11,9|19|14,4|12,9|12,4|
|CT|NMP/100 mL|4900|1,8|7900|54000|54000|4500|
|Nn|mg N/L|11,6|11,7|10,7|3,2|3,2|2,8|
|Na|mg N/L|0,98|0,58|0,96|0,98|0,96|1,02|
|pH|unidad de pH|7,23|7,48|7,55|7,36|7,65|7,63|
|Pinorg|mg P/L|4,1|4|4,2|2,6|1,5|1,6|
|Porg|mg P/L|0,2|0,2|0,2|1,5|0,5|0,5|
|Norg|mg N/L|1,5|1,6|1|0,59|0,46|1,3|
|OD|mg/l|9,61|10,23|11,17|14,64|14,37|14,45|
|T°|°C|20,6|20,7|20,6|20,7|20,6|20,7|

Fuente: elaboración propia.

7.2.2.3 Fuentes puntuales

A continuación, en la Tabla 7-8 se detallan los valores de los parámetros fisicoquímicos que se
ingresan como entradas de la única fuente puntual del sistema, específicamente para río Maipo.

**Tabla 7-8. Parámetros fisicoquímicos de las fuentes puntuales.**

|Parámetro|Unidad|Río Maipo|
|---|---|---|
|**Parámetro**|**Unidad**|**Julio 2023**|
|CE|us/cm|1939|
|DBO5|mg/L|15,1|
|CT|NMP/100 mL|7900|
|Nn|mg N/L|2,9|
|Na|mg N/L|1,52|
|pH|mg N/L|7,5|
|Pinorg|mg P/L|2,6|
|Porg|mg P/L|1,1|
|Norg|-|0,84|
|OD|mg/l|14,8|
|T°|°C|20,7|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

16

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

_7.2.3_ _Calibración_

En el modelo QUAL2Kw, la calibración está orientada al ajuste de las constantes cinéticas que
influyen en los procesos del modelo, ya que se asume que la otra información suministrada es
confiable y ha sido depurada en un proceso de aplicación preliminar.

El modelo QUAL2Kw puede realizar la calibración (ajuste de los parámetros) en forma manual o en
forma automática de los parámetros cinéticos mediante el algoritmo AG-PIKAIA (algoritmo
genético), determinando sus valores óptimos entre máximos y mínimos especificados para cada
parámetro, buscando maximizar la bondad de ajuste con respecto a los datos de campo (Reed et al,
2000). Para la auto-calibración de los parámetros cinéticos por medio del AG se empleó la función
recomendada por Kannel et. al 2007 y Pelletier et al. (2005).

La calibración se realizó considerando las condiciones fisicoquímicas del efluente de la descarga para
la fecha de realización de la campaña fisicoquímica en julio del 2023. Para las condiciones hidráulicas
también se consideró aquella muestreada también en ambas campañas. Por lo tanto, para las
calibraciones se utilizan los datos fisicoquímicos de la Tabla 7-6 y Tabla 7-8, los reach definidos
(Tabla 7-1) y los caudales estimados (Tabla 7-4) según corresponda la campaña.

7.2.3.1 ESTIMADORES

Para evaluar el nivel de ajuste de la calibración y de la validación se utilizó principalmente el Error
de la Raíz Cuadrada Media (RMSE), el cual posee las mismas unidades que la variable analizada. La
siguiente ecuación muestra el cálculo de dicho estadístico y los datos que necesita (1). Mientras
menor es el RMSE significa que mejor es la simulación, por ende, el objetivo de la calibración es
minimizar el RMSE de cada parámetro fisicoquímico en estudio.

n
i=1 (y i −ŷ i ) [2] (1)
RMSE= ~~[√]~~ [∑]

n

Donde:

y : dato observado.
ŷ : dato simulado.
n : cantidad de datos.

Además, para comparar los resultados de los diferentes parámetros entre sí, se calcula el RMSE
normalizado (NRMSE), el cual se estima con las siguientes ecuaciones (2), (3), (4) y (5). Se calcula de
cuatro formas diferentes dependiendo del tipo de muestra de datos, por ejemplo, si es una muestra
que gira en torno a un promedio tiene sentido estimarlo en función de un valor promedio, pero si
es un parámetro que va decayendo en el tiempo, se estima en función de un rango de valores.

NRMSE= [RMSE]

y prom

RMSE
NRMSE=
y max −y min

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

(2)

(3)

17

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Donde:

y prom : promedio de la muestra.
y max : dato observado máximo.
y min : dato observado mínimo.
σ : desviación estándar.

y 1 : dato en el percentil 25%.
y 3 : dato en el percentil 75%.

(4)

NRMSE= [RMSE]

σ

NRMSE= [RMSE]

y 1 −y 3

(5)

Para la calibración se consideraron los 11 parámetros fisicoquímicos que se muestran en la Tabla
7-9, y a cada uno de ellos se le da un peso en función de su importancia para la calibración. Algunos
parámetros son más estables en el espacio y tiempo, por lo tanto, la simulación de ellos significa
menor dificultad y se les da un menor peso o importancia, este es el caso de la CE y el pH. Luego
está el OD, la DBO 5 y los CFT, los cuales tienen más procesos implicados en su simulación, por lo
tanto, se les da un peso de 2 en la calibración. Los parámetros con mayor importancia corresponden
a los nutrientes, ya que sus valores pueden variar en tramos cortos, así que se les da un peso de 3.
Finalmente, a la temperatura también se le da un peso de 3, a pesar de que es uno de los parámetros
más estable, ya que participa en los procesos de decaimiento y producción de todos los parámetros
fisicoquímicos.

**Tabla 7-9. Parámetros fisicoquímicos y sus respectivos pesos para la calibración.**

|Parámetro|Unidad|Peso|
|---|---|---|
|Nn|mg/l|3|
|Norg|mg/l|3|
|NT|mg/l|1|
|Pinorg|mg/l|3|
|PT|mg/l|1|
|T°|°C|3|
|OD|mg/l|3|
|DBO5|mg/l|2|
|CFT|NMP/100ml|2|
|CE|us/cm|1|
|pH|-|1|

Fuente: elaboración propia.

En función de la razón entre el peso de cada parámetro fisicoquímico y su respectivo NRMSE se
estimó un factor que denominamos Fitness en el contexto de la modelación. Este factor es un
número positivo, el cual mientras mayor sea, significa que mejor es la calibración. En la ecuación (6)

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

18

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

se presenta la forma en que se calcula dicho factor. Por lo tanto, el objetivo de la calibración es

maximizar el factor Fitness.

Peso (6)
Fitness=
NRMSE

Además de los estadísticos RMSE y NRMSE se evaluó el coeficiente de determinación (R [2] ) y el
estadístico PBIAS. En las ecuaciones (7) y (8) se presentan las fórmulas para estimar dichos
coeficientes. El coeficiente R [2] mientras más cercano a uno mejor será el ajuste, en cambio el
coeficiente PBIAS mientras más cercano a cero mejor será el ajuste. En la Tabla 7-10 se muestran
los rangos de clasificación de los estadísticos R [2] y PBIAS para evaluar los resultados de la calibración.

R [2] =

∑ Ni=1 (ŷ i −y prom ) [2]
∑ Ni=1 (y i −y prom ) [2]

PBIAS=

Donde:

y : dato observado.
ŷ : dato simulado.
y prom : promedio de la muestra.

∑ Ni=1 ŷ i −y i

∑ Ni=1 y i

x100

(7)

(8)

**Tabla 7-10. Rangos de clasificación para el R** **[2]** **y PBIAS.**

|Criterio|Valor|Clasificación|
|---|---|---|
|R2|0,75 < R2 < 1,00|Muy bueno|
|R2|0,65 < R2 < 0,75|Bueno|
|R2|0,50 < R2 < 0,65|Satisfactorio|
|R2|R2 < 0,50|Insatisfactorio|
|PBIAS|PBIAS < 10|Muy bueno|
|PBIAS|10 < PBIAS < 15|Bueno|
|PBIAS|15 < PBIAS < 25|Satisfactorio|
|PBIAS|20 <|Insatisfactorio|

Fuente: elaboración propia (RIIARn, 2020).

_7.2.4_ _DEFINICIÓN DE ESCENARIOS DE SIMULACIÓN_

Con el objetivo de comprender y analizar el funcionamiento de la PTAS Buin se definen distintos
escenarios para comprobar la influencia de la PTAS Buin en el canal de desagüe y en el río Maipo, y
así, estimar una posible área de influencia. Por lo tanto, se definieron 4 escenarios, que solo se
diferencian hidráulicamente, es decir, en los caudales y no en las concentraciones de los parámetros
fisicoquímicos del agua. En la Tabla 7-11 se detallan los caudales establecidos.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

19

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 7-11. Caudales fijados para los 4 escenarios.**

|Escenario|Caudales ingresados [m3/s]|Col3|Operación PTAS|
|---|---|---|---|
|**Escenario**|**Descarga PTAS Buin**|**Río Maipo**|**Río Maipo**|
|1|0,544|0,243|Futura|
|2|0,544|0,122|Futura|
|3|0,298|0,243|Actual|
|4|0,298|0,122|Actual|

Fuente: elaboración propia.

En relación a las concentraciones de los parámetros fisicoquímicos, para los 4 escenarios se
consideró lo siguiente: en el punto P1 (río Maipo aguas arriba) se fijaron las concentraciones
promedio entre las 4 campañas de estudio (marzo 2022, julio 2023 y, abril y junio del 2024); y en el
punto de descarga se fijaron las concentraciones en función de los límites máximos establecidos en

la tabla 1 del D.S. N°90.

En relación al caudal, el ingresado en el punto de descarga se fija como el caudal proyectado en la
ampliación de la PTAS Buin, 544 l/s, y el caudal actual, 298 l/s; y además, los escenarios se
diferencian en el caudal ingresado aguas arriba de la descarga en el río Maipo, para el cual se definen
2 valores: uno definido como el menor valor de caudal asociado a una probabilidad de excedencia
de un 95% sin considerar valores nulos, 243 l/s; y otro considerando la mitad del caudal anterior,
0,122 m [3] /s, también asociado a una probabilidad de excedencia de 95%. Este último caudal se asocia
al caudal ecológico determinado mediante la minuta 212 del MMA, el cual indica que el caudal
ecológico a mantener en un río para el proceso de otorgamiento de derechos de aguas es el 50%
del caudal mensual de 95% de excedencia con valores acotados entre el 10% y 20% del caudal medio

anual.

En la Tabla 7-12 se presentan los dos caudales considerados en el río Maipo como principal cuerpo

receptor.

**Tabla 7-12. Caudales asociados a los distintos escenarios de simulación.**

|Escenario|Descripción|Caudal (m3/s)|
|---|---|---|
|E1 y E3<br>(Q95%)|Menor valor de caudal asociado a una probabilidad de excedencia<br>de un 95% sin considerar valores nulos.|0,243|
|E2 y E4<br>(50% Q95%)|Mitad del menor valor de caudal asociado a una probabilidad de<br>excedencia de un 95% sin considerar valores nulos.|0,122|

Fuente: EcoHyd, 2022a.

En la Tabla 7-13 se presentan las concentraciones en los afluentes fijadas para los 6 escenarios. En
el punto de descarga se establecieron las concentraciones en función de los límites máximos
establecidos en la tabla 1 del D.S. N°90, lo cual aplica para la temperatura, los CFT (1000
NMP/100ml), la DBO 5 (35 mg/l), el NTK (50 mg/l) y pH (6,5 - 8,5). El restante de los parámetros
simulados, no está establecido en la tabla 1 del D.S. N°90 y se definieron en función del promedio
aritmético de las 4 campañas en el punto P2.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

20

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 7-13. Concentraciones fijadas para los 4 escenarios.**

|Parámetro|Unidad|Descarga PTAS y<br>P2|Río Maipo<br>(P1-P1a)|
|---|---|---|---|
|Temperatura|°C|35|9,7|
|Conductividad Eléctrica|us/cm|1655,8|1624,2|
|Oxígeno Disuelto|mg/L|6,5|9,6|
|Demanda Biológica de Oxígeno|mg/L|35,0|5,2|
|Nitrógeno orgánico|mg N/L|28,0|1,0|
|Nitrógeno amoniacal|mg N/L|7,0|0,4|
|Nitrato|mg N/L|59,0|2,1|
|Nitrógeno Total Kjedhal|mg N/L|50,0|1,2|
|Fósforo Orgánico|mg P/L|0,5|0,7|
|Fósforo inogánico|mg P/L|9,5|0,9|
|Coliformes Totales|NMP/100ml|1000|830,9|
|pH|-|6,0|7,9|

Fuente: elaboración propia.

Para el caso del NTK, este no es parte de los datos de entrada del modelo QUAL2Kw, pero se define
como la suma entre el nitrógeno orgánico y el nitrógeno amoniacal. Por lo tanto, se estiman los
porcentajes de Norg y Na que componen el NTK en función de los datos fisicoquímicos recopilados
de campañas anteriores. En la Tabla 7-14 se detallan los porcentajes de Norg, Na y NTK respecto al
nitrógeno total, por ende, considerando un total de 50 mg/l de NTK, se estima el Nn, Norg y el Na
presentados en la Tabla 7-13.

**Tabla 7-14. Porcentajes de Nn, Ni, Na, Norg y NKT del nitrógeno total en función de los datos obtenidos en**

**las campañas de monitoreo.**

|% del Nitrógeno Total|P1a|P2|P3|P4|P5|P6|P7|
|---|---|---|---|---|---|---|---|
|Nitrato (N-NO3-)|55%|82%|84%|84%|67%|69%|54%|
|Nitrito (N-NO2-)|1%|1%|0%|0%|0%|1%|1%|
|Nitrógeno amoniacal (NH4+)|29%|7%|4%|8%|20%|21%|20%|
|Nitrógeno Total Kjeldhal (NTK)|45%|18%|15%|15%|33%|31%|45%|
|Nitrogeno organico|16%|11%|12%|8%|12%|10%|25%|
|Nitrogeno Total (NT)|100%|100%|100%|100%|100%|100%|100%|

Fuente: elaboración propia.

Por otro lado, la NSCA del Río Maipo considera el límite máximo que pueden tener los cuerpos de
agua naturales que pertenecen a la red hidrográfica del río Maipo. El río Maipo a la altura de la zona
de estudio pertenece al área de vigilancia Ambiental asociada a la cuenca del río Maipo, denotada

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

21

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

como MA-4. En la tabla C de la normativa se muestran los valores límites de esta área de vigilancia
(Tabla 7-15), la cual incluye OD, CE, pH, Nn, Pinorg y DBO 5 .

**Tabla 7-15. Concentraciones máximas permitidas en el área de vigilancia MA-4 de la NSCA del Río Maipo.**

|Parámetro|Unidad|MA-4|
|---|---|---|
|Oxígeno Disuelto|mg/l|8|
|Conductividad Eléctrica|S/cm|1600|
|pH|-|6,5 - 8,7|
|DBO5|mg/l|8|
|Nitrato|mg/l|4|
|Ortofosfato|mg/l|0,15|

Fuente: elaboración propia.

7.2.4.1 Relación concentración y caudales

La relación entre la magnitud de los caudales y las concentraciones no es directa, un aumento en el
caudal del río Maipo no se traduce en que kilómetros aguas abajo la concentración será menor en
comparación a que el río Maipo tuviese un caudal menor. Un mayor caudal en el cuerpo de agua
generará que inmediatamente después de la descarga se observe una disminución mayor al caso en
que el caudal fuese menor. Pero aguas debajo de la descarga, la tasa de decaimiento se ve afectada
en función de la magnitud del caudal, para algunos parámetros el decaimiento será menor y el
caudal es mayor, y viceversa. Esto se debe a los siguientes factores:

1. **Mayor tiempo de residencia** : A menor caudal, el agua se mueve más lentamente, lo que

aumenta el tiempo de residencia de los nutrientes en el cuerpo de agua. Esto permite que
los procesos de eliminación, como la sedimentación, la absorción por plantas y
microorganismos, y las reacciones químicas, tengan más tiempo para actuar.

2. **Mayor interacción con el sustrato** : Un caudal menor generalmente implica una mayor

interacción del agua con el lecho del río o del lago. Esto puede aumentar la tasa de
sedimentación de los nutrientes y la absorción por parte del sustrato y los organismos

bentónicos.

3. **Mayor actividad biológica** : En condiciones de bajo caudal, la velocidad del agua es más baja,

lo que puede facilitar la actividad biológica, como la fotosíntesis y la absorción de nutrientes
por las plantas acuáticas y los microorganismos. Esto puede conducir a una mayor
eliminación de nutrientes del agua.

4. **Condiciones de oxígeno** : Un caudal más bajo puede llevar a una estratificación del agua y a

la creación de zonas con diferentes niveles de oxígeno. En zonas bien oxigenadas, los
procesos biológicos y químicos que eliminan nutrientes suelen ser más eficaces.

5. **Evaporación y concentración** : A menor caudal, especialmente en climas cálidos, la

evaporación puede ser más significativa, lo que puede concentrar algunos nutrientes y
hacerlos más disponibles para los procesos de eliminación.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

22

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Estos factores combinados pueden explicar por qué los nutrientes tienden a decaer más rápido en
condiciones de menor caudal en comparación con condiciones de mayor caudal. Se hace esta
aclaración para comprender los resultados que se presentarán.

7.3 MODELO DE DISPERSIÓN DE METALES

_7.3.1_ _Estructura de modelo de dispersión_

7.3.1.1 Parámetros simulados

En base a las observaciones pronunciadas en el ICSARA del proyecto “Ampliación de la PTAS Buin
Maipo” donde se solicita la incorporación en el análisis de dispersión de contaminantes todos los
parámetros de la Norma Secundaria de Calidad del Agua de la Cuenca del Río Maipo. En esta se
incluyen los metales pesados de plomo disuelto, níquel disuelto, cinc disuelto y cromo total los

cuales se modelaron en WASP8 en su módulo de tóxicos avanzado.

7.3.1.2 Segmentación y características hidráulicas

En el contexto de un modelo de calidad de agua en el software WASP (Water Quality Analysis
Simulation Program), el proceso de segmentación del tramo de río a modelar es crucial. Consiste en
dividir longitudinalmente el sistema acuático en diferentes segmentos o celdas discretas,
representando distintas partes del cuerpo de agua. Esta segmentación permite abordar de manera
precisa los procesos de transporte y mezcla que ocurren en distintas partes del sistema.

Cada segmento tiene propiedades hidráulicas y características específicas que influirán en el
transporte de contaminantes y en la calidad del agua. Para llevar a cabo la caracterización hidráulica
de un segmento en WASP, es necesario ingresar variables clave como la longitud, el ancho, la
pendiente y la rugosidad de Manning. Estos parámetros son fundamentales para describir y analizar
el flujo de agua en el sistema.

La longitud se refiere a la distancia entre los puntos de entrada y salida del segmento, lo que influye
en la velocidad y el tiempo de transporte del agua y los contaminantes en esa sección. El ancho del
segmento es la distancia promedio entre las orillas, lo que afecta la distribución de la velocidad del
flujo y la profundidad del agua. La pendiente, por su parte, indica la inclinación del terreno y es un
factor crítico en la determinación de la velocidad del flujo y la dirección del transporte.

Además, la rugosidad de Manning, que describe la resistencia al flujo en el canal y afecta la velocidad
y la distribución del flujo de agua. Esta rugosidad es determinante para el cálculo preciso del
transporte de contaminantes en el modelo de calidad de agua.

El modo de transporte utilizado en el modelo es el "kinematic wave", se parte de la suposición de
que las variaciones en la velocidad del flujo a lo largo de una sección transversal son insignificantes
en comparación con las variaciones en la profundidad del agua. Esta simplificación puede ser
adecuada en ciertas situaciones, pero es importante reconocer que puede no capturar
completamente la dinámica del flujo en escenarios más complejos.

En la Figura 7-3 se aprecia un modelo conceptual idealizado que explica cómo se abordó la
segmentación del cuerpo de agua y la distribución de las fuentes puntuales y sus tributarios.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

23

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 7-3. Modelo conceptual de la segmentación de un río utilizada en WASP.**

Fuente: sitito web https://www.epa.gov/ceam/wasp-model-examples.

Los segmentos para la modelación se definieron basándose en los puntos de calidad del agua y
fuentes de ingreso al Canal desagüe efluente y el río Maipo. En la Tabla 7-16 se presenta el detalle
de los segmentos junto a las características hidráulicas de cada uno, como se observa el modelo
queda definido por 27 tramos donde los primeros 16 tramos corresponden al Canal desagüe
efluente siendo el Tramo_1 el más aguas arriba (punto de descarga PTAS Buin), luego sigue el tramo
Río_Maipo que corresponde a la confluencia del Canal desagüe efluente con el río Maipo, por lo que
los tramos del Tramo_17 al Tramo 26 corresponden al río Maipo aguas abajo de la confluencia con
el Canal desagüe efluente.

**Tabla 7-16. Segmentos definidos para la modelación.**

|Tramo|Kilómetros|Ancho (m)|Pendiente|Rugosidad|
|---|---|---|---|---|
|Tramo_1|0-0,02|2,08883|0,00645|<br>0,039|
|Tramo_2|0,02-0,102|1,52508|0,01230|<br>0,039|
|Tramo_3|0,102-0,147|3,07006|0,00315|<br>0,039|
|Tramo_4|0,147-0,174|3,0392|0,00015|<br>0,039|
|Tramo_5|0,174-0,23|3,45952|0,00288|<br>0,039|
|Tramo_6|0,23-0,261|2,64601|0,00534|<br>0,039|
|Tramo_7|0,261-0,291|4,35492|0,00483|<br>0,039|
|Tramo_8|0,291-0,334|2,3961|0,00483|<br>0,025|
|Tramo_9|0,334-0,385|1,35142|0,00045|<br>0,025|
|Tramo_10|0,385-0,406|1,96784|0,00436|<br>0,025|
|Tramo_11|0,406-0,462|7,43615|0,00089|<br>0,025|
|Tramo_12|0,462-0,544|0,56387|0,00111|<br>0,025|
|Tramo_13|0,544-0,585|8,69852|0,00056|<br>0,025|
|Tramo_14|0,585-0,617|6,08124|0,00162|<br>0,049|
|Tramo_15|0,617-0,649|2,7586|0,00268|<br>0,049|
|Tramo_16|0,649-0,668|2,72616|0,00011|<br>0,049|
|Rio_Maipo|0,668-0,71|29,6075|0,00821|<br>0,053|
|Tramo_17|0,71-0,785|29,6075|0,00821|<br>0,053|
|Tramo_18|0,785-0,889|29,6075|0,00821|<br>0,053|
|Tramo_19|0,889-1,127|47,0507|0,00733|<br>0,053|
|Tramo_20|1,127-1,31|47,0507|0,00733|<br>0,053|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

24

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Tramo|Kilómetros|Ancho (m)|Pendiente|Rugosidad|
|---|---|---|---|---|
|Tramo_21|1,31-1,51|47,0507|0,00733|<br>0,053|
|Tramo_22|1,51-1,71|47,0507|0,00733|<br>0,053|
|Tramo_23|1,71-1,91|47,0507|0,00733|<br>0,053|
|Tramo_24|1,91-2,11|47,0507|0,00733|<br>0,053|
|Tramo_25|2,11-2,31|47,0507|0,00733|<br>0,053|
|Tramo_26|2,31-2,51|47,0507|0,00733|<br>0,053|

Fuente: elaboración propia.

7.3.1.3 Variables meteorológicas

El balance de calor y temperatura es en función de datos meteorológicos, tales como, temperatura
del aire, temperatura del punto de rocío, humedad relativa, velocidad del viento y fracción del cielo
cubierto por nubes. Sin embargo, se asume despreciable la influencia de estas variables dentro del
modelo dado que estas pierden relevancia en el modelo de metales implementado.

7.3.1.4 Caudal y calidad de las aguas

Los caudales utilizados en la calibración corresponden a los medidos en la campaña de julio de 2023,
en la Tabla 7-17 se presentan los caudales determinados, en el punto de descarga de la PTAS Buin
(P2) y en el Río Maipo (P5-1 y P5-2).

**Tabla 7-17. Caudales definidos para las calibraciones del modelo.**

|Punto|Caudal [m3/s]|
|---|---|
|**Punto**|**Julio 2023**|
|P2|0,021|
|P5-1 + P5-2|5,405|

Fuente: elaboración propia.

Los resultados de concentración de metales obtenidos en la campaña de julio de 2023 se presentan
en la Tabla 7-18, en esta se aprecia que para el cromo y níquel disuelto las concentraciones están
bajo el límite de detección en todos los puntos, en el caso del cinc disuelto y plomo disuelto se

tienen concentraciones variables.

**Tabla 7-18. Caudales definidos para las calibraciones del modelo.**

|Punto de medición|Cinc disuelto|Cromo|Níquel disuelto|Plomo|
|---|---|---|---|---|
|**Punto de medición**|**mg Zn/L**|**mg Cr/L**|**mg Ni/L**|**mg Pb/L**|
|P1|0,03|< 0,005|< 0,005|0,0122|
|P2|0,061|< 0,005|< 0,005|0,0071|
|P3|0,021|< 0,005|< 0,005|0,0015|
|P4|0,051|< 0,005|< 0,005|0,0024|
|P5|0,045|< 0,005|< 0,005|0,0119|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

25

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Punto de medición|Cinc disuelto|Cromo|Níquel disuelto|Plomo|
|---|---|---|---|---|
|**Punto de medición**|**mg Zn/L**|**mg Cr/L**|**mg Ni/L**|**mg Pb/L**|
|P1a|0,023|< 0,005|< 0,005|0,0084|
|P6|0,056|< 0,005|< 0,005|0,0049|
|P7|0,028|< 0,005|< 0,005|0,0115|
|Límite de detección laboratorio|0,002|0,005|0,005|0,0001|

Fuente: elaboración propia.

_7.3.2_ _Calibración_

La calibración del modelo de metales se realizó como un proceso iterativo que busco ajustar los
resultados de concentración de los distintos parámetros modelados con los datos observados en el
a campaña de julio de 2023. Para construir el modelo se tuvieron los siguientes supuestos:

 - Las concentraciones bajo el límite de detección se les asigno una concentración igual al

límite de detección.

 - La tasa de decaimiento solo se aplicó al cinc disuelto y el plomo disuelto producto de que

solo este parámetro presento variación en sus resultados, para el cromo y níquel disuelto

no se utilizó tasa de decaimiento.

 - El modelo se construyó físicamente similar al de nutrientes implementado en Qual2kw

donde se dejó como flujo principal el Canal desagüe efluente - Río Maipo y el afluente

principal se define por el río Maipo aguas arriba de la confluencia del Canal desagüe efluente

como fuente puntual de ingreso al flujo principal.

El modelo de metales en WASP se implementó con 27 segmentos (Tabla 7-16) con un modelo de
transporte de onda cinemática (Kinematic Wave) que es una opción realista y sencilla para dirigir el
transporte advectivo en tramos de corriente de flujo libre unidimensional. La ecuación de onda
cinemática calcula la propagación de la onda de flujo y las variaciones resultantes en caudales,
velocidades, anchos y profundidades en toda la red de corriente. Esta ecuación bien conocida es
una solución de la ecuación de continuidad unidimensional y una forma simplificada de la ecuación
de momento que considera los efectos de la gravedad y la fricción.

En lo que respecta a las propiedades de los metales se les asigno el coeficiente de partición K d a
partir de los presentados por la U.S Enviromental Protection Agency en su informe “Partition
Ceficients For Metals In Surface Water, Soil, And Waste” de julio de 2005. El parámetro de
calibración del modelo fue el coeficiente de primer orden de decaimiento para el cinc disuelto con
un valor de 0,28 y de 0,85 para el plomo disuelto, respecto a los otros parámetros dado que se
mantuvo constante la concentración a causa del supuesto antes mencionado no existe decaimiento

de estos metales.

Al igual que para el caso de la modelación de nutriente, para evaluar los resultados de la calibración
se utilizó el Error de la Raíz Cuadrada Media (RMSE), el cual posee las mismas unidades que la

variable analizada.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

26

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

_7.3.3_ _Escenarios simulados_

Con el objetivo de comprender y analizar el funcionamiento de la PTAS Buin se definieron 4
escenarios para comprobar la influencia de la PTAS Buin en el Canal desagüe efluente posterior, en
el río Maipo, y así, simular las concentraciones de los distintos metales y evaluar el cumplimiento
de la NSCA del río Maipo.

Los escenarios son similares a los definidos para la modelación de nutrientes. En la Tabla 7-19 se
detallan los caudales establecidos para los 4 escenarios, tanto para la descarga de la PTAS Buin como
para el cuerpo receptor (río Maipo).

**Tabla 7-19. Caudales de los distintos cursos de aguas definidos para los 4 escenarios.**

|Escenario|Caudales ingresados [m3/s]|Col3|
|---|---|---|
|**Escenario**|**Descarga PTAS Buin**|**Río Maipo**|
|1|0,544|0,243|
|2|0,544|0,122|
|3|0,298|0,243|
|4|0,298|0,122|

Fuente: Decreto 53 (BCN, 2023).

Respecto a las concentraciones asociadas a cada curso de agua para cada escenario definido, no se
realizó una proyección de la concentración de metales dado que el DS 90 no limita los metales

disueltos modelados.

Ante esto, en el río Maipo se fijaron para los 4 escenarios las concentraciones promedio entre las 4
campañas de estudio (marzo 2022, julio 2023 y, abril y junio del 2024). En lo que respecta al canal
de desagüe se utilizó la información disponible de las 4 campañas bajo los siguientes criterios:

 - Para los parámetros cuyas concentraciones superaron el límite de detección del laboratorio,
se calculó el promedio considerando únicamente los valores superiores a dicho límite. Las
campañas con concentraciones por debajo del límite de detección no fueron incluidas en el
cálculo. Este caso aplica para el plomo y el cinc disueltos.

 - Para los parámetros con concentraciones inferiores al límite de detección en todas las
campañas de calidad del agua, se fijó el límite de detección como la concentración de la
campaña. Posteriormente, se calculó el promedio de todas las campañas como la
concentración proyectada de la PTAS Buin. Este caso aplica para el Cromo y Níquel disuelto.

En la Tabla 7-20 se presentan las concentraciones medidas en las distintas campañas junto a la
concentración proyectada de la PTAS Buin en base a estas mediciones. Como se observa para el
plomo disuelto solo se tienen un valor medido sobre el límite de detección correspondiente a la
campaña de julio de 2023 por lo que se adopta este como el valor proyectado de la PTAS Buin para
los 4 escenarios de simulación, en el caso del cinc disuelto se tienen valores en la campaña de marzo
de 2022 y julio de 2023 por sobre el límite fijando como concentración proyectada el promedio de
estas dos campañas, en lo que respecta al cromo y níquel disuelto al no tener valores por sobre el
límite de detección se fijó como concentración dicho límite y se obtuvo el promedio de las cuatro
campañas como la concentración proyectada para ambos parámetros.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

27

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 7-20. Concentraciones en las distintas campañas de calidad del agua.**

|Parámetro|Unidad|Marzo 2022|Julio 2023|Abril 2024|Junio 2024|Descarga<br>PTAS Buin|
|---|---|---|---|---|---|---|
|Plomo disuelto|mg/l|<0,01|0,0071|<0,012|<0,012|0,0071|
|Cinc Disuelto|mg/l|0,039|0,061|<0,006|<0,006|0,05|
|Cromo|mg/l|<0,005|<0,005|<0,026|<0,024|0,015|
|Níquel disuelto|mg/l|<0,005|<0,005|<0,018|<0,018|0,0115|

Fuente:elaboración propia.

En la Tabla 7-21 se presentan las concentraciones de la descarga - canal de desagüe de la PTAS Buin
y la del río Maipo fijadas para los 4 escenarios.

**Tabla 7-21. Concentraciones fijadas para los 6 escenarios.**

|Parámetro|Unidad|Descarga- Canal desagüe afluente|Río Maipo|
|---|---|---|---|
|Plomo disuelto|mg/l|0,0071|0,011|
|Cinc Disuelto|mg/l|0,05|0,012|
|Cromo|mg/l|0,015|0,016|
|Níquel disuelto|mg/l|0,0115|0,012|

Fuente:elaboración propia.

Por otro lado, la NSCA del Río Maipo considera el límite máximo que deben los cuerpos de agua
naturales que pertenecen a la red hidrográfica del río Maipo. El río Maipo a la altura de la PTAS Buin
pertenece al área de vigilancia Ambiental MA-4. En la tabla C de la normativa se muestran los valores
límites de esta área de vigilancia (Tabla 7-22), la cual incluye plomo disuelto, cinc disuelto, cromo y
níquel disuelto.

**Tabla 7-22. Concentraciones máximas permitidas en el área de vigilancia MA-4 de la NSCA del Río Maipo.**

|Parámetro|Unidad|MA-4|
|---|---|---|
|Plomo disuelto|mg/l|0,007|
|Cinc Disuelto|mg/l|0,03|
|Cromo|mg/l|0,05|
|Níquel disuelto|mg/l|0,02|

Fuente: Decreto 53 (BCN, 2023).

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

28

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

7.4 MODELO DE DISPERSIÓN DE IONES

La modelación de los iones en cuerpos de agua superficial es un elemento poco desarrollado, el
mayor desarrollo de este tipo de modelación se realiza en la hidrogeoquímica. Esto debido a los
flujos subterráneos son lentos y al estar en contacto con distintas formaciones geológicas se
favorecen las reacciones químicas, en donde se busca determinar las distintas especiaciones de un
compuesto mediante reactores batch a través de una modelación inversa.

Amplia es la experiencia en la utilización de modelos hidrogeoquímicos para estudiar el
comportamiento químico del agua subterránea con iones mayoritarios en estudios de impacto
ambiental bajo el marco del SEIA. Al contrario de las aguas superficiales, en donde este tipo de

estudio son escasos.

Una revisión bibliográfica permitió definir que para el caso del Sulfato (SO 4 [-2] ) existe mayor evidencia
de estudios en aguas superficiales, pero estos se remiten cuerpos de agua lacustre, en donde, al
igual que para el caso de aguas subterráneas, los tiempos de residencia permiten apreciar los
cambios químicos de especiación.

En ríos, estos tiempos son acotados ya que dependen de la velocidad media del flujo, en el caso de
los ríos Chile, particularmente en el río Maipo, son bastante más acotados que los tiempos de
retención hidráulico en un lago o los tiempos de contacto entre el agua subterránea y la geología.

Los cloruros son considerados sustancias conservativas y el transporte y decaimiento de su
concentración en aguas se debe a procesos de advección y dispersión (Camacho, 2016). En el caso
del azufre, sí se evidencia que existan cambios en las especiaciones del azufre. La presencia de
oxígeno con el azufre forma sulfatos, SO 4 [-2] . Sin embargo, cuando existen condiciones de anoxia se
forma sulfuros, (H 2 S). La forma química en la que se presentas los sulfuros en el agua depende del
pH y el potencial de oxidación que haya en el sistema. En condiciones oxidantes la tendencia es que
los sulfuros se oxiden a sulfatos; para condiciones anóxicas, aún más oxidantes, la especie
dominante son los sulfitos (Howard, 1998 citado por Camacho 2016).

Considerando que el río Maipo no presenta condiciones de anoxia evidenciado en las distintas
campañas de terreno realizadas para este proyecto, es posible suponer que la forma del sulfato
predominante será el sulfato.

_7.4.1_ _Implementación del modelo_

De acuerdo a los antecedentes de modelación del ión Cloruro y del ión Sulfato, se implementó un
modelo de mezcla puntual considerando a estos iones como conservativos **sin decaimiento**, ya que
esto permite evaluar una condición conservadora sobre el cuerpo receptor.

La estructura del modelo se basó en la configuración de la red hidrográfica de los cursos de agua
que son receptores a la descarga del efluente y a sus afluentes. En primer lugar, se consideró la
descarga al canal de desagüe, el cual posteriormente confluye al río Maipo. El modelo se construye
con los puntos P2 a P4 sobre el canal desagüe para luego confluir al río Maipo (puntos P5, P6 y P7)
como se muestra en la Figura 7-4.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

29

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 7-4. Esquema conceptual del modelo de calidad del agua para cloruro y sulfato.**

Fuente: elaboración propia

De esta forma, el modelo se centra en los puntos de monitoreo: Descarga (P2), P3, P4, P5, P6 y P7,
mientras los puntos de monitoreo P1 y P1A se ubican en el río Maipo aguas arriba de la confluencia
del canal desagüe (Tabla 7-23).

<!-- INICIO TABLA 7-23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- De esta forma, el modelo se centra en los puntos de monitoreo: Descarga (P2), P3, P4, P5, P6 y P7, mientras los puntos de monitoreo P1 y P1A se ubican en el río Maipo aguas arriba de la confluencia del canal desagüe (Tabla 7-23). -->

**Tabla 7-23: Puntos de monitoreo presentes en el dominio del modelo****

| Punto | Curso de agua |
| --- | --- |
| Descarga<br>(P2) | Canal Desagüe |
| P3 | Canal Desagüe |
| P4 | Canal Desagüe |
| P5 | Río Maipo |
| P6 | Río Maipo |
| P7 | Río Maipo |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: elaboración propia Ambos modelos consideran la ecuación de mezcla puntual, en donde se determina la concentración Ci en el punto “i” a partir de la concentración Ci-1 ubicado aguas arriba “i-1” y de la concentración -->
<!-- FIN TABLA 7-23 -->


**Tabla 7-23 Puntos de monitoreo presentes en el dominio del modelo**

|Punto|Curso de agua|
|---|---|
|Descarga<br>(P2)|Canal Desagüe|
|P3|Canal Desagüe|
|P4|Canal Desagüe|
|P5|Río Maipo|
|P6|Río Maipo|
|P7|Río Maipo|

Fuente: elaboración propia

Ambos modelos consideran la ecuación de mezcla puntual, en donde se determina la concentración
Ci en el punto “i” a partir de la concentración Ci-1 ubicado aguas arriba “i-1” y de la concentración

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

30

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Cj del afluente “j” y de la continuidad de caudales. De esta forma, la concentración se determina

como:

Ci= [C] [i−1] [ ∗Q] [i−1] [ + C] [j] [∗Q] [j]

Q i−1 + Q j

_7.4.2_ _Calibración_

La calibración de ambos modelos (para el cloruro y para el sulfato) se llevó a cabo con las
concentraciones y caudales obtenidos en la campaña llevada a cabo en julio del 2023. Para evaluar
el nivel de ajuste se utilizó el método de RMSE.

_7.4.3_ _Generación de escenarios_

Con el objetivo de comprender y analizar el funcionamiento de la PTAS Buin se definen distintos
escenarios para comprobar la influencia de la PTAS Buin en el canal de desagüe y en el río Maipo, y
así, estimar una posible área de influencia y si se está cumpliendo con la NSCA Maipo. Por lo tanto,
para el caso del modelo Qual2KW se definieron 4 escenarios, que solo se diferencian
hidráulicamente, es decir, en los caudales y no en las concentraciones de los parámetros
fisicoquímicos del agua.

Respecto a la variación del caudal, se generaron dos combinaciones de caudales, tales que
maximicen el efecto de la descarga sobre los cuerpos receptores. Para ello, se consideraron dos
caudales de estiaje del río Maipo (ver Tabla 7-24).

<!-- INICIO TABLA 7-24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a la variación del caudal, se generaron dos combinaciones de caudales, tales que maximicen el efecto de la descarga sobre los cuerpos receptores. Para ello, se consideraron dos caudales de estiaje del río Maipo (ver Tabla 7-24). -->

**Tabla 7-24: Caudales en el río Maipo considerados para los escenarios de simulación.****

| Escenario | Descripción | Caudal (m3/s) |
| --- | --- | --- |
| E1 y E3<br>(Q95%) | Menor valor de caudal asociado a una probabilidad de excedencia<br>de un 95% sin considerar valores nulos. | 0,243 |
| E2 y E4<br>(50% Q95%) | Mitad del menor valor de caudal asociado a una probabilidad de<br>excedencia de un 95% sin considerar valores nulos. | 0,122 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: elaboración propia Respecto a la variación de la concentración de cloruro y sulfato, se impuso la máxima concentración que la Tabla 1 del Decreto Supremo N°90 /01 permite para este tipo de descargas. -->
<!-- FIN TABLA 7-24 -->


**Tabla 7-24 Caudales en el río Maipo considerados para los escenarios de simulación.**

|Escenario|Descripción|Caudal (m3/s)|
|---|---|---|
|E1 y E3<br>(Q95%)|Menor valor de caudal asociado a una probabilidad de excedencia<br>de un 95% sin considerar valores nulos.|0,243|
|E2 y E4<br>(50% Q95%)|Mitad del menor valor de caudal asociado a una probabilidad de<br>excedencia de un 95% sin considerar valores nulos.|0,122|

Fuente: elaboración propia

Respecto a la variación de la concentración de cloruro y sulfato, se impuso la máxima concentración
que la Tabla 1 del Decreto Supremo N°90 /01 permite para este tipo de descargas.

En la Tabla 7-25 se presentan las concentraciones de cloruro y sulfato muestreadas en las distintas
campañas fisicoquímicas realizadas. Como se observa en las cuatro campañas realizadas, las
concentraciones de cloruro y sulfato se mantienen en el mismo orden de magnitud, en torno a 234
mg/l para cloruro y 396 mg/l para sulfato. La menor concentración de cloruro ocurre en la campaña
de abril 2024, mientras que para el sulfato ocurre en la campaña de julio 2023. A su vez, las
concentraciones mayores para cloruro y sulfato ocurren en las campañas julio 2023 y junio 2024,
respectivamente.

Actualmente, las concentraciones de cloruro y sulfato exceden lo establecido por la NSCA en el área
de vigilancia MA-04. Recordar que las concentraciones limites impuestas para el cloruro y sulfato

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

31

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

son 180 y 380 mg/l, respectivamente. En la Tabla 7-25 se señalan en rojo aquellas concentraciones
que sobrepasan dichas concentraciones.

**Tabla 7-25. Concentraciones en las distintas campañas de calidad del agua en el río Maipo aguas arriba de**

**la descarga.**

|Parámetro|Unidad|Marzo 2022|Julio 2023|Abril 2024|Junio 2024|
|---|---|---|---|---|---|
|Cloruro|mg/l|241|276|195.7|224|
|Sulfato|mg/l|397|320|386|480|

Fuente:elaboración propia.

Finalmente, la composición de cada escenario se muestra en la Tabla 7-26.

<!-- INICIO TABLA 7-26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente:elaboración propia. Finalmente, la composición de cada escenario se muestra en la Tabla 7-26. -->

**Tabla 7-26: Escenarios de simulación para modelación de cloruros y sulfatos****

| Col1 | Caudal (l/s) | Col3 | Concentración efluente (mg/l) | Col5 | Concentración Maipo (mg/l) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Qdescarga** | **Rio Maipo** | **Cloruro** | **Sulfato** | **Cloruro** | **Sulfato** |
| **Escenario 1** | 0,544 | 0,243 | 400 | 1000 | 234 | 396 |
| **Escenario 2** | 0,544 | 0,122 | 400 | 1000 | 234 | 396 |
| **Escenario 3** | 0,298 | 0,243 | 400 | 1000 | 234 | 396 |
| **Escenario 4** | 0,298 | 0,122 | 400 | 1000 | 234 | 396 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: elaboración propia Plataforma de Investigación EcoHyd Ltda. Villaseca 21, oficina 501, Ñuñoa-Santiago -->
<!-- FIN TABLA 7-26 -->


**Tabla 7-26 Escenarios de simulación para modelación de cloruros y sulfatos**

|Col1|Caudal (l/s)|Col3|Concentración efluente (mg/l)|Col5|Concentración Maipo (mg/l)|Col7|
|---|---|---|---|---|---|---|
||**Qdescarga**|**Rio Maipo**|**Cloruro**|**Sulfato**|**Cloruro**|**Sulfato**|
|**Escenario 1**|0,544|0,243|400|1000|234|396|
|**Escenario 2**|0,544|0,122|400|1000|234|396|
|**Escenario 3**|0,298|0,243|400|1000|234|396|
|**Escenario 4**|0,298|0,122|400|1000|234|396|

Fuente: elaboración propia

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

32

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 8 RESULTADOS MODELACIÓN DE DISPERSIÓN

8.1 MODELO DE NUTRIENTES

_8.1.1_ _Calibración_

Una vez construido e ingresada toda la información al modelo en QUAL2Kw se procedió a realizar
una auto calibración de los parámetros cinéticos que modelan los parámetros en estudio
obteniendo un primer ajuste de las constantes. Posteriormente se precisó el valor de los parámetros
hasta lograr un ajuste aceptable de las concentraciones simuladas respecto a los valores medidos
en terreno en las estaciones de monitoreo. A continuación, se presentan los resultados de la
calibración para los siguientes parámetros: conductividad eléctrica, oxígeno disuelto, DBO 5,
nitrógeno orgánico, nitrato, fósforo inorgánico, coliformes fecales, temperatura, fósforo orgánico,
clorofila, alcalinidad y pH.

El ajuste del modelo a los datos observados se basó en la minimización del RMSE para cada uno de
los parámetros modelados. En la Tabla 8-1 se presentan los resultados de los estadísticos utilizados
para la validación del modelo.

**Tabla 8-1. Resultados de los estadísticos para la calibración.**

|Modelo|MD_BUIN|
|---|---|
|Campaña|Julio 2023|
|Fitness|4,24|
|NRMSE|0,20|
|R2|0,57|
|PBIAS|0,12|

Fuente: elaboración propia.

Además, en la Tabla 8-2 se detallan los valores de RMSE, NRMSE, R [2] y PBIAS para todos los
parámetros por separado. Analizando el coeficiente R [2] se observan parámetros que se ajustan bien
en función de este estadístico, como lo es la CE, Nn, Pinorg, clorofila, alcalinidad, NT y PT, con valores
sobre los 0,95.

En general los errores son bajos, los estadísticos asociados directamente a la diferencia entre los
valores observados versus los predichos corresponden al NRMSE y PBIAS, los cuales presentan
valores de 0,20 y 0,12 respectivamente, es decir, un 20% y un 12% de error. Parámetros como la T°,
la CE, Nn, clorofila, alcalinidad, pH y NT poseen NRMSE menor a un 10%.

Por lo tanto, luego de analizar los resultados de la calibración y sus respectivos estadísticos, se
concluye una calibración con un ajuste adecuado.

**Tabla 8-2. Resultados de los estadísticos para la evaluación de la calibración.**

|Parámetro|RMSE|NRMSE|R2|PBIAS|
|---|---|---|---|---|
|T°|0,374|0,018|0,039|0,014|
|CE|6,585|0,004|1,000|0,002|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

33

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetro|RMSE|NRMSE|R2|PBIAS|
|---|---|---|---|---|
|OD|4,166|0,376|0,169|0,293|
|DBO5|4,049|0,316|0,067|0,186|
|Norg|453,075|0,397|0,289|0,174|
|Na|567,394|0,518|0,442|0,435|
|Nn|732,722|0,082|0,993|0,009|
|Porg|346,444|0,266|0,711|0,225|
|Pinorg|540,318|0,200|0,963|0,151|
|Clorofila a|3,871|0,073|0,974|0,008|
|CT|1727,779|0,316|0,008|0,056|
|Alcalinidad|6,442|0,051|0,987|0,003|
|pH|0,694|0,088|0,079|0,088|
|NT|893,833|0,097|0,988|0,092|
|PT|547,912|0,156|0,849|0,069|

Fuente: elaboración propia.

A continuación, se presentan los resultados gráficos de la calibración en función de los datos de julio
del 2023. Se presentan los resultados para los siguientes parámetros: conductividad eléctrica,
oxígeno disuelto, DBO 5, nitrógeno orgánico, nitrato, fósforo inorgánico, coliformes fecales,
temperatura, fósforo orgánico, clorofila, alcalinidad y pH. Para comprender algunos de los aumentos
o disminuciones de concentraciones de algún parámetro, en la Tabla 8-3 se detalla la distancia del
afluente al eje principal del modelo.

**Tabla 8-3. Cursos de aguas afluentes al eje principal del modelo.**

|Punto|Cuerpo afluente|Distancia [km]|
|---|---|---|
|P1a|Río Maipo|0,70|

Fuente: elaboración propia.

En la Figura 8-1 se presenta la calibración de la conductividad eléctrica y visualmente se percibe un
buen ajuste de la simulación a los datos observados, obteniendo un RMSE de 6,6 S/cm y un NRMSE
de 0,4%, por lo cual se considera un buen ajuste. En el kilómetro 0,7 hay un aumento de la
concentración debido al ingreso del río Maipo al modelo, ya que este posee mayor concentración
que el canal de desagüe en el punto de unión. Caso similar a lo ocurrido con el oxígeno disuelto
(Figura 8-2), el cual también visualmente se ajusta a los datos observados en el canal de desagüe y
se considera aceptable en función de los estadísticos presentados en la Tabla 8-2, datando un valor
de RMSE de 4,2 mg/l, este también presenta un aumento en la concentración debido a la
superioridad de concentración de OD del río Maipo versus el canal de desagüe. La calibración del
oxígeno se realizó mediante un modelo de reaireación Owens-Gibbs con una temperatura de
corrección de 1,07.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

34

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-1. Resultados de la calibración para la conductividad eléctrica.**

Fuente: elaboración propia.

**Figura 8-2. Resultados de la calibración para el oxígeno disuelto.**

Fuente: elaboración propia.

En relación de la DBO 5, en la Figura 8-3 se presentan los resultados de la calibración, en general, se
logran simular los datos observado a excepción del ubicado justo antes de la unión del canal de
desagüe con el río Maipo, es decir, un poco antes del kilómetro 0,7. De todas maneras, los 3 puntos
en el río Maipo son simulados adecuadamente, por lo tanto, en función de la inspección visual y de
los estadísticos presentados en la Tabla 8-2, se considera una calibración aceptable, con un valor de
RMSE de 4,0 mg/l.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

35

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-3. Resultados de la calibración para la DBO5.**

Fuente: elaboración propia.

En la Figura 8-4 se presenta la calibración del nitrógeno orgánico, se logran replicar todos los datos
observados a excepción del punto más aguas abajo (P7). El ajuste tiene un valor de RMSE de 453,1
ug/l, error aportado principalmente por el último punto. Por otro lado, en la Figura 8-5 se muestra
la calibración del nitrato con un ajuste muy bueno en función de los estadísticos de la Tabla 8-2,
obteniendo un valor de RMSE de 732,7 ug/l, el cual normalizándolo corresponde a un 8% de error.
Por lo tanto, se considera un ajuste aceptable del nitrato.

**Figura 8-4. Resultados de la calibración para el nitrógeno orgánico.**

Fuente: elaboración propia.

No existen antecedentes en el área de estudio donde se presenten valores de los parámetros
cinéticos que gobiernan cada una de las ecuaciones que QUAL2Kw utiliza para modelar los distintos

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

36

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

parámetros físico químicos, para el caso del nitrógeno orgánico se tienen como parámetros
cinéticos la tasa de hidrólisis de nitrógeno orgánico dependiente de la temperatura, la velocidad de
sedimentación del nitrógeno orgánico y el factor de corrección de temperatura. Según Fuentes
(2012) en su memoria de título “Evaluación de la NSCA para la protección de las aguas continentales
superficiales de la cuenca del río BíoBío” determina un rango para hidrólisis que va desde 0,018
1/día a 0,36 1/día. Por otra parte, Rivera (2016) presenta un estudio donde determina la tasa de
nitrificación para ríos de montaña en Colombia, obteniendo valores entre 0,09 1/día hasta 63,6
1/día presentando las concentraciones y condiciones de distintos sectores en la cuenca que se
realizó el estudio donde se tiene que para los sectores de cotas medias la hidrólisis de nitrógeno
orgánico dependiente de la temperatura tiene valores cercanos a 2,1/día. Hossain (2013) realizó un
modelo en QUAL2Kw del río Tunggak en Malasia donde obtiene valores de 2,27 1/día para la
hidrólisis de nitrógeno orgánico dependiente de la temperatura y 1,67 m/día para la velocidad de
sedimentación. Basappa (2013) presenta los resultados de la implementación de un modelo
QUAL2Kw para el río Karanaja en la India determinando un valor para la hidrólisis de nitrógeno
orgánico dependiente de la temperatura de 4,31 1/día y una velocidad de sedimentación de 1,17
m/día.

Como se desprende de los datos encontrados se da cuenta que no existe un rango definido para los
parámetros que modelan el nitrógeno orgánico y va a depender de las condiciones del cuerpo de
agua, así como también de las concentraciones de los parámetros que se estén evaluando.

**Figura 8-5. Resultados de la calibración para el nitrato.**

Fuente: elaboración propia.

Para el caso del fósforo inorgánico, específicamente del ortofosfato, en la Figura 8-6 se presenta su
calibración, el canal de desagüe se genera un ajuste adecuado de los puntos de monitoreo, en
cambio, en el río Maipo se simula la forma y el decaimiento, pero no la magnitud, obteniendo un
valor de RMSE de 540,3 ug/l, el cual normalizándolo corresponde a un 20% de error. Por lo tanto,
se considera un ajuste aceptable del ortofosfato.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

37

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-6. Resultados de la calibración para el ortofosfato.**

Fuente: elaboración propia.

En relación Porg, en la Figura 8-7 se presentan los resultados de la calibración, en general, se logran
simular los datos observado a excepción del ubicado justo aguas abajo de la unión del canal de
desagüe con el río Maipo, es decir, un poco después del kilómetro 0,7. De todas maneras, los demás
puntos en el río Maipo son simulados adecuadamente, por lo tanto, en función de la inspección
visual y de los estadísticos presentados en la Tabla 8-2, se considera una calibración aceptable, con
un valor de RMSE de 346,4 mg/l.

**Figura 8-7. Resultados de la calibración para el fósforo orgánico.**

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

38

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

En la Figura 8-8 se muestra la calibración para las coliformes totales, para la cual se logra una
representación adecuada de todos los datos observados, simulando los aumentos y disminuciones
de concentración de coliformes totales. En función de los estadísticos de la Tabla 8-2, se obtiene un
valor de RMSE de 1727,8 NMP/100ml.

**Figura 8-8. Resultados de la calibración para los coliformes totales.**

Fuente: elaboración propia.

Respecto al pH presentado en la Figura 8-9, la calibración es aceptable en función de la inspección
visual y de los estadísticos. Presenta un valor de RMSE de 0,7 unidad de pH y un porcentaje de error

de un 8%.

**Figura 8-9. Resultados de la calibración para el pH.**

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

39

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Finalmente, en relación a la temperatura presentada en la Figura 8-10, la calibración es aceptable
en función de la inspección visual y de los estadísticos. Presenta un valor de RMSE de 0,4 °C y un
porcentaje de error de un 2%.

**Figura 8-10. Resultados de la calibración para la temperatura.**

Fuente: elaboración propia.

Finalmente, en la Tabla 8-4 se presentan los promedios de las variables calibradas, entre ellas tasas
de decaimiento, procesos de oxidación, reaireación, velocidad de sedimentación, hidrólisis,
nitrificación y desnitrificación. En primer lugar, se definieron los rangos de cada parámetro en
función de bibliografía, y luego mediante la auto calibración se ajustó cada variable dentro de los
rangos definidos (EPA, 2019).

Se debe destacar que para el caso de la velocidad de sedimentación del nitrato y del fósforo
inorgánico se definieron dos valores por fuera de los rangos fijados, ya que al momento de calibrar
no se producía decaimiento de dichos parámetros. La magnitud de esas tasas no significa que
efectivamente haya una sedimentación de tal magnitud, sino que esas tasas están incluyendo
salidas, procesos y/o factores externos que el modelo no puede simular.

También se debe tener en cuenta factores que no están estipulados en el modelo, como lo es la
infiltración en la tierra para pasar a formar parte de las aguas subterráneas, proceso por el cual
existiría decaimiento del nitrato y del ortofosfato. Otra particularidad del nitrato es que es
fácilmente transportado en agua, por ende, si es que hay salidas del eje principal del modelo, ya sea
en el canal de desagüe y el río Maipo, podría significar una disminución del nitrato (Bauder, J.).

**Tabla 8-4. Variables calibradas.**

|Variables|Unidad|Rango|Valor|
|---|---|---|---|
|Reaireación|1/d|-|416|
|Oxidación DBO5|/d|0-4,3|3,27|
|Hidrólisis N|/d|0,01-50|12,5|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

40

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Variables|Unidad|Rango|Valor|
|---|---|---|---|
|Vel. Sedimentación N|m/d|0,01-5|67637|
|Nitrificación|/d|0-10|9,7|
|Desnitrificación|/d|0,01-33|0,41|
|Hidrólisis P|/d|0,01-50|10,5|
|Vel. Sedimentación Porg|m/d|0,01-5|1,4|
|Vel. Sedimentación Pinorg|m/d|0-30|401263|
|Decaimiento Patógenos|/d|0,01-50|4,3|
|Sedimentación patógenos|m/d|0,1-4|1,0|

Fuente: elaboración propia.

_8.1.2_ _Simulación de escenarios de modelación_

Como se menciona en la metodología, se simularon 4 escenarios. Los resultados de cada escenario
simulado se presentan a continuación para cada parámetro evaluado. Se debe destacar que el área
de influencia o longitud de influencia, se estima en función del río Maipo (P1a), es decir, cuántos
kilómetros, desde la confluencia del canal de desagüe con el río Maipo, el río recupera la
concentración que posee antes de la junta con el canal.

Por lo tanto, para definir el área de influencia se utilizan los escenarios 1, 2, 3 y 4, debido a que el
Río Maipo presenta una concentración/condición inicial.

A continuación, se presentan los resultados para los siguientes parámetros: conductividad eléctrica,
oxígeno disuelto, DBO 5, nitrógeno orgánico, nitrato, ortofosfato, fósforo orgánico y coliformes
fecales. Se debe destacar que en cada gráfico se presentan los 4 escenarios por parámetro y además,
la concentración que posee el río Maipo antes de la junta con el canal de desagüe y el límite fijado
en la NSCA Maipo.

8.1.2.1 Conductividad eléctrica

En la Figura 8-11 se presenta la simulación de los escenarios 1, 2, 3 y 4 para la conductividad
eléctrica. Se debe destacar que la conductividad es un parámetro estable y solo se percibe una
perturbación a la altura de la unión del canal de desagüe con el río Maipo (0,7 km). Comparando los
4 escenarios, la diferencia es mínima y el peor escenario corresponde al 2, ya que el caudal en el río
Maipo es menor (122 l/s), y además, se considera la descarga futura (544 l/s).

Por último, en relación a la NSCA Maipo, analizando la Figura 8-11 y **¡Error! No se encuentra el o**
**rigen de la referencia.**, el límite máximo permisible es 1600 us/cm, y la máxima concentración que
se evidencia en el escenario 2 es de 1650 us/cm. Esto se debe principalmente a que el río Maipo al
inicio del tramo de modelación ya presenta valores por sobre la norma NSCA aguas arriba de la
descarga del efluente, es decir, en los puntos P1 y P1a de muestreo.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

41

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

La conductividad eléctrica en el agua se considera una propiedad conservativa en el sentido de que
no cambia significativamente a lo largo del tiempo en ausencia de procesos que alteren la
composición iónica del agua. Sin embargo, si se producen procesos que alteren la concentración de
iones, como la dilución, la evaporación, la adición de contaminantes o reacciones químicas, la
conductividad puede cambiar. Por lo tanto, en sistemas acuáticos donde las condiciones
ambientales son relativamente estables y no hay adición o remoción significativa de iones, la
conductividad puede considerarse conservativa (Benjamin, 2014).

**Figura 8-11. Resultados de la simulación de escenarios para la CE.**

Fuente: elaboración propia.

8.1.2.2 Oxígeno disuelto

En la Figura 8-12 se presenta la simulación de los escenarios 1, 2, 3 y 4 para el oxígeno disuelto. En
principio, en el canal de desagüe se observa un decaimiento considerable, esto debido a los valores
de los demás parámetros ingresados en función de la tabla 1 D.S.90, y posterior se percibe una
perturbación a la altura de la unión del canal de desagüe con el río Maipo (0,7 km). Comparando los
4 escenarios, la diferencia es mínima y no se genera un área de influencia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

42

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-12. Resultados de la simulación de escenarios para el OD.**

Fuente: elaboración propia.

8.1.2.3 DBO 5

En la Figura 8-13 se la simulación de los escenarios 1, 2, 3 y 4 para la DBO 5 . Se percibe una
perturbación a la altura de la unión del canal de desagüe con el río Maipo (0,7 km), específicamente
disminución de la concentración, debido a que la concentración del río Maipo es menor que la del

canal.

Respecto con la concentración inicial del río Maipo (5,2 mg/l), se genera un área de influencia de
6,57 y 6,53 km para los escenarios 1 y 2 respectivamente y un área de influencia de 5,86 y 5,85 km
para los escenarios 3 y 4 respectivamente.

Por último, en relación a la NSCA Maipo, el límite máximo permisible es 8 mg/l, y en los primeros
kilómetros posterior a la descarga se observa un valor máximo de concentración de 26,28 mg/l para

el escenario 2.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

43

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-13. Resultados de la simulación de escenarios para la DBO5.**

Fuente: elaboración propia.

8.1.2.4 Nitrógenos

En la Figura 8-14 y Figura 8-15 se presenta la simulación de escenarios 1, 2, 3 y 4 para el nitrógeno
orgánico y del nitrato. En ambas se percibe una perturbación a la altura de la unión del canal de
desagüe con el río Maipo (0,7 km), específicamente disminución de la concentración, debido a que
la concentración del río Maipo es menor que la del canal.

Respecto con la concentración inicial del río Maipo, 1000 ug/l para el nitrógeno orgánico y 2100 ug/l
para el nitrato, se genera un área de influencia para el nitrógeno orgánico de 2,53 y 2,67 km para
los escenarios 1 y 2 respectivamente, y de 1,94 y 2,13 km para los escenarios 3 y 4 respectivamente.
El área de influencia para el nitrato corresponde a 9,79 y 8,80 km para los escenarios 1 y 2
respectivamente, y 9,18 y 7,49 km para los escenarios 3 y 4 respectivamente.

Por último, en relación a la NSCA Maipo, observando la Figura 8-15 y **¡Error! No se encuentra el o**
**rigen de la referencia.**, el límite máximo permisible para el nitrato es 4000 ug/l, y en los primeros
kilómetros posterior a la descarga se observa un valor máximo de concentración de 37690 ug/l para

el escenario 2.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

44

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-14. Resultados de la simulación de escenarios para el Norg.**

Fuente: elaboración propia.

**Figura 8-15. Resultados de la simulación de escenarios para el Nn.**

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

45

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

8.1.2.5 Fósforos

En la Figura 8-16 y Figura 8-17 se presenta la simulación de escenarios para el fósforo inorgánico (en
su forma de ortofosfato) y del fósforo orgánico. En ambas se percibe una perturbación a la altura
de la unión del canal de desagüe con el río Maipo (0,7 km), específicamente disminución de la
concentración, debido a que la concentración del río Maipo es menor que la del canal.

Respecto con la concentración inicial del río Maipo, 900 ug/l para el ortofosfato y 700 ug/l para el
fósforo orgánico, se genera un área de influencia para el Pinorg de 0,72 y 0,68 km para los escenarios
1 y 2 respectivamente y 0,59 y 0,54 km para los escenarios 3 y 4 respectivamente. El área de
influencia para el fósforo orgánico corresponde a 0,25 y 0,15 km para los escenarios 1 y 2
respectivamente, y 0,41 y 0,23 km para los escenarios 3 y 4 respectivamente.

Por último, en relación a la NSCA Maipo el límite máximo permisible es de 150 ug/l, y observando
la Figura 8-16 y **¡Error! No se encuentra el origen de la referencia.** en los primeros metros posterior a
la descarga se observa un valor máximo de concentración de 3812 ug/l para el escenario 2. Esto se
debe principalmente a que el río Maipo ya presenta valores superiores a la norma NSCA aguas arriba
de la descarga del efluente, es decir, en los puntos P1 y P1a de muestreo al inicio del tramo de

modelación.

**Figura 8-16. Resultados de la simulación de escenarios para el Pinorg.**

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

46

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-17. Resultados de la simulación de escenarios para el Porg.**

Fuente: elaboración propia.

8.1.2.6 Coliformes totales

En la Figura 8-18 se presenta la simulación de escenarios para los CT, para los escenarios 1, 2, 3 y 4.
Se percibe una perturbación a la altura de la unión del canal de desagüe con el río Maipo (0,7 km),
específicamente una disminución de la concentración, debido a que la concentración del río Maipo
es menor que la del canal.

Respecto con la concentración inicial del río Maipo (830,9 NMP/100ml), las concentraciones del Río
Maipo en ningún momento superan la concentración inicial, por lo tanto, no se genera un área de

influencia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

47

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-18. Resultados de la simulación de escenarios para los CT.**

Fuente: elaboración propia.

_8.1.3_ _Áreas de influencia_

A continuación, se presentan las áreas de influencia para el OD, DBO 5, nitrógeno orgánico, nitrato,
ortofosfato, fósforo orgánico y coliformes fecales.

**Tabla 8-5. Áreas de influencia para los escenarios 1, 2, 3 y 4.**

|Parámetro|Área de influencia [km]|Col3|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**E1**|**E2**|**E3**|**E4**|
|OD|0,00|0,00|0,00|0,00|
|DBO5|6,57|6,53|5,86|5,85|
|Norg|2,53|2,67|1,94|2,13|
|Nn|9,79|8,80|9,18|7,49|
|Porg|0,25|0,15|0,41|0,23|
|Pinorg|0,72|0,68|0,59|0,54|
|CT|0,00|0,00|0,00|0,00|
|Q Río Maipo [m3/s]|0,243|0,122|0,243|0,122|
|Q Descarga [m3/s]|0,544|0,544|0,298|0,298|

Fuente: elaboración propia.

Se debe destacar que el área de influencia va a estar definida por el escenario 1 o 2, ya que para
ellos se considera un mayor caudal en la descarga de la PTAS Buin.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

48

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Analizando las áreas de influencias de los 4 escenarios, comparando los escenarios más críticos, es
decir, el 1 con el 2, se desprenden 3 conclusiones:

 - Para el caso del oxígeno disuelto y de las coliformes totales el área de influencia es igual a
cero kilómetros, es decir, la descarga de la PTAS Buin no genera una afectación negativa
sobre el Río Maipo, y no hay una influencia directa en la magnitud del caudal pasante por el

río.

 - Para el caso del nitrógeno orgánico, el decaimiento es menor para el escenario 2, es decir,
cuando el caudal del Río Maipo es menor.

 - Para el caso del nitrato, fósforo orgánico e inorgánico y para la DBO5, el decaimiento es
menor para el escenario 1, es decir, cuando el caudal del Río Maipo es mayor.

Al comparar las simulaciones entre los escenarios máximos permitidos actualmente y la condición
máxima proyectada, permite determinar el aumento de concentración proyectado sobre el río
Maipo. Finalmente, se concluye que el área de influencia está definida por el escenario 1 para el
caso del nitrato, indicando un área de influencia de 9,79 km.

_8.1.4_ _Comentarios_

Se implementó el modelo de dispersión QUAL2Kw sobre el canal de desagüe de la PTAS Buin y sobre
el río Maipo para determinar el comportamiento fisicoquímico de este río ante la descarga del

efluente de la PTAS Buin.

La calibración se realizó en función de una campaña de terreno realizada en julio del 2023 y se
evaluó en función de estadísticos, obteniendo un valor de NRMSE 20%, R2 de 0,57 y PBIAS de un
12%, considerando el ajuste del modelo adecuado.

Se logra un ajuste aceptable con un RMSE de 4,2 mg/l para el OD, 453 ug/l para el nitrógeno
orgánico, 733 ug/l para el nitrato, 540 ug/l para el fósforo inorgánico y 4 mg/l para la DBO5, estos
resultados demuestran que el ajuste a los datos de terreno es válido debido al bajo error alcanzado.
Por lo tanto, se cumple el objetivo principal de caracterizar el sistema mediante un modelo de
dispersión.

Analizando las áreas de influencias de los 4 escenarios, comparando los escenarios más críticos, es
decir, el 1 con el 2, se desprenden 3 conclusiones:

 - Para el caso del oxígeno disuelto y de las coliformes totales el área de influencia es igual a
cero kilómetros, es decir, la descarga de la PTAS Buin no genera una afectación negativa
sobre el Río Maipo, y no hay una influencia directa en la magnitud del caudal pasante por el

río.

 - Para el caso del nitrógeno orgánico, el decaimiento es menor para el escenario 2, es decir,
cuando el caudal del Río Maipo es menor.

 - Para el caso del nitrato, fósforo orgánico e inorgánico y para la DBO5, el decaimiento es
menor para el escenario 1, es decir, cuando el caudal del Río Maipo es mayor.

Finalmente, se concluye que el área de influencia está definida por el escenario 1 para el caso del
nitrato, indicando un área de influencia de 9,79 km.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

49

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Se debe destacar que la CE y el fósforo inorgánico al inicio del tramo de modelación ya presentan
valores superiores a la normativa NSCA del río Maipo.

8.2 MODELO DE METALES

_8.2.1_ _Calibración_

Los valores de los parámetros calibrados se muestran en la Tabla 8-6. En esta se presenta el peso
molecular, la solubilidad, el coeficiente de partición y el coeficiente de decaimiento de primer orden
del cinc disuelto ajustado a los datos de la campaña de calidad del agua de agosto de 2023.

**Tabla 8-6.Resultados de la calibración.**

|Parámetro|Plomo disuelto|Cinc disuelto|Cromo|Níquel disuelto|
|---|---|---|---|---|
|Peso molecular [g/mol]|207,2|65,37|51,99|58,69|
|Solubilidad [g/m3]|4|2300|140|0,2|
|Coeficiente de partición|4,2|3,1|3,9|3,1|
|Decaimiento 1° orden|0.85|0,25|--|--|

Fuente: elaboración propia.

De la modelación se tiene que cromo y níquel disuelto presentan un ajuste igual al de los datos de
terreno no presentando decaimiento producto de calibrar estos parámetros para concentraciones
iguales a lo largo del dominio de modelación. En lo que respecta al cinc disuelto, se obtuvo un RMSE
de 0,012 mg/l que equivale a un 30% del límite impuesto por la NSCA, esto se debe a que los valores
observados tienen una alta variación dentro de los cuerpos de agua presentando aumentos no
atribuibles a laguna fuente tanto para el Canal desagüe efluente y el río Maipo, por ejemplo en el
Canal desagüe efluente en el punto P3 presenta una concentración de 0,021 mg/l y el punto aguas
abajo denominado P4 0,051 mg/l lo que indica un aumento en la concentración del cinc disuelto sin
existir una fuente que produzca este aumento, por lo tanto, a pesar de que el RMSE para este
parámetro no es bajo es un ajuste aceptable para el modelo implementado. Para el plomo disuelto
se el RMSE es de 0,0015 mg/l lo que es un valor válido para la calibración y que significa un valor 4,5
veces menor al límite establecido por la NSCA. En la Tabla 8-7 se presentan los resultados del RMSE
para cada parámetro simulado.

**Tabla 8-7.Resultados de RMSE para cada parámetro modelado.**

|Parámetro|RMSE [mg/l]|
|---|---|
|Plomo disuelto|0,0015|
|Cinc Disuelto|0,012|
|Cromo|0,00|
|Níquel disuelto|0,00|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

50

31 de julio de 2024

|PTAS BUIN<br>ón de dispersión Río Maipo<br>para: Aguas Andinas<br>de 2024|Col2|
|---|---|
|entración a lo largo del domini<br> se presentan en la Figura 8-1<br>fico se ingresa el límite establ<br>encia del Canal desagüe eflue|o de modelación para el plomo disuelto, cinc disuelto<br>9**, **Figura 8-20**, **Figura 8-21 y Figura 8-22 respectivam<br>ecido por la NSCA, los puntos de calibración y la ubic<br>nte y el río Maipo indicado por la línea vertical gris.|
|0<br>0,005<br>0,01<br>0,015<br>0,02<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Pb (mg/l)<br>Distancia (km)<br>Plomo disuelto<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|0<br>0,005<br>0,01<br>0,015<br>0,02<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Pb (mg/l)<br>Distancia (km)<br>Plomo disuelto<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|

Figura 8-19. Resultados de modelación para el plomo disuelto.

Fuente: elaboración propia.

Figura 8-20. Resultados de modelación para el cinc disuelto.

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

51

31 de julio de 2024

|PTAS BUIN ón de dispersión Río Maipo o para: Aguas Andinas|Col2|Col3|
|---|---|---|
|de 2024|||
||||
|0<br>0,01<br>0,02<br>0,03<br>0,04<br>0,05<br>0,06<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Cr (mg/l)<br>Distancia (km)<br>Cromo<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|0<br>0,01<br>0,02<br>0,03<br>0,04<br>0,05<br>0,06<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Cr (mg/l)<br>Distancia (km)<br>Cromo<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|0<br>0,01<br>0,02<br>0,03<br>0,04<br>0,05<br>0,06<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Cr (mg/l)<br>Distancia (km)<br>Cromo<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|
|Figura 8-21. Re<br>|Figura 8-21. Re<br>|sultados de modelación para el cromo. <br>Fuente: elaboración propia.|
|0<br>0,005<br>0,01<br>0,015<br>0,02<br>0,025<br>0,03<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Ni (mg/l)<br>Distancia (km)<br>Níquel disuelto<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|0<br>0,005<br>0,01<br>0,015<br>0,02<br>0,025<br>0,03<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Ni (mg/l)<br>Distancia (km)<br>Níquel disuelto<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|0<br>0,005<br>0,01<br>0,015<br>0,02<br>0,025<br>0,03<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Ni (mg/l)<br>Distancia (km)<br>Níquel disuelto<br>Modelo<br>NSCA<br>Canal lateral - Maipo<br>Calibración|

Figura 8-22. Resultados de modelación para el níquel disuelto.

Fuente: elaboración propia.

_8.2.2_ _Simulación de escenarios_

Como se menciona en la metodología, se simularon 4 escenarios manteniendo las condiciones de
calidad del agua del río Maipo y la descarga en el Tramo_1 variando los caudales de cada uno de los
cursos de agua los que se resumen en la Tabla 8-8.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

52

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 8-8.Concentraciones y caudales por cada escenario.**

|Escenario|Punto|Caudal<br>[m3/s]|Plomo<br>disuelto<br>[mg/l]|Cinc Disuelto<br>[mg/l]|Cromo<br>[mg/l]|Níquel<br>disuelto<br>[mg/l]|
|---|---|---|---|---|---|---|
|1|P2 (Tramo_1)|0,544|0,0071|0,05|0,015|0,0115|
|1|P1-A<br>(Rio_Maipo)|0,243|0,011|0,012|0,016|0,012|
|2|P2 (Tramo_1)|0,544|0,0071|0,05|0,015|0,0115|
|2|P1-A<br>(Rio_Maipo)|0,122|0,011|0,012|0,016|0,012|
|3|P2 (Tramo_1)|0,298|0,0071|0,05|0,015|0,0115|
|3|P1-A<br>(Rio_Maipo)|0,243|0,011|0,012|0,016|0,012|
|4|P2 (Tramo_1)|0,298|0,0071|0,05|0,015|0,0115|
|4|P1-A<br>(Rio_Maipo)|0,122|0,011|0,012|0,016|0,012|

Fuente: elaboración propia.

A continuación, se presentan los resultados para el plomo disuelto, cinc disuelto, cromo y níquel
disuelto. Se debe destacar que en cada gráfico se presentan los 4 escenarios por parámetro y,
además, el límite fijado en la NSCA Maipo.

8.2.2.1 Plomo disuelto

En la Figura 8-23 se muestra la evolución espacial de la concentración de plomo disuelto.
Observamos que el escenario 3 es el que mayor concentración de plomo disuelto aporta al sistema,
debido a que el caudal de la descarga de la PTAS y el del río Maipo son similares y como la
concentración del río es más alta que la de la Descarga se produce un aumento en la concentración
de plomo disuelto en el sistema.

Al analizar los resultados de los escenarios, se aprecia que la influencia en la concentración de plomo
en el río Maipo viene dada por el mismo río Maipo debido a las elevadas concentraciones de este
metal que el río transporta desde aguas arriba de la descarga. Esta influencia se aprecia en los
escenarios 1 y 3. Recordando, los escenarios 1 y 3 consideran la situación futura y actual
(respectivamente), de la descarga de la PTAS Buin, y en ambos se mantiene que el caudal del río
Maipo es igual a 0,243 m [3] /s. Es en estos escenarios donde se aprecia una mayor concentración en
el río Maipo.

En cambio, los escenarios 2 y 4 (que consideran la situación futura y actual, respectivamente, de la
descarga de la PTAS Buin, y en ambos se mantiene que el caudal del río Maipo es igual a 0,122 m [3] /s
(caudal asociado al 50% del considerado en los escenarios 1 y 3), presentan una menor

concentración.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

53

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|men, se puede indicar que el<br>endo la influencia que pueda<br>establecido por la Norma Secu<br>g/l y de los escenarios simulad<br>de 0,0068 mg/l.|río Maipo influye en la concentración del plomo<br>tener el caudal de descarga.<br>ndaria de Calidad Ambiental (NSCA) para el río Mai<br>os la concentración más alta se alcanza en el escena|
|---|---|
|0<br>0,002<br>0,004<br>0,006<br>0,008<br>0,01<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Pb (mg/l)<br>Distancia (km)<br>Plomo disuelto<br>E1<br>E2<br>E3<br>E4<br>NSCA<br>Canal lateral - Maipo|0<br>0,002<br>0,004<br>0,006<br>0,008<br>0,01<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Pb (mg/l)<br>Distancia (km)<br>Plomo disuelto<br>E1<br>E2<br>E3<br>E4<br>NSCA<br>Canal lateral - Maipo|

Figura 8-23. Resultados de la simulación del plomo disuelto para los 4 escenarios.

Fuente: elaboración propia.

8.2.2.2 Cinc disuelto

En la Figura 8-24 se presenta la evolución espacial de la concentración del cinc disuelto a lo largo
del área de estudio para los 4 escenarios. Se observa que para todos los escenarios la concentración
es de 0,05 mg/l en la descarga de la PTAS Buin la cual una vez confluye con el río Maipo a los 0,7 km
decae a valores de 0,0191 mg/l en el escenario 4 y 0,0243 mg/l para el escenario 2. En lo que
respecta a los limites de la NSCA del río Maipo el límite establecido es de 0,03 mg/l y para los
escenarios simulados se tiene que la concentración es inferior a partir de los 800 m en el escenario
4 siendo el que más rápido alcanza esta condición y hasta los 1,21 km en el escenario 2 quien
presenta la mayor extensión.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

54

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-24. Resultados de la simulación del cinc disuelto para los 4 escenarios simulados.**

Fuente: elaboración propia.

8.2.2.3 Cromo

En la Figura 8-25 se presenta la evolución espacial de la concentración del cromo a lo largo del
dominio de modelación para los 4 escenarios simulados. Se observa que no existen variaciones en
la concentración dado que no se tiene decaimiento del cromo y que las concentraciones tanto del

|sagüe efluente y el río Maipo<br>g/l que es inferior al establec|tienen la misma concentración. El máximo alcanza<br>ido en la NSCA del río Maipo de 0,05 mg/l.|
|---|---|
|0<br>0,01<br>0,02<br>0,03<br>0,04<br>0,05<br>0,06<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Cr (mg/l)<br>Distancia (km)<br>Cromo<br>E1<br>E2<br>E3<br>E4<br>NSCA<br>Canal lateral - Maipo|0<br>0,01<br>0,02<br>0,03<br>0,04<br>0,05<br>0,06<br>0,00<br>0,50<br>1,00<br>1,50<br>2,00<br>2,50<br>Cr (mg/l)<br>Distancia (km)<br>Cromo<br>E1<br>E2<br>E3<br>E4<br>NSCA<br>Canal lateral - Maipo|

**Figura 8-25. Resultados de la simulación del cromo para los 4 escenarios simulados.**

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

55

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

8.2.2.4 Níquel disuelto

En la Figura 8-26 se muestra la evolución espacial de la concentración de níquel disuelto a lo largo
del área de estudio para los cuatro escenarios. Los resultados indican que todos los escenarios
presentan una evolución similar a lo largo del tramo modelado alcanzando una concentración
máxima de 0,0117 mg/l que es inferior al establecido en la NSCA del río Maipo de 0,02 mg/l. Esto se
debe a que el modelo fue calibrado utilizando concentraciones menores al límite de detección del
laboratorio, lo que implica que no se consideró una tasa de decaimiento para este parámetro.
Además, todos los afluentes tienen la misma concentración, independientemente del caudal

asociado a ellos.

Figura 8-26. Resultados de la simulación del níquel disuelto para los 4 escenarios simulados.

Fuente: elaboración propia.

_8.2.3_ _Comentarios_

El modelo calibrado demostró un ajuste aceptable con respecto a los datos de la campaña de calidad
del agua de julio de 2023. Para el cinc disuelto, se logró un RMSE de 0,012 mg/l y para el plomo
disuelto un valor de 0,0015 mg/l, lo cual indica una calibración válida para los datos observados.

Se llevaron a cabo simulaciones de cuatro escenarios, manteniendo constantes las condiciones de
calidad del agua en el río Maipo y el canal de desagüe efluente, variando únicamente los caudales
del río Maipo y los caudales de descarga de la PTAS (condición actual y futura).

El análisis mostró que el escenario 3 es el que mayor concentración de plomo disuelto aporta al
sistema, debido a que el caudal de la descarga de la PTAS y el del río Maipo son similares, y como la
concentración del río es más alta que la de la descarga, se produce un aumento en la concentración
de plomo disuelto en el sistema. La influencia en la concentración de plomo en el río Maipo proviene
principalmente de las elevadas concentraciones de este metal transportadas desde aguas arriba de
la descarga. Esta influencia se aprecia en los escenarios 1 y 3, que consideran la situación futura y
actual (respectivamente) de la descarga de la PTAS Buin, con un caudal del río Maipo de 0,243 m3/s.
En cambio, los escenarios 2 y 4, que consideran la misma situación, pero con un caudal del río Maipo

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

56

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

de 0,122 m3/s, presentan una menor concentración. En todos los escenarios, las concentraciones
son inferiores al límite establecido por la NSCA del río Maipo.

La evolución espacial de la concentración de cinc disuelto mostró que, en todos los escenarios, la
concentración de cinc disuelto desde la descarga de la PTAS Buin es de 0,05 mg/l. la cual disminuye
a lo largo del sistema, siendo el escenario 2 el que presentan una extensión mayor para decaer bajo
el límite de 0,03 mg/l establecido en la NSCA.

La evolución espacial de la concentración de cromo y níquel disuelto no presenta diferencias
significativas entre los escenarios simulados. En el caso del cromo, esto se debe a que no se
considera un decaimiento para este parámetro y las concentraciones del canal de desagüe y el río
Maipo son iguales. Para el níquel disuelto, el modelo fue calibrado utilizando concentraciones
menores al límite de detección del laboratorio, lo que implica que no se consideró una tasa de
decaimiento para este parámetro, y todos los afluentes tienen la misma concentración,
independientemente del caudal asociado a ellos. En todos los escenarios, los niveles de cromo y
níquel disuelto en el río Maipo son inferiores a los límites establecidos en la NSCA del río Maipo.

Los resultados obtenidos de la modelación y simulación de escenarios indican que la variación de
caudales genera un impacto en la distribución del plomo y cinc disuelto, no repercutiendo de la
misma forma con el cromo y níquel disuelto.

8.3 MODELO DE IONES

_8.3.1_ _Calibración_

Como se mencionó en el capítulo de metodología, la calibración fue realizada con los datos
obtenidos en la campaña de julio 2023, tanto de caudal como de la concentración de cloruro y

sulfato.

Para el cloruro el nivel de ajuste fue muy bueno, logrando un RMSE= 2,1 mg/l, logrando ajustes
bastantes cercanos a los datos observados (Ver Figura 8-27).

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

57

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-27 Comparación de la concentración del cloruro entre la concentración simulada y la observada**

**en campaña julio 2023**
Fuente: elaboración propia

Se observa, más allá del nivel de ajuste dado por el RMSE, que el nivel de ajuste es muy bueno
respecto a los datos observados, siendo la mayor diferencia ante la existencia de un leve aumento
del cloruro en el río Maipo cuando el canal desagüe confluye a este que el modelo no es capaz de

realizar.

De forma similar, la calibración del modelo del sulfato fue realizada con los datos de concentración
y caudal de la campaña de julio de 2023, logrando un ajuste muy bueno con un RMSE= 3,4 mg/l,
logrando ajustes bastante cercanos a los datos observados (Figura 8-28).

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

58

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-28 Comparación de la concentración del sulfato entre la concentración simulada y la observada**

**en campaña julio 2023**
Fuente: elaboración propia

Se observa, más allá del nivel de ajuste dado por el RMSE, que el nivel de ajuste es muy bueno
respecto a los datos observados, siendo la mayor diferencia ante la existencia de un leve aumento
del sulfato en el río Maipo que el modelo no es capaz de realizar.

_8.3.2_ _Simulación de escenarios_

Se simularon un total de 4 escenarios, en los cuales se consideraron combinaciones conservadoras
para los cuerpos de agua, maximizando la descarga y minimizando la capacidad de dilución de río
Maipo. En la Tabla 8-9 se resumen los escenarios estipulados y su explicación más detallada puede
verse en el acápite 7.4.3.

**Tabla 8-9 Escenarios de simulación para modelación de cloruros y sulfatos**

|Col1|Caudal (l/s)|Col3|Concentración efluente (mg/l)|Col5|Concentración Maipo (mg/l)|Col7|
|---|---|---|---|---|---|---|
||**Qdescarga**|**Rio Maipo**|**Cloruro**|**Sulfato**|**Cloruro**|**Sulfato**|
|**Escenario 1**|0,544|0,243|380|500|234|396|
|**Escenario 2**|0,544|0,122|380|500|234|396|
|**Escenario 3**|0,298|0,243|380|500|234|396|
|**Escenario 4**|0,298|0,122|380|500|234|396|

Fuente: elaboración propia

Para los iones Cloruro y Sulfato, las concentraciones del efluente son menores a las establecidas en
el DS90/01, debido a que este tipo de Planta de tratamiento no remueve cloruro y sulfato, por tanto,
la concentración del efluente será similar a la concentración afluente a la PTAS. En este sentido, se
realizó un análisis estadístico de las concentraciones de dichos parámetros en el afluente a la PTAS

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

59

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Buin y a otras PTAS de administración del Titular, permitiendo determinar las concentraciones
máximas que serán descargadas en la PTAS Buin.

8.3.2.1 Cloruro

La simulación de los 4 escenarios para el cloruro (ver Figura 8-29 y Figura 8-30 ), muestra que para la
totalidad de los escenarios, el río Maipo tiene el efecto de disolución sobre el cloruro, tanto para la

condición actual como condición futura.

Por ejemplo, el escenario 1 considera un caudal igual a 243 l/s sobre el río Maipo y la concentración
de cloruro en este último (puntos P5, P6 y P7) es igual a 334,9 mg/l, mientras que para el escenario
2, donde el caudal en el río Maipo es igual a 122 l/s, la concentración en estos puntos sube a 353,3
mg/l. Similar situación ocurre con el escenario 3 y 4 (condición actual), en donde el menor caudal
del río Maipo (escenario 4), se traduce en una mayor concentración. Esto permite verificar la
importancia del efecto de dilución del río Maipo.

En la Figura 8-29 se muestra los resultados de la simulación bajo la condición futura proyectada
(escenarios 1 y 2) y en la Figura 8-30 se muestra la condición actual máxima permitida de la descarga
(escenario 3 y 4)

El área de vigilancia de la NSCA en el punto de descarga, corresponde a la MA-4 definida entra las
confluencias de los ríos Clarillo y Mapocho. En esta área de vigilancia se fija como límite de
concentración igual a 180 mg/l para el cloruro y una concentración igual a 380 mg/l para el sulfato.

**Figura 8-29 Concentraciones del cloruro en el canal de desagüe (P3 y P4) y sobre el río Maipo (P5, P6 y P7)**

**para la condición futura proyectada**

Fuente: elaboración propia

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

60

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-30 Concentraciones simuladas para el cloruro en el canal de desagüe (P3 y P4) y sobre el río**

**Maipo (P5, P6 y P7) bajo la condición actual máxima permitida**

Fuente: elaboración propia

Las mediciones realizadas en las distintas campaña (4) dan cuenta que el río Maipo presenta
concentraciones por sobre lo establecido en la NSCA para esta área de vigilancia (ver Tabla 7-25),
presentando una concentración promedio igual a 234 mg/l.

Como resultado, para la totalidad de los escenarios simulados se observa que las concentraciones
sobre el río Maipo presentan valores por sobre lo establecido en la NSCA. Esta situación también se
vislumbra cuando se simula manteniendo las condiciones de escurrimiento en el río Maipo, pero
descargando el caudal actual del efluente.

8.3.2.2 Sulfato

Al igual que el cloruro, la simulación de los 4 escenarios, muestran que para la totalidad de los
escenarios, el río Maipo tiene el efecto de disolución.

Por ejemplo, el escenario 1 considera un caudal igual a 243 l/s sobre el río Maipo y la concentración
de sulfato en este último (puntos P5, P6 y P7) es igual a 467,9 mg/l, mientras que para el escenario
2, donde el caudal en el río Maipo es igual a 122 l/s, la concentración en estos puntos sube a 480,9
mg/l. Similar situación ocurre con el escenario 3 y 4 (condición actual máxima permitida), en donde
el menor caudal del río Maipo (escenario 4), se traduce en una mayor concentración. Esto permite
verificar la importancia del efecto de dilución del río Maipo. Esto permite verificar la importancia
del efecto de dilución del río Maipo.

En la Figura 8-31 se muestra los resultados de la simulación bajo la condición futura (escenarios 1 y
2) y en la Figura 8-32 se muestra la condición futura actual de la descarga.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

61

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Figura 8-31 Concentraciones del Sulfato en el canal desagüe (P3 y P4) y sobre el río Maipo (P5, P6 y P7)**

**para la condición futura**
Fuente: elaboración propia

**Figura 8-32. Concentraciones del Sulfato en el canal desagüe (P3 y P4) y sobre el río Maipo (P5, P6 y P7)**

**para la condición actual máxima permitida**

Fuente: elaboración propia

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

62

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

Las mediciones realizadas en las distintas campaña (4) dan cuenta que el río Maipo presenta
concentraciones por sobre lo establecido en la NSCA para esta área de vigilancia (ver Tabla 7-25),
presentando una concentración promedio igual a 396 mg/l.

Como resultado, para la totalidad de los escenarios simulados se observa que las concentraciones
sobre el río Maipo presentan valores por sobre lo establecido en la NSCA. Esta situación también se
vislumbra cuando se simula manteniendo las condiciones de escurrimiento en el río Maipo, pero
descargando el caudal actual del efluente.

**Tabla 8-10 Aumentos porcentuales de la concentración de cloruro y sulfato para la condición proyectada**

**respecto a la condición actual.**

|Punto|Escenarios 1-3|Escenarios 2-4|
|---|---|---|
|P2|0%|0%|
|P3|0%|0%|
|P4|0%|0%|
|P1|0%|0%|
|P1a + P1|0%|0%|
|P5|39%|7%|
|P6|39%|7%|
|P7|39%|7%|

Fuente: elaboración propia

Se aprecia que el aumento sobre el río Maipo (puntos P5, P6 y P7), es igual a 39% para el cloruro y
40% para el sulfato. Este aumento en la concentración en el río Maipo, se debe a la capacidad de
dilución que presenta el río Maipo, y un aumento de un 83% en el caudal máximo de descarga solo
se traduce en un aumento de un 39% y 40% para cloruro y sulfato respectivamente.

## 9 SITUACIÓN ACTUAL VS SITUACIÓN FUTURA

En este capítulo se compara la situación actual, es decir, considerando una descarga de la PTAS Buin
igual a 298 l/s, con la situación futura de la descarga, es decir, fijando la descarga con 544 l/s. Por lo
tanto, a continuación, se comparan los escenarios 1 y 3 entre sí, y los escenarios 2 y 4 entre sí. La
comparación se realiza en relación a dos aspectos: la máxima concentración que se observa aguas
debajo de la descarga de la PTAS Buin en el río Maipo, y en base a las longitudes de las áreas de
influencia definidas para cada escenario.

9.1 CONCENTRACIÓN MÁXIMA

En la Tabla 9-1 y Tabla 9-2 se presenta la comparación de las concentraciones máximas aguas abajo
de la descarga de la PTAS Buin. En relación a la comparación de los escenarios 1 y 3, los parámetros
fisicoquímicos evidencian variaciones inferiores a un 15% de la concentración máxima, siendo la
mayor para el caso de la DBO5, 14,9%, además, el porcentaje promedio de variación es de 6,2%. Y
respecto con los escenarios 2 y 4, la variación de los parámetros es inferior a un 10% de aumento

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

63

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

de concentración máxima, siendo la mayor para el caso de la DBO5, con un aumento de un 7,7%,
por último, la variación promedio es de un 0,8%. En cuanto a los metales, la mayor diferencia
porcentual se observa en el cinc disuelto en los escenarios 1 y 3, con una disminución en los demás
parámetros. En los escenarios 2 y 4, la diferencia porcentual del cinc disuelto es del 10,25%, mientras
que las concentraciones máximas de plomo disuelto y cromo muestran una disminución. En el caso
del níquel disuelto, no se aprecia variación entre los escenarios comparados.

Respecto a los iones Cloruro y Sulfato, el aumento de la descarga del efluente de la PTAS Buin, no
genera un aumento significativo de ambos iones sobre el rio Maipo, aumentando entre un 2% y un
7% la concentración de ambos iones respecto a la condición actual.

**Tabla 9-1. Comparación de concentraciones máximas sobre el río Maipo (P5, P6, P7)), E1 y E3.**

|Parámetro|Unidad|Concentración<br>máxima actual<br>E3|Concentración<br>máxima futura<br>E1|%|
|---|---|---|---|---|
|Conductividad eléctrica|us/cm|1641,61|1646,04|0,3%|
|DBO5|mg/l|20,31|23,33|14,9%|
|Nitrógeno orgánico|mg/l|4,27|4,78|11,8%|
|Nitrato|mg/l|29,83|34,01|14,0%|
|Ortofosfato|mg/l|3,27|3,52|7,6%|
|Fosforo orgánico|mg/l|1,25|1,10|-11,7%|
|Cinc disuelto|mg/l|0,0329|0,0383|16,4%|
|Plomo disuelto|mg/l|0,00678|0,00612|-9,7%|
|Cromo|mg/l|0,0154|0,0153|-0,65%|
|Níquel disuelto|mg/l|0,0117|0,0117|0%|
|Sulfato|mg/l|453,3|480,9|6%|
|Cloruro|mg/l|314|335|7%|

Fuente: elaboración propia.

**Tabla 9-2. Comparación de concentraciones máximas, E2 y E4.**

|Parámetro|Unidad|Concentración<br>máxima actual<br>E4|Concentración<br>máxima futura<br>E2|%|
|---|---|---|---|---|
|Conductividad eléctrica|us/cm|1641,61|1646,04|0,3%|
|DBO5|mg/l|20,31|23,33|14,9%|
|Nitrógeno orgánico|mg/l|4,27|4,78|11,8%|
|Nitrato|mg/l|29,83|34,01|14,0%|
|Ortofosfato|mg/l|3,27|3,52|7,6%|
|Fosforo orgánico|mg/l|1,25|1,10|-11,7%|
|Cinc disuelto|mg/l|0,0039|0,043|10,25%|
|Plomo disuelto|mg/l|0,00557|0,00524|-5,92%|
|Cromo|mg/l|0,0153|0,0152|-0,65%|
|Níquel disuelto|mg/l|0,0116|0,0116|0%|
|Sulfato|mg/l|469,8|480,9|2%|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

64

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetro|Unidad|Concentración<br>máxima actual<br>E4|Concentración<br>máxima futura<br>E2|%|
|---|---|---|---|---|
|Cloruro|mg/l|337,6|353,3|5%|

Fuente: elaboración propia.

9.2 LONGITUD DEL ÁREA DE INFLUENCIA

En la Tabla 9-3 y Tabla 9-4 se presenta la comparación de las longitudes de las áreas de influencias
definidas en la simulación de escenarios. En relación a la comparación de los escenarios 1 y 3, el
aumento de las áreas son inferiores a los 0,75 km, siendo el mayor para el caso de la DBO5, con un
aumento de 0,73 km. El promedio de aumento es de 0,24 km y sin considerar los parámetros donde
el aumento del área de influencia es nulo, el promedio es de 0,38 km. Respecto con los escenarios
2 y 4, el aumento de las áreas son inferiores a los 1,35 km, siendo el mayor para el caso del nitrato,
con un aumento de 1,31 km. El promedio de aumento es de 0,32 km y sin considerar los parámetros
donde el aumento del área de influencia es nulo, el promedio es de 0,52 km.

**Tabla 9-3. Comparación de las áreas de influencia, E1 y E3.**

|Parámetro|Área de<br>influencia actual<br>E3 [km]|Área de<br>influencia futura<br>E1 [km]|Diferencia [km]|
|---|---|---|---|
|Conductividad eléctrica|0,00|0,00|0,00|
|Oxígeno disuelto|0,00|0,00|0,00|
|DBO5|5,84|6,57|0,73|
|Nitrógeno orgánico|1,94|2,53|0,59|
|Nitrato|9,18|9,79|0,61|
|Ortofosfato|0,59|0,72|0,13|
|Fosforo orgánico|0,41|0,25|-0,16|
|Coliformes totales|0,00|0,00|0,00|

Fuente: elaboración propia.

**Tabla 9-4. Comparación de las áreas de influencia, E2 y E4.**

|Parámetro|Área de<br>influencia actual<br>E4 [km]|Área de<br>influencia futura<br>E2 [km]|Diferencia [km]|
|---|---|---|---|
|Conductividad eléctrica|0,00|0,00|0,00|
|Oxígeno disuelto|0,00|0,00|0,00|
|DBO5|5,85|6,53|0,68|

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

65

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

|Parámetro|Área de<br>influencia actual<br>E4 [km]|Área de<br>influencia futura<br>E2 [km]|Diferencia [km]|
|---|---|---|---|
|Nitrógeno orgánico|2,13|2,67|0,54|
|Nitrato|7,49|8,80|1,31|
|Ortofosfato|0,54|0,68|0,14|
|Fosforo orgánico|0,23|0,15|-0,08|
|Coliformes totales|0,00|0,00|0,00|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

66

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## 10 CONCLUSIONES

La descarga del efluente de la PTAS Buin se realiza al río Maipo, que por sus características
Hidromorfológicas, se genera un canal de desagüe en el cauce del río. Este canal avanza hacia aguas
abajo, hasta confluir al cauce vivo del río Maipo. Este canal de desagüe se modifica su trazado cada
vez que el caudal del río crece producto de las crecidas.

Esta existencia del canal de desagüe generó una conceptualización del modelo de dispersión, de tal
forma que deba ser incorporado. Así, el modelo fue construido para que la descarga del efluente se
realice a este canal de desagüe y posteriormente confluya al río Maipo.

Entendiendo que el régimen hidrológico del río Maipo esta altamente modificado debido a la gran
cantidad de extracciones, la caracterización hidrológica se llevó a cabo considerando dichas
extracciones. Los caudales de extracción de cada usuario fueron entregadas por el Titular, basado
en información oficial de la Junta de Vigilancia del río Maipo (primera sección). De esta forma, se
determinó el caudal pasante en el río Maipo mediante la ecuación de continuidad al restar los
caudales extraídos desde aguas arriba.

Los caudales resultantes, reflejan que el río Maipo a la altura de la descarga de la PTAS Buin presenta
caudales nulos principalmente en invierno y durante la época de deshielo el río Maipo presenta un
pequeño escurrimiento. Así, es posible considerar un caudal nulo en época de invernal y una caudal
de estiaje igual a 243 l/s en época estival

El estudio cumple el objetivo de analizar la dispersión de nutrientes, metales e iones. Se implementó
el modelo de dispersión de nutrientes en QUAL2Kw sobre el río Maipo y canal de desagüe para
determinar el comportamiento fisicoquímico del río Maipo ante la descarga del efluente de la PTAS
Buin. También se implementó el modelo matemático de simulación de la calidad del agua en WASP
en ambos cuerpos receptores con el objetivo de identificar el efecto de los metales establecidos en
la Norma Secundaría de Calidad del Agua de la cuenca del río Maipo sobre el área d vigilancia MA04. Y finalmente, se configuró un modelo matemático de los iones Cloruro (Cl [-] ) y Sulfato (SO 4 )
producto de la descarga del efluente de la PTAS de Buin sobre el canal de desagüe y posteriormente
sobre el río Maipo.

Para cada uno de los modelos se simularon escenarios de modelación para estudiar la influencia de
la PTAS Buin sobre el canal de desagüe y sobre el río Maipo propiamente tal. Se simularon un total
de 4 escenarios, variando únicamente el caudal del río Maipo, el caudal descargado por la PTAS Buin
e imponiendo una concentración de descarga del efluente igual a lo estipulado en el D.S. n° 90/01
(Tabla 1).

Así, se modelaron los parámetros nitrógeno orgánico, nitrato, fósforo orgánico e inorgánico,
oxígeno disuelto, pH, conductividad eléctrica, DBO 5, temperatura y coliformes fecales con el modelo
Qual 2K, los metales cromo total, níquel disuelto, plomo disuelto y cinc disuelto con el modelo WASP
(toxic module) y se realizó un modelo conservativo para los iones cloruro y sulfatos

En el caso de la modelación de nutrientes, se debe destacar que en general los peores escenarios
corresponden al 1 y 2, es decir, los escenarios con un mayor caudal de descarga (544 l/s). Bajo este
escenario, las áreas de influencias de los nutrientes varían entre un valor nulo y los 9,79 kilómetros.
En el caso de las áreas de influencia nulas, se debe a que el proceso de decaimiento de coliformes

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

67

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

totales ocurre principalmente en el canal de desagüe, y para cuando confluye al río Maipo, la
concentración simulada es menor que la concentración en el río Maipo.

El área de influencia de la demanda bioquímica de oxígeno varía entre 5,85 y 6,57 km,
respectivamente. Para el fósforo inorgánico varía entre 0,54 y 0,72. Finalmente, las mayores áreas
de influencia se presentan para los escenarios de simulación del nitrato, variando de 7,49 a 9,79 km,
siendo el peor caso correspondiente al escenario 1.

Respecto a los metales, la concentración de plomo disuelto es inferior al límite establecido en la
NSCA del río Maipo dentro del dominio de modelación. La concentración de cinc disuelto mostró
variaciones entre los escenarios, debido a la diferencia en los caudales en el río Maipo simulados, lo
que influye en la dilución del cinc disuelto en el agua. En todos los escenarios simulados, los niveles
de cinc disuelto en el río Maipo son inferiores a los de la NSCA del río Maipo. Por otra parte, las
concentraciones de cromo total y de níquel disuelto están por debajo del límite de detección del
laboratorio, por tanto, la modelación no entrega mayor información sobre el comportamiento de la

concentración de estos metales.

Respecto a los iones cloruro y sulfato, se aprecia que la capacidad de disolución de estos elementos
que tiene el río Maipo se ve limitada, no por los bajos caudales simulados, sino por las altas
concentraciones actuales de ambos iones, lo cuales sobrepasan el umbral indicado en la NSCA para
el área de vigilancia MA-04.

En cuanto a las áreas de influencia de metales, se establecen estas como nulas pues la concentración
de los metales logra valores bajo la NSCA en forma previa a la confluencia del canal de desagüe y el
río Maipo. El sulfato, al igual que el cloruro, la simulación muestra que para la totalidad de los
escenarios, el río Maipo tiene el efecto de disolución, siendo el área de influencia de solo metros.

Por último, la mayor longitud de las áreas de influencia se determina para los nitratos, la cual
corresponde a 9,79 km.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

68

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## REFERENCIAS

Área Metropolitana del Valle de Aburrá, (2011). _“Red de monitoreo ambiental en la cuenca_
_hidrográfica del Río Aburrá-Medellín en jurisdicción del área metropolitana fase III_ ”. Informe de

modelación.

Bauder, J., Sigler, W. A. _“Nitrato y nitrito”._ Universidad estatal de Montana Programa de Extensión
en Calidad del Agua. Departamento de Recursos de la Tierra y Ciencias Ambientales.

Benjamin, M. M. (2002). _Water Chemistry_ . McGraw-Hill.

Cossavella, A. M., Larrosa, N. B., & Nadal, A. F. (2014). “Determinación de la tasa de reaireación y
modelación hidrodinámica de un tramo del río Tercero (Ctalamochita)”. Revista facultad de ciencia
exactas, físicas y naturales.

EcoHyd, 2022a. _Estudio hidrológico_ . Planta de tratamiento de Aguas Servidas Rinconada. Informe

Técnico"

EcoHyd, 2022b. _Estudio topográfico_ . Planta de tratamiento de Aguas Servidas Rinconada. Informe

Técnico.

EcoHyd, 2022c. _Estudio de calidad del agua_ . Planta de tratamiento de Aguas Servidas Rinconada.

Informe Técnico.

EPA, (2019 _). “Literature Reviw on Nutrient-Related Rates, Constants, and Kinetics Formulationes in_
_Surface Water Quality Modeling”._ U.S. Environmental Protection Agency. Office of Research and
Development.

Fuentes, I. (2012). _EVALUACIÓN DE LA NORMA SECUNDARIA DE CALIDAD AMBIENTAL PARA LA_
_PROTECCIÓN DE LAS AGUAS CONTINENTALES SUPERFICIALES DE LA CUENCA DEL RÍO BIOBÍO_ .

Universidad de Chile.

Hossain MA, Sujaul IM, & Nasly MA. (2014). _Application of QUAL2Kw for water quality modeling in_
_the Tunggak River, Kuantan, Pahang, Malaysia_ . Research Journal of Recent Sciences, 3(6), 6-14.

[www.isca.me](http://www.isca.me/)

Kori, B. B., Shashidhar, T., & Mise, S. (2013). _APPLICATION OF AUTOMATED QUAL2Kw FOR WATER_
_QUALITY MODELING IN THE RIVER KARANJA_, INDIA. 2(2), 193-203.

Orenda Technologies, (2023). _“Diferentes tipos de fosfatos”_ .

RIIARn, (202). _“Bases hidrológicas para la conservación de los recursos naturales en la cuenca del_
_lago Moa, Bolivia”._ Revista de Investigación e Innovación Agropecuaria y de Recursos Naturales.
Artículos científcios originales en producción agrícola.

Rivera Gutiérrez, Jorge Virgilio. (2016 _). Determinación de las tasas de oxidación, nitrificación y_
_sedimentación en el proceso de autopurificación de un río de montaña_ . _Ingeniare. Revista chilena de_
_ingeniería_, _24_ (2), 314-326. [https://dx.doi.org/10.4067/S0718-33052016000200013](https://dx.doi.org/10.4067/S0718-33052016000200013)

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

69

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

## ANEXOS ANEXO A - FICHAS TÉCNICAS DE AFORO

Se presentan las fichas técnicas de los aforos realizados en terreno. Distancia corresponde al perfil
transversal, profundidad a la altura de escurrimiento, 0,2H, 0,6H y 0,8H a la medida de velocidad
según sea el caso, y OBS corresponde a observaciones, donde se detalla si corresponde a lámina de
agua derecha (LAD) o lámina de agua izquierda (LAI).

**Tabla 0-1. Ficha técnica Aforo P2.**

|Punto|P2 - Caudal post Pulso|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal Descarga|Canal Descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|10:05|10:05|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|2,60|0,00|-|0,000|-|LAD|
|2,80|6,00|-|0,013|-|-|
|3,00|5,00|-|0,021|-|-|
|3,20|5,00|-|0,027|-|-|
|3,40|5,00|-|0,017|-|-|
|3,70|0,00|-|0,000|-|OBS|
|4,15|4,00|-|0,003|-|-|
|4,30|0,00|-|0,000|-|LAI|

Fuente: elaboración propia.

**Tabla 0-2. Ficha técnica Aforo P2.**

|Punto|P2 - Caudal sin pulso|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal Descarga|Canal Descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|10:25|10:25|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|3,70|0,00|-|0,000|-|LAI|
|3,50|5,00|-|0,030|-|-|
|3,25|4,00|-|0,001|-|-|
|3,10|4,00|-|0,026|-|-|
|2,85|4,00|-|0,001|-|-|
|2,60|0,00|-|0,000|-|LAD|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

70

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 0-3. Ficha técnica Aforo P2.**

|Punto|P2 - Caudal en pulso|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal Descarga|Canal Descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|10:51|10:51|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|3,00|0,00|-|0,000|-|LAD|
|3,30|3,00|-|0,131|-|-|
|3,60|6,00|-|0,526|-|-|
|3,90|5,00|-|0,394|-|-|
|4,35|4,00|-|0,107|-|-|
|4,65|0,00|-|0,000|-|LAI|

Fuente: elaboración propia.

**Tabla 0-4. Ficha técnica Aforo PA.**

|Punto|P2 - Acequia en pulso|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Acequia|Acequia|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|10:30|10:30|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|2,64|0,00|-|0,000|-|LAD|
|2,80|16,00|-|0,655|-|-|
|2,90|16,00|-|0,845|-|-|
|3,05|26,00|-|0,989|-|-|
|3,20|26,00|-|0,984|-|-|
|3,35|22,00|-|1,071|-|-|
|3,60|14,00|-|0,628|-|-|
|3,80|7,00|-|0,160|-|-|
|3,90|0,00|-|0|-|LAI|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

71

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 0-5. Ficha técnica Aforo PA.**

|Punto|P2 - Acequia post pulso|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Acequia|Acequia|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|10:30|10:30|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|3,90|0,00|-|0,000|-|LAI|
|3,70|12,00|-|0,346|-|-|
|3,35|20,00|-|0,533|-|-|
|3,10|24,00|-|0,439|-|-|
|2,80|24,00|-|0,094|-|-|
|2,64|0,00|-|0,000|-|LAD|

Fuente: elaboración propia.

**Tabla 0-6. Ficha técnica Aforo P3.**

|Punto|P3|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal de descarga|Canal de descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|11:20|11:20|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|4,40|0,00|-|0,000|-|LAD|
|4,20|34,00|-|0,006|-|-|
|4,00|35,00|-|0,004|-|-|
|3,80|44,00|-|0,074|-|-|
|3,60|45,00|-|0,131|-|-|
|3,40|33,00|-|0,056|-|-|
|3,20|16,00|-|0,071|-|-|
|3,00|5,00|-|0,033|-|-|
|2,87|0,00|-|0,000|-|LAI|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

72

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 0-7. Ficha técnica Aforo P3.**

|Punto|P3|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal de descarga|Canal de descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|11:40|11:40|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|2,87|0,00|-|0,000|-|LAI|
|3,10|10,00|-|0,074|-|-|
|3,30|24,00|-|0,048|-|-|
|3,50|42,00|-|0,058|-|-|
|3,70|46,00|0,088|-|0,082|-|
|3,90|45,00|-|0,015|-|-|
|4,10|34,00|-|-0,002|-|-|
|4,40|0,00|-|0,000|-|LAD|

Fuente: elaboración propia.

**Tabla 0-8. Ficha técnica Aforo P4’.**

|Punto|P4'|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal de descarga|Canal de descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|12:15|12:15|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|1,70|0,00|-|0,000|-|LAD|
|1,85|6,00|-|0,106|-|-|
|2,00|10,00|-|0,149|-|-|
|2,15|17,00|-|0,214|-|-|
|2,30|17,00|-|0,138|-|-|
|2,45|13,00|-|0,020|-|-|
|2,60|12,00|-|-0,044|-|-|
|2,75|6,00|-|-0,063|-|-|
|3,00|0,00|-|0,000|-|LAI|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

73

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 0-9. Ficha técnica Aforo P4’.**

|Punto|P4'|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Canal de descarga|Canal de descarga|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|12:40|12:40|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|3,00|0,00|-|0,000|-|LAI|
|2,70|6,00|-|-0,052|-|-|
|2,50|13,00|-|0,016|-|-|
|2,35|15,00|-|0,059|-|-|
|2,20|17,00|-|0,190|-|-|
|2,05|12,00|-|0,157|-|-|
|1,90|6,00|-|0,076|-|-|
|1,70|0,00|-|0,000|-|LAD|

Fuente: elaboración propia.

**Tabla 0-10. Ficha técnica Aforo P5-1.**

|Punto|P5 - Brazo Izquierdo|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Río Maipo|Río Maipo|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|13:00|13:00|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|18,10|0,00|-|0,000|-|LAI|
|17,00|13,00|-|0,109|-|-|
|16,00|17,00|-|0,169|-|-|
|15,00|22,00|-|0,506|-|-|
|14,00|13,00|-|0,454|-|-|
|13,00|16,00|-|0,419|-|-|
|12,00|24,00|-|0,494|-|-|
|11,00|31,00|-|0,275|-|-|
|10,00|23,00|-|0,763|-|-|
|9,00|29,00|-|0,609|-|-|
|8,00|32,00|-|0,585|-|-|
|7,00|32,00|-|0,692|-|-|
|6,00|16,00|-|0,394|-|-|
|5,00|17,00|-|0,508|-|-|
|3,50|0,00|-|0,000|-|LAD|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

74

Descarga PTAS BUIN
Modelación de dispersión Río Maipo
Elaborado para: Aguas Andinas
31 de julio de 2024

**Tabla 0-11. Ficha técnica Aforo P5-2**

|Punto|P5 - Brazo Derecho|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Cauce**|Río Maipo|Río Maipo|**Proyecto**|PTAS BUIN|PTAS BUIN|
|**Hora inicio**|13:30|13:30|**Fecha**|14-07-2023|14-07-2023|
|Distancia [m]|Profundidad [cm]|0.2 H [m/s]|0.6 H [m/s]|0.8 H [m/s]|OBS|
|19,20|0,00|-|0,000|-|LAI|
|18,00|44,00|-|0,238|-|-|
|17,00|67,00|0,808|-|1,599|-|
|16,00|60,00|0,863|-|1,312|-|
|15,00|50,00|1,078|-|1,185|-|
|14,00|41,00|-|0,922|-|-|
|13,00|36,00|-|0,856|-|-|
|12,00|30,00|-|0,949|-|-|
|11,00|28,00|-|0,550|-|-|
|10,00|25,00|-|0,802|-|-|
|9,00|22,00|-|0,644|-|-|
|8,00|31,00|-|0,457|-|-|
|7,00|31,00|-|0,771|-|-|
|6,00|25,00|-|0,656|-|-|
|4,80|0,00|-|0,000|-|LAD|

Fuente: elaboración propia.

Plataforma de Investigación EcoHyd Ltda.
Villaseca 21, oficina 501, Ñuñoa-Santiago
contacto@ecohyd.com

75

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1.: Detalles de las salidas a terreno.****

| Campaña | Fecha | Descripción |
| --- | --- | --- |
| C1 | Marzo 2022 | Muestreo de calidad del agua |
| C2 | Julio 2023 | Determinación de batimetría, aforos y calidad del agua |
| C3 | Abril 2024 | Muestreo de calidad del agua |
| C4 | Junio 2024 | Muestreo de calidad del agua |

**Tabla 4-2.: Detalle de los profesionales participantes en las diferentes campañas.****

| Profesional | Nombre | Cargo |
| --- | --- | --- |
| 1 | Luis Abrigo | Especialista de limnología y calidad del agua |
| 2 | Felipe Aguilar | Ingeniero de Proyecto |
| 3 | Tomás Cabrera | Ingeniero de Proyecto |

**Tabla 4-3.: Campañas y sus puntos de muestreo.****

| Punto | Campañas | Col3 | Col4 | Col5 | Curso de agua |
| --- | --- | --- | --- | --- | --- |
| **Punto** | **Marzo 2022** | **Julio 2023** | **Abril 2024** | **Junio 2024** | **Junio 2024** |
| P1 | X | X | X | X | Río Maipo |
| P1a | * | X | X | X | Río Maipo |
| P2 | X | X | X | X | Canal desagüe efluente |
| P3 | X | X | X | X | Canal desagüe efluente |
| P4 | X | X | X | X | Canal desagüe efluente |
| P5 | X | X | * | * | Río Maipo |
| P6 | * | X | X | X | Río Maipo |

**Tabla 4-4.: Resultados muestreo puntos P1 y P1a.****

| Parámetros | Unidad | P1 | Col4 | Col5 | Col6 | P1a | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetros** | **Unidad** | **C1** | **C2** | **C3** | **C4** | **C1** | **C2** | **C3** | **C4** |
| Alcalinidad | mg/l | 145 | 110 | 112 | 109 | * | 110 | 109 | 110 |
| Temperatura | °C | 14,5 | 6,41 | 9,1 | 9,92 | * | 7,59 | 10,6 | 9,79 |
| Clorofila a | mg/l | * | 27,9 | 1,36 | 0,8 | * | 57 | 0,32 | 0,92 |
| Conductividad | us/cm | 1597 | 1894 | 1549 | 1399 | * | 1939 | 1575 | 1402 |
| Coliformes fecales | NMP/100ml | 1,8 | 4900 | 640 | 490 | * | 1,8 | 230 | 230 |
| OD | mg/l | 6,99 | 14,67 | 9,03 | 5,25 | * | 14,8 | 10,6 | 5,27 |
| pH | - | 8,02 | 7,65 | 8,54 | 8,28 | * | 7,5 | 8,7 | 6,95 |
| Nitrato | mg/l | 1,2 | 3,8 | 1,9 | 2 | * | 2,9 | 1,8 | 1,5 |
| Ortofosfato | mg/l | 0,2 | 1,5 | 0,5 | 0,5 | * | 2,6 | 0,5 | 0,5 |
| DBO5 | mg/l | 2 | 15,1 | 1 | 1 | * | 14,9 | 1 | 1 |
| Nitrito | mg/l | 0,03 | 0,05 | 0,039 | 0,039 | * | 0,03 | 0,039 | 0,028 |
| Nitrógeno amoniacal | mg/l | * | 0,58 | 0,16 | 0,02 | * | 1,52 | 0,02 | 0,02 |
| NTK | mg/l | 0,867 | 1,23 | 2,3 | 0,58 | * | 2,36 | 0,6 | 0,55 |
| NT | mg/l | 2,067 | 5,08 | 2,73 | 1,09 | * | 5,26 | 1,01 | 1,13 |
| PT | mg/l | 0,2 | 2,6 | 0,66 | 0,43 | * | 2,7 | 0,17 | 0,48 |
| Fosfato | mg/l | * | 0,13 | 0,05 | 0,05 | * | 0,13 | 0,05 | 0,05 |
| Norg | mg/l | * | 0,65 | 2,17 | 0,7 | * | 0,84 | 0,7 | 0,7 |
| Porg | mg/l | * | 1,1 | * | * | * | 0,2 | * | * |

**Tabla 4-5.: Resultados muestreo puntos P2 y P3.****

| Parámetros | Unidad | P2 | Col4 | Col5 | Col6 | P3 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetros** | **Unidad** | **C1** | **C2** | **C3** | **C4** | **C1** | **C2** | **C3** | **C4** |
| Alcalinidad | mg/l | 145 | 144 | 2 | 155 | 175 | 146 | 2 | 115 |
| Temperatura | °C | 15,1 | 15,73 | 17,4 | 18,3 | 16,4 | 14,15 | 11 | 9,57 |
| Clorofila a | mg/l | * | 10 | 0,02 | 0,02 | * | 10 | 0,47 | 0,47 |
| Conductividad | us/cm | 1666 | 1753 | 1659 | 1545 | 1680 | 1752 | 1572 | 1413 |
| Coliformes fecales | NMP/100ml | 1,8 | 3300 | 640 | 2 | 1,8 | 1,8 | 240 | 23 |
| OD | mg/l | 5,36 | 9,61 | 7,26 | 3,63 | 5,45 | 10,23 | 11 | 5,05 |
| pH | - | 7,61 | 7,23 | 7,69 | 8,95 | 7,8 | 7,48 | 8,7 | 8,11 |
| Nitrato | mg/l | 14,4 | 11,6 | 27,1 | 8,86 | 7,3 | 11,7 | 0,203 | 1,5 |
| Ortofosfato | mg/l | 0,2 | 4,1 | 4,2 | 0,006 | 0,2 | 4 | 0,05 | 0,05 |
| DBO5 | mg/l | 2,54 | 10,4 | 1 | 1 | 4,5 | 11,9 | 1 | 1 |
| Nitrito | mg/l | 0,03 | 0,03 | 0,039 | 0,005 | 0,23 | 0,03 | 0,039 | 0,039 |
| Nitrógeno amoniacal | mg/l | * | 0,98 | 0,02 | 0,02 | * | 0,58 | 0,02 | 0,02 |

**Tabla 4-6.: Resultados muestreo puntos P4 y P5.****

| Parámetros | Unidad | P4 | Col4 | Col5 | Col6 | P5 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetros** | **Unidad** | **C1** | **C2** | **C3** | **C4** | **C1** | **C2** | **C3** | **C4** |
| Alcalinidad | mg/l | 167 | 151 | 2 | 111 | 162 | 110 | * | * |
| Temperatura | °C | 24,02 | 14,28 | 10,6 | 9,6 | 20,3 | 7,22 | * | * |
| Clorofila a | mg/l | * | 10,7 | 0,02 | 1,06 |  | 59,9 | * | * |
| Conductividad | us/cm | 1685 | 1752 | 1570 | 1410 | 1665 | 1944 | * | * |
| Coliformes fecales | NMP/100ml | 1,8 | 4900 | 330 | 330 | 1,8 | 35000 | * | * |
| OD | mg/l | 5,01 | 11,17 | 8,93 | 5,05 | 5,55 | 14,64 | * | * |
| pH | - | 7,95 | 7,55 | 8,72 | 8,28 | 8,32 | 7,36 | * | * |
| Nitrato | mg/l | 7,4 | 10,7 | 2,1 | 1,6 | 8,1 | 3,2 | * | * |
| Ortofosfato | mg/l | 0,2 | 4,2 | 0,06 | 0,5 | 0,2 | 2,6 | * | * |
| DBO5 | mg/l | 2 | 19 | 1 | 1 | 2,47 | 14,4 | * | * |
| Nitrito | mg/l | 0,08 | 0,04 | 0,039 | 0,039 | 0,06 | 0,03 | * | * |
| Nitrógeno amoniacal | mg/l |  | 0,96 | 0,02 | 0,02 |  | 0,98 | * | * |
| NTK | mg/l | 1,7 | 1,97 | 0,23 | 0,5 | 1,2 | 1,57 | * | * |
| NT | mg/l | 9,18 | 12,7 | 0,47 | 0,9 | 9,36 | 4,77 | * | * |
| PT | mg/l | 0,2 | 2,3 | 0,35 | 0,2 | 0,2 | 4,1 | * | * |
| Fosfato | mg/l | * | 0,13 | 0,02 | 0,02 | * | 0,13 | * | * |
| Norg | mg/l | * | 1 | 0,7 | 0,7 | * | 0,59 | * | * |
| Porg | mg/l | * | 0,2 | * | * | * | 1,5 | * | * |

**Tabla 4-7.: Resultados muestreo puntos P6 y P7.****

| Parámetros | Unidad | P6 | Col4 | Col5 | Col6 | P7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetros** | **Unidad** | **C1** | **C2** | **C3** | **C4** | **C1** | **C2** | **C3** | **C4** |
| Alcalinidad | mg/l | * | 112 | 111 | 111 | * | 110 | 113 | 110 |
| Temperatura | °C | * | 7,8 | 9,2 | 9,96 | * | 7,7 | 9,3 | 9,98 |
| Clorofila a | mg/l | * | 51,3 | 73 | 58 | * | 63,3 | 36 | 64 |
| Conductividad | us/cm | * | 1950 | 1575 | 1405 | * | 1945 | 1579 | 1404 |

**Tabla 4-8.: Coordenadas y cotas de los puntos de referencia.****

| PUNTO | UTM N [m] | UTM E [m] | COTA [msnm] |
| --- | --- | --- | --- |
| PR1 | 6.264.075 | 332.529 | 445 |

**Tabla 4-9.: Resultados de los aforos.****

| Punto | Caudal [m3/s] | Hora | Caudal [L/s] | Detalle |
| --- | --- | --- | --- | --- |
| P2 | 0,0008 | 10:05 | 0,8 | Canal desagüe |
| P2 | 0,0005 | 10:25 | 0,5 | Canal desagüe |
| P2 | 0,0177 | 10:51 | 17,7 | Canal desagüe |
| PA | 0,1673 | 10:30 | 167,3 | Canal regadío |
| PA | 0,0735 | 10:40 | 73,5 | Canal regadío |
| P3 | 0,0242 | 11:20 | 24,2 | Canal desagüe |
| P3 | 0,0173 | 11:40 | 17,3 | Canal desagüe |
| P4' | 0,0105 | 12:15 | 10,5 | Canal desagüe |
| P4' | 0,0088 | 12:40 | 8,8 | Canal desagüe |
| P5 - 1 | 1,3769 | 13:00 | 1376,9 | Río Maipo |
| P5 - 2 | 4,0279 | 13:30 | 4027,9 | Río Maipo |

**Tabla 5-3.: Caudales mensuales.****

| Año | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sept | Oct | Nov | Dic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2009 | 35,2 | 20,1 | 3,2 | 0,0 | 0,8 | 0,0 | 0,0 | 0,0 | 7,9 | 1,9 | 9,5 | 38,8 |
| 2010 | 39,1 | 24,8 | 8,0 | 0,7 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,2 | 1,3 | 1,3 |
| 2011 | 0,1 | 0,2 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 2,7 | 5,1 |

**Tabla 5-4.: Caudales anuales.****

| Año | Promedio anual [m3/s] |
| --- | --- |
| 2009 | 9,8 |
| 2010 | 6,3 |
| 2011 | 0,7 |
| 2012 | 2,8 |
| 2013 | 3,5 |
| 2014 | 0,9 |
| 2015 | 2,6 |
| 2016 | 7,8 |

**Tabla 5-5.: Caudales medios mensuales.****

| Mes | Caudal [m3/s] |
| --- | --- |
| abr | 1,03 |
| may | 0,74 |
| jun | 1,16 |

**Tabla 5-6.: Variación estacional.****

| Mes | Caudales asociados a probabilidades de excedencia [m3/s] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **1%** | **5%** | **10%** | **25%** | **50%** | **80%** | **90%** | **95%** |
| Abril | 16,2 | 6,0 | 2,8 | 0,4 | 0,0 | 0,0 | 0,0 | 0,0 |
| Mayo | 11,2 | 4,3 | 2,1 | 0,3 | 0,0 | 0,0 | 0,0 | 0,0 |
| Junio | 19,0 | 6,8 | 3,0 | 0,4 | 0,0 | 0,0 | 0,0 | 0,0 |
| Julio | 0,4 | 0,1 | 0,1 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 |
| Agosto | 4,4 | 1,8 | 0,9 | 0,2 | 0,0 | 0,0 | 0,0 | 0,0 |
| Septiembre | 10,2 | 4,1 | 2,1 | 0,4 | 0,0 | 0,0 | 0,0 | 0,0 |
| Octubre | 5,0 | 2,7 | 1,8 | 0,8 | 0,2 | 0,0 | 0,0 | 0,0 |
| Noviembre | 24,3 | 16,1 | 12,6 | 7,8 | 4,1 | 1,4 | 0,7 | 0,4 |
| Diciembre | 63,3 | 39,3 | 29,1 | 16,2 | 7,0 | 1,7 | 0,6 | 0,2 |
| Enero | 471,9 | 92,0 | 40,9 | 11,6 | 3,2 | 0,8 | 0,4 | 0,3 |
| Febrero | 144,6 | 36,7 | 17,7 | 5,2 | 1,3 | 0,2 | 0,1 | 0,0 |
| Marzo | 10,8 | 4,5 | 2,4 | 0,5 | 0,0 | 0,0 | 0,0 | 0,0 |

**Tabla 6-1.: Límites máximos permitidos para la descarga de residuos líquidos a cuerpos de agua fluviales****

| Parámetro | Unidad | Límite máximo permitido |
| --- | --- | --- |
| Temperatura | °C | 35 |
| DBO5 | mg/L | 35,0 |
| Nitrógeno total Kjeldahl | mg N/L | 50,0 |
| Fósforo | mg P/L | 0,2 |
| Coliformes totales fecales | NMP/100ml | 1000 |
| pH | - | 8,5 |
| Sulfatos | mg/L | 1000 |
| Cloruros | mg/L | 400 |
| Cromo | mg/L | 0,05 |
| Plomo | mg/L | 0,05 |
| Zinc | mg/L | 3 |

**Tabla 6-2.: Concentraciones máximas permitidas en el área de vigilancia MA-4 de la NSCA del Río Maipo.****

| Parámetro | Unidad | MA-4 |
| --- | --- | --- |
| Oxígeno Disuelto | mg/l | 8 |
| Conductividad Eléctrica | S/cm | 1600 |
| pH | - | 6,5 - 8,7 |
| DBO5 | mg/l | 8 |
| Nitrato | mg/l | 4 |
| Ortofosfato | mg/l | 0,15 |
| Cromo total | mg/l | 0,05 |
| Níquel disuelto | mg/l | 0,02 |
| Plomo disuelto | mg/l | 0,007 |
| Zinc disuelto | mg/l | 0,03 |
| Cloruro | mg/l | 180 |
| Sulfato | mg/l | 380 |

**Tabla 7-1.: Reach definidos para la modelación en QUAL2Kw.****

| Reach | Distancia ac.<br>[km] | Cuerpo de agua | Pendiente [-] | Manning [-] | Ancho [m] |
| --- | --- | --- | --- | --- | --- |
| Reach 0 | 0,00 | Canal de desagüe | 0,005 | 0,039 | 1,6 |
| Reach 1 | 0,020 | Canal de desagüe | 0,006 | 0,039 | 2,1 |
| Reach 2 | 0,102 | Canal de desagüe | 0,012 | 0,039 | 1,5 |
| Reach 3 | 0,147 | Canal de desagüe | 0,003 | 0,039 | 3,1 |
| Reach 4 | 0,174 | Canal de desagüe | 0,000 | 0,039 | 3,0 |
| Reach 5 | 0,230 | Canal de desagüe | 0,003 | 0,039 | 3,5 |
| Reach 6 | 0,261 | Canal de desagüe | 0,005 | 0,039 | 2,6 |

**Tabla 7-2.: Tramos representativos para la estimación del número de manning.****

| Tramo | Kilómetros | Rango de Reach del<br>modelo |
| --- | --- | --- |
| 1 | 0,00 - 0,29 | Reach 0 - 7 |

**Tabla 7-3.: Valores número de Manning** **por tramos.****

| Parámetro | Col2 | Valor por tramo | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Parámetro** | **1 ** | **2 ** | **3 ** | **4 ** |
| Material involucrado | n0 | 0,024 | 0,020 | 0,024 | 0,028 |
| Grado de irregularidad | n1 | 0,005 | 0,000 | 0,005 | 0,020 |
| Variaciones en la sección transversal | n2 | 0,005 | 0,005 | 0,005 | 0,005 |
| Efecto relativo de las obstrucciones | n3 | 0,000 | 0,000 | 0,010 | 0,000 |
| Vegetación | n4 | 0,005 | 0,000 | 0,005 | 0,000 |
| Grado sinuosidad | m | 1,000 | 1,000 | 1,000 | 1,000 |
| Manning adoptado | n | 0,039 | 0,025 | 0,049 | 0,053 |

**Tabla 7-4.: Caudales definidos para las calibraciones del modelo.****

| Punto | Curso de agua | Caudal [m3/s] |
| --- | --- | --- |
| **Punto** | **Curso de agua** | **Julio 2023** |
| P3 | Canal de desagüe | 0,021 |
| P5 | Río Maipo | 5,401 |

**Tabla 7-5.: Parámetros fisicoquímicos modelados.****

| Parámetros modelados | Unidad | Abreviación | Parámetros de<br>entrada |
| --- | --- | --- | --- |
| Conductividad eléctrica | us/cm | CE | X |
| Demanda Biológica de Oxígeno | mg/l | DBO5 | X |
| Coliformes Fecales Totales | NMP/100ml | CFT | X |
| Nitrato | mg/l | Nn | X |
| Nitrito | mg/l | Ni | - |
| Nitrógeno Amoniacal | mg/l | Na | X |
| Nitrógeno Total Kjeldahl | mg/l | NTK | - |
| Nitrógeno orgánico | mg/l | Norg | X |
| Nitrógeno Total | mg/l | NT | - |
| Fósforo orgánico | mg/l | Porg | X |
| Fósforo Inorgánico | mg/l | Pinorg | X |

**Tabla 7-6.: Condiciones fisicoquímicas aguas arribas.****

| Parámetro | Unidad | Julio 2023 |
| --- | --- | --- |
| CE | s/cm | 1753 |
| DBO5 | mg/L | 10,4 |
| CT | NMP/100 mL | 4900 |
| Nn | mg N/L | 11,60 |
| Na | mg N/L | 0,98 |
| Norg | mg N/L | 1,5 |
| NTK | mg N/L | 1,35 |
| Pinorg | mg P/L | 4,1 |
| pH | - | 7,23 |
| OD | mg/l | 9,61 |
| T° | °C | 20,6 |

**Tabla 7-8.: Parámetros fisicoquímicos de las fuentes puntuales.****

| Parámetro | Unidad | Río Maipo |
| --- | --- | --- |
| **Parámetro** | **Unidad** | **Julio 2023** |
| CE | us/cm | 1939 |
| DBO5 | mg/L | 15,1 |
| CT | NMP/100 mL | 7900 |
| Nn | mg N/L | 2,9 |
| Na | mg N/L | 1,52 |
| pH | mg N/L | 7,5 |
| Pinorg | mg P/L | 2,6 |
| Porg | mg P/L | 1,1 |
| Norg | - | 0,84 |
| OD | mg/l | 14,8 |
| T° | °C | 20,7 |

**Tabla 7-9.: Parámetros fisicoquímicos y sus respectivos pesos para la calibración.****

| Parámetro | Unidad | Peso |
| --- | --- | --- |
| Nn | mg/l | 3 |
| Norg | mg/l | 3 |
| NT | mg/l | 1 |
| Pinorg | mg/l | 3 |
| PT | mg/l | 1 |
| T° | °C | 3 |
| OD | mg/l | 3 |
| DBO5 | mg/l | 2 |
| CFT | NMP/100ml | 2 |
| CE | us/cm | 1 |
| pH | - | 1 |

**Tabla 7-10.: Rangos de clasificación para el R** **[2]** **y PBIAS.****

| Criterio | Valor | Clasificación |
| --- | --- | --- |
| R2 | 0,75 < R2 < 1,00 | Muy bueno |
| R2 | 0,65 < R2 < 0,75 | Bueno |
| R2 | 0,50 < R2 < 0,65 | Satisfactorio |
| R2 | R2 < 0,50 | Insatisfactorio |
| PBIAS | PBIAS < 10 | Muy bueno |
| PBIAS | 10 < PBIAS < 15 | Bueno |
| PBIAS | 15 < PBIAS < 25 | Satisfactorio |
| PBIAS | 20 < | Insatisfactorio |

**Tabla 7-11.: Caudales fijados para los 4 escenarios.****

| Escenario | Caudales ingresados [m3/s] | Col3 | Operación PTAS |
| --- | --- | --- | --- |
| **Escenario** | **Descarga PTAS Buin** | **Río Maipo** | **Río Maipo** |
| 1 | 0,544 | 0,243 | Futura |
| 2 | 0,544 | 0,122 | Futura |
| 3 | 0,298 | 0,243 | Actual |
| 4 | 0,298 | 0,122 | Actual |

**Tabla 7-12.: Caudales asociados a los distintos escenarios de simulación.****

| Escenario | Descripción | Caudal (m3/s) |
| --- | --- | --- |
| E1 y E3<br>(Q95%) | Menor valor de caudal asociado a una probabilidad de excedencia<br>de un 95% sin considerar valores nulos. | 0,243 |
| E2 y E4<br>(50% Q95%) | Mitad del menor valor de caudal asociado a una probabilidad de<br>excedencia de un 95% sin considerar valores nulos. | 0,122 |

**Tabla 7-13.: Concentraciones fijadas para los 4 escenarios.****

| Parámetro | Unidad | Descarga PTAS y<br>P2 | Río Maipo<br>(P1-P1a) |
| --- | --- | --- | --- |
| Temperatura | °C | 35 | 9,7 |
| Conductividad Eléctrica | us/cm | 1655,8 | 1624,2 |
| Oxígeno Disuelto | mg/L | 6,5 | 9,6 |
| Demanda Biológica de Oxígeno | mg/L | 35,0 | 5,2 |
| Nitrógeno orgánico | mg N/L | 28,0 | 1,0 |
| Nitrógeno amoniacal | mg N/L | 7,0 | 0,4 |
| Nitrato | mg N/L | 59,0 | 2,1 |
| Nitrógeno Total Kjedhal | mg N/L | 50,0 | 1,2 |
| Fósforo Orgánico | mg P/L | 0,5 | 0,7 |
| Fósforo inogánico | mg P/L | 9,5 | 0,9 |
| Coliformes Totales | NMP/100ml | 1000 | 830,9 |
| pH | - | 6,0 | 7,9 |

**Tabla 7-14.: Porcentajes de Nn, Ni, Na, Norg y NKT del nitrógeno total en función de los datos obtenidos en****

| % del Nitrógeno Total | P1a | P2 | P3 | P4 | P5 | P6 | P7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nitrato (N-NO3-) | 55% | 82% | 84% | 84% | 67% | 69% | 54% |
| Nitrito (N-NO2-) | 1% | 1% | 0% | 0% | 0% | 1% | 1% |
| Nitrógeno amoniacal (NH4+) | 29% | 7% | 4% | 8% | 20% | 21% | 20% |
| Nitrógeno Total Kjeldhal (NTK) | 45% | 18% | 15% | 15% | 33% | 31% | 45% |
| Nitrogeno organico | 16% | 11% | 12% | 8% | 12% | 10% | 25% |
| Nitrogeno Total (NT) | 100% | 100% | 100% | 100% | 100% | 100% | 100% |

**Tabla 7-15.: Concentraciones máximas permitidas en el área de vigilancia MA-4 de la NSCA del Río Maipo.****

| Parámetro | Unidad | MA-4 |
| --- | --- | --- |
| Oxígeno Disuelto | mg/l | 8 |
| Conductividad Eléctrica | S/cm | 1600 |
| pH | - | 6,5 - 8,7 |
| DBO5 | mg/l | 8 |
| Nitrato | mg/l | 4 |
| Ortofosfato | mg/l | 0,15 |

**Tabla 7-16.: Segmentos definidos para la modelación.****

| Tramo | Kilómetros | Ancho (m) | Pendiente | Rugosidad |
| --- | --- | --- | --- | --- |
| Tramo_1 | 0-0,02 | 2,08883 | 0,00645 | <br>0,039 |
| Tramo_2 | 0,02-0,102 | 1,52508 | 0,01230 | <br>0,039 |
| Tramo_3 | 0,102-0,147 | 3,07006 | 0,00315 | <br>0,039 |
| Tramo_4 | 0,147-0,174 | 3,0392 | 0,00015 | <br>0,039 |
| Tramo_5 | 0,174-0,23 | 3,45952 | 0,00288 | <br>0,039 |
| Tramo_6 | 0,23-0,261 | 2,64601 | 0,00534 | <br>0,039 |
| Tramo_7 | 0,261-0,291 | 4,35492 | 0,00483 | <br>0,039 |
| Tramo_8 | 0,291-0,334 | 2,3961 | 0,00483 | <br>0,025 |
| Tramo_9 | 0,334-0,385 | 1,35142 | 0,00045 | <br>0,025 |
| Tramo_10 | 0,385-0,406 | 1,96784 | 0,00436 | <br>0,025 |
| Tramo_11 | 0,406-0,462 | 7,43615 | 0,00089 | <br>0,025 |
| Tramo_12 | 0,462-0,544 | 0,56387 | 0,00111 | <br>0,025 |
| Tramo_13 | 0,544-0,585 | 8,69852 | 0,00056 | <br>0,025 |
| Tramo_14 | 0,585-0,617 | 6,08124 | 0,00162 | <br>0,049 |
| Tramo_15 | 0,617-0,649 | 2,7586 | 0,00268 | <br>0,049 |
| Tramo_16 | 0,649-0,668 | 2,72616 | 0,00011 | <br>0,049 |
| Rio_Maipo | 0,668-0,71 | 29,6075 | 0,00821 | <br>0,053 |
| Tramo_17 | 0,71-0,785 | 29,6075 | 0,00821 | <br>0,053 |
| Tramo_18 | 0,785-0,889 | 29,6075 | 0,00821 | <br>0,053 |
| Tramo_19 | 0,889-1,127 | 47,0507 | 0,00733 | <br>0,053 |
| Tramo_20 | 1,127-1,31 | 47,0507 | 0,00733 | <br>0,053 |

**Tabla 7-17.: Caudales definidos para las calibraciones del modelo.****

| Punto | Caudal [m3/s] |
| --- | --- |
| **Punto** | **Julio 2023** |
| P2 | 0,021 |
| P5-1 + P5-2 | 5,405 |

**Tabla 7-18.: Caudales definidos para las calibraciones del modelo.****

| Punto de medición | Cinc disuelto | Cromo | Níquel disuelto | Plomo |
| --- | --- | --- | --- | --- |
| **Punto de medición** | **mg Zn/L** | **mg Cr/L** | **mg Ni/L** | **mg Pb/L** |
| P1 | 0,03 | < 0,005 | < 0,005 | 0,0122 |
| P2 | 0,061 | < 0,005 | < 0,005 | 0,0071 |
| P3 | 0,021 | < 0,005 | < 0,005 | 0,0015 |
| P4 | 0,051 | < 0,005 | < 0,005 | 0,0024 |
| P5 | 0,045 | < 0,005 | < 0,005 | 0,0119 |

**Tabla 7-19.: Caudales de los distintos cursos de aguas definidos para los 4 escenarios.****

| Escenario | Caudales ingresados [m3/s] | Col3 |
| --- | --- | --- |
| **Escenario** | **Descarga PTAS Buin** | **Río Maipo** |
| 1 | 0,544 | 0,243 |
| 2 | 0,544 | 0,122 |
| 3 | 0,298 | 0,243 |
| 4 | 0,298 | 0,122 |

**Tabla 7-20.: Concentraciones en las distintas campañas de calidad del agua.****

| Parámetro | Unidad | Marzo 2022 | Julio 2023 | Abril 2024 | Junio 2024 | Descarga<br>PTAS Buin |
| --- | --- | --- | --- | --- | --- | --- |
| Plomo disuelto | mg/l | <0,01 | 0,0071 | <0,012 | <0,012 | 0,0071 |
| Cinc Disuelto | mg/l | 0,039 | 0,061 | <0,006 | <0,006 | 0,05 |
| Cromo | mg/l | <0,005 | <0,005 | <0,026 | <0,024 | 0,015 |
| Níquel disuelto | mg/l | <0,005 | <0,005 | <0,018 | <0,018 | 0,0115 |

**Tabla 7-21.: Concentraciones fijadas para los 6 escenarios.****

| Parámetro | Unidad | Descarga- Canal desagüe afluente | Río Maipo |
| --- | --- | --- | --- |
| Plomo disuelto | mg/l | 0,0071 | 0,011 |
| Cinc Disuelto | mg/l | 0,05 | 0,012 |
| Cromo | mg/l | 0,015 | 0,016 |
| Níquel disuelto | mg/l | 0,0115 | 0,012 |

**Tabla 7-22.: Concentraciones máximas permitidas en el área de vigilancia MA-4 de la NSCA del Río Maipo.****

| Parámetro | Unidad | MA-4 |
| --- | --- | --- |
| Plomo disuelto | mg/l | 0,007 |
| Cinc Disuelto | mg/l | 0,03 |
| Cromo | mg/l | 0,05 |
| Níquel disuelto | mg/l | 0,02 |

**Tabla 7-25.: Concentraciones en las distintas campañas de calidad del agua en el río Maipo aguas arriba de****

| Parámetro | Unidad | Marzo 2022 | Julio 2023 | Abril 2024 | Junio 2024 |
| --- | --- | --- | --- | --- | --- |
| Cloruro | mg/l | 241 | 276 | 195.7 | 224 |
| Sulfato | mg/l | 397 | 320 | 386 | 480 |

**Tabla 8-1.: Resultados de los estadísticos para la calibración.****

| Modelo | MD_BUIN |
| --- | --- |
| Campaña | Julio 2023 |
| Fitness | 4,24 |
| NRMSE | 0,20 |
| R2 | 0,57 |
| PBIAS | 0,12 |

**Tabla 8-2.: Resultados de los estadísticos para la evaluación de la calibración.****

| Parámetro | RMSE | NRMSE | R2 | PBIAS |
| --- | --- | --- | --- | --- |
| T° | 0,374 | 0,018 | 0,039 | 0,014 |
| CE | 6,585 | 0,004 | 1,000 | 0,002 |

**Tabla 8-3.: Cursos de aguas afluentes al eje principal del modelo.****

| Punto | Cuerpo afluente | Distancia [km] |
| --- | --- | --- |
| P1a | Río Maipo | 0,70 |

**Tabla 8-4.: Variables calibradas.****

| Variables | Unidad | Rango | Valor |
| --- | --- | --- | --- |
| Reaireación | 1/d | - | 416 |
| Oxidación DBO5 | /d | 0-4,3 | 3,27 |
| Hidrólisis N | /d | 0,01-50 | 12,5 |

**Tabla 8-5.: Áreas de influencia para los escenarios 1, 2, 3 y 4.****

| Parámetro | Área de influencia [km] | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **E1** | **E2** | **E3** | **E4** |
| OD | 0,00 | 0,00 | 0,00 | 0,00 |
| DBO5 | 6,57 | 6,53 | 5,86 | 5,85 |
| Norg | 2,53 | 2,67 | 1,94 | 2,13 |
| Nn | 9,79 | 8,80 | 9,18 | 7,49 |
| Porg | 0,25 | 0,15 | 0,41 | 0,23 |
| Pinorg | 0,72 | 0,68 | 0,59 | 0,54 |
| CT | 0,00 | 0,00 | 0,00 | 0,00 |
| Q Río Maipo [m3/s] | 0,243 | 0,122 | 0,243 | 0,122 |
| Q Descarga [m3/s] | 0,544 | 0,544 | 0,298 | 0,298 |

**Tabla 8-6.: Resultados de la calibración.****

| Parámetro | Plomo disuelto | Cinc disuelto | Cromo | Níquel disuelto |
| --- | --- | --- | --- | --- |
| Peso molecular [g/mol] | 207,2 | 65,37 | 51,99 | 58,69 |
| Solubilidad [g/m3] | 4 | 2300 | 140 | 0,2 |
| Coeficiente de partición | 4,2 | 3,1 | 3,9 | 3,1 |
| Decaimiento 1° orden | 0.85 | 0,25 | -- | -- |

**Tabla 8-7.: Resultados de RMSE para cada parámetro modelado.****

| Parámetro | RMSE [mg/l] |
| --- | --- |
| Plomo disuelto | 0,0015 |
| Cinc Disuelto | 0,012 |
| Cromo | 0,00 |
| Níquel disuelto | 0,00 |

**Tabla 8-8.: Concentraciones y caudales por cada escenario.****

| Escenario | Punto | Caudal<br>[m3/s] | Plomo<br>disuelto<br>[mg/l] | Cinc Disuelto<br>[mg/l] | Cromo<br>[mg/l] | Níquel<br>disuelto<br>[mg/l] |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | P2 (Tramo_1) | 0,544 | 0,0071 | 0,05 | 0,015 | 0,0115 |
| 1 | P1-A<br>(Rio_Maipo) | 0,243 | 0,011 | 0,012 | 0,016 | 0,012 |
| 2 | P2 (Tramo_1) | 0,544 | 0,0071 | 0,05 | 0,015 | 0,0115 |
| 2 | P1-A<br>(Rio_Maipo) | 0,122 | 0,011 | 0,012 | 0,016 | 0,012 |
| 3 | P2 (Tramo_1) | 0,298 | 0,0071 | 0,05 | 0,015 | 0,0115 |
| 3 | P1-A<br>(Rio_Maipo) | 0,243 | 0,011 | 0,012 | 0,016 | 0,012 |
| 4 | P2 (Tramo_1) | 0,298 | 0,0071 | 0,05 | 0,015 | 0,0115 |
| 4 | P1-A<br>(Rio_Maipo) | 0,122 | 0,011 | 0,012 | 0,016 | 0,012 |

**Tabla 8-9: Escenarios de simulación para modelación de cloruros y sulfatos****

| Col1 | Caudal (l/s) | Col3 | Concentración efluente (mg/l) | Col5 | Concentración Maipo (mg/l) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Qdescarga** | **Rio Maipo** | **Cloruro** | **Sulfato** | **Cloruro** | **Sulfato** |
| **Escenario 1** | 0,544 | 0,243 | 380 | 500 | 234 | 396 |
| **Escenario 2** | 0,544 | 0,122 | 380 | 500 | 234 | 396 |
| **Escenario 3** | 0,298 | 0,243 | 380 | 500 | 234 | 396 |
| **Escenario 4** | 0,298 | 0,122 | 380 | 500 | 234 | 396 |

**Tabla 8-10: Aumentos porcentuales de la concentración de cloruro y sulfato para la condición proyectada****

| Punto | Escenarios 1-3 | Escenarios 2-4 |
| --- | --- | --- |
| P2 | 0% | 0% |
| P3 | 0% | 0% |
| P4 | 0% | 0% |
| P1 | 0% | 0% |
| P1a + P1 | 0% | 0% |
| P5 | 39% | 7% |
| P6 | 39% | 7% |
| P7 | 39% | 7% |

**Tabla 9-1.: Comparación de concentraciones máximas sobre el río Maipo (P5, P6, P7)), E1 y E3.****

| Parámetro | Unidad | Concentración<br>máxima actual<br>E3 | Concentración<br>máxima futura<br>E1 | % |
| --- | --- | --- | --- | --- |
| Conductividad eléctrica | us/cm | 1641,61 | 1646,04 | 0,3% |
| DBO5 | mg/l | 20,31 | 23,33 | 14,9% |
| Nitrógeno orgánico | mg/l | 4,27 | 4,78 | 11,8% |
| Nitrato | mg/l | 29,83 | 34,01 | 14,0% |
| Ortofosfato | mg/l | 3,27 | 3,52 | 7,6% |
| Fosforo orgánico | mg/l | 1,25 | 1,10 | -11,7% |
| Cinc disuelto | mg/l | 0,0329 | 0,0383 | 16,4% |
| Plomo disuelto | mg/l | 0,00678 | 0,00612 | -9,7% |
| Cromo | mg/l | 0,0154 | 0,0153 | -0,65% |
| Níquel disuelto | mg/l | 0,0117 | 0,0117 | 0% |
| Sulfato | mg/l | 453,3 | 480,9 | 6% |
| Cloruro | mg/l | 314 | 335 | 7% |

**Tabla 9-2.: Comparación de concentraciones máximas, E2 y E4.****

| Parámetro | Unidad | Concentración<br>máxima actual<br>E4 | Concentración<br>máxima futura<br>E2 | % |
| --- | --- | --- | --- | --- |
| Conductividad eléctrica | us/cm | 1641,61 | 1646,04 | 0,3% |
| DBO5 | mg/l | 20,31 | 23,33 | 14,9% |
| Nitrógeno orgánico | mg/l | 4,27 | 4,78 | 11,8% |
| Nitrato | mg/l | 29,83 | 34,01 | 14,0% |
| Ortofosfato | mg/l | 3,27 | 3,52 | 7,6% |
| Fosforo orgánico | mg/l | 1,25 | 1,10 | -11,7% |
| Cinc disuelto | mg/l | 0,0039 | 0,043 | 10,25% |
| Plomo disuelto | mg/l | 0,00557 | 0,00524 | -5,92% |
| Cromo | mg/l | 0,0153 | 0,0152 | -0,65% |
| Níquel disuelto | mg/l | 0,0116 | 0,0116 | 0% |
| Sulfato | mg/l | 469,8 | 480,9 | 2% |

**Tabla 9-3.: Comparación de las áreas de influencia, E1 y E3.****

| Parámetro | Área de<br>influencia actual<br>E3 [km] | Área de<br>influencia futura<br>E1 [km] | Diferencia [km] |
| --- | --- | --- | --- |
| Conductividad eléctrica | 0,00 | 0,00 | 0,00 |
| Oxígeno disuelto | 0,00 | 0,00 | 0,00 |
| DBO5 | 5,84 | 6,57 | 0,73 |
| Nitrógeno orgánico | 1,94 | 2,53 | 0,59 |
| Nitrato | 9,18 | 9,79 | 0,61 |
| Ortofosfato | 0,59 | 0,72 | 0,13 |
| Fosforo orgánico | 0,41 | 0,25 | -0,16 |
| Coliformes totales | 0,00 | 0,00 | 0,00 |

**Tabla 9-4.: Comparación de las áreas de influencia, E2 y E4.****

| Parámetro | Área de<br>influencia actual<br>E4 [km] | Área de<br>influencia futura<br>E2 [km] | Diferencia [km] |
| --- | --- | --- | --- |
| Conductividad eléctrica | 0,00 | 0,00 | 0,00 |
| Oxígeno disuelto | 0,00 | 0,00 | 0,00 |
| DBO5 | 5,85 | 6,53 | 0,68 |

**Tabla 0-1.: Ficha técnica Aforo P2.****

| Punto | P2 - Caudal post Pulso | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal Descarga | Canal Descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 10:05 | 10:05 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 2,60 | 0,00 | - | 0,000 | - | LAD |
| 2,80 | 6,00 | - | 0,013 | - | - |
| 3,00 | 5,00 | - | 0,021 | - | - |
| 3,20 | 5,00 | - | 0,027 | - | - |
| 3,40 | 5,00 | - | 0,017 | - | - |
| 3,70 | 0,00 | - | 0,000 | - | OBS |
| 4,15 | 4,00 | - | 0,003 | - | - |
| 4,30 | 0,00 | - | 0,000 | - | LAI |

**Tabla 0-2.: Ficha técnica Aforo P2.****

| Punto | P2 - Caudal sin pulso | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal Descarga | Canal Descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 10:25 | 10:25 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 3,70 | 0,00 | - | 0,000 | - | LAI |
| 3,50 | 5,00 | - | 0,030 | - | - |
| 3,25 | 4,00 | - | 0,001 | - | - |
| 3,10 | 4,00 | - | 0,026 | - | - |
| 2,85 | 4,00 | - | 0,001 | - | - |
| 2,60 | 0,00 | - | 0,000 | - | LAD |

**Tabla 0-3.: Ficha técnica Aforo P2.****

| Punto | P2 - Caudal en pulso | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal Descarga | Canal Descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 10:51 | 10:51 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 3,00 | 0,00 | - | 0,000 | - | LAD |
| 3,30 | 3,00 | - | 0,131 | - | - |
| 3,60 | 6,00 | - | 0,526 | - | - |
| 3,90 | 5,00 | - | 0,394 | - | - |
| 4,35 | 4,00 | - | 0,107 | - | - |
| 4,65 | 0,00 | - | 0,000 | - | LAI |

**Tabla 0-4.: Ficha técnica Aforo PA.****

| Punto | P2 - Acequia en pulso | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Acequia | Acequia | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 10:30 | 10:30 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 2,64 | 0,00 | - | 0,000 | - | LAD |
| 2,80 | 16,00 | - | 0,655 | - | - |
| 2,90 | 16,00 | - | 0,845 | - | - |
| 3,05 | 26,00 | - | 0,989 | - | - |
| 3,20 | 26,00 | - | 0,984 | - | - |
| 3,35 | 22,00 | - | 1,071 | - | - |
| 3,60 | 14,00 | - | 0,628 | - | - |
| 3,80 | 7,00 | - | 0,160 | - | - |
| 3,90 | 0,00 | - | 0 | - | LAI |

**Tabla 0-5.: Ficha técnica Aforo PA.****

| Punto | P2 - Acequia post pulso | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Acequia | Acequia | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 10:30 | 10:30 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 3,90 | 0,00 | - | 0,000 | - | LAI |
| 3,70 | 12,00 | - | 0,346 | - | - |
| 3,35 | 20,00 | - | 0,533 | - | - |
| 3,10 | 24,00 | - | 0,439 | - | - |
| 2,80 | 24,00 | - | 0,094 | - | - |
| 2,64 | 0,00 | - | 0,000 | - | LAD |

**Tabla 0-6.: Ficha técnica Aforo P3.****

| Punto | P3 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal de descarga | Canal de descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 11:20 | 11:20 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 4,40 | 0,00 | - | 0,000 | - | LAD |
| 4,20 | 34,00 | - | 0,006 | - | - |
| 4,00 | 35,00 | - | 0,004 | - | - |
| 3,80 | 44,00 | - | 0,074 | - | - |
| 3,60 | 45,00 | - | 0,131 | - | - |
| 3,40 | 33,00 | - | 0,056 | - | - |
| 3,20 | 16,00 | - | 0,071 | - | - |
| 3,00 | 5,00 | - | 0,033 | - | - |
| 2,87 | 0,00 | - | 0,000 | - | LAI |

**Tabla 0-7.: Ficha técnica Aforo P3.****

| Punto | P3 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal de descarga | Canal de descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 11:40 | 11:40 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 2,87 | 0,00 | - | 0,000 | - | LAI |
| 3,10 | 10,00 | - | 0,074 | - | - |
| 3,30 | 24,00 | - | 0,048 | - | - |
| 3,50 | 42,00 | - | 0,058 | - | - |
| 3,70 | 46,00 | 0,088 | - | 0,082 | - |
| 3,90 | 45,00 | - | 0,015 | - | - |
| 4,10 | 34,00 | - | -0,002 | - | - |
| 4,40 | 0,00 | - | 0,000 | - | LAD |

**Tabla 0-8.: Ficha técnica Aforo P4’.****

| Punto | P4' | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal de descarga | Canal de descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 12:15 | 12:15 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 1,70 | 0,00 | - | 0,000 | - | LAD |
| 1,85 | 6,00 | - | 0,106 | - | - |
| 2,00 | 10,00 | - | 0,149 | - | - |
| 2,15 | 17,00 | - | 0,214 | - | - |
| 2,30 | 17,00 | - | 0,138 | - | - |
| 2,45 | 13,00 | - | 0,020 | - | - |
| 2,60 | 12,00 | - | -0,044 | - | - |
| 2,75 | 6,00 | - | -0,063 | - | - |
| 3,00 | 0,00 | - | 0,000 | - | LAI |

**Tabla 0-9.: Ficha técnica Aforo P4’.****

| Punto | P4' | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Canal de descarga | Canal de descarga | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 12:40 | 12:40 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 3,00 | 0,00 | - | 0,000 | - | LAI |
| 2,70 | 6,00 | - | -0,052 | - | - |
| 2,50 | 13,00 | - | 0,016 | - | - |
| 2,35 | 15,00 | - | 0,059 | - | - |
| 2,20 | 17,00 | - | 0,190 | - | - |
| 2,05 | 12,00 | - | 0,157 | - | - |
| 1,90 | 6,00 | - | 0,076 | - | - |
| 1,70 | 0,00 | - | 0,000 | - | LAD |

**Tabla 0-10.: Ficha técnica Aforo P5-1.****

| Punto | P5 - Brazo Izquierdo | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Río Maipo | Río Maipo | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 13:00 | 13:00 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 18,10 | 0,00 | - | 0,000 | - | LAI |
| 17,00 | 13,00 | - | 0,109 | - | - |
| 16,00 | 17,00 | - | 0,169 | - | - |
| 15,00 | 22,00 | - | 0,506 | - | - |
| 14,00 | 13,00 | - | 0,454 | - | - |
| 13,00 | 16,00 | - | 0,419 | - | - |
| 12,00 | 24,00 | - | 0,494 | - | - |
| 11,00 | 31,00 | - | 0,275 | - | - |
| 10,00 | 23,00 | - | 0,763 | - | - |
| 9,00 | 29,00 | - | 0,609 | - | - |
| 8,00 | 32,00 | - | 0,585 | - | - |
| 7,00 | 32,00 | - | 0,692 | - | - |
| 6,00 | 16,00 | - | 0,394 | - | - |
| 5,00 | 17,00 | - | 0,508 | - | - |
| 3,50 | 0,00 | - | 0,000 | - | LAD |

**Tabla 0-11.: Ficha técnica Aforo P5-2****

| Punto | P5 - Brazo Derecho | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Cauce** | Río Maipo | Río Maipo | **Proyecto** | PTAS BUIN | PTAS BUIN |
| **Hora inicio** | 13:30 | 13:30 | **Fecha** | 14-07-2023 | 14-07-2023 |
| Distancia [m] | Profundidad [cm] | 0.2 H [m/s] | 0.6 H [m/s] | 0.8 H [m/s] | OBS |
| 19,20 | 0,00 | - | 0,000 | - | LAI |
| 18,00 | 44,00 | - | 0,238 | - | - |
| 17,00 | 67,00 | 0,808 | - | 1,599 | - |
| 16,00 | 60,00 | 0,863 | - | 1,312 | - |
| 15,00 | 50,00 | 1,078 | - | 1,185 | - |
| 14,00 | 41,00 | - | 0,922 | - | - |
| 13,00 | 36,00 | - | 0,856 | - | - |
| 12,00 | 30,00 | - | 0,949 | - | - |
| 11,00 | 28,00 | - | 0,550 | - | - |
| 10,00 | 25,00 | - | 0,802 | - | - |
| 9,00 | 22,00 | - | 0,644 | - | - |
| 8,00 | 31,00 | - | 0,457 | - | - |
| 7,00 | 31,00 | - | 0,771 | - | - |
| 6,00 | 25,00 | - | 0,656 | - | - |
| 4,80 | 0,00 | - | 0,000 | - | LAD |
