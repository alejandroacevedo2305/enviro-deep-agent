---
title: GOBIERNO DE CHILE
author: Angelina Alarcon
date: D:20240805112855-04'00'
language: es
type: report
pages: 33
has_toc: False
has_tables: True
extraction_quality: high
---

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

## PROYECTO AMPLIACIÓN PORTAL TEMUCO “EMPALME A RED SECUNDARIA” MEMORIA DE CÁLCULO

INDICE Página

**1.** **GENERALIDADES .............................................................................................. 3**
1.1. Descripción del Proyecto .............................................................................. 6
1.2. Descripción de las obras ............................................................................... 7
1.2.1 Ubicación de las obras ................................................................................ 7

1.3. Consideraciones Generales .......................................................................... 7
**2.** **TOPOGRAFÍA ..................................................................................................... 8**
**3.** **HIDROLOGÍA. ..................................................................................................... 9**

3.1 Antecedentes ................................................................................................ 9

3.2 Cálculo de Caudal ......................................................................................... 9

3.2.1 Caudales Mediante Método Racional .......................................................... 9

3.3 Periodo de Retorno ..................................................................................... 15
**4.** **ESTUDIO HIDRÁULICO .................................................................................... 16**

4.1 Generalidades ............................................................................................. 16

4.2 Modelación hidráulica con EPA SWMM 5.1 ................................................ 16

**5.** **RESULTADOS Y ANEXOS DEL ESTUDIO ...................................................... 19**

**6.** **CONCLUSIONES .............................................................................................. 23**

**7.** **ANEXOS ............................................................................................................ 24**
**Anexo No1: “Modelación Hidráulica en EPA SWMM”. .......................................... 24**
**Anexo No2:** **“Verificación** **Hidráulica Colector** **Situación** **Sin** **Proyecto**
**considerando un periodo de retorno de 5, 10 y 100 años”. ................................. 26**
**Anexo No3: “Verificación Hidráulica Colector Situación Con Proyecto**
**considerando un periodo de retorno de 5, 10 y 100 años”. ................................. 28**
**Anexo No4: “Perfil Longitudinal Colector para T = 5 años, T = 10 años y T = 100**
**años”. ....................................................................................................................... 30**

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

## PROYECTO AMPLIACIÓN PORTAL TEMUCO “EMPALME A RED SECUNDARIA” MEMORIA DE CÁLCULO

**1. GENERALIDADES**

El presente documento se enmarca dentro del proyecto de Ampliación del Portal
Temuco, asociado al empalme de una tubería a la red secundaria, ubicada en la calle
España, la cual que tiene como objetivo sanear las aguas lluvias provenientes de su
ampliación. La ampliación se encuentra ubicada en el sector nororiente del terreno del
Portal, en la comuna de Temuco, provincia de Cautín, región de la Araucanía.

_Figura 1.1 Ubicación Área de estudio_

_Fuente: Elaboración propia_

**3**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

Actualmente, el Portal Temuco posee una red interna que recolecta las aguas lluvias
generadas dentro de su área para luego descargarlas a un colector secundario ubicado
en la calle España, tal como se muestra en la Figura 1.2. Además de las aguas lluvias
recolectadas, dentro del área del centro comercial existen 7 pozos de abatimiento,
situados a lo largo del perímetro del Portal, con el objetivo de deprimir la napa y
mantener su nivel bajo la cota del subterráneo del sector. Las aguas generadas por el
abatimiento de los distintos pozos son recolectadas y trasladadas por un colector
interno del Portal Temuco, para luego descargarlas a la red secundaria mencionada
anteriormente.

_Figura 1.2 Portal Temuco Situación Actual_

_Fuente: Elaboración propia_

**4**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

Por otro lado, se considera la ampliación del Portal Temuco en el sector nororiente,
con una superficie nueva de 0.55 ha, generando una red interna aguas lluvias, además
de un nuevo pozo de abatimiento ubicado en su ampliación, tal como se muestra en la
siguiente figura. Dichas aguas serán descargadas al colector secundario existente.

_Figura 1.3 Ampliación Portal Temuco, situación con proyecto_

_Fuente: Elaboración propia_

A partir de lo anterior, el presente documento surge de la necesidad de verificar
hidráulicamente el colector secundario en una situación proyectada y para un periodo
de retorno determinado, debido a las descargadas de aguas lluvias generadas en el
área existente del Portal Temuco, en conjunto con el caudal generado por el
abatimiento de los 7 pozos existentes y de la descarga nueva producto de las aguas
lluvias generadas en la superficie correspondiente a su ampliación, y el caudal de
abatimiento del pozo proyectado. El colector secundario corresponde a un cajón de
hormigón de 0.7 x 1.2 m. Cabe destacar que el proyecto contempla solo la descarga a
la cámara pública existente, la cual no necesita rotura y reposición de pavimento, como
también un diseño de pavimento asociado a la ampliación.

**5**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

El tramo en estudio del colector se define desde Norte: 5710179.49 - Este: 707652.55

hasta Norte: 5710434.58- Este: 707773.07
Este documento presenta los datos considerados para la evaluación actual (situación
sin proyecto) y la situación futura (situación con proyecto) debido al empalme de una
tubería de aguas lluvias, producto de la implementación del pozo y ampliación del
portal, al colector secundario. Además, este informe presenta otros antecedentes
básicos como la topografía de todo el trazado a intervenir, además de los estudios
hidrológicos e hidráulicos correspondientes.

**1.1.** **Descripción del Proyecto**

