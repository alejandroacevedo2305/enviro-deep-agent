---
title: MEMORIA DE CÁLCULO DRENAJES
author: Expedito Sanchez Mederos
date: D:20230906112031+01'00'
language: es
type: report
pages: 13
has_toc: False
has_tables: True
extraction_quality: high
keywords: [1136]
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - AMPLIACIÓN S/E DON GOYO
-->

# AMPLIACIÓN S/E DON GOYO

**CLIENTE** **:** Sonnedix Don Goyo Transmisión S.A.

**ÁREA** **:** AMPLIACIÓN S/E DON GOYO

**TÍTULO** **:** MEMORIA DE CÁLCULO DRENAJES

**ELABORADO POR** **:** Quadrante Engenharia e Consultoria

**CONTROLADO POR :** Ferrovial Construcción Chile S.A.

**N.U.P. (CEN)** **:** 3284

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|0|06-09-2023|Válido para construcción|JPC|RAU|AMT|
|B|11-08-2023|Emitido para revisión y comentarios|JPC|RAU|AMT|
|A|03-07-2023|Emitido para revisión interna|JPC|RAU|AMT|
|**REV.**|**FECHA**|**MOTIVO DE LA EMISIÓN**|**PREPARÓ**|**REVISÓ**|**APROBÓ**|

|CÓDIGO DOC.|:|GB607-110-CV-DR-CR-01|REVISIÓN<br>:<br>ACTUAL|0|
|---|---|---|---|---|
|**CÓDIGO EXTERNO**|**: **|DGY-SE-CI-GE-01|DGY-SE-CI-GE-01|DGY-SE-CI-GE-01|

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**ÍNDICE**

**CONTENIDO**

**AMPLIACIÓN S/E DON GOYO ................................................................................................................................ 0**

**1. INTRODUCCIÓN ................................................................................................................................................. 2**

**2. OBJETIVO .......................................................................................................................................................... 2**

**3. ALCANCE ........................................................................................................................................................... 2**

**4. METODOLOGÍA ................................................................................................................................................. 2**

**5. NORMAS Y REFERENCIAS .................................................................................................................................. 3**

**5.1. Planos ........................................................................................................................................................ 3**

**5.2. Normas ...................................................................................................................................................... 3**

**6. DEFINICIÓN DEL TRAZADO DEL SISTEMA DE RECOLECCIÓN DE AGUAS LLUVIAS ................................................ 3**

**7. DEFINICIÓN ÁREAS DE DRENAJE ........................................................................................................................ 5**

**8. CALCULO DE CAUDALES ..................................................................................................................................... 6**

**8.1. Aplicación de fórmula racional ................................................................................................................... 6**

**8.2. Coeficiente de escurrimiento ..................................................................................................................... 6**

**8.3. Intensidad de diseño de las precipitaciones ............................................................................................... 7**

**9. VERIFICACIÓN HIDRÁULICA DEL SISTEMA DE DRENAJE ..................................................................................... 9**

**9.1. Colectores Horizontales.............................................................................................................................. 9**

**9.2. Extensión del canal existente ....................................................................................................................10**

**9.3. Descarga hacia quebrada ..........................................................................................................................11**

**ÍNDICE DE FIGURAS**

Figura 6-1 Planta general Don Goyo, en verde se muestra la ampliación. ................................................................... 3
Figura 6-2 Planta general sistema de Drenaje. ............................................................................................................. 4
Figura 6-3 Esquema de sistema de drenaje propuesto Ampliación SE. ........................................................................ 4
Figura 7-1 Áreas de drenaje ampliación SE. .................................................................................................................. 5
Figura 8-1 Precipitaciones máximas La Paloma ............................................................................................................ 8
Figura 9-1 Perfil transversal extensión canal proyectado. .......................................................................................... 10
Figura 9-2 Sistema de descarga propuesto. ................................................................................................................ 11

**ÍNDICE DE TABLAS**

Tabla 7.1 - Áreas de drenaje. ........................................................................................................................................ 5

Tabla 8.1 - Coeficientes de escurrimiento recomendados en Manual de Carreteras. .................................................. 6

Tabla 8.2 - Coeficientes de escorrentía adoptados en cada área de drenaje. .............................................................. 7
Tabla 8.3 - Estaciones pluviográficas de Chile en la zona de estudio ............................................................................ 7
Tabla 8.4 - Caudales generados por las áreas tributarias al sistema de recolección de ALL. ........................................ 8

