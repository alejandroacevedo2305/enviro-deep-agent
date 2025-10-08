---
title: Sin título
author: Carlos Calderón F.
date: D:20230724170649-04'00'
language: es
type: manual
pages: 16
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. GENERALIDADES
  - 2. UBICACIÓN
  - 3. MODIFICACION DE CAUCE
  - 4. VERIFICACION DE DISEÑOS a) DESCRIPCIÓN DEL MODELO NUMÉRICO
  - b) PARÁMETROS DE LA MODELACIÓN
  - 5. MODIFICACION DE CAUCE SIN PROYECTO
  - 6. MODIFICACION DE CAUCE CON PROYECTO
  - 7. CONCLUSIONES
-->

_CCF Ingeniero Civil_
_Proyecto CANAL_

## MODIFICACION DE CANAL LA ROMINA LOTEO RESERVA FUNDO EL RECREO

# 1. GENERALIDADES

El presente análisis corresponde a la modificación de cauce del canal **La Romina**, perteneciente
a la **Asociación del Canal La Romina** en el predio donde se construirá el proyecto de Loteo
Reserva Fundo El Recreo, perteneciente a la Inmobiliaria Manquehue.

El proyecto en síntesis corresponde a la canalización a través de las calles que tiene el Loteo de
modo de no entorpecer el escurrimiento de las aguas de riego hacia predios agrícolas que se
encuentran aguas abajo del Loteo.

En el canal no se verterán aguas lluvias provenientes del loteo por la modificación de la
escorrentía, estas serán infiltradas mediante pozos absorbentes al interior del predio. También
existe un tema de altimetría por lo que no se verterán las aguas lluvias al canal, debido a que
este está en la parte alta del terreno, y por lo tanto gravitacionalmente no se puede de ninguna
manera evacuar las aguas lluvias hacia este canal. Con esto se mantendrá la cantidad de agua
que siempre ha sido transportada por este. El trazado de la entubación queda en el punto alto
del predio donde se construirá la urbanización del presente estudio.

Se verifican que las secciones solicitadas por la Asociación cumplen capacidades de caudales
de los canales, manejado el régimen de caudal con la pendiente de estos.

# 2. UBICACIÓN

El proyecto de Loteo se ubica al norte de la comuna, cercano a la Avenida San Juan sector de
Curva de la Muerte, a un costado del proyecto Portones de Machalí.
El terreno limita al norte, oriente y poniente con terrenos particulares, y al sur con Camino El
Recreo, según se muestra en croquis adjunto.

_CCF Ingeniero Civil_
_Proyecto CANAL_

# 3. MODIFICACION DE CAUCE

Para determinar la influencia del proyecto de modificación de cauce, es necesario analizar el
comportamiento hidráulico de éste en la situación actual. De este modo, es necesario explicar
las condiciones actuales del cauce.

El canal La Romina, se deriva en dos una vez que cruza la Calle El Recreo, en la parte sur oriente
del predio, tal como se indica en el croquis que se adjunta correspondiente.

 - Es un canal de regadío administrado por la **Asociación Canal La Romina.**

 Es un cauce abierto en tierra con una sección con tendencia trapezoidal irregular.

 Los canales que serán modificados tanto en trazados en sección y materialidad trabajan
en forma correcta de acuerdo con los caudales calculados para la condición de máxima
capacidad, y los informados por la Asociación, correspondiente a Q=330 l/s

 La canalización se efectuará con cajones de hormigón armado de 1.000 x 1.000mm
(ancho x alto) para cruces bajo calzada y sección de hormigón de 1.000x800 para el

_CCF Ingeniero Civil_
_Proyecto CANAL_

resto del canal a modificar, con tapas removibles de 1.200x1.000x40mm (largo x ancho
x espesor)

 Canal Romina, que accede al loteo desde el oriente por el costado norte de Camino El
Recreo para luego quebrar hacia el norte hasta salir de la propiedad. Este canal recibe
el Desagüe El Monte-Zanjón la Vinilla.

 Canal Sin Nombre, Ramal que surge del Canal Romina pocos metros aguas abajo su
quiebre hacia el norte y que encauza sus aguas hacia el nororiente.

 Canal Molino Ramal Derecho (Oriente). Procede del Canal Molino Ramal Derecho, que
accede al Loteo en la zona surponiente del Loteo cruzando mediante un travieso bajo
pavimento de Camino El Recreo. Después del cruce se bifurca y hacia la derecha u
oriente y continua lo que denominaremos el Canal Molino Ramal Derecho Oriente que
escurrirá por el costado norte del Camino El Recreo hacia al oriente y hasta alcanzar la
ubicación del Canal La Romina, desde donde paralelamente al mismo dirigirá sus aguas
hacia el norte hasta salir de la propiedad.

 Canal Molino Ramal Derecho (Poniente), es la bifurcación hacia el poniente del Canal