Debido a la ampliación del Portal Temuco con una superficie de 0.55 ha, se considera
una red interna que evacúa las aguas lluvias de la ampliación y un pozo proyectado
dentro de esta superficie, el cual corresponde a un pozo de abatimiento de profundidad
50 m y un diámetro de 12’’, cuyo caudal de extracción es de 40 L/s. A su vez, como se
mencionó anteriormente, dentro del área de estudio existen 7 pozos de abatimiento,
cuyos caudales de extracción son los que se muestran en la siguiente tabla.

_Tabla 1.1 caudales_ _extraídos_ _en cada_ _pozo_

|Pozo|Caudal (L/s)|
|---|---|
|Pozo A|31.3|
|Pozo C|22.0|
|Pozo D|40.0|
|Pozo E|40.0|
|Pozo F|30.0|
|Pozo G|37.5|
|Pozo H|32.6|
|Pozo Proyectado|40.0|

_Fuente: Elaboración propia_

Por otro lado, el área actual posee una red interna que recolecta las aguas lluvias
generadas en este sector, por lo que, Las aguas de los 7 pozos actuales, en conjunto
con el agua lluvia generada en el área del portal, son trasladadas y descargadas a una
cámara existente perteneciente a un colector secundario (Figura 1.3). Adicional a lo
anterior, el pozo proyectado junto con las aguas lluvias nuevas generadas en la
ampliación, serán descargadas en una tubería de PVC de 315 mm de diámetro,
empalmándola a la misma cámara existente, en conjunto con el sistema actual que
existe en el Portal, como se muestra en la Figura 1.3

La materialidad del colector que traslada las aguas es de hormigón y sus dimensiones
son de 0.7 x 1.2 m.

**6**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**1.2.** **Descripción de las obras**

A partir de lo anterior, las obras consisten en el empalme de la descarga de aguas
provenientes de las aguas lluvias generadas en la ampliación del Portal Temuco y del
caudal adicional producto de la implementación de un nuevo pozo. Dicho empalme se
realiza en la cámara existente ubicada en la calle España.

1.2.1 Ubicación de las obras

**Empalme de tubería a cámara de inspección existente:**

**Norte:** 5710180.481 **ESTE:** 707651.543

Todas las coordenadas están en metros y referidas al sistema UTM Datum WGS 1984
Huso 18S

_Figura 1.4 Empalme tubería Portal Temuco proyectada a cámara existente de colector secundario_

_Fuente: Elaboración propia_

**1.3.** **Consideraciones Generales**

Para el desarrollo del proyecto, se analizarán dos situaciones:

 Sin Proyecto: Situación actual considerando el empalme a la red secundaria

existente, en el cual llega el caudal de extracción de los 7 pozos existentes, en

**7**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

conjunto con el caudal de aguas lluvias generado en el área actual del Portal
Temuco.

 Con Proyecto: Situación futura considerando el nuevo empalme a la red

secundaria existente, en el cual llega el caudal mencionado anteriormente,
además del caudal de aguas lluvias que se produce en la ampliación del Portal
Temuco y el caudal de extracción del pozo proyectado.

**2. TOPOGRAFÍA**

Se realizó una topografía detallada del trazado del colector levantando las cámaras
existentes a lo largo de 390 m de recorrido, obteniendo los valores de cota de radier
de entrada, cota de radier de salida y cota de anillo.

**8**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**3. HIDROLOGÍA.**

En este capítulo se describen los procedimientos necesarios a fin de determinar el
caudal asociado al área tributaria del Portal Temuco para el periodo de retorno de
5 años, 10 años y 100 años.

Se han adoptado las siguientes bases de cálculo en consideración de las
características topográficas e hidrológicas del sector y lo indicado en el Plan Maestro
de Aguas Lluvias de Temuco.

**3.1** **Antecedentes**

Para la elaboración del presente estudio se cuenta con los siguientes antecedentes:

 Plan Maestro de Evacuación y Drenaje de Aguas Lluvias de Temuco.

 Manual de Carreteras Volumen 3, Parte III. Dirección de Vialidad, Dirección

General de Obras Públicas, Ministerio de Obras Públicas, 2023.

 Manual de cálculo de Crecidas y caudales mínimos en cuencas sin Información

Fluviométrica.

**3.2** **Cálculo de Caudal**

Se estimó el caudal de aguas lluvias del Portal Temuco mediante el método Racional.

3.2.1 Caudales Mediante Método Racional

Para el cálculo del caudal asociado a distintos periodos de retorno de precipitación, y
en particular para periodo de 5 años, se hace uso de la formula racional, definida por
la siguiente expresión:

=
Q [T]

C× i tT c × A

3.6

Donde:

Q : Caudal en m [3] /s
C : Coeficiente de escorrentía de la cuenca
A : Área aportante en km [2]
i tT c : Intensidad de la lluvia de diseño, asociada a una duración igual al

tiempo de concentración de la cuenca ( t c ), y al periodo de retorno indicado ( T )
en mm/h.

Para el cálculo del caudal es necesario estimar las intensidades de lluvia según el
periodo de retorno, el tiempo de concentración de la cuenca y el coeficiente de

**9**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

escorrentía ponderado. Para ello se muestra la metodología utilizada para estimar
cada variable del método.

A continuación, se muestra la metodología.

**Área Tributaria**

El área tributaria corresponde al terreno donde se emplaza el Portal Temuco, ya que
de acuerdo a los antecedentes recopilados, el colector existente fue construido para
evacuar las aguas lluvias y las del agotamiento subterráneo pertenecientes al centro
comercial. La siguiente figura muestra el área tributaria.