Tabla 9.1 - Resultados dimensionamiento canal......................................................................................................... 11

Tabla 9.2 - Tabla extraída desde el Vol. 3 Manual de Carreteras. ............................................................................... 12

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 1 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**1.** **INTRODUCCIÓN**

Ferrovial Construcción Chile S.A., en adelante “Ferrovial Construcción” o "el Contratista" indistintamente,
ha sido seleccionado como adjudicatario del grupo de obras N°2, del Decreto Exento 171-2020, del
Ministerio de Energía, quedando oficializada la adjudicación a través del Decreto Supremo 11T de 2021.
De acuerdo con lo anterior, Ferrovial Construcción, ejecuta las labores inherentes al proyecto N.U.P. 3284
bajo un contrato en modalidad EPC suscrito con Sonnedix Don Goyo Transmisión S.A., en adelante “el

Mandante”.

El proyecto, ubicado en la región de Coquimbo, Provincia Limarí, comuna de Ovalle, consiste en el
seccionamiento de la línea 2x220 kV Nueva Pan de Azúcar - Punta Sierra, que, por medio de 2 tramos de
línea paralelos, doble circuito, con una longitud aproximada de 2,5 km cada uno y una potencia de 580
MVA, se conectará a ambas secciones de barra de la subestación Don Goyo mediante la construcción de
cuatro nuevas posiciones de entrada de línea. Adicionalmente, considera la eliminación del
seccionamiento de la línea 2x220 kV Pan de Azúcar - La Cebada mediante la construcción de un bypass en
las inmediaciones de la subestación Don Goyo y el retiro de conductores, equipos y estructuras al interior

de la subestación.

El presente documento presenta la memoria de cálculo del sistema de drenaje de aguas lluvia para el
proyecto de “Ampliación en S/E Don Goyo”, ubicada en la Región de Coquimbo.

**2.** **OBJETIVO**

Dimensionar y verificar el sistema de drenaje de aguas lluvias del proyecto “Ampliación en S/E Don Goyo”.

- Definir parámetros de diseño.

- Determinar áreas aportantes.

- Definir caudales de recolección.

- Verificar diámetros y pendientes de los colectores de ALL.

**3.** **ALCANCE**

El alcance de la memoria es el diseño y verificación del sistema de drenaje e infiltración de la “Ampliación
en S/E Don Goyo”. Lo anterior, de acuerdo con las consideraciones de diseño hidráulico definidas en las
normas vigentes.

**4.** **METODOLOGÍA**

Para el análisis del drenaje hidráulico, se seguirá la siguiente metodología de trabajo:

a) Análisis de las pendientes del terreno y definición del trazado: La primera etapa consiste en

determinar la dirección del escurrimiento en la zona de proyecto. A partir de este análisis, se

propone el trazado que seguirá el drenaje de las ALL.

b) La segunda etapa es determinar las áreas tributarias a los canales y colectores proyectados.

c) Luego, se determina el caudal aportante de cada área tributarías a los tramos de colector

proyectados. En esta etapa es necesario definir la intensidad de precipitación para la zona de

proyecto, además de definir el periodo de retorno de diseño.

d) Posteriormente realizará la verificación hidráulica del sistema de recolección proyectado y

actual.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 2 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**5.** **NORMAS Y REFERENCIAS**

**5.1.** **Planos**

[1]. GB607-110-CV-DR-DW-01-001 - Sistema de Drenaje interior - Planta y detalles.

[2]. GB607-110-CV-DR-DW-02-001 - Plataforma Planta Geometría y Cortes.

**5.2.** **Normas**

Se aplicarán las siguientes normas:

[3]. Manual de Carreteras, Volumen 3. Instrucciones y Criterios de Diseño.

[4]. ETG A.0.02-2013: Condiciones generales para el diseño de obras civiles de Subestaciones.

**6.** **DEFINICIÓN DEL TRAZADO DEL SISTEMA DE RECOLECCIÓN DE AGUAS LLUVIAS**

Se debe generar el drenaje de la ampliación de la sub-estación. En la siguiente figura, se aprecia el plano
en planta de la sub estación. En color verde se aprecia la ampliación a la cual se debe diseñar el sistema
de drenaje de aguas lluvias.

_Figura 6-1 Planta general Don Goyo, en verde se muestra la ampliación._