Molino Ramal Derecho, anteriormente mencionado. Este canal afecta al Loteo en su
límite poniente dirigiéndose hacia el norte.

_CCF Ingeniero Civil_
_Proyecto CANAL_

# 4. VERIFICACION DE DISEÑOS a) DESCRIPCIÓN DEL MODELO NUMÉRICO

La modelación hidráulica se realiza mediante el uso del software HEC-RAS 5.0.3 desarrollado

por el U.S. Army Corps of Engineers. Este programa permite realizar cálculos hidráulicos de flujo
unidimensional de ríos en régimen permanente y no permanente.

#### • a.1. Ecuación de cálculo del Eje Hidráulico

El cálculo del eje hidráulico resulta de un proceso iterativo, partiendo de una altura conocida a
otra por determinar. En términos generales, los perfiles se calculan resolviendo la ecuación de
energía entre una sección y otra, que se muestra a continuación:

2

2 2

[1]
#### 2g [+ L∗S] [f] [+ C|α] [2] [ ∗V] 2g [2]

2

[2]
#### 2g [−α] [1] [ ∗V] 2g [1]

2

2

[1]
#### 2g [|]

2

#### z 2 + h 2 + α 2 ∗ [V] [2]

#### [V] [2] 2g [= z] [1] [ + h] [1] [ + α] [1] [ ∗V] 2g [1]

Donde:

z+h: Elevación de la superficie del agua [m]
V: Velocidad media [m/s]

α: Coeficiente de Coriolis

g: Aceleración de gravedad [m/s2]
L: Largo del tramo ponderado por el caudal [m]
S f : Pendiente de fricción representativa entre dos secciones [m/m]
C: Coeficiente de pérdida por expansión o contracción
(Las secciones transversales 1 y 2 son consecutivas)
El largo del tramo ponderado, L, se calcula como sigue:

#### ̅̅̅̅ + L c ∗Q̅̅̅ + L c rd ∗Q̅̅̅̅̅ rd L= [L] [ri] [∗Q] [ri] ̅̅̅̅̅ Q̅̅̅̅ + Q ri ̅̅̅ + Q c rd

Donde:

L ri, L c, L rd : Largo de tramo entre secciones transversales en ribera izquierda, cauce principal y
ribera derecha, respectivamente.
Q ri, Q c, Q rd : Caudal promedio (aritmético) entre secciones transversales para la ribera izquierda,
cauce principal y ribera derecha, respectivamente.

_CCF Ingeniero Civil_
_Proyecto CANAL_

#### • a.2. Evaluación de las Pérdidas de Fricción

Las pérdidas de fricción se evalúan como el producto de S f y el largo ponderado L. Para el
cálculo de la pendiente de fricción (pendiente de la línea de energía) se escoge la ecuación de
Pendiente de Fricción Promedio, que se muestra a continuación:

### S = [S] [f][1] [ + S] [f][2] [̅ ] f 2

Donde:

S f1 : Pendiente de fricción en la sección 1 [m/m]
S f2 : Pendiente de fricción en la sección 2 [m/m]
(Las secciones transversales 1 y 2 son consecutivas)

#### • a.3. Evaluación de las Pérdidas de Contracción y Expansión

Las pérdidas de contracción y expansión se evalúan mediante la siguiente expresión:

2

2

[1]
#### 2g [|]

2

2
#### h ce = C|α 2 ∗ 2g [V] [2]

#### [V] [2] 2g [−α] [1] [ ∗V] 2g [1]

Donde:

C: Coeficiente de pérdida por expansión o contracción
El programa asume que una contracción ocurre siempre cuando la altura de la línea de
velocidad aguas abajo es mayor que la de aguas arriba. De la misma manera, cuando la línea
de velocidad aguas arriba es mayor que la de aguas abajo, el programa asume que ocurre una
expansión.

_CCF Ingeniero Civil_
_Proyecto CANAL_

# b) PARÁMETROS DE LA MODELACIÓN

#### • b.1. Caudales de Modelación

De acuerdo con la Guía, acápite 2.5.2.2.3 “Caudales Operacionales en Canales de Riego”, como
es el caso, _“...cuando no se disponga de registros de caudales del canal matriz ni del cauce fuente,_
_se podrá determinar el gasto máximo mediante la estimación de la capacidad de porteo,_
_incluyendo la revancha o borde libre. Para ello se debe modelar hidráulicamente el canal en un_
_tramo suficientemente largo para generar un régimen uniforme. Si el sector de proyecto no_
_permite entregar resultados confiables de la modelación, puede optarse por un tramo aguas_
_arriba o abajo que mantenga el mismo flujo. Estos resultados deben compararse con los_
_informados por la Organización de Usuarios para el tramo en el cual se produce la intervención_
_y con la capacidad de porteo de cauce. Se deberá incluir un Certificado de la organización”._