_Figura 3.1 Área tributaria Portal Temuco_

_Fuente: Elaboración propia_

**10**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

De esta manera, el área tributaria correspondiente a la superficie actual del Portal es
0.041 km [2], equivalente a 4.1 ha. Además el área de ampliación es de 0.55 ha, por lo
que el área total del Portal Temuco corresponde a 4.64 ha.

**Intensidad de la lluvia**

Para estimar esta variable, el método realiza el supuesto que la intensidad de la lluvia
está asociada a una duración igual al tiempo de concentración de la cuenca. Es por
ello, para el caso del área de influencia de Portal Temuco, se estima el tiempo de
concentración (Tc) considerando el tiempo que demora la partícula más alejada en
entrar al colector utilizando la ecuación de Kerby y la de la Federal Aviation Agency
dada por la siguiente expresión.

 **Kerby**

(2 ∗L∗n) [0.467]
Tc=

(0.9144 ∗i [0.5] ) [0.467]

 **Federal Aviation Agency**

Tc= [3.26(1.1 −C)L] [0.5]

(100S) [0.33]

Donde:
Tc = Tiempo de concentración (min)
L = Longitud escurrimiento superficial (m)
n = Coeficiente de rugosidad según material, de acuerdo a la tabla 3.1
i = Pendiente Longitudinal (°/1)
C = Coeficiente de escorrentía
S = pendiente (%)

_Tabla_ _3.1 Coeficiente_ _de Rugosidad_ _según material_

|Material|Coeficiente|
|---|---|
|Cajones de Hormigón|0.015|
|Tuberías de Cemento Comprimido|0.013|
|Cañerias de PVC|0.011|
|Cañerias de HDPE|0.012|

_Fuente: Elaboración propia_

A partir de ello, el tiempo de concentración estimado para cada fórmula se muestra en
la siguiente tabla.

**11**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

_Tabla_ _3.2 Coeficiente_ _de Rugosidad_ _según material_

|Fórmula|Tiempo (min)|
|---|---|
|Kerby|13.00|
|Federak Aviation Agency|20.23|

_Fuente: Elaboración propia_

De esta manera, el tiempo de concentración adoptado es de 16.6 minutos.

Luego, en el Plan Maestro de aguas lluvias de Temuco se han determinado las
precipitaciones máximas y las curvas IDF en la estación Maquehue AD para períodos
de retorno de 2 a 100 años, las cuales fueron las utilizadas para estimar la intensidad.
Los valores se muestran en la siguiente tabla.

_Tabla 3.3 Curva Intensidad Duración Frecuencia Estación Maquehue AD, Temuco_

_Fuente: Plan Maestro de Aguas Lluvia de Temuco_

A partir de lo anterior, se estimó la intensidad asociado a un tiempo de concentración
de 16.6 minutos, mediante interpolación lineal, cuyos valores se muestran en la
siguiente tabla.

_Tabla 3.4 Intensidad_ _asociado_ _a_ _una_ _duración igual al tiempo_ _de_ _concentración de 10 minutos_

|T (Años)|PP (mm)|I (mm/h)|
|---|---|---|
|2|5.2|31.1|
|5|6.6|39.9|
|10|7.6|45.6|
|25|8.8|52.9|
|50|9.7|58.3|
|100|10.6|63.7|

_Fuente: Elaboración Propia_

**12**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**Coeficiente de escorrentía**

La determinación del coeficiente de escorrentía se hizo en base a lo expuesto en el
Plan Maestro de Aguas Lluvias de Temuco, en el cual definen distintos rangos de
coeficiente para cada uno de los tipos de uso de suelo definidos en el PM, asignando
un valor de coeficiente de escorrentía a las diferentes distribuciones de cobertura de

suelo al interior de cada tipo de ocupación. De esta forma se obtuvo un valor del
coeficiente de escorrentía para el área de estudio, asociado a un coeficiente
perteneciente a sector comercial y centro, cuyo valor de coeficiente para 10 años de
periodo de retorno es de Ce = 0.79.

Por lo tanto la siguiente tabla muestran los valores de coeficientes de escorrentías
adoptados para el loteo del Portal Temuco y para distintos periodos de retorno. Cabe
destacar que el coeficiente calculado corresponde para un periodo de retorno de
10 años, por lo que según el acápite 3.702.503 del Manual de Carreteras Volumen 3,
para periodos de retorno mayores se debe multiplicar por un factor de amplificación de
1.1, 1.2 y 1.25 para periodos de retorno de 25, 50 y 100 años respectivamente.

_Tabla_ _3.5_ _Coeficiente_ _de_ _escorrentía_

|T (años)|Coeficiente de escorrentía|
|---|---|
|2|0.79|
|5|0.79|
|10|0.79|
|25|0.869|
|50|0.948|
|100|0.9875|

_Fuente: Elaboración Propia_

De esta manera, los valores obtenidos para cada variable de interés son los que se
muestran en la siguiente tabla.

_Tabla_ _3.6 variables_ _a_ _utilizar método racional_

|T (años)|Coeficiente de escorrentía|Intensidad (mm/h)|Área km2|Área km2 (con<br>ampliación)|
|---|---|---|---|---|
|2|0.79|24.90|0.044|0.046|
|5|0.79|31.92|0.044|0.046|
|10|0.79|36.50|0.044|0.046|
|25|0.869|42.35|0.044|0.046|
|50|0.948|46.69|0.044|0.046|
|100|0.9875|50.97|0.044|0.046|

_Fuente: Elaboración Propia_