Actualmente, la subestación presenta dos sistemas de drenaje.

 - El sistema interno que consiste en la conducción e infiltración de aguas lluvias a través de drenes.

 - El sistema externo, está encargado de interceptar las aguas provenientes desde el exterior a
través de un canal que descarga hacia una quebrada existente.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 3 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

El sistema proyectado consiste en un sistema de colectores que captan el agua desde los puntos bajos del
camino interior a través de sumideros. Posteriormente, el agua captada se dirige hacia la canaleta
existente, la que presentará una extensión hacia la ampliación. En la siguiente figura, se muestra el
sistema de recolección propuesto.

_Figura 6-2 Planta general sistema de Drenaje._

_Figura 6-3 Esquema de sistema de drenaje propuesto Ampliación SE._

A continuación, se determinará el área de drenaje para generar el cálculo del caudal de escorrentía.

Posteriormente se realizará el dimensionamiento hidráulico de las obras.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 4 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**7.** **DEFINICIÓN ÁREAS DE DRENAJE**

Debido a que la situación proyectada se unirá al canal existente, se debe determinar el área que
actualmente drena al canal. Esta corresponde a 7419 m [2] y está ubicada al norte de la sub estación, en su

extremo oriente.

El sistema interno de drenaje proyectad para la ampliación, considera el área de drenaje que se muestra
en la siguiente figura:

_Figura 7-1 Áreas de drenaje ampliación SE._

Así, el área total de drenaje que debe considerar el sistema propuesto es de 13066 m [2] .

_Tabla 7.1 - Áreas de drenaje._

|ÁREA|Total|Área camino|Área libre|
|---|---|---|---|
|Área canal Existente|7419|0|7419|
|A1|444|145|299|
|A2|1070|227|843|
|A3|1099|179|920|
|A4|439|325|114|
|A5|492|323|169|
|A6|838|144|694|
|A7|863|147|716|
|A8|402|152|250|
|Total (m2)|13066|1642|11424|

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 5 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**8.** **CALCULO DE CAUDALES**

**8.1.** **Aplicación de fórmula racional**

El cálculo de caudales es realizado de acuerdo con las secciones 3.702.5, 3.702.6, 3.702.7, y 3.702.8 del

Manual de Carreteras del MOP.

Los caudales se dimensionan en función del tamaño de las áreas aportantes respectivas. Se utiliza el

Método Racional para determinar los caudales, con la ecuación 3.702.5.1 del Manual de Carreteras y las

unidades indicadas en este:

Q= [CAI]

3,6

Donde:

 - Q = Caudal (m3/s)

 - C = Coeficiente de escorrentía (adimensional)

 - A = Superficie de la cuenca aportante, (km [2] )

 - I = Intensidad máxima, correspondiente a una lluvia de duración igual al tiempo de

concentración del sector analizado (mm/hr).

**8.2.** **Coeficiente de escurrimiento**

Para definir el coeficiente de rugosidad de las áreas tributarias, se utilizarán las recomendaciones del

Manual de Carreteras.

_Tabla 8.1 - Coeficientes de escurrimiento recomendados en Manual de Carreteras._

De acuerdo al informe de Mecánica de Suelos, la plataforma de la Subestación se compone de una grava
arenosa con presencia de bolones y limos, además de una pendiente del 1%.

Considerando los antecedentes antes descritos y la Tabla anterior, a continuación, se presenta el detalle
de los coeficientes de escorrentía adoptados en cada área de drenaje.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 6 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

_Tabla 8.2 - Coeficientes de escorrentía adoptados en cada área de drenaje._

|Áreas|C|
|---|---|
|Área Canal Existente|0,35|
|A1|0,54|
|A2|0,44|
|A3|0,44|
|A4|0,63|
|A5|0,78|
|A6|0,33|
|A7|0,35|
|A8|0,44|

**8.3.** **Intensidad de diseño de las precipitaciones**

Por la importancia de las obras, se considera un periodo de retorno T de 50 años y un tiempo de

concentración tc de 10 minutos para la intensidad máxima de lluvia. Según el apartado 3.702.404 del

Manual de carreteras, para un tiempo de concentración menor a 1 hora, la intensidad de lluvia debe

estimarse mediante la fórmula de Bell, detallada en la sección 3.702.405 (Bell, F.C. 1969. Generalized

Rainfall-Duration-Frecuency Relationships. Journal of Hydraulics Division of ASCE, 95 N° HY1, 311-327):

