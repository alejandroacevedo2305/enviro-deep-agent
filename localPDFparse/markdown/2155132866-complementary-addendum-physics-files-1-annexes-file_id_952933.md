---
title: Sin título
author: Fernanda Arriagada
date: D:20221025150908-03'00'
language: es
type: report
pages: 47
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ÍNDICE DE FIGURAS
  - INDICE DE TABLAS
-->

**Inversiones Quildos**
**Limitada**

**ESTUDIO CALIDAD DE AGUA DESCARGA**

**P.T.A.S. VESPUCIO**

**“CANAL ORTUZANO”**

**BSF-04-22-H-RP-0001**

**ESTUDIO CALIDAD DEL AGUA CANAL ORTUZANO**

Para

**INVERSIONES QUILDOS Ltda.**

Preparado por

**DSS S.A.**

|Rev.|por|Emitido para|Fecha|Revisado por|Aprobado por|
|---|---|---|---|---|---|
|A|LDC|Coordinación interna|11.10.2022|ECC|JHG|
|B|LDC|Comentarios de cliente|18.10.2022|ECC|JHG|
|C|LDC|Comentarios de cliente|20.10.2022|ECC|JHG|
|0|LDC|Ingreso evaluación|25.10.2022|ECC|JHG|

**2022**

**ÍNDICE**
ÍNDICE ...................................................................................................................................... 2

ÍNDICE DE FIGURAS ................................................................................................................... 3

INDICE DE TABLAS ..................................................................................................................... 3

INTRODUCCIÓN .................................................................................................................. 4

OBJETIVOS ......................................................................................................................... 5

ESTUDIO HIDROLOGICO ..................................................................................................... 6

Metodología ................................................................................................................. 6

3.1.1. Estimación precipitación media .............................................................................. 7

3.1.2. Área aportante ..................................................................................................... 8

Resultados Caudales Medios ......................................................................................... 9

ESTUDIO HIDRÁULICO ...................................................................................................... 10

Enfoque y Metodología ............................................................................................... 10

Variables y condiciones de borde ................................................................................ 10

Resultados Modelación Hidráulica Canal Ortuzano ........................................................ 12

ESTUDIO CALIDAD DEL AGUA ........................................................................................... 22

Metodología ............................................................................................................... 22

5.1.1. Balance de Masa ................................................................................................. 22

5.1.2. Modelo Numérico Calidad .................................................................................... 23

Caracterización hidroquímica del cuerpo receptor ......................................................... 24

Caudal Efluente PTAS ................................................................................................. 25

Hidroquímica del efluente emitido por la PTAS ............................................................. 26

Normativa aplicable .................................................................................................... 27

Resultados Balance de masa ....................................................................................... 28

5.6.1. Norma NCh 1333 ................................................................................................ 30

5.6.2. Norma Secundaria de Calidad del Agua Río Maipo DS 53/2003. ............................. 33

Longitud de mezcla .................................................................................................... 38

5.7.1. Teoría Longitud de Mezcla ................................................................................... 38

5.7.2. Resultados Longitud de Mezcla ............................................................................ 40

Resultados Modelo Numérico ...................................................................................... 41

CONCLUSIONES ................................................................................................................ 44

Estudio Calidad del Agua
BSF-04-22-H-RP-0001

Página 2 de 47

# ÍNDICE DE FIGURAS

Figura 1-1. Ubicación Punto de Descarga Vespucio. ..................................................................... 4
Figura 3-1. Visualización áreas aportantes ................................................................................... 8
Figura 4-1. Eje hidráulico Canal Ortuzano tramo de estudio. ....................................................... 20
Figura 4-2. Velocidad del Flujo, situación con y sin proyecto ....................................................... 21
Figura 4-3. Numero de Froude, situación con y sin proyecto. ...................................................... 21
Figura 5-1. Puntos de Muestreo en Canal Ortuzano .................................................................... 24
Figura 5-2. Punto de control área de vigilancia MP-2 .................................................................. 28
Figura 5-3. Cuenca aportante Estero Lampa en punto MP-2. ...................................................... 33
Figura 5-4.Estación de calidad del agua “Rio Mapocho En El Monte” ........................................... 35
Figura 5-5. Solución de ecuación transporte advección-reacción de Coliformes Fecales ................ 41
Figura 5-6. Solución de ecuación transporte advección-reacción de Oxígeno Disuelto................... 42
Figura 5-7. Solución de ecuación transporte advección-reacción de DBO ..................................... 42
Figura 5-8. Solución de ecuación transporte advección-reacción de Sólidos Suspendidos Totales .. 43

# INDICE DE TABLAS

Tabla 1-1. Coordenadas Punto de Descarga Vespucio (Datum WGS84 - HUSO19S). ...................... 4
Tabla 3-1. Área aportante Canal Ortuzano ................................................................................... 8
Tabla 4-1. Coeficientes de Rugosidad de Manning según Método de Cowan. ............................... 11
Tabla 4-2. Caudales modelados situaciones con y sin proyecto. .................................................. 12
Tabla 4-3. Resultados Modelo Hidráulico Canal Ortuzano. .......................................................... 12

Tabla 5-1. Cuadro de Coordenadas Muestras de Agua (Datum WGS84 - Huso 19S) ..................... 24
Tabla 5-2 Resultados Muestras de Agua Levantamiento ............................................................. 25
Tabla 5-3 Características efluente utilizado en la modelación de calidad del agua ........................ 26
Tabla 5-4 Regulación normativa de calidad de aguas. ................................................................ 27
Tabla 5-5 Balance Masa Canal Ortuzano y Descarga concentración máxima Tabla 1 DS90............ 29
Tabla 5-6 Balance Masa Canal Ortuzano y Descarga concentración histórica PTAS ....................... 30
Tabla 5-7 Comparación Resultados Descarga concentración DS90 y concentración histórica PTAS 32
Tabla 5-8.Caudal medio mensual Río Mapocho en MP-2. ............................................................ 34
Tabla 5-9. Concentraciones estimadas para Rio Mapocho en MP-2 Descarga DS90. ..................... 36
Tabla 5-10.Concentraciones estimadas para Rio Mapocho en MP-2 Descarga Histórica................. 37
Tabla 5-11 Parámetros obtenidos a partir del manual EPA .......................................................... 40

Estudio Calidad del Agua
BSF-04-22-H-RP-0001

Página 3 de 47

**INTRODUCCIÓN**

El presente informe corresponde al estudio denominado “Estudio Calidad del Agua” solicitado a DSS

S.A. por Inversiones Quildos Ltda.,, para la Evaluación Ambiental asociada a la Descarga de la Planta

de Tratamiento de Aguas Servidas (PTAS) de Centro Logístico Vespucio en el Canal Ortuzano, ubicada

en la comuna de Pudahuel, en las cercanías del límite sur con la comuna de Maipú, en la Región

Metropolitana; y que se ubica en el punto de coordenadas definidas por el titular en la zona

presentada en la Figura 1-1 y detallada en la Tabla 1-1-1.

En este contexto, el presente informe corresponde a un estudio de calidad de agua de las situaciones

Sin proyecto y Con proyecto para analizar el cumplimiento de la normativa nacional respecto a usos

de agua NCh 1333 of. 1978 mod. 87., los compuestos regulados en la Norma Secundaria de Calidad

del Agua del Río Maipo del Decreto Supremo N°53 del año 2013 del Ministerio del Medio Ambiente,

y la Normativa DS 90 para la Regulación de Contaminantes Asociados a las Descargas de Residuos

Líquidos a Aguas Marinas y Continentales Superficiales.

**Figura 1-1. Ubicación Punto de Descarga Vespucio** **.**

**Fuente: DSS S.A** **.**

**Tabla 1-1. Coordenadas Punto de Descarga Vespucio (Datum WGS84 - HUSO19S).**

|Nombre|Norte (m)|Este (m)|
|---|---|---|
|Descarga Vespucio|6296500.00|334986.00|

**Fuente: Inversiones Quildos Ltda.**

Estudio Calidad del Agua
BSF-04-22-H-RP-0001

Página 4 de 47

**OBJETIVOS**

El objetivo general del documento es presentar el estudio de Calidad de Agua del Canal Ortuzano;

evaluando los posibles cambios producto de la descarga del efluente tratado de la PTAS que se

encuentra en las cercanías. Para esto, se presentan como objetivos específicos:

 - Estimar los caudales medios anuales que circulan por el Canal Ortuzano.

 Evaluar el comportamiento hidráulico del Canal Ortuzano.

 Recopilar y/o generar información necesaria como línea base del estudio, es decir, las que

definen las características actuales del cauce.

 Caracterizar la hidro química tanto del efluente de la planta como de las aguas del Canal

Ortuzano.

 Estimar si existe afectación por la incorporación del efluente tratado que será emitido por la

PTAS hacia el curso de agua donde tributa.

 Evaluar las concentraciones obtenidas frente en la Norma Secundaria de Calidad del Agua del

río Maipo.

Estudio Calidad del Agua
BSF-04-22-H-RP-0001

Página 5 de 47

**ESTUDIO HIDROLOGICO**

Se desarrolló el análisis hidrológico para determinar la disponibilidad de caudales medios anuales en

el Canal Ortuzano utilizando los métodos recomendados por la autoridad. Debido a la no

disponibilidad de información fluviométrica del canal, se realizó la estimación de caudales medios

anuales según la metodología precipitación escorrentía indicada en el estudio “Estimación caudales

medios y máximos de la cuenca del río Checras mediante ecuaciones sintéticas y racionales “.

El canal actualmente es parte del plan maestro de evacuación y drenaje de aguas lluvias del gran

Santiago y forma parte de la red de drenaje en su último tramo, descargando las aguas lluvias

captadas en el Rio Mapocho.

El objetivo general del estudio es caracterizar el régimen hidrológico del Canal Ortuzano en la comuna

de Pudahuel, cercano al límite con la comuna de Maipú, donde se realiza la descarga de la PTAS al

cauce. Esto incluye estimar la magnitud esperable del caudal medio.

**Metodología**

En el estudio realizado por Beatriz Gina Herencia Félix y Cesar Eduardo Carrera Saavedra, se utiliza

la ecuación expuesta a continuación para calcular el caudal medio de una cuenca, en función de la

precipitación media y el coeficiente de concentración.

Donde:

Qm= [31.71 ∗C∗P∗A]

10 [6]

C: Coeficiente de Concentración

P: Precipitación Media mm

A: Área de la cuenca km [2 ]

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 6 de 47

Para la recopilación de antecedentes se estudió la zona de descarga del efluente, donde se

identificaron estaciones meteorológicas en la zona del proyecto, para obtener información de registro

de precipitaciones que permitirán calcular caudales del Canal Ortuzano.

La estación meteorológica que fue utilizada para obtener información de precipitaciones y la ubicación

de ésta se presenta en la Figura 3-1, detallando sus coordenadas en la Tabla 3-1. La estación forma

parte de la red de estaciones meteorológicas de la Dirección General de Aguas (DGA) que mantiene

una plataforma online desde donde se obtuvo la información de los registros de caudales

**Tabla 3-1. Coordenadas Estaciones Meteorológicas Utilizadas (Datum WGS84 - HUSO 19S).**

|Nombre|Norte (m)|Este (m)|
|---|---|---|
|Terraza Oficinas Centrales DGA|6297768|347173|

**Fuente: Dirección General de Aguas.**

**Figura 3-1. Ubicación estación Meteorológica Utilizada**

**Fuente: DSS S.A**

Se utilizaron los datos de precipitación registrados por la estación de monitoreo desde el año 1960

hasta el año 2020, obteniendo un valor de precipitación media anual de 58.06mm.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 7 de 47

Dado que el canal forma parte de la red de drenaje del plan maestro de evacuación de aguas lluvias,

el área de influencia es definida por el plan maestro, donde se indica que el Canal Ortuzano pertenece

al sector NM7.3 que drena las áreas expuestas en la tabla siguiente junto a sus respectivas

codificaciones.

**Tabla 3-1. Área aportante Canal Ortuzano**

|Área Tributaria|Código|ÁREA urbana (km2)|
|---|---|---|
|General Buendía|GBD|4.04|
|San Andrés|AND|0.29|
|Teniente Cruz|TTC|5.45|
|General Bonilla|GOB|1.11|
|Serrano|SRR|1.49|
|San Pablo|PAB|1.05|
|Camino Aeropuerto|CAE|0.85|
|Laguna Sur|LAG|6.42|
|Camino El Maitén|MTN|2.95|
|**Área total**|**Área total**|**23.65**|

**Fuente: Plan maestro de evacuación y drenaje de aguas lluvias del gran Santiago**

La visualización sin escala de las áreas aportantes según la Figura 5-2 del plan maestro, donde en la

parte inferior se encuentran las áreas descritas anteriormente.

**Figura 3-1. Visualización áreas aportantes**
**Fuente: Plan maestro de evacuación y drenaje de aguas lluvias del gran Santiago**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 8 de 47

**Resultados Caudales Medios**

En base a la metodología descrita, a la precipitación calculada y al área de drenaje indicada se determinó la

magnitud del caudal medio anual para el canal Ortuzano, obteniendo que el canal anualmente en promedio

transporta 0.113 m [3] /s.

Para la posterior modelación química se consideraron los siguientes escenarios:

**Situación Sin proyecto**

 - Caudal modelado sin efluente, considera caudal medio anual 0.113 m [3] /s para el Canal