Finalmente, el caudal de aguas lluvias asociado al loteo del Portal Temuco se muestra
en la siguiente tabla.

**13**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

_Tabla 3.7 Caudales_ _estimado_ _a_ _partir del Método Racional_

|T (Años)|Q (L/s)|
|---|---|
|2|237.99|
|5|305.08|
|10|348.84|
|25|445.21|
|50|535.52|
|100|608.95|

_Fuente: Elaboración Propia_

Así, la siguiente tabla muestra el caudal total del lote en situación sin proyecto sumado
al caudal que extraen los pozos.

_Tabla_ _3.8_ _Caudal total área Portal Temuco_ _situación sin proyecto_

|T (Años)|Q (L/s)|Q Pozos (L/s)|Q Total (L/s)|
|---|---|---|---|
|2|237.99|233.4|471.39|
|5|305.08|233.4|538.48|
|10|348.84|233.4|582.24|
|25|445.21|233.4|678.61|
|50|535.52|233.4|768.92|
|100|608.95|233.4|842.35|

_Fuente: Elaboración Propia_

Para la situación con proyecto, es decir, considerando además el caudal de extracción
del pozo proyectado, el cual es de Q = 35 L/s y el caudal de aguas lluvia generada por
la ampliación del Portal, el caudal total del área del Portal es:

_Tabla_ _3.9_ _Caudal total área Portal Temuco_ _en situación Futura_

|T (Años)|Q Aguas<br>Lluvias (L/s)|Q Pozos (L/s)|Q Total (L/s)|
|---|---|---|---|
|2|253.62|273.4|527.02|
|5|325.11|273.4|598.51|
|10|371.74|273.4|645.14|
|25|474.45|273.4|747.85|
|50|570.68|273.4|844.08|
|100|648.94|273.4|922.34|

_Fuente: Elaboración Propia_

**14**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**3.3** **Periodo de Retorno**

Un evento de magnitud dada tiene un periodo de retorno de T años si es igualado o
superado una vez cada T años, su selección depende de la vida útil de la
infraestructura y el riesgo de falla aceptable, el que depende de factores económicos,
sociales, técnicos y otros.

Para el caso de este estudio, se analizan los distintos escenarios considerando un
periodo de retorno de T=5años, además se verifica que para un periodo de retorno de
T=10 años y T=100 años, no exista afloramiento por parte de las cámaras.

**15**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**4. ESTUDIO HIDRÁULICO**

**4.1** **Generalidades**

Se calcula el eje hidráulico para los escenarios sin proyecto y con proyecto,
considerando los caudales mostrados anteriormente, esto con la finalidad de
determinar la influencia de incorporar las obras ya mencionadas en el colector. Se
considera el análisis para periodos de retorno asociado a 5 años, 10 años y 100 años.
En este último se verifica que en las cámaras no exista afloramiento de agua.

**4.2** **Modelación hidráulica con EPA SWMM 5.1**

Se modeló hidráulicamente el funcionamiento del colector del Portal Temuco tanto
para la situación actual y la situación proyectada del pozo a implementar y de la
ampliación del Portal.

Para verificar el comportamiento hidráulico del colector del Portal Temuco, se ejecuta
una modelación hidráulica del sistema en el software EPA SWMM 5.1, el cual permite
analizar el comportamiento hidráulico de redes de aguas por medio de un estudio
nodal. Este modelo permite determinar las alturas de eje hidráulico observadas a lo
largo de la red, considerando condiciones de borde distintas y las pérdidas de energía
observadas a lo largo del trazado.

El modelo SWMM es ejecutado utilizando el método de cálculo de onda dinámica, el
cuál resuelve las ecuaciones de flujo unidimensionales completas de Saint Venant y,
por lo tanto, produce los resultados teóricamente más precisos. Estas ecuaciones
consisten en las ecuaciones de continuidad y momento para conductos y una ecuación
de continuidad de volumen en los nodos. Este método considera el almacenamiento
en conductos, remansos, pérdidas de entrada/salida, contraflujo y el flujo a presión, y
por lo tanto, se puede aplicar a cualquier diseño de red general, incluso aquellos que
contienen múltiples desvíos.

De los resultados de las modelaciones hidráulicas se obtuvieron las alturas de aguas
en el colector y sus cámaras, y se compararon en los distintos escenarios para analizar
que no ocurran problemas de afloramiento.

Para efectos de la modelación se consideró que el ingreso de la escorrentía a los
colectores se produce en el primer nodo con el valor del caudal mostrado en el capítulo
3.2.1 asociado a caudal área Portal Temuco.

**16**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**Definición de Parámetros**

Se definieron los siguientes parámetros en el modelo asociados a los elementos
necesarios que simulan los colectores:

**Nodos**

Cámaras de Inspección de Colector existente

 - Cota de Radier de salida

 - Altura Cámara

**Links**

Colector existente

 Largo
 - Sección del colector

 Diámetro o profundidad del colector

 Rugosidad

 Coeficientes de pérdida singular

 Offset en la salida (CRe de C.I.)

**Outfall (Descarga)**

 Condición de descarga (Normal, ahogada, etc.)

 Condición de borde en la descarga (Normal)

En el nodo de inicial se ingresó el caudal asociado al área del Portal Temuco,
dependiendo del escenario que se está modelando.

A continuación se muestra la planta del colector existente. Cabe destacar que se
analizó hasta 390 m aguas abajo del inicio del colector.

**17**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

_Figura 4.1 Esquema planta Colector Portal Temuco en EPA SWMM_

_Fuente: Elaboración Propia_