T = (0,54 × tc 0.25 −0,5) × (0,21 × ln T+ 0,52) × P 1

P tT = (0,54 × tc 0.25 −0,5) × (0,21 × ln T+ 0,52) × P 110

Donde:

tc = tiempo de concentración en minutos

ln T = Logaritmo Natural del Período de Retorno
P 1 [10] = Precipitación (mm) correspondiente a un período de retorno de T=10 años y duración de 1 hora.

En virtud de la ubicación del proyecto, se emplean los valores de la estación pluviográfica “La Paloma”

P t

_Tabla 8.3_ **-** _Estaciones pluviográficas de Chile en la zona de estudio_

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 7 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**Figura 8-1 Precipitaciones máximas La Paloma**

Por lo tanto, el periodo de retorno en 10 años con una duración de 1 hora es de 11,65 mm. Evaluando la

expresión de lluvia T = 50, para t = 10min, se tiene:

1050 = (0,54 × tc 0.25 −0,5) × (0,21 × ln T+ 0,52) × P 1

P 1050 = (0,54 × tc 0.25 −0,5) × (0,21 × ln T+ 0,52) × P 110 = 10,08 mm

Luego, la intensidad (mm/h) se obtiene mediante la ecuación 3.702.405.2 del Manual de Carreteras, y

utilizando sus respectivas unidades:

P 10

T

I= [P] [t]

t60⁄

= 43,16 [mm]

h

Donde t está en minutos.

De esta manera, para cada área tributaria se obtienen los resultados de caudal que se muestran en la

siguiente Tabla.

_Tabla 8.4 - Caudales generados por las áreas tributarias al sistema de recolección de ALL._

|Sistemas de colectores|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Áreas|A <br>(m2)|C|I (mm/h)|Q (l/s)|
|Área Canal Existente|7419|0,35|43,16|31,1|
|A1|444|0,54|43,16|2,9|
|A2|1070|0,44|43,16|5,7|
|A3|1099|0,44|43,16|5,8|
|A4|439|0,63|43,16|3,3|
|A5|492|0,78|43,16|4,6|
|A6|838|0,33|43,16|3,3|
|A7|863|0,35|43,16|3,6|
|A8|402|0,44|43,16|2,1|
|**Total (l/s)**|**Total (l/s)**|**Total (l/s)**|**Total (l/s)**|**62,35**|

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 8 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

De esta forma el canal existe tendrá los siguientes aportes:

 - 31,1 l/s provenientes del área ubicada al norte de la subestación.

 - 31,2 l/s provenientes de la ampliación de la subestación.

Así, es aporte total al canal existente y su extensión será de 62,35 l/s.

**9.** **VERIFICACIÓN HIDRÁULICA DEL SISTEMA DE DRENAJE**

**9.1.** **Colectores Horizontales**

El dimensionamiento de colectores se realiza considerando el caudal de diseño. Una vez determinados los

caudales a evacuar por la red de colectores, mediante el Método Racional, se

puede establecer los diámetros sujetos a las siguientes restricciones:

Altura normal de escurrimiento máxima : h n < 0,7D

Velocidad normal Mínima : 0,6 m/s (*)

Velocidad normal Máxima : 6,0 m/s (*)

Coeficiente de Rugosidad Manning PVC, HDPE : 0,009

(*) Según lo recomendado en el Manual de Drenaje Urbano, volumen N°5, capítulo 5.3.2.6.a “Colectores

subterráneos de la red secundaria”.

**Cálculo de Altura Normal**

Corresponde a la altura de agua desarrollada dentro de la tubería bajo condiciones de escurrimiento

permanente y uniforme. Se describe a través de la ecuación de Manning.

Q×n

2 3⁄
(1)

~~√~~ i [= A × R] [H]

Donde:

_Q_ : Caudal (m [3] /s)

_n_ : Coeficiente de rugosidad de Manning

_i_ : Pendiente longitudinal (m/m)
_A_ : área de escurrimiento (m [2] )

_R_ _H_ : Radio hidráulico (m)

A través de la ecuación de Manning se puede conocer la altura de agua generada en una tubería de

diámetro dado, conociendo el caudal que circula por ella. De esta manera, se determina el diámetro que

cumple con las restricciones impuestas anteriormente.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 9 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