Los análisis de eje hidráulico para cauce artificial, situación con y sin proyecto del proyecto de
Modificación de Cauce Canal La Romina, se realizarán con el caudal Máximo de Porteo antes
mencionado correspondiente a **Q=0.65 m** **[3]** **/s,** sin aportes de aguas lluvias, dado que éstas
últimas no descargarán en este canal, porque la solución adoptada, de acuerdo con las
metodologías de Serviu, corresponden a zanjas de infiltración. Se verificará para la capacidad
de porteo del cauce.

El valor del caudal corresponde al informado por la comunidad de Regantes corresponde a
**Q=0.330 m3/s**

#### • b.2. Coeficientes de Rugosidad

De acuerdo con la Guía Metodológica, acápite 2.5.3.2.2 señala que para los cauces
naturales de lecho fijo se utilizará el Método de Cowan. También se señala que “Las
tablas que entregan valores de modo directo solo se usarán en casos muy justificados,
como son los cauces artificiales.

Según lo anterior, y dado que se trata de un cauce artificial menor, se descarta Cowan.

Dicho lo anterior, se considerará la rugosidad según lo indicado en tabla 3.705.1.A “Valores del
coeficiente de rugosidad o de Manning en canales” del Manual de Carreteras Volumen 3 del
MOP “Instrucciones y Criterios de Diseño” (Texto “Hidráulica de Canales”, Ven T. Chow, 1959).
Los valores definidos son:

_CCF Ingeniero Civil_
_Proyecto CANAL_

 - **n=0.024**, para “Canales Excavados y Uniformes”, “a) Tierra, Rectos y Uniformes”, “Limpio

en uso”.

 - **n=0.013** para alcantarillas de hormigón armado.

_CCF Ingeniero Civil_
_Proyecto CANAL_

_CCF Ingeniero Civil_
_Proyecto CANAL_

# 5. MODIFICACION DE CAUCE SIN PROYECTO

Para la modelación del canal sin proyecto se utiliza el software Hec-Ras 5.0.3, en el cual, se
representa el canal La Romina y Canal Sin Nombre mediante secciones transversales,
permitiendo realizar el estudio del eje hidráulico en el sector bajo las condiciones actuales
(existentes).

#### • Esquema Canal La Romina Oriente

Para el cálculo se definió un caudal máximo de porteo y se verifica en la sección más
desfavorable del canal si este es capaz de contener el caudal de diseño, para condición de altura
Normal, para el canal previo a la llegada del Zanjón La Vinilla.

_CCF Ingeniero Civil_
_Proyecto CANAL_

#### • Esquema Canal Sin Nombre

Para el cálculo se definió un caudal máximo de porteo y se verifica en la sección más
desfavorable del canal si este es capaz de contener el caudal de diseño, para condición de altura
Normal.

_CCF Ingeniero Civil_
_Proyecto CANAL_

_CCF Ingeniero Civil_
_Proyecto CANAL_

_CCF Ingeniero Civil_
_Proyecto CANAL_

#### • Esquema Canal La Romina Norte

Para el cálculo se definió un caudal máximo de porteo y se verifica en la sección más
desfavorable del canal si este es capaz de contener el caudal de diseño, para condición de altura
Normal, para el canal desde la bifurcación del Canal Sin Nombre hacia el norte.

_CCF Ingeniero Civil_
_Proyecto CANAL_

_CCF Ingeniero Civil_
_Proyecto CANAL_

# 6. MODIFICACION DE CAUCE CON PROYECTO

Para la modelación del canal sin proyecto se utiliza el software **HCanales**, en el cual, se
representan las secciones a verificar, cajón de hormigón armado de 1.0x1.0m para el cruce bajo
calzadas, tuberías de HDPE DN=1.0m con cámaras de inspección para sectores bajo terraplén
y sección rectangular de 1.0x1.0m para la conducción en general de las aguas, solicitada por la
Asociación de Regantes Canal Molino Ramal Derecho.

_CCF Ingeniero Civil_
_Proyecto CANAL_

# 7. CONCLUSIONES

De acuerdo con los análisis de los resultados, tanto para la condición sin y con proyecto, se
puede concluir que el canal a modificar, tanto en trazado, sección y materialidad trabajan en
forma correcta de acuerdo con los caudales informados. Las velocidades y tipo de
escurrimiento, entre otras cosas, se encuentran dentro de los límites indicados en la literatura
y la propia Guía.

De acuerdo con el caudal de 0.65 m [3] /s adoptado, se verifica que el canal en las condiciones
existentes (sin proyecto) funciona sin inconvenientes ni rebasando sus riberas.

Carlos Calderón Fernández

Ingeniero Civil