**18**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**5. RESULTADOS Y ANEXOS DEL ESTUDIO**

A continuación, las siguientes tablas muestran el resumen de los resultados obtenidos
de las verificaciones hidráulicas en el modelo para consideraciones mencionados en
el capítulo 1, considerando una precipitación con periodo de retorno de 5, 10 y 100
años:

 **Situación Sin Proyecto:**

Verificación Hidráulica T = 5, Q = 538.48 (L/s)

_Tabla_ _5.1 Verificación Hidráulica T = 5_ _Sin proyecto_

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 1-CI 2|582.24|1.64|0.47|0.66|
|CI 2-CI 3|582.24|1.13|0.48|0.71|
|CI 3-CI 4|582.24|1.22|0.54|0.73|
|CI 4-CI 5|582.24|1.03|0.51|0.86|
|CI 5-CI 6|582.24|1.15|0.89|0.65|
|CI 6-CI 7|582.24|1.07|0.48|0.65|
|CI 7-CI 8|582.24|1.12|0.43|0.57|

_Fuente: Elaboración Propia_

Verificación Hidráulica T = 10, Q = 582.24 (L/s)

_Tabla_ _5.2 Verificación Hidráulica T = 10_ _Sin proyecto_

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 1-CI 2|582.24|1.67|0.51|0.72|
|CI 2-CI 3|582.24|1.15|0.52|0.76|
|CI 3-CI 4|582.24|1.25|0.57|0.78|
|CI 4-CI 5|582.24|1.05|0.54|0.89|
|CI 5-CI 6|582.24|1.17|0.93|0.7|
|CI 6-CI 7|582.24|1.09|0.51|0.69|
|CI 7-CI 8|582.24|1.14|0.46|0.61|

_Fuente: Elaboración Propia_

Verificación Hidráulica T = 100, Q = 842.35 (L/s)

_Tabla_ _5.3 Verificación Hidráulica T = 100_ _Sin proyecto_

**19**

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 1-CI 2|842.35|1.83|0.83|1|
|CI 2-CI 3|842.35|1.28|0.83|1|
|CI 3-CI 4|842.35|1.41|0.82|1|
|CI 4-CI 5|842.35|1.31|0.77|1|

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 5-CI 6|842.35|1.3|1.1|0.94|
|CI 6-CI 7|842.35|1.21|0.67|0.91|
|CI 7-CI 8|842.35|1.26|0.61|0.8|

_Fuente: Elaboración Propia_

 **Situación Con Proyecto:**

Verificación Hidráulica T = 5, Q = 598.51 (L/s)

_Tabla_ _5.4 Verificación Hidráulica T = 5_ _Con proyecto_

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 1-CI 2|598.51|1.68|0.52|0.73|
|CI 2-CI 3|598.51|1.16|0.53|0.78|
|CI 3-CI 4|598.51|1.26|0.59|0.8|
|CI 4-CI 5|598.51|1.07|0.56|0.9|
|CI 5-CI 6|598.51|1.18|0.94|0.71|
|CI 6-CI 7|598.51|1.1|0.52|0.7|
|CI 7-CI 8|598.51|1.15|0.47|0.62|

_Fuente: Elaboración Propia_

Verificación Hidráulica T = 10, Q = 645.14 (L/s)

_Tabla_ _5.5 Verificación Hidráulica T = 10_ _Con proyecto_

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 1-CI 2|645.14|1.71|0.56|0.79|
|CI 2-CI 3|645.14|1.19|0.57|0.84|
|CI 3-CI 4|645.14|1.3|0.63|0.86|
|CI 4-CI 5|645.14|1.13|0.6|0.93|
|CI 5-CI 6|645.14|1.21|0.97|0.76|
|CI 6-CI 7|645.14|1.12|0.55|0.74|
|CI 7-CI 8|645.14|1.17|0.5|0.65|

_Fuente: Elaboración Propia_

Verificación Hidráulica T = 100, Q = 922.34 (L/s)

_Tabla_ _5.6 Verificación Hidráulica T = 100_ _Con proyecto_

**20**

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 1-CI 2|922.34|1.88|1.04|1|
|CI 2-CI 3|922.34|1.32|1.03|1|
|CI 3-CI 4|922.34|1.45|0.98|1|
|CI 4-CI 5|922.34|1.37|0.91|1|

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

|Link|Q máx (L/s)|V (m/s)|Altura Agua (m)|Capacidad|
|---|---|---|---|---|
|CI 5-CI 6|922.34|1.33|1.22|1|
|CI 6-CI 7|922.34|1.28|0.72|0.96|
|CI 7-CI 8|922.34|1.29|0.65|0.85|

_Fuente: Elaboración Propia_

De los análisis hidráulicos realizados se destaca:

En la condición actual, para un periodo de retorno de T = 5 y T = 10 años, el colector
presenta un buen funcionamiento, teniendo capacidades menores al 80 %,
exceptuando entre la cámara 4 y cámara 5, debido a que este tramo funciona como
sifón y no se intervendrá en este proyecto. Además, se verifica que para un periodo de
retorno de 100 años no existe afloramiento de las cámaras.

Por otro lado, considerando las situaciones futuras, es decir, la adición de un nuevo
pozo de agotamiento y el área tributaria adicional de la ampliación del Portal, se tiene
que para un periodo de retorno de 5 años, el colector no presenta problemas de
funcionamiento en su trazado, presentando capacidades bajo 80 %. Para un T = 10
años, el colector presenta un buen funcionamiento, teniendo capacidades menores a
86 %, sin trabajar de manera exigida, exceptuando el tramo entre la cámara 4 y 5 ya
que funciona como sifón. Además, Para un T = 100 años, tampoco se presenta
afloramiento de las cámaras, tal como se muestra en Anexos.