Ortuzano.

**Situación Con proyecto**

 - Caudal modelado para concentraciones DS 90, considera caudal medio anual 0.113 m [3] /s en

el Canal Ortuzano y efluente de 82 m [3] /día.

 Caudal modelado para concentraciones históricas registradas por en la PTAS, considera

caudal medio anual 0.113 m [3] /s en el Canal Ortuzano y efluente de 82 m [3] /día.

Nota: La magnitud del efluente de descarga por la PTAS Américo Vespucio fue proporcionado por Inversiones

Quildos Ltda.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 9 de 47

**ESTUDIO HIDRÁULICO**

El objetivo del análisis hidráulico es determinar los niveles de aguas máximas y ejes hidráulicos de

manera de visualizar el comportamiento del flujo de acuerdo con las características morfológicas del

cauce.

**Enfoque y Metodología**

La altura de escurrimiento en una sección transversal de un cauce puede ser determinada por la

medición directa en terreno o bien a través de técnicas hidráulicas clásicas, que consideran, entre

otros aspectos, las condiciones físicas del entorno, caudal, forma y características del cauce.

La caracterización hidráulica del flujo se realiza a través de la modelación del cauce con el software

HEC-RAS (Hydraulic Engineering Center - River Analysis System) en su versión 5.0.7 HEC-RAS fue