**RESULTADOS DE VERIFICACIÓN DE COLECTORES**

En la siguiente tabla se muestra la verificación de colectores del sistema de drenaje.

|Tramos|D (m)|D<br>interior|Material|I (%)|Manning|Áreas|Q (m3/s)|Q accu (m3/s)|H (m)|H/D|V|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C1-C2|0.32|0.30|PVC|0.5|0.009|A8+A7|0.006|0.006|0.05|0.17|0.77|
|C2-C3|0.32|0.30|PVC|0.5|0.009|A6+A5|0.008|0.014|0.08|0.26|0.99|
|C3-C4|0.32|0.30|PVC|0.5|0.009|A4+A3|0.009|0.023|0.10|0.33|1.14|
|C4-CANAL|0.32|0.30|PVC|0.5|0.009|A2+A1|0.009|0.031|0.12|0.39|1.24|

Así, el sistema de colectores cumple con la condición H/D ≤ 0,7. Además, las velocidades presentes en los

colectores son mayores a 0,6 m/s y menores a 5 m/s.

**9.2.** **Extensión del canal existente**

El dimensionamiento del canal consiste en determinar su capacidad de porteo y las velocidades

admisibles. La extensión proyectada presenta las siguientes dimensiones:

_Figura 9-1 Perfil transversal extensión canal proyectado._

Se dimensiona considerando el caudal de diseño total que considera el aporte actual y el proyectado. Se

debe cumplir con los siguientes parámetros de diseño:

Revancha (*) : 10 cm

Velocidad normal Mínima (**) : 0,6 m/s

Velocidad normal Máxima (***) : 2,1 m/s

Coeficiente de Rugosidad Manning Canal tierra : 0,02

(*) El Manual de Carreteras Vol.3, capítulo 3.705.3 “Canales erosionables” recomienda en la letra e

agregar una revancha adecuada, no especificando valores.

(**) De acuerdo al texto Ven Te Chow, la velocidad para evitar sedimentación se encuentra entre 0.6 a

0.9 m/s.

(***) Según especificaciones de la tabla 3.703.301.B del Manual de Carreteras Vol. 3 “Velocidades

Máximas admisibles en canales no revestidos”, considerando un canal de material graduado (no coloidal)

desde limo a grava.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 10 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

En la siguiente tabla se muestra la verificación de la extensión del canal existente

_Tabla 9.1 - Resultados dimensionamiento canal._

|Q Total|62,35|l/s|
|---|---|---|
|Altura agua|0,11|m|
|Altura canal|0,4|m|
|Revancha|0,29|m|
|Velocidad|1,27|m/s|
|Froude|1,31||

Así, la extensión del canal existente cumple con los parámetros de diseño.

**9.3.** **Descarga hacia quebrada**

La descarga de aguas lluvias será conducida por la extensión del canal existente hacia una quebrada

ubicada al sur poniente de la subestación. Se realizará de forma controlada a través de un muro boca

según los diseños propuestos en el Manual de Carreteras Vol. 3. Las siguientes figuras presentan el

sistema propuesto.

_Figura 9-2 Sistema de descarga propuesto._

A partir del dimensionamiento del canal y considerando una pendiente del 2%, las velocidades de

escurrimiento obtenidas para el caudal de diseño no superan las velocidades máximas admitidas por un

canal de tierra.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 11 de 12

AMPLIACIÓN S/E DON GOYO
MEMORIA DE CÁLCULO DRENAJES

GB607-110-CV-DR-CR-01_0

_Tabla 9.2 - Tabla extraída desde el Vol. 3 Manual de Carreteras._

Por otro lado, en el Manual de Drenaje Urbano, capítulo 6.9.5.2 “Control de erosión en las descargas”,
señala que las velocidades máximas permisibles para suelos de canto redondo y flujo intermitente es 2.1
m/s. A partir del dimensionamiento presentado, el canal entregaría el agua al final de su trayecto con una
velocidad de 1,27 m/s, estando bajo el límite permitido.

De esta forma, no es necesario proyectar un sistema de control de erosión adicional en la descarga. No

obstante, de forma conservadora se considerará una protección mínima de mampostería de piedra para

la protección de la quebrada.

Ampliación en S/E Don Goyo, Seccionamiento Línea Nueva Pan de Azúcar - Punta
Sierra y Bypass Línea 2x220 kV Pan de Azúcar - La Cebada

Página 12 de 12