En Anexos se muestran los resultados, los cuales se dividen en:

i) **Anexo N°1: “Modelación Hidráulica en EPA SWMM”.**
a. Esquema en planta
b. Datos de entrada de nodos

c. Datos de entrada de conductos

ii) **Anexo N°2: “Verificación Hidráulica Colector Situación Sin Proyecto**
**considerando un periodo de retorno de 5, 10 y 100 años”.**
a. T=5 años

b. T=10 años

c. T=100 años

iii) **Anexo N°3: “Verificación Hidráulica Colector Situación Con Proyecto**
**considerando un periodo de retorno de 5, 10 y 100 años”.**
a. T=5 años

b. T=10 años

c. T=100 años

**21**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

iv) **Anexo No4: “Perfil Longitudinal Colector para T = 5 años, T = 10 años y**
**T = 100 años”**

 **Sin Proyecto**

a. T=5 años

b. T=10 años

c. T=100 años

 **Con Proyecto**

a. T=5 años

b. T=10 años

c. T=100 años

**22**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**6. CONCLUSIONES**

El presente informe presenta la verificación hidráulica del colector secundario ubicado
en calle España, que recibe las aguas lluvias y de agotamiento de napa provenientes
del Portal Temuco. El colector secundario en situación actual (sin proyecto) recibe las
aguas lluvias del Portal Temuco y además recibe el caudal de agotamiento del nivel
freático generado por 7 pozos existentes dentro del centro comercial. A su vez, para
la condición proyectada, se considera la adición de las aguas lluvias generadas en el
área de ampliación del centro comercial y el agua proveniente del agotamiento del
nivel freático generado por 1 pozo adicional a los 7 existentes.

El proyecto consiste en la descarga de aguas provenientes de las aguas lluvias
generadas en la ampliación del Portal Temuco y del caudal adicional producto de la
implementación de un nuevo pozo. Dicho empalme se realiza en la cámara existente
ubicada en la calle España.

En conformidad a los antecedentes expuestos y a la topografía realizada, se desarrolló
un modelo hidráulico del colector Portal Temuco.

De acuerdo con los resultados obtenidos en el modelo hidráulico en el software
EPA SWMM, considerando el proyecto de empalme y por ende el caudal adicional,
para un periodo de retorno de 5 años, se observa que el colector presenta un
funcionamiento con capacidades bajo el 80 %, exceptuando el tramo en donde el
colector actúa como sifón, que por su naturaleza, trabaja a presión, manteniendo el
funcionamiento actual del colector.

Por otro lado, se verificó que para un periodo de retorno de 100 años, no exista un
afloramiento de las cámaras a lo largo del colector, lo cual se cumple, tal como se
muestra en las tablas y perfiles longitudinales presentados en el capítulo de Anexos.

**ALEJANDRO PIZARRO UBILLA**

**Ingeniero Civil**

Concepción, Agosto de 2024.

**23**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**7. ANEXOS**

**ANEXO No1: “MODELACIÓN HIDRÁULICA EN EPA SWMM”.**

a. Esquema en Planta

_Figura 7.1 Esquema en Planta modelo HEC RAS Canal Gabriela Mistral_

_Fuente: Elaboración propia_

**24**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

b. Datos de entrada nodos

_Tabla 7.1 Datos_ _de_ _entrada nodos_ _colector_

|Nodos Colector|Col2|Col3|Col4|
|---|---|---|---|
||**C.R (msnm)**|**C.A (msnm)**|**Altura cámara (m)**|
|CI-1|97.75|99.20|1.45|
|CI-2|97.66|99.11|1.45|
|CI-3|97.48|98.95|1.47|
|CI-4|97.43|98.82|1.39|
|CI-5|97.01|98.84|1.83|
|CI-6|97.26|99.05|1.79|
|CI-7|97.12|99.40|2.28|
|CI-8|96.891<br>|99.00<br>|2.109<br>|

_Fuente: Elaboración propia_

c. Datos de entrada conductos

_Tabla 7.2 Datos_ _de_ _entrada_ _conductos_ _colector_

|Conductos colector|Col2|
|---|---|
|**Entre CI**|**Largo (m)**|
|CI-1 - CI-2|6.556|
|CI-2 - CI-3|75.48|
|CI-3 - CI-4|14.51|
|CI-4 - CI-5|13.58|
|CI-5 - CI-6|84.98|
|CI-6 - CI-7|83.47|
|CI-7 - CI-8<br>|110.47<br>|

_Fuente: Elaboración propia_