desarrollado por el Cuerpo de Ingenieros de los Estados Unidos, US Corp of Engineers

 [(http://www.hec.usace.army.mil/software/hec](http://www.hec.usace.army.mil/software/hec-ras/) ras/).

Al incluir el cálculo de pérdidas de carga singulares derivadas de las contracciones y expansiones del

cauce, HEC-RAS permite considerar alteraciones locales a lo largo de todo el tramo en estudio. El

nivel de aguas máximas se determinó a partir del eje hidráulico, el cual se calculó considerando

escurrimiento gradualmente variado en el sector de estudio. Los coeficientes de rugosidad para cada

tramo del lecho se estimaron mediante el método de Cowan.

**Variables y condiciones de borde**

La modelación HEC-RAS del cauce requiere la caracterización de los perfiles transversales, el

coeficiente de rugosidad de Manning, condición de borde y los caudales a simular. Con estas entradas

HEC-RAS es capaz de simular las condiciones de flujo en el cauce deseado, entregando resultados

tales como velocidad, alturas de escurrimiento, número de Froude, etc.

Si bien una de las hipótesis básicas en HEC-RAS es la unidimensionalidad del flujo, es posible

representar la sección transversal caracterizándola según las planicies de inundación derecha (right

over bank) e izquierda (left over bank), separadas ambas por el cauce principal (main channel). Así,

cada una de dichas partes debe ser caracterizada con su valor del coeficiente de Manning y su

distancia a la sección inmediatamente aguas abajo. Además, es posible obtener una aproximación

unidireccional de la distribución de velocidades en el perfil transversal o un análisis cuasi

bidimensional.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 10 de 47

Tradicionalmente, para este tipo de estudios, la metodología utilizada en la estimación del coeficiente

de rugosidad es la recomendada en el libro “Hidráulica de Canales Abiertos” de Ven Te Chow, según

el método de Cowan. De acuerdo con el método, el coeficiente de rugosidad de Manning se obtiene

a partir de la siguiente expresión:

_n_ = ( _n_ 0 + _n_ 1 + _n_ 2 + _n_ 3 + _n_ 4 )  _m_ 5

Donde n i y m 5 son valores que dependen de las condiciones del cauce.

En este caso tenemos:

n 1 : Material Involucrado.
n 2 : Grado de Irregularidad.
n 3 : Variación de la Sección Transversal.
n 4 : Efecto Relativo de las Obstrucciones.
n 5 : Vegetación.
m 5 : Grado de los Efectos por Meandros.

En el tramo de estudio, el Canal Ortuzano posee características relativamente uniformes respecto a

forma y material constitutivo del lecho. Cabe destacar que tanto el lecho como las paredes del canal

se encuentra revestidas en hormigón.

El coeficiente de rugosidad de Manning se estimó en cada una de las secciones de escurrimiento en

base al método de Cowan y a las sugerencias. Los valores adoptados son:

Tabla 4-1. Coeficientes de Rugosidad de Manning según Método de Cowan.

|Col1|Planicie<br>izquierda|Cauce<br>principal|Planicie<br>derecha|Justificación|
|---|---|---|---|---|
|n0|0.01|0.01|0.01|Revestido de hormigón|
|n1|0.00|0.00|0.00|Grado de Irregularidad insignificante|
|n2|0.00|0.00|0.00|Gradual en cauce y planicies|
|n3|0.00|0.00|0.00|Insignificante en cauce y menor en planicies|
|n4|0.02|0.002|0.02|Baja en cauce principal y medias en planicies|
|m5|1.00|1.00|1.00|Leve en cauce principal y en planicies|
|n|0.012|0.012|0.012|Coeficiente Manning final|

**Fuente: DSS S.A.**

Teniendo en cuenta estas consideraciones, se estableció un coeficiente de rugosidad n=0,012 para

el cauce principal, y n=0,012 para las planicies de inundación.

El régimen de escurrimiento del tramo de estudio es predominantemente subcrítico, por lo que como

condición de contorno se empleó la pendiente de fondo aguas abajo asociada al tirante normal, con

un valor de 3,1%, además se complementó con la pendiente aguas arriba con valor de 0,5 %

generando un modelo mixto.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 11 de 47

Se utilizaron los perfiles transversales considerando una separación de perfiles cada 20 m a lo largo

del perfil longitudinal trazado.

El modelo hidráulico desarrollado para la situación sin proyecto es la base para el desarrollo de la

situación con proyecto. La única diferencia radica en la descarga proyectada, la cual se da a lugar

desde el KM 0+177.68. A partir de este perfil al caudal extraordinario del canal se le suma el aporte

de la descargadas y asociadas a los distintos periodos de retorno como se muestra en la siguiente

tabla.

**Tabla 4-2. Caudales modelados situaciones con y sin proyecto.**

|Situación|Caudal Anual Estero<br>(m3/s)|Caudal Descarga<br>(m3/s)|
|---|---|---|
|Sin Proyecto|0.113|-|
|Con Proyecto|0.113|0.00095|

**Fuente: DSS S.A.**

**Resultados Modelación Hidráulica Canal Ortuzano**

Los resultados obtenidos de la modelación del Canal Ortuzano en la zona del proyecto se resumen

en la siguiente tabla. El perfil 177.68 es donde ocurre la descarga de la PTAS Vespucio en el canal

Ortuzano.

**Tabla 4-3. Resultados Modelo Hidráulico Canal Ortuzano.**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 12 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 13 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 14 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 15 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 16 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 17 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 18 de 47

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 19 de 47

**Fuente: DSS S.A.**

En la Figura 4-1, se encuentra graficado el eje hidráulico del Canal Ortuzano en el tramo estudiado,

se puede ver que la altura de escurrimiento, tienen variaciones insignificantes aguas arriba y aguas

abajo de la descarga proyectada.

490

488

486

484

482

480

478

476

474

472

470

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||Descar|ga|||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

0 500 1000 1500 2000 2500 3000 3500 4000

Distancia canal (m)

Sin Proyecto Con Proyecto

**Figura 4-1. Eje hidráulico Canal Ortuzano tramo de estudio.**

**Fuente: DSS S.A.**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 20 de 47

En cuanto a la velocidad del flujo que se encuentran expuestas a continuación, se observa que la

integración del caudal de descarga proyectada genera un aumento promedio aproximado de 0.3 m/s,

no obstante, se pueden apreciar en diferentes puntos del tramo modelado aumentos abruptos de la

velocidad de flujo. Esto se debe a que el caudal medio anual del canal Ortuzano es muy bajo, por lo

que el aporte de la descarga produce los comportamientos que se observan en la figura. Sin

embargo, al estar el canal construido en hormigón, este aumento en las velocidades no genera

alteración en la estructura del mismo.

Dirección de flujo

Descarga

**Figura 4-2. Velocidad del Flujo, situación con y sin proyecto**

**Fuente: DSS S.A**

Por otro lado, el número de Froude que se encuentra expuesto a continuación, se observa que la

integración del caudal de descarga proyectado genera alteraciones del régimen del flujo pasando de

un régimen subcrítico (F<1) a un régimen super critico (F>1) en diversos puntos del tramo estudiado.

Este comportamiento al igual que los cambios en la velocidades de flujo se deben a pequeño caudal

medio anual que circula por el canal Ortuzano.

Dirección de flujo

Descarga

**Figura 4-3. Numero de Froude, situación con y sin proyecto.**

**Fuente: DSS S.A**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 21 de 47

**ESTUDIO CALIDAD DEL AGUA**

Para el estudio de calidad del agua se consideró la definición de línea base del cauce y,

posteriormente, el análisis de la magnitud del efecto generado por la descarga. Para esto, se realizó

la caracterización hidroquímica del cauce receptor y del efluente. Los compuestos considerados de

interés fueron aquellos regulados en el DS 90/2000 para descargas sobre cuerpos de aguas

superficiales. Adicionalmente, debido a que el cauce es un tributario del río Mapocho, el cual

pertenece a la cuenca del Río Maipo regulado en el D.S. N°53/2013 de Norma Secundaria Calidad

del Agua se evaluaron los compuestos considerados sensibles correspondientes.

**Metodología**

Para los compuestos conservativos se aplicó un balance de masa según la ecuación:

C 3 = [C] [1] [ ∗Q] Q [1] 1 [ + C] + Q [2] 2 [ ∗Q] [2]

En el balance de masa, los parámetros se definen a continuación:

 - C 3 : Concentración aguas abajo de la descarga.

 - C 1 : Concentración del cauce receptor aguas arriba de la descarga.

 - C 2 Concentración del compuesto analizado en el efluente tratado.

 - Q 1 : Caudal del cauce receptor antes de la descarga.

 - Q 2 : Caudal del efluente tratado.

El resultado obtenido corresponde a la mezcla instantánea, siendo ésta la concentración máxima

esperada una vez que la mezcla del cauce con el efluente se realiza en su totalidad, al considerar un

sistema lótico.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 22 de 47

Para estimar la variación de la concentración de los compuestos no conservativos en el sentido

longitudinal del canal se solucionó la ecuación de Advección-Reacción implementando el software

HEC-RAS en su módulo de Calidad de Agua. Éste corresponde a un sistema de balances de masa

dinámico para modelar el destino y transporte de compuestos en aguas superficiales.

Las ecuaciones de transporte consideradas en HEC-RAS están basadas en el principio de la

conservación de masa pues se rastrea cada constituyente desde el punto de entrada espacial y

temporal a su punto final de salida, conservando la masa en el espacio y el tiempo.

Estos datos de entrada, en conjunto con las ecuaciones de balance de masas generales y las

ecuaciones específicas químicas cinéticas, definen un set especial de ecuaciones de calidad de agua.

Estas son integradas numéricamente por HEC-RAS a medida que avanza la simulación.

Donde:

C: Concentración del compuesto en ‘mg/L’.

t: Tiempo en ‘dias’.

U x,y,z: Velocidad advectiva longitudinal, lateral y vertical ‘m/día’.

E x,y,z: Coeficiente de difusión longitudinal, lateral y vertical ‘m [2] /dia’.

S L: Tasa de carga directa y difusa ‘g/m [3] /día’.

S B: Tasa de carga en el borde ‘g/m [3] /día’.

S K: Tasa de transformación cinética total ‘g/m [3] /día’.

Para el modelo físico se asume un esquema unidimensional dividido en volúmenes finitos

heterogéneos, considerando uniforme la concentración de constituyentes en la sección transversal

(flujo pistón).

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 23 de 47

**Caracterización hidroquímica del cuerpo receptor**

Para caracterizar la línea base del Canal Ortuzano, cauce receptor de la descarga, se realizó una

campaña en terreno donde se efectuó la toma de muestras para calidad del agua en puntos de

interés, las cuales fueron analizadas en laboratorio y cuya posición se presenta en la Figura 5-1 y

Tabla 5-1.

**Tabla 5-1. Cuadro de Coordenadas Muestras de Agua (Datum WGS84 - Huso 19S)**

**Fuente: DSS**

**Figura 5-1. Puntos de Muestreo en Canal Ortuzano**

**Fuente: DSS S.A** **.**

En la Tabla 5-2 se presentan los resultados de las concentraciones obtenidas en las muestras de agua

mediante el análisis de laboratorio. Las muestras de agua fueron analizadas por ANAM, los resultados

de laboratorio se encuentran adjuntos en el Anexo A adjunto.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 24 de 47

**Tabla 5-2 Resultados Muestras de Agua Levantamiento**

|Parámetro|Unidad|100m<br>AArriba|Descarga|100m<br>AAbajo|600m<br>AAbajo|700m<br>AAbajo|
|---|---|---|---|---|---|---|
|Aceites y grasas flotantes|mg/L|4|4|4|4|4|
|Cloruro|mg Cl/L|284|286|282|277|282|
|Coliformes fecales|NMP/100 mL|80|500|300|6*|2.30E+03|
|Conductividad|us/cm|1612|1607|1610|1583|1597|
|Cromo|mg Cr/L|0.024|0.024|0.024|0.024|0.024|
|Demanda Bioquímica de Oxígeno|mg/L|4|4|4|17|5|
|Fósforo|mg P/L|0.176|0.135|0.116|0.441|0.31|
|Níquel|mg Ni/L|0.018|0.018|0.018|0.018|0.018|
|Nitrato|mg N/L|1.8|1.5|1.7|3.6|3.7|
|Nitrógeno total Kjeldahl|mg N/L|2.7|1.3|1.65|3.8|3.05|
|Ortofosfato|mg P/L|0.5|0.5|0.5|0.7|0.5|
|Oxígeno|mg/l|10.9|12.6|12.7|13.3|11.6|
|pH|-|9.3|9.3|9.3|10|9.5|
|Plomo|mg Pb/L|0.012|0.012|0.012|0.012|0.012|
|Solidos Suspendidos Totales|mg/l|4|4|3|98|8|
|Sulfatos|mg SO4/L|334|262|351|312|272|
|Zinc|mg Zn/L|0.01|0.008|0.009|0.077|0.006|

- parámetro excluido por no representar el comportamiento observado en los muestreos.

**Fuente: ANAM S.A**

Debido a que todo cauce posee variaciones naturales en la concentración de sus compuestos, para

definir un valor único de línea base se consideró como representativo el valor asociado al percentil

95 de los registros en el Canal Ortuzano, sin embargo, se considera adecuado mencionar que este

valor es representativo y no único, debido a que la concentración de los compuestos varía en un

rango en donde no se observan cambios en las condiciones actuales del cauce. Para representar esta

variación se consideró pertinente acompañar el percentil 95 de cada compuesto con un rango donde

la variación se considera normal, representado por la mínima y máxima concentración medida.

**Caudal Efluente PTAS**

Si bien el régimen de caudales procesados en la PTAS presenta variaciones de forma estacional e

incluso intradiaria, generalmente se puede deducir una expresión que representa el caudal medio de

operación y que, por lo tanto, sea indicativa de los efectos de la descarga en términos medios. Esta

hipótesis de afectación será válida si los resultados tienden a una media clara y estable, en tanto los

efectos que se evalúen sean acumulados y no puntuales o discontinuos como descargas eventuales,

como es el caso del proyecto de la PTAS.

De acuerdo a lo obtenido de datos de diseño desarrollado Inversiones Quildos Ltda., el efluente

emitido desde la PTAS será de **82 [m** **[3]** **/día].**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 25 de 47

**Hidroquímica del efluente emitido por la PTAS**

La instalación proyectada contará con las capacidades para producir un efluente que respeta la

normativa vigente. En particular, la descarga del efluente tratado que se proyecta sobre el Canal

Ortuzano aplicará un tratamiento eficiente, tal que se cumplan con las exigencias para la descarga

de residuos líquidos a cuerpos de agua fluviales, según lo indicado en la Tabla N°1, del DS N°90/2000.

Lo anterior debido a que corresponde a la condición más restrictiva para la operación de la P.T.A.S.

dado que se caracteriza al canal como “Sin Capacidad de Dilución”.

La Tabla 5-3 indica el valor de la concentración de los distintos compuestos considerados en el modelo

de calidad del agua para la P.T.A.S. en la evaluación ambiental. En el caso de los compuestos Oxígeno

Disuelto y Nitrato, éstos no se encuentran regulados en el D.S. 90/2000 respecto a las

concentraciones máximas (o mínimas) a emitir, razón por la cual se caracterizó acorde a mediciones

realizadas en otras plantas con características similares a la planta proyectada.

**Tabla 5-3 Características efluente utilizado en la modelación de calidad del agua**

*Los valores de conductividad, oxígeno disuelto, nitrato y ortofosfato no están regulados en el DS90 por lo
que se escogieron valores conservadores para la operación de plantas similares

**Fuente: DSS S.A.**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 26 de 47

**Normativa aplicable**

Los estándares de calidad hidroquímica del agua corresponden a normativas legales que limitan la

concentración de diversos parámetros en el agua, y que las convierten en aceptables para ser

utilizada con determinados fines. Los objetivos de los estándares de calidad del agua son proteger la

salud pública o bienestar, y realzar la calidad del agua de modo consistente con los usos designados.

En la Tabla 5-4 se exponen las disposiciones legales que aplican sobre el efluente proyectado y las

características necesarias del cauce al que tributa, para ser apta para sus distintos usos.

**Tabla 5-4 Regulación normativa de calidad de aguas.**

|Normativa|Ámbito Normativo|
|---|---|
|NCh 1333 Of.78 y Mod.87|Requisitos de calidad de aguas para diferentes usos. Aplica sobre el agua en<br>los cauces.|
|D.S 90/2000|Regula los residuos líquidos emitidos a cuerpos de agua superficial. Aplica<br>sobre el efluente emitido por la P.T.A.S.|
|D.S. N°53/2013|Norma Secundaria de Calidad del Agua Río Maipo. Aplica sobre el río Maipo<br>y las áreas de vigilancia definidas.|

**Fuente: DSS S.A.**

La Norma Chilena No1.333 (de 1978, modificada en 1987 y vigente a la fecha) establece los

“Requisitos de Calidad del Agua para Diferentes Usos” y corresponde a un estándar de calidad. Es

aplicable a proyectos de cualquier tipo que viertan sus efluentes a cursos de aguas superficiales. Esta

norma fija un criterio de calidad del agua de acuerdo a requerimientos científicos referidos a aspectos

físicos, químicos y biológicos, según el uso determinado, con el objetivo de proteger y preservar la

calidad de las aguas para los diferentes usos, frente a la degradación producida por contaminación

con residuos de cualquier tipo u origen. Esta norma establece los requisitos de calidad del agua de

acuerdo con su uso y se debe aplicar a las aguas destinadas a los usos siguientes: consumo humano

(se debe considerar agua potable acorde a lo indicado en la norma NCh 409/2005), bebida de

animales (se debe considerar agua potable acorde a lo indicado en la norma NCh 409/2005), riego,

recreación y estética (con o sin contacto directo) y vida acuática.

Respecto al D.S. N°53/2013 “Norma Secundaria de Calidad Ambiental (NSCA) para la Protección de

las Aguas Continentales Superficiales de la Cuenca del Río Maipo”, ésta busca preservar las

condiciones actuales del Río Maipo, estableciendo áreas de vigilancia controladas mediante el

monitoreo de distintos puntos de control. En particular, el Canal Ortuzano corresponde a un tributario

del Río Mapocho, que finalmente confluye al Río Maipo en el área de vigilancia MP-2 controlado en

el punto de coordenadas (312694.00 m E, 6 6267832.00 m N) WGS 84 Huso 19 S, el cual se encuentra

ubicado ~39 km aguas abajo del punto de descarga.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 27 de 47

**Figura 5-2. Punto de control área de vigilancia MP-2**

**Fuente: DSS S.A** **.**

**Resultados Balance de masa**

Según las definiciones presentadas anteriormente, se realizó el análisis para el escenario de caudal

medio anual porteado por el Canal Ortuzano, a lo cual se adiciona el efluente emitido desde la PTAS

de 82 m [3] /día.

En la Tabla 5-5, se presenta el resultado del balance de masa para los distintos escenarios evaluados.

En la columna 1 se presenta el compuesto y en la columna 2 se indica la unidad de medida. La

columna 3 muestra la concentración actual en el cauce evaluado (Escenario Sin Proyecto). En la

columna 4 la concentración máxima permitida del efluente emitido por la planta (Tabla 1 DS 90) y

en la columna 5 la concentración final en la situación Con Proyecto del cauce evaluado. En la columna

6 se presentan las concentraciones exigidas en la norma NCh 1333 of. 78 mod. 87 para distintos usos

y el límite normado en el DS 53/2003 Norma Secundaria de Calidad del Agua Río Maipo, en particular,

asociado al área de vigilancia MP-2.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 28 de 47

**Tabla 5-5 Balance Masa Canal Ortuzano y Descarga concentración máxima Tabla 1 DS90**

|1|2|3|4|5|6|
|---|---|---|---|---|---|
|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|**Descarga**|**Con Proyecto**|**Normas**|
|**Parámetro**|**Unidad**|**Caudal Anual**|**DS 90**|**Caudal Anual +**<br>**Descarga DS90**|**Nch**<br>**1333**|
|Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2|

Nota: Valores con el símbolo *, corresponden a valores registrados históricamente por encima de la norma, independientemente de la
descarga. En naranjo concentraciones que incumplen la norma, en verde concentraciones que cumplen la norma.

**Fuente: DSS S.A.**

Adicionalmente se realizó un análisis en base a las concentraciones reales vertidas por la PTAS (Tabla

5-6). Este análisis se realizó utilizando los registros históricos de descarga presentados por el titular

desde el año 2021.

En la Tabla 5-6, se presenta el resultado del balance de masa para los distintos escenarios evaluados.

En la columna 1 se presenta el compuesto y en la columna 2 se indica la unidad de medida. La

columna 3 muestra la concentración actual en el cauce evaluado (Escenario Sin Proyecto). En la

columna 4 la concentración efluente emitida históricamente por la planta y en la columna 5 la

concentración final en la situación Con Proyecto del cauce evaluado. En la columna 6 se presentan

las concentraciones exigidas en la norma NCh 1333 of. 78 mod. 87 para distintos usos.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 29 de 47

**Tabla 5-6 Balance Masa Canal Ortuzano y Descarga concentración histórica PTAS**

|1|2|3|4|5|6|
|---|---|---|---|---|---|
|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|**Descarga**|**Con Proyecto**|**Normas**|
|**Parámetro**|**Unidad**|**Anual**|**Historico**|**Caudal Anual +**<br>**Descarga Hist.**|**Nch**<br>**1333**|
|Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2|Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2|

Nota: Valores con el símbolo *, corresponden a valores registrados históricamente por encima de la norma, independientemente de la
descarga. En naranjo concentraciones que incumplen la norma, en verde concentraciones que cumplen la norma.

**Fuente: DSS S.A.**

#### 5.6.1.1 Descarga Concentración Máxima Tabla 1 DS90

En la Tabla 5-5 se presentaron los resultados relacionados con la evaluación del caudal medio anual,

lo cual se asocia a una condición promedio del cauce bajo condiciones normales de operación.

En las situaciones Con y Sin Proyecto se observó el mismo comportamiento. En donde la mayoría de

los parámetros que se encuentran dentro de la normativa Nch 1333, exceptuando los parámetros de

Cloruro, Coliformes Fecales, Conductividad eléctrica y Sulfatos. Esto se debe a la condición actual

imperante (columna 3) medida en los levantamientos limnológicos, donde las concentraciones

existentes en el estero para estos parámetros sobrepasan la normativa. Por lo que el aumento de la

descarga no es el causante del incumplimiento de la norma (columna 5).

Respecto a los compuestos que se encuentran por encima de la norma por efecto de la descarga

(Nch 133), se encuentran solamente el parámetro de Cloruro, Coliformes Fecales, Conductividad

eléctrica y Sulfatos. Sin embargo, la concentración obtenida para Cloruro se encuentra dentro del

rango observado en el muestreo realizado (277-286 mg Cl/L), para Coliformes Fecales se encuentra

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 30 de 47

dentro del rango observado en el muestreo realizado (80-2300 NMP/100 mL), para Conductividad

eléctrica se encuentra dentro del rango observado en el muestreo realizado (1583-1612 us/cm), por

lo que la descarga no supone una alteración de la situación basal del cauce y finalmente lo mismo

ocurre en el caso de los Sulfatos, donde la concentración Con Proyecto presenta concentraciones que

se enmarcan dentro del rango de concentraciones registradas en el espero en su condición basal,

por lo que no se alteraría dicho status.

#### 5.6.1.2 Descarga Concentración Histórica PTAS

Adicionalmente se realizó un análisis en base a las concentraciones reales vertidas por la PTAS (Tabla

5-6). Este análisis se realizó utilizando los registros históricos de descarga presentados por el titular

desde el año 2021. En las situaciones Con Proyecto se observó el mismo comportamiento que en la

situación con Descarga Tabla 1 DS90. En donde la mayoría de los parámetros que se encuentran

dentro de la normativa Nch 1333, exceptuando los parámetros de Cloruro, Coliformes Fecales,

Conductividad eléctrica y Sulfatos. Esto se debe a la condición actual imperante (columna 3) medida

en los levantamientos limnológicos, donde las concentraciones existentes en el estero para estos

parámetros sobrepasan la normativa. Sin embargo, como se mencionó anteriormente con los

resultados con descarga máxima DS 90, el incumplimiento de la norma no viene dado por la descarga

de la PTAS sino por la situación basal del cauce.

#### 5.6.1.3 Comparación Resultados

En la Tabla 5-7 se presenta una comparación de los resultados del balance de masa para los distintos

escenarios evaluados. En la columna 1 se presenta el compuesto y en la columna 2 se indica la unidad

de medida. La columna 3 muestra la concentración actual en el cauce evaluado (Escenario Sin

Proyecto). En la columna 4, los resultados del balance de masa con descarga máxima permitida por

la Tabla 1 DS 90 y en la columna 5, la concentración final al evaluar la descarga con las

concentraciones registradas históricamente por la PTAS. En la columna 6 se presenta la diferencia

porcentual entre las concentraciones de los escenarios DS90 (columna 4) y descarga histórica

(columna 5), y la columna 6 presenta la reducción porcentual entre el escenario DS90 y Descarga

Historica.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 31 de 47

**Tabla 5-7 Comparación Resultados Descarga concentración DS90 y concentración histórica PTAS**

|1|2|3|4|5|6|
|---|---|---|---|---|---|
|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|<br> <br>**Sin Proyecto**<br>**(Linea Base)**|**Con Proyecto**|**Con Proyecto**|**Comparación**|
|**Parámetro**|**Unidad**<br>mg/L<br>mg Cl/L<br>NMP/100 mL<br>us/cm<br>mg Cr/L<br>mg/L<br>mg P/L<br>mg Ni/L<br>mg N/L<br>mg N/L<br>mg P/L<br>mg/l<br>unidad de pH<br>mg Pb/L<br>mg/l<br>mg SO4/L<br>mg Zn/L|**Anual**<br>4 <br>285.6<br>2030.<br>1611.6<br>0.02<br>14.6<br>0.41<br>0.02<br>3.68<br>3.65<br>0.66<br>13.18<br>9.90<br>0.01<br>80<br>347.6<br>0.06|**Caudal Anual +**<br>**Descarga DS90**|**Caudal Anual +**<br>**Descarga Hist.**|**% **<br>**Reducción**|
|Aceites y grasas flotantes<br>Cloruro<br>Coliformes fecales<br>Conductividad Electrica<br>Cromo<br>Demanda Bioquímica de Oxígeno<br>Fósforo<br>Níquel<br>Nitrato<br>Nitrógeno total Kjeldahl<br>Ortofosfato<br>Oxígeno<br>pH<br>Plomo<br>Solidos Suspendidos Totales<br>Sulfatos<br>Zinc|Aceites y grasas flotantes<br>Cloruro<br>Coliformes fecales<br>Conductividad Electrica<br>Cromo<br>Demanda Bioquímica de Oxígeno<br>Fósforo<br>Níquel<br>Nitrato<br>Nitrógeno total Kjeldahl<br>Ortofosfato<br>Oxígeno<br>pH<br>Plomo<br>Solidos Suspendidos Totales<br>Sulfatos<br>Zinc|Aceites y grasas flotantes<br>Cloruro<br>Coliformes fecales<br>Conductividad Electrica<br>Cromo<br>Demanda Bioquímica de Oxígeno<br>Fósforo<br>Níquel<br>Nitrato<br>Nitrógeno total Kjeldahl<br>Ortofosfato<br>Oxígeno<br>pH<br>Plomo<br>Solidos Suspendidos Totales<br>Sulfatos<br>Zinc|4.133<br>286.550<br>2021.443<br>1616.488<br>0.024<br>14.769<br>0.494<br>0.020<br>0.40<br>4.035<br>0.44<br>13.095<br>9.888<br>0.012<br>80<br>353.02<br>0.088|4.083<br>286.550 <br>2013.152<br>1616.488<br>0.024 <br>14.487<br>0.427 <br>0.018<br>0.36<br>3.644<br>0.384<br>13.095<br>9.876<br>0.012<br>79.369<br>353.02<br>0.063|1%<br>0.0%<br>0.4%<br>0.0%<br>1%<br>2%<br>14%<br>8%<br>10%<br>10%<br>14%<br>0.0%<br>0%<br>2%<br>1%<br>0%<br>28%|

**Fuente: DSS S.A** **.**

En la tabla anterior se muestra como la situación actual de la PTAS se encuentra cumpliendo con la

normativa vigente DS90 en su descarga, generando resultados de concentración menores a los

generados al utilizar las concentraciones máximas de dicho decreto supremo. Se puede observar que

en todos los parámetros evaluados se obtuvieron porcentajes de reducción positivos, generándose

una máxima reducción de ~28% para el caso del zinc, y una reducción mínima del ~0% en Cloruro,

conductividad eléctrica, oxígeno y sulfatos (debido a la alta concentración existente en el estero).

Estos resultados permiten llegar a la conclusión que la descarga de la PTAS no se encuentra

generando efectos negativos sobre la calidad del cauce receptor, debido a que la influencia de la

descarga no genera disrupción en los rangos de concentración obtenidos en la campaña de muestreo

y genera una disminución en las concentraciones en el estero.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 32 de 47

En el caso del cumplimiento del DS 53/2003 que corresponde a la Norma Secundaria de Calidad del

Agua del Río Maipo, los parámetros establecidos corresponden a los del área de vigilancia MP-2. Al

respecto, es importante destacar que el Rio Mapocho corresponde a uno de los tributarios del Río

Maipo, y que antes de llegar al punto de vigilancia MP-2 se generarán procesos de dilución en la

confluencia con el Rio Maipo y el Río Maipo. Se realizó la evaluación de los aportes al punto de

vigilancia MP-2, delimitando la cuenca aportante según lo presentado en la Figura 5-3, donde el área

aportante de la cuenca es de 4415.4 km [2] .

**Figura 5-3. Cuenca aportante Estero Lampa en punto MP-2.**

**Fuente: DSS S.A.**

El aumento de la cuenca también está asociado a aumento de caudal. Se estimó el caudal medio

anual basado en la estadística de caudales de la estación “Río Mapocho en Rinconada de Maipú”

(cuyos registros históricos se presentan en el Anexo C) que tiene una cuenca aportante de 4022.11

km [2], por lo que la relación de áreas es de 1.1 (También se aplicó corrección por precipitación media

mensual de cada cuenca).

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 33 de 47

**Tabla 5-8.Caudal medio mensual Río Mapocho en MP-2.**

|AÑO|AÑO|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC|ENE|FEB|MAR|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1960|1961|14.9|15.5|21.0|20.5|20.1|11.0|13.8|27.8|17.5|9.7|11.5|17.0|
|1961|1962|12.8|14.4|33.8|33.5|33.5|43.5|35.9|31.1|25.7|12.4|14.1|16.1|
|1962|1963|11.3|14.5|36.0|46.1|44.4|14.1|27.8|29.4|21.5|15.1|9.4|8.6|
|1963|1964|8.2|11.4|21.4|36.3|48.4|61.6|45.2|40.4|50.8|31.2|15.4|14.1|
|1964|1965|17.3|20.7|30.3|25.8|27.3|13.6|4.3|2.7|34.1|27.2|23.1|11.2|
|1965|1966|16.8|20.5|27.2|23.1|58.4|30.7|28.3|28.7|25.4|19.0|16.6|15.7|
|1966|1967|21.3|22.0|28.2|45.8|30.6|27.6|23.5|24.6|21.3|15.7|14.2|15.3|
|1967|1968|13.6|17.6|22.3|25.0|16.6|12.0|8.8|7.9|9.8|7.5|6.7|8.6|
|1968|1969|13.0|11.4|8.9|6.6|5.0|3.7|3.5|3.4|2.4|3.2|5.8|7.1|
|1969|1970|4.8|10.9|19.9|20.3|24.8|11.0|6.1|9.9|12.8|11.1|10.5|10.6|
|1970|1971|4.2|11.1|23.4|29.6|26.6|31.8|19.9|22.7|10.5|4.5|5.7|5.9|
|1971|1972|5.5|11.6|22.5|23.4|24.6|14.6|19.5|17.8|15.3|11.7|9.0|10.6|
|1972|1973|8.0|28.1|39.3|37.5|42.9|44.6|29.9|36.1|45.8|31.2|19.0|17.5|
|1973|1974|18.0|23.4|25.6|32.1|37.5|32.1|18.1|19.5|17.2|18.2|20.4|22.0|
|1974|1975|22.0|24.3|29.6|24.3|27.7|27.7|26.2|25.6|22.8|20.5|18.3|17.0|
|1975|1976|21.3|19.9|17.0|28.7|25.9|20.4|19.7|19.8|23.8|20.2|18.4|17.1|
|1976|1977|10.2|11.4|25.5|20.9|20.9|9.7|18.3|26.8|12.3|13.3|12.7|10.2|
|1977|1978|8.3|17.5|25.7|37.3|35.0|34.4|36.3|41.5|33.2|19.8|14.1|17.8|
|1978|1979|22.6|17.7|24.5|35.2|37.8|25.9|30.7|40.5|47.5|29.6|21.6|22.4|
|1979|1980|18.7|24.6|19.3|17.3|29.6|40.3|24.8|24.0|28.4|21.0|26.0|25.6|
|1980|1981|36.8|33.2|43.0|53.5|44.7|30.7|41.5|34.0|40.8|25.8|29.4|31.1|
|1981|1982|22.8|44.1|45.7|31.3|20.5|14.8|16.2|18.0|17.9|11.9|12.7|11.6|
|1982|1983|10.9|25.4|27.7|57.2|43.8|32.5|31.2|47.3|64.6|48.4|32.5|29.2|
|1983|1984|31.9|35.6|37.8|60.7|42.6|40.2|47.8|44.7|39.2|29.5|28.0|26.7|
|1984|1985|21.0|31.5|31.3|125.4|48.7|48.4|58.7|50.1|48.4|35.1|26.7|25.6|
|1985|1986|33.4|33.0|35.5|33.7|24.9|16.2|20.9|27.1|27.6|26.1|23.9|23.3|
|1986|1987|25.6|33.2|85.7|34.0|43.4|33.8|37.1|44.2|48.7|36.4|31.3|31.8|
|1987|1988|29.6|32.6|34.4|163.7|108.6|60.4|64.2|71.2|63.1|48.2|38.1|38.1|
|1988|1989|38.1|28.9|27.4|22.0|26.2|17.2|18.6|24.4|24.3|27.8|31.5|25.6|
|1989|1990|17.2|20.7|15.8|21.8|39.4|40.3|39.2|42.2|36.3|30.1|30.2|22.3|
|1990|1991|17.9|19.1|14.9|26.0|22.9|24.7|17.9|20.9|25.8|22.9|17.8|16.5|
|1991|1992|15.6|30.6|43.1|73.1|45.8|54.1|47.5|50.5|49.0|38.2|33.3|36.8|
|1992|1993|30.5|33.3|68.0|50.4|47.3|49.0|46.1|45.1|40.7|36.1|31.6|32.9|
|1993|1994|39.6|39.6|32.6|37.4|34.1|28.7|25.9|34.0|37.1|34.7|30.5|26.3|
|1994|1995|19.8|20.5|28.4|39.6|40.7|35.9|29.3|39.0|39.9|34.5|29.8|24.8|
|1995|1996|22.6|19.3|28.8|34.7|34.5|33.0|24.6|42.0|40.1|31.0|19.4|19.7|
|1996|1997|27.7|19.1|24.2|24.9|23.5|11.6|9.2|9.0|9.3|14.1|11.2|13.8|
|1997|1998|11.6|19.3|105.3|50.9|74.3|73.4|63.8|72.0|74.5|55.8|38.2|38.6|
|1998|1999|41.6|30.4|31.4|23.9|20.9|14.5|15.5|15.6|23.2|23.3|18.3|15.4|
|1999|2000|14.3|11.6|17.7|23.6|31.7|45.4|40.1|41.9|35.9|32.1|26.1|16.8|
|2000|2001|18.4|16.1|65.2|55.1|50.8|64.0|67.7|62.2|65.0|45.3|44.0|44.4|
|2001|2002|39.2|30.1|37.2|71.9|72.1|62.9|59.1|63.6|64.2|50.7|48.9|46.2|
|2002|2003|40.2|43.4|158.6|74.0|97.8|80.6|69.1|78.5|68.8|43.0|24.5|39.4|
|2003|2004|38.4|37.3|60.2|46.8|45.7|34.1|43.6|55.3|50.2|52.9|50.6|40.4|
|2004|2005|37.0|26.9|29.6|30.8|38.5|36.2|26.5|49.8|45.7|54.2|41.4|40.2|
|2005|2006|32.8|52.7|133.2|57.2|74.4|61.1|66.4|79.7|71.2|47.6|36.6|42.8|
|2006|2007|38.3|22.8|36.8|76.2|63.5|51.4|66.4|66.5|60.4|50.8|41.7|37.4|
|2007|2008|29.3|17.9|32.6|30.4|30.8|29.5|34.1|39.2|36.9|33.3|27.3|21.4|

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 34 de 47

|AÑO|AÑO|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC|ENE|FEB|MAR|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2008|2009|17.8|49.1|82.0|44.9|79.9|36.2|43.1|62.1|49.4|41.8|38.8|34.8|
|2009|2010|23.9|20.5|46.3|35.1|46.1|47.0|33.2|38.5|41.1|35.5|33.6|18.9|
|2010|2011|18.2|18.3|27.8|21.7|19.3|19.7|17.3|23.1|13.8|12.0|12.5|13.3|
|2011|2012|14.7|13.5|15.9|22.1|18.2|16.8|16.4|21.2|22.6|19.0|8.6|5.4|
|2012|2013|17.2|19.8|20.1|16.0|21.3|21.8|22.3|31.4|32.3|27.7|12.7|11.1|
|2013|2014|18.4|24.6|24.3|22.8|25.7|20.5|26.7|37.5|39.1|23.8|18.2|15.1|
|2014|2015|14.3|16.4|21.4|17.0|26.1|24.7|30.1|25.8|24.7|14.1|14.2|14.2|
|2015|2016|14.1|14.1|14.1|15.3|30.6|23.1|29.1|31.8|23.7|23.4|22.6|22.6|
|2016|2017|61.6|29.9|29.6|27.1|25.0|23.7|25.4|24.5|22.5|21.7|22.0|21.1|
|2017|2018|23.4|22.3|22.7|22.1|22.3|22.8|30.3|21.8|21.1|19.1|20.5|17.6|
|2018|2019|21.5|20.6|21.0|22.2|20.7|20.3|15.9|16.8|17.8|17.9|19.3|16.0|
|2019|2020|20.7|20.7|20.6|20.2|20.1|20.2|15.4|14.3|14.6|14.8|15.4|16.5|

**Fuente: DSS S.A.**

**A partir del registro histórico de caudales generado para el Rio Mapocho se determina**

**que el caudal medio anual es de 30.23 m** **[3]** **/s.**

Por otra parte, para caracterizar la hidroquímica del Rio Mapocho se revisaron los datos de la

Dirección General de Aguas, que cuenta con la estación de calidad del agua denominada “RIO

MAPOCHO EN EL MONTE” ubicada antes de la confluencia con el río Maipo según se presenta en la

Figura 5-4.

**Figura 5-4.Estación de calidad del agua “Rio Mapocho En El Monte”**

**Fuente: DGA**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 35 de 47

Se revisaron los registros históricos de la estación y se identificaron los registros de los compuestos

regulados en el DS 53. Se implementó el mismo procedimiento que en la línea base del Canal

Ortuzano y se caracterizó la línea base como el valor promedio. Con dicha caracterización se realizó

un balance de masa para estimar las concentraciones que se esperan en el punto de control MP-2.

Los resultados se presentan en la Tabla 5-9 (Descarga DS90) y en la Tabla 5-10 (Descarga Histórica).

En el escenario con descarga DS90 (Tabla 5-9) se observa que tanto en la situación sin proyecto, así

como la situación con proyecto el aumento de caudal, todos los parámetros indicados por el DS 53

cumplirán los límites establecidos en el punto de control MP-2, exceptuando el parámetro Zinc. Con

el objetivo de mantener el cumplimiento de la normativa DS53, la PTAS deberá asegurarse de evitar

descargar concentraciones de Zinc superiores a los 2 mg/l, límite en el cual se cumple la norma.

Al evaluar la situación con descarga histórica (Tabla 5-10) se puede observar que se cumplen todos

los límites establecidos en el punto de control MP-2 (DS53), no viéndose afectado el cumplimiento

normativo para la condición de caudal medio anual.

**Tabla 5-9. Concentraciones estimadas para Rio Mapocho en MP-2 Descarga DS90.**

|Col1|Col2|SIN PROYECTO|CON PROYECTO|Col5|
|---|---|---|---|---|
|**Compuesto**|**Unidad**|**Conc. MP-2**|**Conc. MP-2 + Descarga DS 90**|**DS 53 (MP-2)**|
|Cloruro|mg Cl/L|157.03|157.03|240|
|Conductividad Eléctrica|us/cm|1387.11|1387.13|1600|
|Cromo|mg Cr/L|0.01|0.01|0.05|
|DBO5|mg/L|4.15|4.15|10|
|Níquel|mg Ni/L|0.01|0.01|0.02|
|Nitrato|mg N/L|4.15|4.15|10|
|Ortofosfato|mg P/L|0.83|0.83|2.5|
|Oxígeno|mg/l|9.05|9.05|6|
|pH|unidad de pH|7.83|7.83|8.5|
|Plomo|mg Pb/L|**0.02***|0.02|0.01|
|Sulfatos|mg SO4/L|276.80|276.82|380|
|Zinc|mg Zn/L|0.02821|0.02830|0.03|

Nota: Valores con el símbolo *, corresponden a valores registrados históricamente por encima de la norma, independientemente de la
descarga. En naranjo concentraciones que incumplen la norma, en verde concentraciones que cumplen la norma.

**Fuente: DSS S.A.**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 36 de 47

**Tabla 5-10.Concentraciones estimadas para Rio Mapocho en MP-2 Descarga Histórica.**

|Col1|Col2|SIN PROYECTO|CON PROYECTO|Col5|
|---|---|---|---|---|
|**Compuesto**|**Unidad**|**Conc. MP-2**|**Conc. MP-2 + Descarga Hist**|**DS 53 (MP-2)**|
|Cloruro|mg Cl/L|157.03|157.03|240|
|Conductividad Eléctrica|us/cm|1387.11|1387.13|1600|
|Cromo|mg Cr/L|0.01|0.01|0.05|
|DBO5|mg/L|4.15|4.15|10|
|Níquel|mg Ni/L|0.01|0.01|0.02|
|Nitrato|mg N/L|4.15|4.15|10|
|Ortofosfato|mg P/L|0.83|0.83|2.5|
|Oxígeno|mg/l|9.05|9.05|6|
|pH|unidad de pH|7.83|7.83|8.5|
|Plomo|mg Pb/L|**0.02050***|0.02050|0.01|
|Sulfatos|mg SO4/L|276.80|276.82|380|
|Zinc|mg Zn/L|0.02821|0.02821|0.03|

Nota: Valores con el símbolo *, corresponden a valores registrados históricamente por encima de la norma, independientemente de la
descarga. En naranjo concentraciones que incumplen la norma, en verde concentraciones que cumplen la norma.

**Fuente: DSS S.A.**

El punto de control MP-2 del DS53 se ubica 39 km aguas abajo del punto de descarga proyectado,

sector donde sólo la concentración de Plomo no cumple la normativa en cuestión, incumplimiento

que es condicionado por las concentraciones de la línea base del rio Mapocho, por lo que se puede

argumentar que la descarga de la PTAS no afectará negativamente la condición actual de calidad de

agua en el punto MP-2, como se puede ver en la Tabla 5-11, columna 5 donde el porcentaje de

incidencia de la descarga en el punto de control es aproximadamente 0 en todos los parámetros

evaluados.

**Tabla 5-11. comparación concentraciones estimadas DS90 y descarga histórica.**

|Col1|Col2|CON PROYECTO|CON PROYECTO|Col5|Col6|
|---|---|---|---|---|---|
|**Compuesto**|**Unidad**|**Conc. MP-2 +**<br>**DS00**|**Conc. MP-2 +**<br>**Descarga Hist**|**Reducción**<br>**% **<br>**DS 53**<br>**(MP-2)**|**Reducción**<br>**% **<br>**DS 53**<br>**(MP-2)**|
|Cloruro|mg Cl/L|157.03|157.03|0.00|240|
|Conductividad Eléctrica|us/cm|1387.11|1387.13|0.00|1600|
|Cromo|mg Cr/L|0.01|0.01|0.00|0.05|
|DBO5|mg/L|4.15|4.15|0.00|10|
|Níquel|mg Ni/L|0.01|0.01|0.00|0.02|
|Nitrato|mg N/L|4.15|4.15|0.00|10|
|Ortofosfato|mg P/L|0.83|0.83|0.00|2.5|
|Oxígeno|mg/l|9.05|9.05|0.00|6|
|pH|unidad de pH|7.83|7.83|0.00|8.5|
|Plomo|mg Pb/L|**0.02050***|0.02050|0.00004|0.01|
|Sulfatos|mg SO4/L|276.80|276.82|0.00|380|
|Zinc|mg Zn/L|0.02821|0.02821|0.00332|0.03|

Nota: Valores con el símbolo *, corresponden a valores registrados históricamente por encima de la norma, independientemente de la
descarga. En naranjo concentraciones que incumplen la norma, en verde concentraciones que cumplen la norma.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 37 de 47

**Longitud de mezcla**

La longitud de mezcla corresponde a una característica de especial interés pues indica la distancia en

que el efluente se ha mezclado totalmente con las aguas del cauce, presentando una concentración

homogénea en la sección transversal. Para estimar la longitud de mezcla se aplicó la metodología de

la Agencia de Protección Ambiental de Estados Unidos (EPA, por sus siglas en inglés).

Actualmente no existe una normativa que regule la zona de mezcla de forma explícita, aunque se

han discutido algunos aspectos de forma somera en los comités de normas secundarias, debido a la

complejidad de abordar este tópico no se ha llegado a un acuerdo donde se limite la extensión de la

zona de mezcla asociada a la descarga de un efluente, permitiendo y limitando al máximo posible el

desarrollo de una zona de altas concentraciones para la mezcla afluente/efluente.

Según la Agencia de Protección del Ambiente Norteamericana (EPA, 1991), la distancia requerida

para que se alcance la condición de mezcla completa debe ser estimada a partir de las condiciones

hidráulicas del flujo y la ubicación del efluente. Para estimar la longitud de mezcla, ésta se ha definido

como la distancia en la cual la diferencia entre el valor máximo y mínimo de concentración de una

sección transversal se encuentra dentro de un rango de 25%, es decir, cuando se ha mezclado

completamente. Finalmente, la longitud de la zona de mezcla está dada por la ecuación:

L m = [m W] D [2] [u]

y

Donde:

W: Ancho del cauce.

u: Velocidad media.

D y : Coeficiente de esparcimiento lateral.

m: Parámetro cuyo valor depende en el grado de uniformidad usado para definir

“mezcla completa‟ y en la ubicación transversal de la salida en el cauce.

El parámetro, si se considera que la variación transversal es del 5% el valor es 0.1 para una descarga

cerca del centro del flujo del estero y aproximadamente 0.4 para una descarga cerca del borde del

estero.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 38 de 47

Esta ecuación semi-empírica ha sido estudiada por múltiples investigadores y, debido a su

concordancia con las observaciones, es ampliamente utilizada por el USGS de Estados Unidos y

muchos organismos ambientales, siendo explícitamente recomendado su uso por el Ministerio de

agricultura y Riego de Perú en su “Guía para la determinación de la zona de mezcla y la evaluación

del impacto del vertimiento de aguas residuales tratadas a un cuerpo natural de agua” (2017).

El coeficiente de esparcimiento lateral, para la mayoría de los cauces puede estimarse

aproximadamente por medio de la ecuación:

D = c d u∗
y

El coeficiente (c) puede variar de 0.3 a 1.0 dependiendo del tipo y grado de irregularidad de las

secciones transversales del estero. Los más rectos y uniformes cauces se caracterizan por valores

bajos de dicho coeficiente y los más irregulares, que poseen curvas o interferencias en las riberas,

se representan por valores altos cercanos a la unidad. Típicamente los cauces que exceden la unidad

son aquellos que se separan en meandros.

La velocidad de corte u* se obtiene de la expresión:

u∗= √g d s

Donde:

g: Aceleración de gravedad.

s: Pendiente del lecho del estero.

d: Profundidad del estero.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 39 de 47

Debido a que la longitud de mezcla depende de las condiciones hidráulicas del flujo, se utilizó el

modelo hidráulico presentado en el punto 4 del presente documentos para obtener los siguientes

resultados.

En base a las indicaciones de la EPA, se estimó la longitud de mezcla según lo resumido en la Tabla

5-12.

**Tabla 5-12 Parámetros obtenidos a partir del manual EPA**

|Parámetros<br>Ancho del cauce<br>Velocidad media del cauce<br>Parámetro ubicación de descarga<br>Aceleración de gravedad<br>Pendiente del lecho del cauce<br>Profundidad del cauce<br>Velocidad de corte<br>Coeficiente curvatura<br>Coeficiente de dispersión lateral|Unidad<br>m<br>m/s<br>adim<br>m/s2<br>m/m<br>m<br>adim<br>adim<br>adim|Símbolo<br>W<br>u<br>m<br>g<br>s<br>d<br>u*<br>c<br>Dy|Q anual<br>3.91<br>0.696<br>0.4<br>9.81<br>0.0049<br>0.10<br>0.69<br>0.3<br>0.0021|
|---|---|---|---|
|**Longitud zona de mezcla**|**m **|**Lzm**|**1992.38**|

**Fuente: DSS S.A.**

Considerando que el resultado depende de las constantes adimensionales escogidas como

representativas, el valor está asociado a un rango de variabilidad, del análisis se determinó un valor

de longitud de mezcla máximo aproximado de 1992 m, comenzando en la descarga proyectada.

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 40 de 47

**Resultados Modelo Numérico**

Todos los modelos de transporte advección-reacción fueron calibrados en base a los valores

observados en el punto 1000m aguas debajo de la descarga. En todos los modelos se obtuvo una

buena calibración de los resultados como se podrá apreciar a continuación.

Seguidamente, se presenta la variación de los distintos compuestos a lo largo del eje longitudinal del

cauce obtenida mediante la modelación de la ecuación transporte advección-reacción.

El gráfico Coliforme Fecales muestra que, si bien el cauce receptor presenta una concentración

superior a la normativa (Nch 1333), se observa que a partir de los 3000 metros aguas debajo del

punto de descarga se obtienen concentraciones menores al límite regulado por la norma (1000

NMP/100 mL).

2500

2000

1500

1000

500

0

|Col1|Col2|Col3|Col4|de flujo|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||Dirección|de flujo|de flujo|de flujo|de flujo|de flujo|
||||||||||
||||||||||
||||||||De|scarga|
||||||||||
||||||||||

-8000 -7000 -6000 -5000 -4000 -3000 -2000 -1000 0

**Distancia (m)**

**Figura 5-5. Solución de ecuación transporte advección-reacción de Coliformes Fecales**

**Fuente: DSS S.A**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 41 de 47

La curva de oxígeno disuelto muestra como la descarga de la PTAS genera una disminución del

oxígeno disuelto en el cauce, generando un baja en su concentración en los primeros 300 m. Sin

embargo, a pesar de que la concentración de Oxígeno disuelto tiende a aumentar aguas abajo,

estando por encima de la norma que establece que el oxígeno disuelto debe ser mayor a 6 mg/l, esta

situación se mantiene durante la longitud del cauce estudiada.

14.000

12.000

10.000

8.000

6.000

4.000

2.000

0.000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
|||||||Des|Des||
|||||||Des|Des|carga|
|||||e flujo|||||
||||Dirección d|e flujo|e flujo|e flujo|e flujo|e flujo|
||||||||||
||||||||||
||||||||||

-7000 -6000 -5000 -4000 -3000 -2000 -1000 0

**Distacia (m)**

**Figura 5-6. Solución de ecuación transporte advección-reacción de Oxígeno Disuelto**

**Fuente: DSS S.A**

Los resultados de la Demanda Biológica de Oxigeno muestran como las concentraciones medidas en

terreno disminuyen aguas debajo de la descarga alcanzando un valor de aproximado 12 mg/l a los

7000 metros aguas abajo. Lo anterior indica que el aporte de la PTAS genera una disminución en las

concentraciones provenientes del estero hasta el punto de descarga.

15.500

13.500

11.500

9.500

7.500

5.500

3.500

1.500

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||Di|Di||flujo||Des|Des|carga|
||Di|Di|ección de|flujo|flujo|flujo|flujo|flujo|
||Di|Di|ección de|flujo|flujo|flujo|flujo||
||||||||||
||||||||||
||||||||||
||||||||||

-7000 -6000 -5000 -4000 -3000 -2000 -1000 0

**Distancia (m)**

**Figura 5-7. Solución de ecuación transporte advección-reacción de DBO**

**Fuente: DSS S.A**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 42 de 47

Los resultados de los Sólidos Suspendidos Totales muestran como las concentraciones medidas en

terreno disminuyen aguas debajo de la descarga alcanzando un valor de aproximado 41 mg/l a los

7000 metros aguas abajo. El aporte de la PTAS genera una disminución en las concentraciones

provenientes del estero hasta el punto de descarga.

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

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
|||||||||De|scarga||
||||||||||||
||||Direcci|ón de flujo|||||||
||||||||||||
||||||||||||
||||||||||||

-7000 -6000 -5000 -4000 -3000 -2000 -1000 0

**Distacia (m)**

**Figura 5-8. Solución de ecuación transporte advección-reacción de Sólidos Suspendidos Totales**

**Fuente: DSS S.A**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 43 de 47

**CONCLUSIONES**

En el documento se presentaron los antecedentes y resultados del Informe de calidad del agua del

cauce del Canal Ortuzano, para la Evaluación Ambiental asociada a la Planta de Tratamiento de Aguas

Servidas del Centro Logístico Vespucio, ubicada en la comuna de Pudahuel.

Respecto a las características de la descarga, acorde a los antecedentes entregados por el titular, el

caudal será de 82 m [3] /día.

Respecto al estudio de calidad del agua, se definieron las características actuales del agua porteada

en los cauces en base a la toma de muestras de agua en terreno. Los compuestos considerados de

interés fueron aquellos regulados en el DS 90/2000 (Tabla 1: Cauce sin capacidad de dilución) para

descargas sobre cuerpos de aguas superficiales, así como los parámetros regulados por la Nch 1333.

Adicionalmente, debido a que el Canal Ortuzano pertenece a la cuenca del Río Maipo, cuyas

características hidroquímicas son reguladas en el D.S. N°53/2013- Norma Secundaria Calidad del

Agua del Río Maipo, se evaluaron los compuestos considerados sensibles.

Para los escenarios evaluado (situación Con y Sin Proyecto) se observó el mismo comportamiento,

en donde los parámetros que se encontraron fuera de la norma Nch 1333 fueron: Cloruro,

Conductividad Eléctrica, Coliformes Fecales y Sulfatos. Al Evaluar la norma secuandaria DS 53 se

observa que único parámetro que no cumple es el Plomo. Para ambas normas (Nch 1333 y DS 53)

la situación de incumplimiento esta dada por la condición actual e histórica observada tanto en el

levantamiento limnológico como en la estación de monitoreo Rio Mapocho En El Monte.

Para evaluar la extensión del efecto de la descarga en la componente agua se estableció una longitud

de mezcla de **1992.38** m. Esta distancia teórica corresponde al espacio en que las concentraciones

en el cauce se mantienen constantes luego de la descarga.

Considerando que el escenario evaluado cumple con los límites indicados en la normativa que se

utilizó como referencia (NCh 1333/78, DS 53) y que los compuestos fuera de norma se mantendrán

en concentraciones similares y menores a la actualidad.

**De este modo, se puede observar que las características de la descarga no generarán**

**cambios significativos en las características actuales del agua del curso receptor.**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 44 de 47

**Anexo A**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 45 de 47

**Anexo B**

**Tabla B-1. Registro histórico caudal medio mensual Río Mapocho en rinconada Maipu**

|AÑO|AÑO|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC|ENE|FEB|MAR|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1960|1961|13.6|14.1|19.1|18.7|18.3|10|12.6|25.3|15.9|8.8|10.5|15.5|
|1961|1962|11.7|13.1|30.8|30.5|30.5|39.6|32.7|28.3|23.4|11.3|12.8|14.7|
|1962|1963|10.3|13.2|32.8|42|40.4|12.8|25.3|26.8|19.6|13.8|8.6|7.8|
|1963|1964|7.5|10.4|19.5|33.1|44.1|56.1|41.2|36.8|46.3|28.4|14|12.8|
|1964|1965|15.8|18.9|27.6|23.5|24.9|12.4|3.9|2.5|31.1|24.8|21|10.2|
|1965|1966|15.3|18.7|24.8|21|53.2|28|25.8|26.1|23.1|17.3|15.1|14.3|
|1966|1967|19.4|20|25.7|41.7|27.9|25.1|21.4|22.4|19.4|14.3|12.9|13.9|
|1967|1968|12.4|16|20.3|22.8|15.1|10.9|8|7.2|8.9|6.8|6.1|7.8|
|1968|1969|11.8|10.4|8.1|6|4.6|3.4|3.2|3.1|2.2|2.9|5.3|6.5|
|1969|1970|4.4|9.9|18.1|18.5|22.6|10|5.6|9|11.7|10.1|9.6|9.7|
|1970|1971|3.8|10.1|21.3|27|24.2|29|18.1|20.7|9.6|4.1|5.2|5.4|
|1971|1972|5|10.6|20.5|21.3|22.4|13.3|17.8|16.2|13.9|10.7|8.2|9.7|
|1972|1973|7.3|25.6|35.8|34.2|39.1|40.6|27.2|32.9|41.7|28.4|17.3|15.9|
|1973|1974|16.4|21.3|23.3|29.2|34.2|29.2|16.5|17.8|15.7|16.6|18.6|20|
|1974|1975|20|22.1|27|22.1|25.2|25.2|23.9|23.3|20.8|18.7|16.7|15.5|
|1975|1976|19.4|18.1|15.5|26.1|23.6|18.6|17.9|18|21.7|18.4|16.8|15.6|
|1976|1977|9.3|10.4|23.2|19|19|8.8|16.7|24.4|11.2|12.1|11.6|9.3|
|1977|1978|7.6|15.9|23.4|34|31.9|31.3|33.1|37.8|30.2|18|12.8|16.2|
|1978|1979|20.6|16.1|22.3|32.1|34.4|23.6|28|36.9|43.3|27|19.7|20.4|
|1979|1980|17|22.4|17.6|15.8|27|36.7|22.6|21.9|25.9|19.1|23.7|23.3|
|1980|1981|33.5|30.2|39.2|48.7|40.7|28|37.8|31|37.2|23.5|26.8|28.3|
|1981|1982|20.8|40.2|41.6|28.5|18.7|13.5|14.8|16.4|16.3|10.8|11.6|10.6|
|1982|1983|9.9|23.1|25.2|52.1|39.9|29.6|28.4|43.1|58.8|44.1|29.6|26.6|
|1983|1984|29.1|32.4|34.4|55.3|38.8|36.6|43.5|40.7|35.7|26.9|25.5|24.3|
|1984|1985|19.1|28.7|28.5|114|44.4|44.1|53.5|45.6|44.1|32|24.3|23.3|
|1985|1986|30.4|30.1|32.3|30.7|22.7|14.8|19|24.7|25.1|23.8|21.8|21.2|
|1986|1987|23.3|30.2|78.1|31|39.5|30.8|33.8|40.3|44.4|33.2|28.5|29|
|1987|1988|27|29.7|31.3|149|98.9|55|58.5|64.9|57.5|43.9|34.7|34.7|
|1988|1989|34.7|26.3|25|20|23.9|15.7|16.9|22.2|22.1|25.3|28.7|23.3|
|1989|1990|15.7|18.9|14.4|19.9|35.9|36.7|35.7|38.4|33.1|27.4|27.5|20.3|
|1990|1991|16.3|17.4|13.6|23.7|20.9|22.5|16.3|19|23.5|20.9|16.2|15|
|1991|1992|14.2|27.9|39.3|66.6|41.7|49.3|43.3|46|44.6|34.8|30.3|33.5|
|1992|1993|27.8|30.3|61.9|45.9|43.1|44.6|42|41.1|37.1|32.9|28.8|30|
|1993|1994|36.1|36.1|29.7|34.1|31.1|26.1|23.6|31|33.8|31.6|27.8|24|
|1994|1995|18|18.7|25.9|36.1|37.1|32.7|26.7|35.5|36.3|31.4|27.1|22.6|
|1995|1996|20.6|17.6|26.2|31.6|31.4|30.1|22.4|38.3|36.5|28.2|17.7|17.9|

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 46 de 47

|AÑO|AÑO|ABR|MAY|JUN|JUL|AGO|SEP|OCT|NOV|DIC|ENE|FEB|MAR|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1996|1997|25.2|17.4|22|22.7|21.4|10.6|8.4|8.2|8.5|12.8|10.2|12.6|
|1997|1998|10.6|17.6|95.9|46.4|67.7|66.9|58.1|65.6|67.9|50.8|34.8|35.2|
|1998|1999|37.9|27.7|28.6|21.8|19|13.2|14.1|14.2|21.1|21.2|16.7|14|
|1999|2000|13|10.6|16.1|21.5|28.9|41.4|36.5|38.2|32.7|29.2|23.8|15.3|
|2000|2001|16.8|14.7|59.4|50.2|46.3|58.3|61.7|56.7|59.2|41.3|40.1|40.4|
|2001|2002|35.7|27.4|33.9|65.5|65.7|57.3|53.8|57.9|58.5|46.2|44.5|42.1|
|2002|2003|36.6|39.5|145|67.4|89.1|73.4|62.9|71.5|62.7|39.2|22.3|35.9|
|2003|2004|35|34|54.8|42.6|41.6|31.1|39.7|50.4|45.7|48.2|46.1|36.8|
|2004|2005|33.7|24.5|27|28.1|35.1|33|24.1|45.4|41.6|49.4|37.7|36.6|
|2005|2006|29.9|48|121|52.1|67.8|55.7|60.5|72.6|64.9|43.4|33.3|39|
|2006|2007|34.9|20.8|33.5|69.4|57.8|46.8|60.5|60.6|55|46.3|38|34.1|
|2007|2008|26.7|16.3|29.7|27.7|28.1|26.9|31.1|35.7|33.6|30.3|24.9|19.5|
|2008|2009|16.2|44.7|74.7|40.9|72.8|33|39.3|56.6|45|38.1|35.3|31.7|
|2009|2010|21.8|18.7|42.2|32|42|42.8|30.2|35.1|37.4|32.3|30.6|17.2|
|2010|2011|16.6|16.7|25.3|19.8|17.6|17.9|15.8|21|12.6|10.9|11.4|12.1|
|2011|2012|13.4|12.3|14.5|20.1|16.6|15.3|14.9|19.3|20.6|17.3|7.8|4.9|
|2012|2013|15.7|18|18.3|14.6|19.4|19.9|20.3|28.6|29.4|25.2|11.6|10.1|
|2013|2014|16.8|22.4|22.1|20.8|23.4|18.7|24.3|34.2|35.6|21.7|16.6|13.8|
|2014|2015|13|14.9|19.5|15.5|23.8|22.5|27.4|23.5|22.5|12.8|12.9|12.9|
|2015|2016|12.8|12.8|12.8|13.9|27.9|21|26.5|29|21.6|21.3|20.6|20.6|
|2016|2017|56.1|27.2|27|24.7|22.8|21.6|23.1|22.3|20.5|19.8|20|19.2|
|2017|2018|21.3|20.3|20.7|20.1|20.3|20.8|27.6|19.9|19.2|17.4|18.7|16|
|2018|2019|19.6|18.8|19.1|20.2|18.9|18.5|14.5|15.3|16.2|16.3|17.6|14.6|
|2019|2020|18.9|18.9|18.8|18.4|18.3|18.4|14|13|13.3|13.5|14|15|

**Fuente: DGA**

Estudio Calidad del agua
BSF-04-22-H-RP-0001

Página 47 de 47

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1-1.: Coordenadas Punto de Descarga Vespucio (Datum WGS84 - HUSO19S).****

| Nombre | Norte (m) | Este (m) |
| --- | --- | --- |
| Descarga Vespucio | 6296500.00 | 334986.00 |

**Tabla 3-1.: Área aportante Canal Ortuzano****

| Área Tributaria | Código | ÁREA urbana (km2) |
| --- | --- | --- |
| General Buendía | GBD | 4.04 |
| San Andrés | AND | 0.29 |
| Teniente Cruz | TTC | 5.45 |
| General Bonilla | GOB | 1.11 |
| Serrano | SRR | 1.49 |
| San Pablo | PAB | 1.05 |
| Camino Aeropuerto | CAE | 0.85 |
| Laguna Sur | LAG | 6.42 |
| Camino El Maitén | MTN | 2.95 |
| **Área total** | **Área total** | **23.65** |

**Tabla 4-1.: Coeficientes de Rugosidad de Manning según Método de Cowan.**

| Col1 | Planicie<br>izquierda | Cauce<br>principal | Planicie<br>derecha | Justificación |
| --- | --- | --- | --- | --- |
| n0 | 0.01 | 0.01 | 0.01 | Revestido de hormigón |
| n1 | 0.00 | 0.00 | 0.00 | Grado de Irregularidad insignificante |
| n2 | 0.00 | 0.00 | 0.00 | Gradual en cauce y planicies |
| n3 | 0.00 | 0.00 | 0.00 | Insignificante en cauce y menor en planicies |
| n4 | 0.02 | 0.002 | 0.02 | Baja en cauce principal y medias en planicies |
| m5 | 1.00 | 1.00 | 1.00 | Leve en cauce principal y en planicies |
| n | 0.012 | 0.012 | 0.012 | Coeficiente Manning final |

**Tabla 4-2.: Caudales modelados situaciones con y sin proyecto.****

| Situación | Caudal Anual Estero<br>(m3/s) | Caudal Descarga<br>(m3/s) |
| --- | --- | --- |
| Sin Proyecto | 0.113 | - |
| Con Proyecto | 0.113 | 0.00095 |

**Tabla 5-2: Resultados Muestras de Agua Levantamiento****

| Parámetro | Unidad | 100m<br>AArriba | Descarga | 100m<br>AAbajo | 600m<br>AAbajo | 700m<br>AAbajo |
| --- | --- | --- | --- | --- | --- | --- |
| Aceites y grasas flotantes | mg/L | 4 | 4 | 4 | 4 | 4 |
| Cloruro | mg Cl/L | 284 | 286 | 282 | 277 | 282 |
| Coliformes fecales | NMP/100 mL | 80 | 500 | 300 | 6* | 2.30E+03 |
| Conductividad | us/cm | 1612 | 1607 | 1610 | 1583 | 1597 |
| Cromo | mg Cr/L | 0.024 | 0.024 | 0.024 | 0.024 | 0.024 |
| Demanda Bioquímica de Oxígeno | mg/L | 4 | 4 | 4 | 17 | 5 |
| Fósforo | mg P/L | 0.176 | 0.135 | 0.116 | 0.441 | 0.31 |
| Níquel | mg Ni/L | 0.018 | 0.018 | 0.018 | 0.018 | 0.018 |
| Nitrato | mg N/L | 1.8 | 1.5 | 1.7 | 3.6 | 3.7 |
| Nitrógeno total Kjeldahl | mg N/L | 2.7 | 1.3 | 1.65 | 3.8 | 3.05 |
| Ortofosfato | mg P/L | 0.5 | 0.5 | 0.5 | 0.7 | 0.5 |
| Oxígeno | mg/l | 10.9 | 12.6 | 12.7 | 13.3 | 11.6 |
| pH | - | 9.3 | 9.3 | 9.3 | 10 | 9.5 |
| Plomo | mg Pb/L | 0.012 | 0.012 | 0.012 | 0.012 | 0.012 |
| Solidos Suspendidos Totales | mg/l | 4 | 4 | 3 | 98 | 8 |
| Sulfatos | mg SO4/L | 334 | 262 | 351 | 312 | 272 |
| Zinc | mg Zn/L | 0.01 | 0.008 | 0.009 | 0.077 | 0.006 |

**Tabla 5-4: Regulación normativa de calidad de aguas.****

| Normativa | Ámbito Normativo |
| --- | --- |
| NCh 1333 Of.78 y Mod.87 | Requisitos de calidad de aguas para diferentes usos. Aplica sobre el agua en<br>los cauces. |
| D.S 90/2000 | Regula los residuos líquidos emitidos a cuerpos de agua superficial. Aplica<br>sobre el efluente emitido por la P.T.A.S. |
| D.S. N°53/2013 | Norma Secundaria de Calidad del Agua Río Maipo. Aplica sobre el río Maipo<br>y las áreas de vigilancia definidas. |

**Tabla 5-5: Balance Masa Canal Ortuzano y Descarga concentración máxima Tabla 1 DS90****

| 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- |
| <br> <br>**Sin Proyecto**<br>**(Linea Base)** | <br> <br>**Sin Proyecto**<br>**(Linea Base)** | <br> <br>**Sin Proyecto**<br>**(Linea Base)** | **Descarga** | **Con Proyecto** | **Normas** |
| **Parámetro** | **Unidad** | **Caudal Anual** | **DS 90** | **Caudal Anual +**<br>**Descarga DS90** | **Nch**<br>**1333** |
| Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>20<br>4.133<br>10<br>Cloruro<br>mg Cl/L<br>**285.60***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030.00***<br>1000<br>2021.443<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.60***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.05<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.60<br>35<br>14.769<br>- <br>Fósforo<br>mg P/L<br>0.41<br>10<br>0.494<br>- <br>Níquel<br>mg Ni/L<br>0.02<br>0.2<br>0.020<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>5 <br>0.40<br>- <br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>50<br>4.035<br>- <br>Ortofosfato<br>mg P/L<br>0.66<br>9 <br>0.44<br>- <br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>8.5<br>9.888<br> <br>Plomo<br>mg Pb/L<br>0.01<br>0.05<br>0.012<br>>5<br>Solidos Suspendidos Totales<br>mg/l<br>80<br>80<br>80<br>- <br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000<br>353.02<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>3 <br>0.088<br>2 |

**Tabla 5-6: Balance Masa Canal Ortuzano y Descarga concentración histórica PTAS****

| 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- |
| <br> <br>**Sin Proyecto**<br>**(Linea Base)** | <br> <br>**Sin Proyecto**<br>**(Linea Base)** | <br> <br>**Sin Proyecto**<br>**(Linea Base)** | **Descarga** | **Con Proyecto** | **Normas** |
| **Parámetro** | **Unidad** | **Anual** | **Historico** | **Caudal Anual +**<br>**Descarga Hist.** | **Nch**<br>**1333** |
| Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2 | Aceites y grasas flotantes<br>mg/L<br>4 <br>14<br>4.083<br>10<br>Cloruro<br>mg Cl/L<br>**285.6***<br>400<br>286.550<br>200<br>Coliformes fecales<br>NMP/100 mL<br>**2030***<br>2 <br>2013.152<br>1000<br>Conductividad Electrica<br>us/cm<br>**1611.6***<br>2200<br>1616.488<br>1500<br>Cromo<br>mg Cr/L<br>0.02<br>0.01<br>0.024<br>0.1<br>Demanda Bioquímica de Oxígeno<br>mg/L<br>14.6<br>1 <br>14.487<br>-<br>Fósforo<br>mg P/L<br>0.41<br>1.88<br>0.427<br>-<br>Níquel<br>mg Ni/L<br>0.02<br>0.02<br>0.018<br>0.2<br>Nitrato<br>mg N/L<br>3.68<br>0.30<br>0.36<br>-<br>Nitrógeno total Kjeldahl<br>mg N/L<br>3.65<br>2.98<br>3.644<br>-<br>Ortofosfato<br>mg P/L<br>0.66<br>1.692<br>0.384<br>-<br>Oxígeno<br>mg/l<br>**13.18***<br>3 <br>13.095<br>5 <br>pH<br>unidad de pH<br>9.90<br>7.02<br>9.876<br>-<br>Plomo<br>mg Pb/L<br>0.01<br>0.03<br>0.012<br>5 <br>Solidos Suspendidos Totales<br>mg/l<br>80<br>4 <br>79.369<br>-<br>Sulfatos<br>mg SO4/L<br>**347.60***<br>1000.00<br>353.020<br>250<br>Zinc<br>mg Zn/L<br>0.06<br>0.01<br>0.063<br>2 |

**Tabla 5-7: Comparación Resultados Descarga concentración DS90 y concentración histórica PTAS****

| 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- |
| <br> <br>**Sin Proyecto**<br>**(Linea Base)** | <br> <br>**Sin Proyecto**<br>**(Linea Base)** | <br> <br>**Sin Proyecto**<br>**(Linea Base)** | **Con Proyecto** | **Con Proyecto** | **Comparación** |
| **Parámetro** | **Unidad**<br>mg/L<br>mg Cl/L<br>NMP/100 mL<br>us/cm<br>mg Cr/L<br>mg/L<br>mg P/L<br>mg Ni/L<br>mg N/L<br>mg N/L<br>mg P/L<br>mg/l<br>unidad de pH<br>mg Pb/L<br>mg/l<br>mg SO4/L<br>mg Zn/L | **Anual**<br>4 <br>285.6<br>2030.<br>1611.6<br>0.02<br>14.6<br>0.41<br>0.02<br>3.68<br>3.65<br>0.66<br>13.18<br>9.90<br>0.01<br>80<br>347.6<br>0.06 | **Caudal Anual +**<br>**Descarga DS90** | **Caudal Anual +**<br>**Descarga Hist.** | **% **<br>**Reducción** |
| Aceites y grasas flotantes<br>Cloruro<br>Coliformes fecales<br>Conductividad Electrica<br>Cromo<br>Demanda Bioquímica de Oxígeno<br>Fósforo<br>Níquel<br>Nitrato<br>Nitrógeno total Kjeldahl<br>Ortofosfato<br>Oxígeno<br>pH<br>Plomo<br>Solidos Suspendidos Totales<br>Sulfatos<br>Zinc | Aceites y grasas flotantes<br>Cloruro<br>Coliformes fecales<br>Conductividad Electrica<br>Cromo<br>Demanda Bioquímica de Oxígeno<br>Fósforo<br>Níquel<br>Nitrato<br>Nitrógeno total Kjeldahl<br>Ortofosfato<br>Oxígeno<br>pH<br>Plomo<br>Solidos Suspendidos Totales<br>Sulfatos<br>Zinc | Aceites y grasas flotantes<br>Cloruro<br>Coliformes fecales<br>Conductividad Electrica<br>Cromo<br>Demanda Bioquímica de Oxígeno<br>Fósforo<br>Níquel<br>Nitrato<br>Nitrógeno total Kjeldahl<br>Ortofosfato<br>Oxígeno<br>pH<br>Plomo<br>Solidos Suspendidos Totales<br>Sulfatos<br>Zinc | 4.133<br>286.550<br>2021.443<br>1616.488<br>0.024<br>14.769<br>0.494<br>0.020<br>0.40<br>4.035<br>0.44<br>13.095<br>9.888<br>0.012<br>80<br>353.02<br>0.088 | 4.083<br>286.550 <br>2013.152<br>1616.488<br>0.024 <br>14.487<br>0.427 <br>0.018<br>0.36<br>3.644<br>0.384<br>13.095<br>9.876<br>0.012<br>79.369<br>353.02<br>0.063 | 1%<br>0.0%<br>0.4%<br>0.0%<br>1%<br>2%<br>14%<br>8%<br>10%<br>10%<br>14%<br>0.0%<br>0%<br>2%<br>1%<br>0%<br>28% |

**Tabla 5-8.: Caudal medio mensual Río Mapocho en MP-2.****

| AÑO | AÑO | ABR | MAY | JUN | JUL | AGO | SEP | OCT | NOV | DIC | ENE | FEB | MAR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1960 | 1961 | 14.9 | 15.5 | 21.0 | 20.5 | 20.1 | 11.0 | 13.8 | 27.8 | 17.5 | 9.7 | 11.5 | 17.0 |
| 1961 | 1962 | 12.8 | 14.4 | 33.8 | 33.5 | 33.5 | 43.5 | 35.9 | 31.1 | 25.7 | 12.4 | 14.1 | 16.1 |
| 1962 | 1963 | 11.3 | 14.5 | 36.0 | 46.1 | 44.4 | 14.1 | 27.8 | 29.4 | 21.5 | 15.1 | 9.4 | 8.6 |
| 1963 | 1964 | 8.2 | 11.4 | 21.4 | 36.3 | 48.4 | 61.6 | 45.2 | 40.4 | 50.8 | 31.2 | 15.4 | 14.1 |
| 1964 | 1965 | 17.3 | 20.7 | 30.3 | 25.8 | 27.3 | 13.6 | 4.3 | 2.7 | 34.1 | 27.2 | 23.1 | 11.2 |
| 1965 | 1966 | 16.8 | 20.5 | 27.2 | 23.1 | 58.4 | 30.7 | 28.3 | 28.7 | 25.4 | 19.0 | 16.6 | 15.7 |
| 1966 | 1967 | 21.3 | 22.0 | 28.2 | 45.8 | 30.6 | 27.6 | 23.5 | 24.6 | 21.3 | 15.7 | 14.2 | 15.3 |
| 1967 | 1968 | 13.6 | 17.6 | 22.3 | 25.0 | 16.6 | 12.0 | 8.8 | 7.9 | 9.8 | 7.5 | 6.7 | 8.6 |
| 1968 | 1969 | 13.0 | 11.4 | 8.9 | 6.6 | 5.0 | 3.7 | 3.5 | 3.4 | 2.4 | 3.2 | 5.8 | 7.1 |
| 1969 | 1970 | 4.8 | 10.9 | 19.9 | 20.3 | 24.8 | 11.0 | 6.1 | 9.9 | 12.8 | 11.1 | 10.5 | 10.6 |
| 1970 | 1971 | 4.2 | 11.1 | 23.4 | 29.6 | 26.6 | 31.8 | 19.9 | 22.7 | 10.5 | 4.5 | 5.7 | 5.9 |
| 1971 | 1972 | 5.5 | 11.6 | 22.5 | 23.4 | 24.6 | 14.6 | 19.5 | 17.8 | 15.3 | 11.7 | 9.0 | 10.6 |
| 1972 | 1973 | 8.0 | 28.1 | 39.3 | 37.5 | 42.9 | 44.6 | 29.9 | 36.1 | 45.8 | 31.2 | 19.0 | 17.5 |
| 1973 | 1974 | 18.0 | 23.4 | 25.6 | 32.1 | 37.5 | 32.1 | 18.1 | 19.5 | 17.2 | 18.2 | 20.4 | 22.0 |
| 1974 | 1975 | 22.0 | 24.3 | 29.6 | 24.3 | 27.7 | 27.7 | 26.2 | 25.6 | 22.8 | 20.5 | 18.3 | 17.0 |
| 1975 | 1976 | 21.3 | 19.9 | 17.0 | 28.7 | 25.9 | 20.4 | 19.7 | 19.8 | 23.8 | 20.2 | 18.4 | 17.1 |
| 1976 | 1977 | 10.2 | 11.4 | 25.5 | 20.9 | 20.9 | 9.7 | 18.3 | 26.8 | 12.3 | 13.3 | 12.7 | 10.2 |
| 1977 | 1978 | 8.3 | 17.5 | 25.7 | 37.3 | 35.0 | 34.4 | 36.3 | 41.5 | 33.2 | 19.8 | 14.1 | 17.8 |
| 1978 | 1979 | 22.6 | 17.7 | 24.5 | 35.2 | 37.8 | 25.9 | 30.7 | 40.5 | 47.5 | 29.6 | 21.6 | 22.4 |
| 1979 | 1980 | 18.7 | 24.6 | 19.3 | 17.3 | 29.6 | 40.3 | 24.8 | 24.0 | 28.4 | 21.0 | 26.0 | 25.6 |
| 1980 | 1981 | 36.8 | 33.2 | 43.0 | 53.5 | 44.7 | 30.7 | 41.5 | 34.0 | 40.8 | 25.8 | 29.4 | 31.1 |
| 1981 | 1982 | 22.8 | 44.1 | 45.7 | 31.3 | 20.5 | 14.8 | 16.2 | 18.0 | 17.9 | 11.9 | 12.7 | 11.6 |
| 1982 | 1983 | 10.9 | 25.4 | 27.7 | 57.2 | 43.8 | 32.5 | 31.2 | 47.3 | 64.6 | 48.4 | 32.5 | 29.2 |
| 1983 | 1984 | 31.9 | 35.6 | 37.8 | 60.7 | 42.6 | 40.2 | 47.8 | 44.7 | 39.2 | 29.5 | 28.0 | 26.7 |
| 1984 | 1985 | 21.0 | 31.5 | 31.3 | 125.4 | 48.7 | 48.4 | 58.7 | 50.1 | 48.4 | 35.1 | 26.7 | 25.6 |
| 1985 | 1986 | 33.4 | 33.0 | 35.5 | 33.7 | 24.9 | 16.2 | 20.9 | 27.1 | 27.6 | 26.1 | 23.9 | 23.3 |
| 1986 | 1987 | 25.6 | 33.2 | 85.7 | 34.0 | 43.4 | 33.8 | 37.1 | 44.2 | 48.7 | 36.4 | 31.3 | 31.8 |
| 1987 | 1988 | 29.6 | 32.6 | 34.4 | 163.7 | 108.6 | 60.4 | 64.2 | 71.2 | 63.1 | 48.2 | 38.1 | 38.1 |
| 1988 | 1989 | 38.1 | 28.9 | 27.4 | 22.0 | 26.2 | 17.2 | 18.6 | 24.4 | 24.3 | 27.8 | 31.5 | 25.6 |
| 1989 | 1990 | 17.2 | 20.7 | 15.8 | 21.8 | 39.4 | 40.3 | 39.2 | 42.2 | 36.3 | 30.1 | 30.2 | 22.3 |
| 1990 | 1991 | 17.9 | 19.1 | 14.9 | 26.0 | 22.9 | 24.7 | 17.9 | 20.9 | 25.8 | 22.9 | 17.8 | 16.5 |
| 1991 | 1992 | 15.6 | 30.6 | 43.1 | 73.1 | 45.8 | 54.1 | 47.5 | 50.5 | 49.0 | 38.2 | 33.3 | 36.8 |
| 1992 | 1993 | 30.5 | 33.3 | 68.0 | 50.4 | 47.3 | 49.0 | 46.1 | 45.1 | 40.7 | 36.1 | 31.6 | 32.9 |
| 1993 | 1994 | 39.6 | 39.6 | 32.6 | 37.4 | 34.1 | 28.7 | 25.9 | 34.0 | 37.1 | 34.7 | 30.5 | 26.3 |
| 1994 | 1995 | 19.8 | 20.5 | 28.4 | 39.6 | 40.7 | 35.9 | 29.3 | 39.0 | 39.9 | 34.5 | 29.8 | 24.8 |
| 1995 | 1996 | 22.6 | 19.3 | 28.8 | 34.7 | 34.5 | 33.0 | 24.6 | 42.0 | 40.1 | 31.0 | 19.4 | 19.7 |
| 1996 | 1997 | 27.7 | 19.1 | 24.2 | 24.9 | 23.5 | 11.6 | 9.2 | 9.0 | 9.3 | 14.1 | 11.2 | 13.8 |
| 1997 | 1998 | 11.6 | 19.3 | 105.3 | 50.9 | 74.3 | 73.4 | 63.8 | 72.0 | 74.5 | 55.8 | 38.2 | 38.6 |
| 1998 | 1999 | 41.6 | 30.4 | 31.4 | 23.9 | 20.9 | 14.5 | 15.5 | 15.6 | 23.2 | 23.3 | 18.3 | 15.4 |
| 1999 | 2000 | 14.3 | 11.6 | 17.7 | 23.6 | 31.7 | 45.4 | 40.1 | 41.9 | 35.9 | 32.1 | 26.1 | 16.8 |
| 2000 | 2001 | 18.4 | 16.1 | 65.2 | 55.1 | 50.8 | 64.0 | 67.7 | 62.2 | 65.0 | 45.3 | 44.0 | 44.4 |
| 2001 | 2002 | 39.2 | 30.1 | 37.2 | 71.9 | 72.1 | 62.9 | 59.1 | 63.6 | 64.2 | 50.7 | 48.9 | 46.2 |
| 2002 | 2003 | 40.2 | 43.4 | 158.6 | 74.0 | 97.8 | 80.6 | 69.1 | 78.5 | 68.8 | 43.0 | 24.5 | 39.4 |
| 2003 | 2004 | 38.4 | 37.3 | 60.2 | 46.8 | 45.7 | 34.1 | 43.6 | 55.3 | 50.2 | 52.9 | 50.6 | 40.4 |
| 2004 | 2005 | 37.0 | 26.9 | 29.6 | 30.8 | 38.5 | 36.2 | 26.5 | 49.8 | 45.7 | 54.2 | 41.4 | 40.2 |
| 2005 | 2006 | 32.8 | 52.7 | 133.2 | 57.2 | 74.4 | 61.1 | 66.4 | 79.7 | 71.2 | 47.6 | 36.6 | 42.8 |
| 2006 | 2007 | 38.3 | 22.8 | 36.8 | 76.2 | 63.5 | 51.4 | 66.4 | 66.5 | 60.4 | 50.8 | 41.7 | 37.4 |
| 2007 | 2008 | 29.3 | 17.9 | 32.6 | 30.4 | 30.8 | 29.5 | 34.1 | 39.2 | 36.9 | 33.3 | 27.3 | 21.4 |

**Tabla 5-9.: Concentraciones estimadas para Rio Mapocho en MP-2 Descarga DS90.****

| Col1 | Col2 | SIN PROYECTO | CON PROYECTO | Col5 |
| --- | --- | --- | --- | --- |
| **Compuesto** | **Unidad** | **Conc. MP-2** | **Conc. MP-2 + Descarga DS 90** | **DS 53 (MP-2)** |
| Cloruro | mg Cl/L | 157.03 | 157.03 | 240 |
| Conductividad Eléctrica | us/cm | 1387.11 | 1387.13 | 1600 |
| Cromo | mg Cr/L | 0.01 | 0.01 | 0.05 |
| DBO5 | mg/L | 4.15 | 4.15 | 10 |
| Níquel | mg Ni/L | 0.01 | 0.01 | 0.02 |
| Nitrato | mg N/L | 4.15 | 4.15 | 10 |
| Ortofosfato | mg P/L | 0.83 | 0.83 | 2.5 |
| Oxígeno | mg/l | 9.05 | 9.05 | 6 |
| pH | unidad de pH | 7.83 | 7.83 | 8.5 |
| Plomo | mg Pb/L | **0.02*** | 0.02 | 0.01 |
| Sulfatos | mg SO4/L | 276.80 | 276.82 | 380 |
| Zinc | mg Zn/L | 0.02821 | 0.02830 | 0.03 |

**Tabla 5-10.: Concentraciones estimadas para Rio Mapocho en MP-2 Descarga Histórica.****

| Col1 | Col2 | SIN PROYECTO | CON PROYECTO | Col5 |
| --- | --- | --- | --- | --- |
| **Compuesto** | **Unidad** | **Conc. MP-2** | **Conc. MP-2 + Descarga Hist** | **DS 53 (MP-2)** |
| Cloruro | mg Cl/L | 157.03 | 157.03 | 240 |
| Conductividad Eléctrica | us/cm | 1387.11 | 1387.13 | 1600 |
| Cromo | mg Cr/L | 0.01 | 0.01 | 0.05 |
| DBO5 | mg/L | 4.15 | 4.15 | 10 |
| Níquel | mg Ni/L | 0.01 | 0.01 | 0.02 |
| Nitrato | mg N/L | 4.15 | 4.15 | 10 |
| Ortofosfato | mg P/L | 0.83 | 0.83 | 2.5 |
| Oxígeno | mg/l | 9.05 | 9.05 | 6 |
| pH | unidad de pH | 7.83 | 7.83 | 8.5 |
| Plomo | mg Pb/L | **0.02050*** | 0.02050 | 0.01 |
| Sulfatos | mg SO4/L | 276.80 | 276.82 | 380 |
| Zinc | mg Zn/L | 0.02821 | 0.02821 | 0.03 |

**Tabla 5-11.: comparación concentraciones estimadas DS90 y descarga histórica.****

| Col1 | Col2 | CON PROYECTO | CON PROYECTO | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Compuesto** | **Unidad** | **Conc. MP-2 +**<br>**DS00** | **Conc. MP-2 +**<br>**Descarga Hist** | **Reducción**<br>**% **<br>**DS 53**<br>**(MP-2)** | **Reducción**<br>**% **<br>**DS 53**<br>**(MP-2)** |
| Cloruro | mg Cl/L | 157.03 | 157.03 | 0.00 | 240 |
| Conductividad Eléctrica | us/cm | 1387.11 | 1387.13 | 0.00 | 1600 |
| Cromo | mg Cr/L | 0.01 | 0.01 | 0.00 | 0.05 |
| DBO5 | mg/L | 4.15 | 4.15 | 0.00 | 10 |
| Níquel | mg Ni/L | 0.01 | 0.01 | 0.00 | 0.02 |
| Nitrato | mg N/L | 4.15 | 4.15 | 0.00 | 10 |
| Ortofosfato | mg P/L | 0.83 | 0.83 | 0.00 | 2.5 |
| Oxígeno | mg/l | 9.05 | 9.05 | 0.00 | 6 |
| pH | unidad de pH | 7.83 | 7.83 | 0.00 | 8.5 |
| Plomo | mg Pb/L | **0.02050*** | 0.02050 | 0.00004 | 0.01 |
| Sulfatos | mg SO4/L | 276.80 | 276.82 | 0.00 | 380 |
| Zinc | mg Zn/L | 0.02821 | 0.02821 | 0.00332 | 0.03 |

**Tabla 5-12: Parámetros obtenidos a partir del manual EPA****

| Parámetros<br>Ancho del cauce<br>Velocidad media del cauce<br>Parámetro ubicación de descarga<br>Aceleración de gravedad<br>Pendiente del lecho del cauce<br>Profundidad del cauce<br>Velocidad de corte<br>Coeficiente curvatura<br>Coeficiente de dispersión lateral | Unidad<br>m<br>m/s<br>adim<br>m/s2<br>m/m<br>m<br>adim<br>adim<br>adim | Símbolo<br>W<br>u<br>m<br>g<br>s<br>d<br>u*<br>c<br>Dy | Q anual<br>3.91<br>0.696<br>0.4<br>9.81<br>0.0049<br>0.10<br>0.69<br>0.3<br>0.0021 |
| --- | --- | --- | --- |
| **Longitud zona de mezcla** | **m ** | **Lzm** | **1992.38** |