**25**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl Concepción](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

**ANEXO No2: “VERIFICACIÓN HIDRÁULICA COLECTOR SITUACIÓN SIN PROYECTO CONSIDERANDO UN**

**PERIODO DE RETORNO DE 5, 10 Y 100 AÑOS”.**

a. T = 5 años

_Tabla 7.3 Verificación Hidráulica_ _Colector T = 5_ _años_ _Situación Sin Proyecto._

|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Dimensión|Pendiente|Material|Caudal<br>máx|H/D|Velocidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|
|Denominación|Desde<br>Hasta|(Ha)|(Ha)|(minutos)|(mm/hr)|(m)|(m)<br>(m)|(%)|(%)|(L/s)|(L/s)|(m/s)|
|Colector<br>Portal<br>Temuco|1 <br>2 <br>2 <br>3 <br>3 <br>4 <br>4 <br>5 <br>5 <br>6 <br>6 <br>7 <br>7 <br>8|4.36<br>4.36<br>4.36<br>4.36<br>4.36<br>4.36<br>4.36|0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79|16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6|36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5|6.556<br>75.48<br>14.51<br>13.58<br>84.98<br>83.47<br>110.47|1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7|1.07<br>0.21<br>0.21<br>3.09<br>0.22<br>0.16<br>0.21|Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón|538.48<br>538.48<br>538.48<br>538.48<br>538.48<br>538.48<br>538.48|0.66<br>0.71<br>0.73<br>0.86<br>0.65<br>0.65<br>0.57|1.64<br>1.13<br>1.22<br>1.03<br>1.15<br>1.07<br>1.12|

|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Dimensión|Pendiente|Material|Caudal<br>máx|H/D|Velocidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|<br>Intensidad<br>de<br>precipitación|Longitud|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|
|Denominación|Desde<br>Hasta|(Ha)|(Ha)|(minutos)|(mm/hr)|(m)|(m)<br> (m)|(%)|(%)|(L/s)|(L/s)|(m/s)|
|Colector<br>Portal<br>Temuco|1 <br>2 <br>2 <br>3 <br>3 <br>4 <br>4 <br>5 <br>5 <br>6 <br>6 <br>7 <br>7 <br>8|4.36<br>4.36<br>4.36<br>4.36<br>4.36<br>4.36<br>4.36|0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79|16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>|36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>|6.556<br>75.48<br>14.51<br>13.58<br>84.98<br>83.47<br>110.47<br>|1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7|1.07<br>0.21<br>0.21<br>3.09<br>0.22<br>0.16<br>0.21|Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón|582.24<br>582.24<br>582.24<br>582.24<br>582.24<br>582.24<br>582.24|0.72<br>0.76<br>0.78<br>0.89<br>0.7<br>0.69<br>0.61|1.67<br>1.15<br>1.25<br>1.05<br>1.17<br>1.09<br>1.14|

_Fuente: Elaboración propia_

_Fuente: Elaboración propia_

b. T = 10 años

_Tabla 7.4 Verificación Hidráulica_ _Colector T = 10_ _años_ _Situación Sin Proyecto._

**26**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl Concepción](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

c. T = 100 años

_Tabla 7.5 Verificación Hidráulica_ _Colector T = 100_ _años_ _Situación Sin Proyecto._

|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Dimensión|Pendiente|Material|Caudal<br>máx|H/D|Velocidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|
|Denominación|Desde<br>Hasta|(Ha)|(Ha)|(minutos)|(mm/hr)|(m)|(m)<br>(m)|(%)|(%)|(L/s)|(L/s)|(m/s)|
|Colector<br>Portal<br>Temuco|1 <br>2 <br>2 <br>3 <br>3 <br>4 <br>4 <br>5 <br>5 <br>6 <br>6 <br>7 <br>7 <br>8|4.36<br>4.36<br>4.36<br>4.36<br>4.36<br>4.36<br>4.36|0.98<br>0.98<br>0.98<br>0.98<br>0.98<br>0.98<br>0.98|16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>|36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>|6.556<br>75.48<br>14.51<br>13.58<br>84.98<br>83.47<br>110.47<br>|1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7|1.07<br>0.21<br>0.21<br>3.09<br>0.22<br>0.16<br>0.21|Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón|842.35<br>842.35<br>842.35<br>842.35<br>842.35<br>842.35<br>842.35|1 <br>1 <br>1 <br>1 <br>0.94<br>0.91<br>0.8|1.83<br>1.28<br>1.41<br>1.31<br>1.3<br>1.21<br>1.26|

_Fuente: Elaboración propia_

**27**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl Concepción](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

**ANEXO No3: “VERIFICACIÓN HIDRÁULICA COLECTOR SITUACIÓN CON PROYECTO CONSIDERANDO UN**

**PERIODO DE RETORNO DE 5, 10 Y 100 AÑOS”.**

a. T = 5 años

_Tabla 7.6 Verificación Hidráulica_ _Colector T = 5_ _años_ _Situación Con Proyecto._

|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Dimensión|Pendiente|Material|Caudal<br>máx|H/D|Velocidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|<br>Intensidad<br>de<br>precipitación|Longitud|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|
|Denominación|Desde<br>Hasta|(Ha)|(Ha)|(minutos)|(mm/hr)|(m)|(m)<br> (m)|(%)|(%)|(L/s)|(L/s)|(m/s)|
|Colector<br>Portal<br>Temuco|1 <br>2 <br>2 <br>3 <br>3 <br>4 <br>4 <br>5 <br>5 <br>6 <br>6 <br>7 <br>7 <br>8|4.64<br>4.64<br>4.64<br>4.64<br>4.64<br>4.64<br>4.64|0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79|16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>|36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>|6.556<br>75.48<br>14.51<br>13.58<br>84.98<br>83.47<br>110.47<br>|1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7|1.07<br>0.21<br>0.21<br>3.09<br>0.22<br>0.16<br>0.21|Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón|598.51<br>598.51<br>598.51<br>598.51<br>598.51<br>598.51<br>598.51|0.73<br>0.78<br>0.8<br>0.9<br>0.71<br>0.7<br>0.62|1.68<br>1.16<br>1.26<br>1.07<br>1.18<br>1.1<br>1.15|

|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Dimensión|Pendiente|Material|Caudal<br>máx|H/D|Velocidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|<br>Intensidad<br>de<br>precipitación|Longitud|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|
|Denominación|Desde<br>Hasta|(Ha)|(Ha)|(minutos)|(mm/hr)|(m)|(m)<br> (m)|(%)|(%)|(L/s)|(L/s)|(m/s)|
|Colector<br>Portal<br>Temuco|1 <br>2 <br>2 <br>3 <br>3 <br>4 <br>4 <br>5 <br>5 <br>6 <br>6 <br>7 <br>7 <br>8|4.64<br>4.64<br>4.64<br>4.64<br>4.64<br>4.64<br>4.64|0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79<br>0.79|16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>|36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>|6.556<br>75.48<br>14.51<br>13.58<br>84.98<br>83.47<br>110.47<br>|1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7|1.07<br>0.21<br>0.21<br>3.09<br>0.22<br>0.16<br>0.21|Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón|645.14<br>645.14<br>645.14<br>645.14<br>645.14<br>645.14<br>645.14|0.79<br>0.84<br>0.86<br>0.93<br>0.76<br>0.74<br>0.65|1.71<br>1.19<br>1.3<br>1.13<br>1.21<br>1.12<br>1.17|

_Fuente: Elaboración propia_

_Fuente: Elaboración propia_

b. T = 10 años

_Tabla 7.7 Verificación Hidráulica_ _Colector T = 10_ _años_ _Situación Con Proyecto._

**28**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl Concepción](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

c. T = 100 años

_Tabla 7.8 Verificación Hidráulica_ _Colector T = 100_ _años_ _Situación Con Proyecto._

|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|Intensidad<br>de<br>precipitación|Longitud|Dimensión|Pendiente|Material|Caudal<br>máx|H/D|Velocidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Denominación|Cámara de<br>Inspección|Área<br>Aportante|Coeficiente<br>de<br>escorrentía|Tiempo de<br>Concentración|<br>Intensidad<br>de<br>precipitación|Longitud|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|Base<br>Altura|
|Denominación|Desde<br>Hasta|(Ha)|(Ha)|(minutos)|(mm/hr)|(m)|(m)<br> (m)|(%)|(%)|(L/s)|(L/s)|(m/s)|
|Colector<br>Portal<br>Temuco|1 <br>2 <br>2 <br>3 <br>3 <br>4 <br>4 <br>5 <br>5 <br>6 <br>6 <br>7 <br>7 <br>8|4.64<br>4.64<br>4.64<br>4.64<br>4.64<br>4.64<br>4.64|0.98<br>0.98<br>0.98<br>0.98<br>0.98<br>0.98<br>0.98|16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>16.6<br>|36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>36.5<br>|6.556<br>75.48<br>14.51<br>13.58<br>84.98<br>83.47<br>110.47<br>|1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7<br>1.2<br>0.7|1.07<br>0.21<br>0.21<br>3.09<br>0.22<br>0.16<br>0.21|Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón<br>Hormigón|922.34<br>922.34<br>922.34<br>922.34<br>922.34<br>922.34<br>922.34|1 <br>1 <br>1 <br>1 <br>1 <br>0.96<br>0.85|1.88<br>1.32<br>1.45<br>1.37<br>1.33<br>1.28<br>1.29|

_Fuente: Elaboración propia_

**29**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

**ANEXO No4: “PERFIL LONGITUDINAL COLECTOR PARA T = 5 AÑOS,**

**T = 10 AÑOS Y T = 100 AÑOS”.**

A continuación se presentan los perfiles longitudinales obtenidos de la modelación
hidráulica del colector Portal Temuco para los distintos escenarios mediante el
software EPA SWMM. La siguiente tabla muestra el caudal utilizado en cada uno de
ellos

_Tabla 7.9_ _Caudales_ _utilizados_ _en cada_ _escenario_

|Escenario|Caudal T=5<br>(m3/s)|Caudal T=10<br>(m3/s)|Caudal T=100<br>(m3/s)|
|---|---|---|---|
|Sin proyecto|538.48|582.24|842.35|
|Con proyecto|598.51|645.14|922.34|

_Fuente: Elaboración propia_

 **Sin Proyecto:**

a. T = 5 años

_Figura 7.2 Eje Hidráulico colector T=5 años situación Sin Proyecto_

_Fuente: Elaboración propia_

**30**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

b. T = 10 años

_Figura 7.3 Eje Hidráulico colector T=10 años situación Sin Proyecto_

_Fuente: Elaboración propia_

c. T = 100 años

_Figura 7.4 Eje Hidráulico colector T=100 años situación Sin Proyecto_

_Fuente: Elaboración propia_

**31**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

 **Con Proyecto**

a. T = 5 años

_Figura 7.5 Eje Hidráulico colector T=5 años situación Con Proyecto_

_Fuente: Elaboración propia_

b. T = 10 años

_Figura 7.6 Eje Hidráulico colector T=10 años situación Con Proyecto_

_Fuente: Elaboración propia_

**32**

Proyecto de Empalme a Red Secundaria Comuna de Temuco

**A. PIZARRO & ASOCIADOS**

**INGENIEROS CIVILES**

[Cochrane #635, Torre A, Of. 802 Edificio Alto Plaza. Fono:(41)2698362 - 2698384 Email: alejandro.pizarro@apaingenieria.cl](mailto:alejandro.pizarro@apaingenieria.cl%20Concepción)

Concepción

c. T = 100 años

_Figura 7.7 Eje Hidráulico colector T=100 años situación Con Proyecto_

_Fuente: Elaboración propia_

**33**

Proyecto de Empalme a Red Secundaria Comuna de Temuco