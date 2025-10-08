---
title: Sin título
author: Santiago_U
date: D:20220105175908-03'00'
language: es
type: report
pages: 54
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN HIDRÁULICA
-->

## PROYECTO AMPLIACIÓN CENTRO CRUCERO

# MODELACIÓN HIDRÁULICA

**Comuna de Purranque - Región de Los Lagos**

**Diciembre 2021 - REV 1 - Emitido para DGA**

### TABLA DE CONTENIDOS

1. INTRODUCCIÓN .............................................................................................................. 3

2. ALCANCES ....................................................................................................................... 7

3. ANTECEDENTES GENERALES ........................................................................................... 8

3.1 Antecedentes Disponibles ....................................................................................... 8

3.2 Referencias Bibliográficas ........................................................................................ 8

4. MODELACIÓN HIDRÁULICA ............................................................................................ 9

4.1 Objetivos de la Modelación ..................................................................................... 9

4.2 Enfoque y Metodología ........................................................................................... 9

4.3 Variables y Condiciones de Borde Utilizados en la Simulación ............................. 10

4.3.1 Geometría del Cauce y Planicie de Inundación .............................................. 10

4.3.2 Coeficiente de Manning ................................................................................. 12

4.3.3 Condiciones de Borde ..................................................................................... 17

4.3.4 Determinación de Caudales ........................................................................... 19

4.4 Modelación Estero Potrerillo de las Yeguas .......................................................... 22

4.5 Modelación Estero Sin Nombre ............................................................................. 25

4.5.1 Resultados Modelación Sin Proyecto ............................................................. 25

4.5.2 Resultados Modelación Con Proyecto............................................................ 30

4.6 Modelación Canal de Desagüe de Aguas Lluvia ..................................................... 36

4.7 Análisis Comparativo ............................................................................................. 37

5. SOCAVACIÓN LOCAL ..................................................................................................... 43

5.1 Dimensiones Socavación ........................................................................................ 44

5.1.1 Dimensiones en Planta de la Fosa de Socavación .......................................... 45

5.2 Resultados de Socavación Local ................................................................................. 45

6. CÁLCULO DE ENROCADO DE PROTECCIÓN .................................................................. 48

6.1 Taludes de Fondo ...................................................................................................... 48

7. CONCLUSIÓN ................................................................................................................ 52

1

2

### 1. INTRODUCCIÓN

Zero Corp SpA está orientada a la valorización y reutilización de los residuos industriales

provenientes de la industria sanitaria, láctea, acuícola, cárnica y agroindustrial, utilizando

estos como materia prima para la generación de productos que entreguen soluciones

integrales y agreguen valor a las actividades de nuestros clientes.

La ampliación de la planta crucero busca entregar un nuevo destino a los lodos que se

generan actualmente; evitando así que estos sean derivados a un relleno sanitario, o

cualquier otro mecanismo de disposición final; es decir, prolongando en el tiempo el ciclo

de uso benéfico que se le pueda dar a un elemento que es un residuo de una actividad

industrial.

El presente informe trata del análisis del comportamiento hidráulico del Estero Sin Nombre

en la zona afectada por la modificación de cauce asociado al proyecto de la planta de

compostaje, la cual para su operación hace cambios en la condición natural del suelo,

alterando así la forma en que se descargan las aguas lluvia que caen sobre el área de la

planta.

La planta busca mantener el drenaje natural de las aguas lluvia, razón por la cual utiliza el

mismo sistema de drenaje natural, el cual consiste en un pequeño canal, el cual conduce

sus aguas hacia el estero sin nombre. Siendo la principal diferencia entre la condición sin y

con proyecto, el hecho que la instalación de la planta y su ampliación, aumentan el

coeficiente de escorrentía de las aguas lluvia, debido a que para una condición con

proyecto, se presentan zonas más impermeables, además las aguas lluvia son capturadas

por sumideros y conducidas por alcantarillas de HDPE hacia el canal de desagüe natural.

Adicionalmente el proyecto considera la construcción de un camino de acceso, el cual pasa

sobre el mismo Estero Sin Nombre, en una sección muy cercana al desagüe descrito en el

párrafo anterior.

En la Figura 1.1 se muestra una vista en planta con el tramo de estudio del Estero Sin

Nombre, en donde se puede ver el Estero Potrerillo de las Yeguas, y cómo se relaciona la

Planta Crucero con estos dos esteros.

3

**Figura 1.1 Plano Planta Estero Sin Nombre, zona Entubamiento.**
**Fuente: Elaboración propia en base a Google Earth.**

Como se ve, el Estero Sin nombre descarga sus aguas a un cauce mayor llamado Estero

Potrerillo de las Yeguas. El contexto de drenaje global no se altera, es decir, por un lado el

predio donde se instala la planta descarga sus aguas sobre el estero Sin Nombre para una

condición sin y con proyecto, y a su vez el Estero Sin Nombre descarga sus aguas sobre el

Estero Potrerillo de las Yeguas, también para una condición sin y con proyecto. Dicho lo

anterior, el área de influencia de la entrada en operación de la planta no alcanza a afectar

al Estero Potrerillo de las Yeguas, ya sea por el entubamiento del entubamiento o la

descarga de sus aguas sobre el estero sin nombre, razón por la que la modelación se basa

solo en el Estero Sin Nombre.

Para poder dar mayor respaldo a lo aseverado en el plano anterior, al modelo se le agregará

una pequeña zona del Estero Sin Nombre. No es necesario modelar una gran sección de

este Estero, ya que solo se quiere ver si para los casos de crecida existe una influencia de la

cota de inundación del Estero Potrerillo de las Yeguas sobre el Estero Sin Nombre.

4

Para el análisis hidráulico del estero se realizó un estudio hidrológico de las crecidas de

diseño, asociada a un caudal de 100 años período de retorno. Luego se hace una revisión

del diseño para una crecida de 200 años.

**Figura 1.2 Fotos de obra del Entubamiento para camino de acceso a la planta sobre el Estero Sin Nombre.**
**Fuente: Elaboración propia.**

5

**Figura 1.3 Foto Canal Natural de Desagüe de Aguas Lluvia.**
**Fuente: Elaboración propia.**

6

### 2. ALCANCES

Esta memoria hidráulica tiene por objetivo modelar y analizar las condiciones de

escurrimiento del Estero Sin Nombre para una situación con la condición original sin la

presencia del entubamiento y una situación con el entubamiento y la descarga ya en

operación, denominado una condición sin y con proyecto respectivamente. Para esto se

analiza un tramo del canal de 340 metros de largo, en donde se incluye el área de influencia

del entubamiento y el área de influencia del desagüe.

Para alcanzar este objetivo se realizan los siguientes pasos:

 - Generar un modelo del Estero Sin Nombre en la zona de la planta mediante el

software computacional HEC-RAS, en base a datos topográficos e hidrológicos.

 - Obtener un perfil longitudinal del Estero Sin Nombre en la zona donde se emplaza

el proyecto, y generar los perfiles transversales de éste.

 - Obtener y analizar los parámetros hidráulicos del modelo en HEC-RAS para una

situación sin proyecto.

 - Obtener y analizar los parámetros hidráulicos del modelo en HEC-RAS para una

situación con proyecto, es decir, implementado el entubamiento del cauce.

Una vez obtenidos los resultados de la modelación hidráulica del Estero Sin Nombre, es

posible determinar el impacto que generan las obra implementadas en el estero,

determinando así la necesidad de implementar obras de mitigación, por posibles efectos de

procesos erosivos.

7

### 3. ANTECEDENTES GENERALES

#### 3.1 Antecedentes Disponibles

Para la elaboración de la presente memoria, se dispone de los siguientes antecedentes.

 - Estudio Hidrológico de Crecidas de la cuenca de la cuenca en estudio.

 - Levantamiento topográfico del sector.

 - Visitas a Terreno.

#### 3.2 Referencias Bibliográficas

Para la elaboración de la siguiente memoria, se han consultado las siguientes referencias

bibliográficas:

[Ref.1]: Guía de Presentación y Aprobación de Proyectos de Modificación de Cauces.

[Ref.2]: Design of Small Canals, Bureau of Reclamation.

[Ref.3]: Hidráulica, F.J Domínguez.

[Ref.4]: Open Channel Hydraulics, Ven Te Chow.

8

### 4. MODELACIÓN HIDRÁULICA

#### 4.1 Objetivos de la Modelación

De acuerdo a lo indicado en el instructivo de la Dirección General de Aguas se debe realizar

un análisis hidráulico del escurrimiento para diferentes condiciones de caudal,

determinando ejes hidráulicos para las crecidas, velocidades, régimen de escurrimiento y

definición de zonas de inundación. Debido a la particularidad del canal, solo se analiza los

ejes hidráulicos para el caso del caudal de diseño.

El objetivo del análisis hidráulico es, a partir de las características morfológicas del canal,

determinar los niveles de aguas máximas, ejes hidráulicos y las zonas de inundación para

poder visualizar el comportamiento del mismo y su capacidad máxima antes y después de

ejecutar las obras en el cauce, enfocado específicamente en la zona de emplazamiento del

entubamiento.

#### 4.2 Enfoque y Metodología

La altura de escurrimiento en una sección de un cauce puede ser determinada por la

medición directa en terreno o bien, puede ser estimada a través de las técnicas clásicas de

la hidráulica conociendo las condiciones físicas del entorno. Esta altura depende del caudal

y las formas y características del cauce.

La caracterización hidráulica del flujo se realiza a través de la modelación del

funcionamiento hidráulico del cauce con el programa HEC-RAS. Este es un programa de

análisis hidráulico desarrollado por el _Hydrologic Engineering_ Center (del Cuerpo de

Ingenieros del Ejército de EE.UU.) que a partir de datos topográficos y de caudales permite

simular el comportamiento hidráulico del cauce. HEC-RAS es un programa que se utiliza

9

frecuentemente para este tipo de modelaciones y entrega resultados adecuados para este

tipo de análisis.

#### 4.3 Variables y Condiciones de Borde Utilizados en la Simulación

El software HEC-RAS requiere para la simulación del canal la caracterización de los perfiles

transversales, el coeficiente de rugosidad de Manning y los caudales a simular. HEC-RAS

permite la simulación del caudal en el cauce deseado entregando resultados tales como

velocidades, alturas de escurrimiento y número de Froude, entre otros.

**4.3.1** **Geometría del Cauce y Planicie de Inundación**

Se realizó un levantamiento topo batimétrico del lecho del estero Sin Nombre,

construyendo curvas de nivel cada 0,5 [m] que caracterizan la morfología del lecho del Canal

en la zona del proyecto. Este mismo topo batimétrico se realizó para el canal que desagua

las aguas lluvias desde la planta al Estero Sin Nombre, y para el estero Potrerillo de las

Yeguas, que es donde llegan todas las aguas drenadas por la planta y por el estero Sin

Nombre.

El eje a analizar del Estero Sin Nombre tiene una longitud de 340 [m], considerando en este

tramo la zona de influencia del entubamiento y del desagüe. De esta forma, se cumple con

el tramo mínimo exigido de 100 [m] aguas arriba y aguas abajo de la obra proyectada

estipulado por la Dirección General de Aguas en la Referencia 1 mencionada en el Capítulo

4. Finalmente, se trazaron perfiles transversales cada 20 [m] aproximadamente a lo largo

del eje de en estudio, abarcando entre 15 [m] de ancho de cada sección del estero.

Por su parte, el Canal de Desagüe se analiza en todo su trayecto, el que asciende a un largo

total de 100 metros, en donde se analizaron perfiles cada 20 metros, en un ancho de 5

metros. Por su parte, el Estero Potrerillo de las Yeguas se analiza en la sección de

intersección con el Estero Sin nombre, para un largo de 100 metros, en donde se analizan

perfiles cada 20 metros con anchos de 20 metros.

10

En la Figura 4.1 se muestra la topografía utilizada y luego en la Figura 4.2 se muestra el

alineamiento trazado en la modelación hidráulica.

**Figura 4.1 Planta Topo Batimetría, Estero Son Nombre, Sector Planta Crucero.**
**Fuente: Levantamiento Topo Batimétrico.**

**Figura 4.2 Alineamiento utilizado en modelo hidráulico HEC-RAS.**
**Fuente: Modelación HECRAS.**

11

Notar que el alineamiento trazado en la planta topográfica es la misma utilizada en la

modelación hidráulica, respetando la morfología del estero.

En la figura a continuación se muestra la modelación del entubamiento del camino, el que

consiste en un camino 5 metros de ancho aproximadamente, por donde el estero fue

entubado con dos tuberías de sección circular de 1.5 metros de diámetro.

**Figura 4.2 Sección transversal del entubamiento del Canal, Modelo hidráulico HEC-RAS.**
**Fuente: Levantamiento Topo Batimétrico.**

**4.3.2** **Coeficiente de Manning**

Si bien una de las hipótesis básicas en HEC-RAS es la unidimensionalidad del flujo, se

permite representar la sección caracterizándola según las planicies de inundación derecha

12

( _right over bank)_ e izquierda ( _left over bank_ ) separadas ambas por el cauce principal ( _main_

_channel_ ). Así, cada una de dichas partes debe ser caracterizada con su valor del coeficiente

de Manning y su distancia a la sección inmediatamente aguas abajo. Tradicionalmente para

este tipo de estudios, la metodología utilizada es la recomendada en el libro “Hidráulica de

Canales Abiertos” de Ven Te Chow de acuerdo al método de Cowan. Según este método, el

coeficiente de rugosidad de Manning se obtiene a partir de la ecuación 1.

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m (1)

Donde n i y m son valores que dependen de las condiciones del cauce, las cuales se detallan

a continuación:

n 0 Valor base, relacionado al material del lecho.

n 1 Grado de Irregularidad

n 2 Variación de la Sección Transversal

n 3 Efecto Relativo de las Obstrucciones

n 4 Vegetación

m Grado de los Efectos por Meandros

El estero Sin Nombre tiene una pendiente baja en el tramo de estudio, presenta algunas

singularidades en su recorrido, y caracteriza por poseer una vegetación ribereña en casi

todo el trazado del canal, con excepción en la zona donde se construyó en donde la

vegetación fue removida para el proceso constructivo del puente y camino de acceso.

Algo similar se tiene para el caso del Estero Potrerillo de las Yeguas, en donde hay baja

pendiente, pero la vegetación es más intensa, sobre todo en las riberas.

13

**Figura 4.3 Fotografías del Lecho del Estero Potrerillo de las Yeguas Aguas arriba de la Unión con Estero Sin**

**Nombre.**

**Fuente: Elaboración Propia**

14

**Figura 4.4 Fotografías del Lecho del Estero Sin Nombre Aguas abajo del entubamiento.**
**Fuente: Elaboración Propia**

Si bien la vegetación ribereña es abundante en todo el tramo, esta es más intensa desde el

perfil Km0+260, sección del estero aguas abajo del canal de desagüe. Por lo anterior, los

coeficientes de Manning característicos del estero sin nombre en estudio, se separan entre

esas dos secciones.

Dadas las características del Estero Sin Nombre, en el tramo de interés, y con base en

valores entregados por Ven Te Chow (1959) en el libro “Hidráulica de Canales Abiertos”, y

de los datos se determinaron los coeficientes ya mencionados tanto para el cauce principal

como para las planicies de inundación izquierda y derecha del cauce en análisis.

En la Tabla 4.1 se muestra los valores estimados para n i y m, tanto para riberas y cauce

principal, separando la zona de captación, que presenta una condición particular.

|Tabla 4.1 Determinación del coeficiente de rugosidad de Manning por método de Cowan, Estero Sin Nombre|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Entre perfil km0+000 al perfil km 0+240|Entre perfil km0+000 al perfil km 0+240|Entre perfil km0+000 al perfil km 0+240|Entre perfil km0+000 al perfil km 0+240|Entre perfil km0+000 al perfil km 0+240|
|**Descripción Coeficiente**|**Cauce**|**Cauce**|**Ribera**|**Ribera**|
|**Descripción Coeficiente**|**Justificación**|**Valor**|**Justificación**|**Valor**|

15

|n0|Material|Tierra|0.020|Tierra|0.02|
|---|---|---|---|---|---|
|**n1**|Grado de Irregularidad Perímetro<br>Mojado|Moderado|0.005|Moderado|0.005|
|**n2**|Variaciones de las Secciones|Moderado|0.003|Moderado|0.003|
|**n3**|Efecto Relativo de las Obstrucciones|Leve|0.012|Leve|0.012|
|**n4**|Densidad de Vegetación|Baja|0.005|Media|0.012|
|**m **|Sinuosidad y Frecuencia de Meandros|Leve|1|Leve|1|
|**n **|**Rugosidad de Manning Río Pitreño**|**Manning**|**0.045**|**Manning**|**0.052**|
|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|
|Entre perfil km0+260 al perfil km 0+340|Entre perfil km0+260 al perfil km 0+340|Entre perfil km0+260 al perfil km 0+340|Entre perfil km0+260 al perfil km 0+340|Entre perfil km0+260 al perfil km 0+340|Entre perfil km0+260 al perfil km 0+340|
|**Descripción Coeficiente**|**Descripción Coeficiente**|**Cauce**|**Cauce**|**Ribera**|**Ribera**|
|**Descripción Coeficiente**|**Descripción Coeficiente**|**Justificación**|**Valor**|**Justificación**|**Valor**|
|**n0**|Material|Tierra|0.020|Tierra|0.02|
|**n1**|Grado de Irregularidad Perímetro<br>Mojado|Moderado|0.005|Moderado|0.005|
|**n2**|Variaciones de las Secciones|Moderado|0.003|Moderado|0.003|
|**n3**|Efecto Relativo de las Obstrucciones|Leve|0.012|Leve|0.012|
|**n4**|Densidad de Vegetación|Alta|0.015|Alta|0.02|
|**m **|Sinuosidad y Frecuencia de Meandros|Leve|1|Leve|1|
|**n **|**Rugosidad de Manning Río Pitreño**|**Manning**|**0.055**|**Manning**|**0.060**|

**Fuente: Elaboración propia.**

Por otro lado la construcción de la planta supone una limpieza y mayor definición del caudal

de desagüe de las aguas lluvia, teniendo como resultado una disminución considerable en

el coeficiente de Manning en ese sector. En la tabla a continuación se presentan la condición

particular de los coeficientes de Manning de este canal.

**Tabla 4.2 Determinación del coeficiente de rugosidad de Manning por método de Cowan, Canal de Desagüe.**

|Descripción Coeficiente|Col2|Cauce|Col4|Ribera|Col6|
|---|---|---|---|---|---|
|**Descripción Coeficiente**|**Descripción Coeficiente**|**Justificación**|**Valor**|**Justificació**<br>**n **|**Valor**|
|**n**<br>**0 **|Material|Tierra|0.020|Tierra|0.02|
|**n**<br>**1 **|Grado de Irregularidad Perímetro<br>Mojado|Moderado|0.005|Moderado|0.005|
|**n**<br>**2 **|Variaciones de las Secciones|Moderado|0.003|Moderado|0.003|
|**n**<br>**3 **|Efecto Relativo de las Obstrucciones|Leve|0.012|Leve|0.012|

16

|n<br>4|Densidad de Vegetación|Baja|0.005|Baja|0.005|
|---|---|---|---|---|---|
|**m **|Sinuosidad y Frecuencia de<br>Meandros|Leve|1|Leve|1|
|**n**|**Rugosidad de Manning Río Pitreño**|**Manning**|**0.045**|**Manning**|**0.045**|

**Fuente: Elaboración propia.**

Por último, se muestran los coeficientes de Manning para el caso del tramo de estudio del

Estero Potrerillos de las Yeguas, el cual presenta mayores meandros y vegetación más

intensa en las riberas.

**Tabla 4.3 Determinación del coeficiente de rugosidad de Manning por método de Cowan, Estero Potrerillo de**
**las Yeguas.**

|Descripción Coeficiente|Col2|Cauce|Col4|Ribera|Col6|
|---|---|---|---|---|---|
|**Descripción Coeficiente**|**Descripción Coeficiente**|**Justificación**|**Valor**|**Justificación**|**Valor**|
|**n0**|Material|Tierra|0.020|Tierra|0.02|
|**n1**|Grado de Irregularidad Perímetro Mojado|Moderado|0.005|Moderado|0.005|
|**n2**|Variaciones de las Secciones|Moderado|0.003|Moderado|0.003|
|**n3**|Efecto Relativo de las Obstrucciones|Leve|0.012|Leve|0.012|
|**n4**|Densidad de Vegetación|baja|0.005|Alta|0.02|
|**m **|Sinuosidad y Frecuencia de Meandros|Leve|1.1|Media|1.1|
|**n **|**Rugosidad de Manning Río Pitreño**|**Manning**|**0.050**|**Manning**|**0.066**|

**Fuente: Elaboración propia.**

Los valores estimados coinciden con los criterios establecidos por Chow (1959), donde se

indica que para la planicie menor el coeficiente de Manning es 0.045 y para los taludes de
0.052 s/m [1/3] . El elevado valor del coeficiente de Manning para el caso de los taludes, es por

la presencia de vegetación en algunos tramos y meandros en la zona de influencia del sector

de estudio. Si bien esta situación es corregida con la limpieza del canal, de forma

conservadora se modela con una situación donde hay presencia de vegetación.

**4.3.3** **Condiciones de Borde**

La morfología del Estero Sin Nombre es similar a lo largo del tramo de estudio, sin presentar
grandes variaciones en cuanto a su pendiente, sinuosidad y planicie de inundación
considerando el tramo en estudio. Por esta razón, como condición de contorno se empleó
una pendiente de fondo del cauce acorde a la pendiente media del tramo de estudio de la
zona aguas arriba y aguas abajo, la cual se supone similar a la pendiente de escurrimiento.
La pendiente media es 0.009 [m/m] (0.9%) para la zona de estudio. De esta forma, queda
determinada una condición de borde que representa el entorno del estero en estudio.

17

Por otra parte, el régimen de escurrimiento del tramo de estudio es predominantemente
subcrítico, con algunos tramos donde se muestra supercrítico o crítico. Para este caso,
resulta conveniente la posibilidad del software HEC-RAS de simular el escurrimiento en
forma mixta, asumiendo la condición de borde de la pendiente aguas arriba como aguas
abajo.

En la Tabla 4.4 se resume las condiciones de contorno utilizadas en modelo hidráulico HEC
RAS.

**Tabla 4.4 Resumen de condiciones de contorno calibradas para la modelación hidráulica de Estero Sin**

**Nombre.**

|Variables|Descripción|
|---|---|
|Geometría|Levantamiento realizado en la zona de estudio.|
|Coeficiente de<br>Rugosidad de Manning|Cauce principal: n = 0.045<br>Planicies de inundación: n = 0.052|
|Tipo de Modelación|Flujo Permanente en Escurrimiento Mixto|
|Condición de Borde<br>Aguas Arriba y Abajo|Estero Sin Nombre: Pendiente fondo A. Arriba 0.9 [%]<br>Estero Sin Nombre: Unión con Estero Potrerillo de las<br>Yeguas|

**Fuente: Elaboración propia.**

Por su parte el canal de desagüe también presenta características similares, es decir, bajas
pendientes y pocas variaciones en la sección. En la Tabla 4.5 se resume las condiciones de
contorno utilizadas en modelo hidráulico HEC-RAS para este canal, siendo la principal
diferencia la ausencia de vegetación densa, tanto en el cauce como en sus riberas.

**Tabla 4.5 Resumen de condiciones de contorno calibradas para la modelación hidráulica del Canal de**
**Desagüe.**

|Variables|Descripción|
|---|---|
|Geometría|Levantamiento realizado en la zona de estudio.|
|Coeficiente de<br>Rugosidad de Manning|Cauce principal: n = 0.045<br>Planicies de inundación: n = 0.045|
|Tipo de Modelación|Flujo Permanente en Escurrimiento Mixto|

18

**Fuente: Elaboración propia.**

Por último se presentan las condiciones de borde del Estero Potrerillo de las Yeguas.

**Tabla 4.6 Resumen de condiciones de contorno calibradas para la modelación hidráulica del Estero Potrerillo**
**de las Yeguas.**

|Variables|Descripción|
|---|---|
|Geometría|Levantamiento realizado en la zona de estudio.|
|Coeficiente de<br>Rugosidad de Manning|Cauce principal: n = 0.05<br>Planicies de inundación: n = 0.066|
|Tipo de Modelación|Flujo Permanente en Escurrimiento Mixto|
|Condición de Borde<br>Aguas Arriba y Abajo|Estero Sin Nombre: Pendiente fondo A. Arriba 0.92 [%]<br>Estero Sin Nombre: Pendiente fondo A. Abajo 0.92 [%]|

**Fuente: Elaboración propia.**

**4.3.4** **Determinación de Caudales**

Para determinar los caudales a modelar en el presente estudio, se realizó un estudio

hidrológico de la cuenca del estero Sin Nombre. Para ello, se utilizan los datos hidráulicos

representativos de la zona del proyecto, con el fin de estimar los caudales máximos

instantáneos para diferentes periodos de retorno. Estos últimos son los caudales de diseño

y verificación para obras civiles del entubamiento a verificar.

Para obtener una correcta medición de los parámetros morfológicos de la cuenta, se hizo

un análisis de ésta a través de la carta IGM de Riachuelo, H-031, 2da Edición 2009, escala

1:50.000. A continuación un resumen de los parámetros obtenidos.

19

**Tabla 4.7 Parámetros morfológicos utilizados para el cálculo del tiempo de concentración. v**

Fuente: Elaboración propia.

Con la ayuda de la misma carta IGM, se obtuvo el área aportante de la cuenca del Estero

Sin Nombre. En la imagen a continuación se presenta un extracto del área obtenida. Para
mayor detalle, ver **Plano 1 “Área Aportante”** del **PAS 156** .

**Figura 4.5 Área Aportante Estero Sin Nombre**

**Fuente: Elaboración propia.**

20

 - **CAUDALES MÁXIMOS INSTANTÁNEOS**

El objetivo del estudio de los caudales máximos instantáneos son dos, por un lado es
verificar el diseño el sistema de conducción de aguas lluvias producidas al interior de
la planta, y el manejo de éste de manera de evacuar este volumen de agua de manera
segura. De esta manera se asegura que el sistema de conducción evita que se mezcle las
aguas lluvia con lixiviados del proceso productivo de la planta en operación. Por otro
lado se busca que el drenaje de las aguas lluvia producida al interior de la planta se
realice de manera segura, sin producir efectos. Para esto, el presente estudio analiza los
caudales de crecida del estero sin nombre, que es el drenaje natural del área de
emplazamiento de la planta. Este dato también es útil para comprobar el diseño de un
entubamiento del estero en una sección de él, de manera de comprobar la capacidad

hidráulica de esta obra hidráulica.

Para este estudio, se optó por utilizar métodos indirectos de estimación de caudales

máximos instantáneos por sobre los métodos directos. Esto es debido a que no se cuenta

con estaciones fluviométricas en las cercanías del proyecto.

Los valores de caudales máximos obtenidos para cada uno de los cauces en estudio se

muestran en la tabla a continuación.

**Tabla 4.8 Caudales máximos instantáneos Seleccionados en m3/s.**

**Fuente: Estudio Hidrológico.**

Dado que las metodologías no entregan por defecto caudales con periodo de retorno mayor

a 100 años, se utilizó un ajuste logarítmico para cada curva, con el fin de extrapolar el caudal

máximo instantáneo con periodo de retorno de 200 años, tal como se muestra en los

resultados anteriores.

21

La memoria de cálculo hidrológico realizado sobre la cuenca del estero Sin Nombre y el

Estero Potrerillo de las Yeguas se puede ver con mayor detalle en el **Anexo 1 “Estudio**

**Hidrológico** ” del **PAS 156** .

#### 4.4 Modelación Estero Potrerillo de las Yeguas

Con el fin de obtener las condiciones de borde del estero Sin nombre en la sección aguas

abajo, se modela un tramo de 100 metros del Estero Potrerillo de las Yeguas. En la Figura

4.6 se muestra el modelo desarrollado en HEC-RAS en donde el perfil km 0+060 representa

el punto de intersección de los dos esteros. Para representar esta unión, se hace un

aumento de caudal en la sección, tal como ocurre en la realidad.

Para modelar se incluyen las condiciones de borde mencionadas en inciso 4.3 para el estero

en cuestión.

22

**Figura 4.6 Vista 3D de modelo hidráulico de Estero Potrerillo de las Yegas para situación sin proyecto.**

**Fuente: Modelo hidráulico HEC-RAS.**

En la Figura 4.7 se muestra el eje hidráulico de los tramos de estudio del estero Potrerillo

de las Yeguas, para el caudal de diseño y el caudal de verificación.

23

**Figura 4.7 Eje Hidráulico Estero Potrerillo de las Yeguas para caudal de diseño y Verificación.**

**Fuente: Modelo hidráulico HEC-RAS.**

Además, en la Tabla 4.9 y Tabla 4.10 se muestran los principales resultados de la simulación

hidráulica para el tramo en estudio del Estero Potrerillo de las Yeguas. Se entregan los

valores del eje hidráulico, velocidad de escurrimiento, ancho superficial, y número de

Froude.

**Tabla 4.9 Resultados simulación hidráulica Estero Potrerillo de las Yeguas para caudal de Diseño.**

|Perfil|Caudal|Cota<br>Fondo|Cota Pelo<br>de Agua|Velocidad<br>Media|Área<br>Mojada|Ancho<br>Superficial|Número<br>de Froude|
|---|---|---|---|---|---|---|---|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|27.68|149.23|151.26|2.14|13.85|11.37|0.56|
|km 0+020|27.68|149.11|151.27|1.29|21.52|14.09|0.33|
|km 0+040|27.68|149.33|151.14|1.67|17.49|14.88|0.44|
|km 0+060|27.68|149.2|151.12|1.36|22.97|17.14|0.33|
|km 0+080|33.02|149.18|150.93|1.89|17.48|13.82|0.54|
|km 0+100|33.02|149.16|150.71|2.16|15.28|11.39|0.6|

**Fuente: Modelo hidráulico Estero Potrerillo de las Yeguas, HEC-RAS.**

**Tabla 4.10 Resultados simulación hidráulica Estero Potrerillo de las Yeguas para caudal de Verificación.**

|Perfil|Caudal|Cota<br>Fondo|Cota Pelo<br>de Agua|Velocidad<br>Media|Área<br>Mojada|Ancho<br>Superficial|Número<br>de Froude|
|---|---|---|---|---|---|---|---|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|

24

|km 0+000|32.06|149.23|151.38|2.27|15.23|12.08|0.58|
|---|---|---|---|---|---|---|---|
|km 0+020|32.06|149.11|151.4|1.38|23.29|14.52|0.35|
|km 0+040|32.06|149.33|151.26|1.78|19.22|15.49|0.45|
|km 0+060|32.06|149.2|151.23|1.46|24.96|18|0.35|
|km 0+080|37.05|149.18|151.05|1.94|19.09|14.26|0.54|
|km 0+100|37.05|149.16|150.82|2.25|16.5|11.51|0.6|

**Fuente: Modelo hidráulico Estero Potrerillo de las Yeguas, HEC-RAS.**

Para obtener las condiciones de escurrimiento con las que se enfrenta el estero Sin Nombre,

se obtienen las alturas de agua con las que circula el Estero Potrerillo de las Yeguas en el

perfil Km 0+060, tal como se observa a continuación.

**Figura 4.8 Perfil Transversal Sección Empalme Estero Potrerillo de las Yeguas con Estero Sin nombre.**

**Fuente: Modelo hidráulico HEC-RAS.**

Con la información entregada, se tiene que el estero Sin Nombre está condicionado aguas

abajo en la cota 151.12.

#### 4.5 Modelación Estero Sin Nombre

**4.5.1** **Resultados Modelación Sin Proyecto**

25

El objetivo de la modelación es evaluar las condiciones hidráulicas en el Estero Sin Nombre

para una situación base, sin la construcción del entubamiento. En la Figura 4.9 se muestra

el modelo desarrollado en HEC-RAS para la condición sin proyecto, que incluye las

condiciones de borde mencionadas en inciso 4.3.

**Figura 4.9 Vista 3D de modelo hidráulico de Estero Sin Nombre para situación sin proyecto.**

**Fuente: Modelo hidráulico HEC-RAS.**

En la Figura 4.10 se muestra el eje hidráulico de los tramos de estudio del estero Sin

Nombre, para el caudal de diseño y el caudal de verificación, para la condición sin proyecto.

Es posible observar que no tiene grandes variaciones de pendiente en el tramo estudiado,

produciendo así que no existan alteraciones en el régimen de escurrimiento,

manteniéndose en régimen de río. En el gráfico se puede apreciar claramente la influencia

26

de la crecida del Estero Potrerillo de las Yeguas al final del trazado del Estero Sin Nombre,

en donde el agua se peralta por el hecho de la condición de escurrimiento del Estero

Potrerillo de las Yeguas.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||

**Figura 4.10 Eje Hidráulico Estero Sin Nombre, situación sin proyecto para caudal de diseño y Verificación.**
**Fuente: Modelo hidráulico HEC-RAS.**

Además, en la Tabla 4.11 se muestran los principales resultados de la simulación hidráulica

para el tramo en estudio del Estero Sin Nombre, para la situación sin proyecto y caudal de

diseño. La misma información, pero para la el caudal de verificación se presenta en la Tabla

4.12. Se entregan los valores del eje hidráulico, velocidad de escurrimiento, ancho

superficial, y número de Froude.

**Tabla 4.11 Resultados simulación hidráulica en situación sin proyecto de Estero Sin Nombre para caudal de**

|Col1|Col2|Col3|Diseño.|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Perfil**|**Caudal**|**Cota Fondo**|**Cota Pelo**<br>**de Agua**|**Velocidad**<br>**Media**|**Área**<br>**Mojada**|**Ancho**<br>**Superficial**|**Número de**<br>**Froude**|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|4.47|152.33|153.13|1.13|3.94|9.91|0.57|
|km 0+020|4.47|152.18|152.97|1.03|4.35|11.16|0.53|
|km 0+040|4.47|152.03|152.57|1.93|2.32|5.17|0.92|
|km 0+060|4.47|151.6|152.51|0.89|5.05|9.31|0.38|
|km 0+080|4.47|151.6|152.37|1.19|3.75|7.25|0.53|
|km 0+100|4.47|151.41|152.2|1.19|3.76|9.76|0.61|

27

|km 0+120|4.47|151.36|152.12|0.79|5.71|12.17|0.36|
|---|---|---|---|---|---|---|---|
|km 0+140|4.47|151.21|151.99|1.11|4.09|9.45|0.52|
|km 0+160|4.47|151.01|151.63|1.65|2.71|10.56|1.02|
|km 0+180|4.47|150.61|151.43|0.84|5.35|12.16|0.4|
|km 0+200|4.47|150.47|151.26|1.25|3.61|8.76|0.6|
|km 0+220|4.47|150.12|151.21|0.7|6.41|11.86|0.3|
|km 0+240|4.47|149.86|151.2|0.47|9.48|11.89|0.17|
|km 0+260|4.47|149.93|151.17|0.65|6.89|10.04|0.24|
|km 0+280|4.47|149.74|151.16|0.41|10.91|11.74|0.13|
|km 0+300|4.47|149.6|151.13|0.6|7.54|11.18|0.23|
|km 0+320|4.47|149.53|151.12|0.36|12.93|15|0.11|

**Fuente: Modelo hidráulico Estero Sin Nombre, HEC-RAS.**

**Tabla 4.12 Resultados simulación hidráulica en situación sin proyecto de Estero Sin Nombre para caudal de**

**Verificación.**

|Perfil|Caudal|Cota Fondo|Cota Pelo<br>de Agua|Velocidad<br>Media|Área<br>Mojada|Ancho<br>Superficial|Número de<br>Froude|
|---|---|---|---|---|---|---|---|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|4.49|152.33|153.13|1.14|3.95|9.92|0.58|
|km 0+020|4.49|152.18|152.97|1.03|4.36|11.16|0.53|
|km 0+040|4.49|152.03|152.57|1.93|2.32|5.18|0.92|
|km 0+060|4.49|151.6|152.52|0.89|5.07|9.33|0.38|
|km 0+080|4.49|151.6|152.38|1.2|3.76|7.26|0.53|
|km 0+100|4.49|151.41|152.2|1.19|3.78|9.79|0.61|
|km 0+120|4.49|151.36|152.12|0.79|5.73|12.18|0.36|
|km 0+140|4.49|151.21|151.99|1.11|4.1|9.45|0.52|
|km 0+160|4.49|151.01|151.63|1.66|2.72|10.57|1.02|
|km 0+180|4.49|150.61|151.43|0.83|5.4|12.2|0.4|
|km 0+200|4.49|150.47|151.27|1.21|3.75|8.87|0.57|
|km 0+220|4.49|150.12|151.23|0.67|6.68|12.08|0.29|
|km 0+240|4.49|149.86|151.22|0.46|9.76|12.03|0.16|
|km 0+260|4.49|149.93|151.19|0.63|7.17|10.77|0.23|
|km 0+280|4.49|149.74|151.18|0.4|11.23|11.86|0.13|
|km 0+300|4.49|149.6|151.16|0.57|7.88|11.57|0.22|
|km 0+320|4.49|149.53|151.15|0.35|13.38|15|0.11|

**Fuente: Modelo hidráulico Estero Sin Nombre, HEC-RAS.**

En la Figura 4.11 se muestra los valores de velocidad media del flujo para cada perfil. Al

existir una pendiente regular en el tramo de estudio, como resultado se obtienen

velocidades sin grandes cambios.

28

**Figura 4.11 Gráfico Velocidad de escurrimiento en Estero Sin Nombre, para la condición sin proyecto, para**
**caudal de diseño y Verificación.**

**Fuente: Elaboración propia.**

En la Figura 4.12 se muestra los valores del número de Froude en el Estero Sin Nombre para

cada perfil. Se concluye, que el tramo en estudio posee régimen de río en todo su trazado,

con excepción del perfil km 0+160 donde se llega a la condición de escurrimiento crítico, el

cual presente un aumento en la velocidad alcanzando velocidad crítica. Esto se origina por

pequeños cambios de pendiente entre un perfil y otro.

29

**Figura 4.12 Gráfico número de Froude en Estero Sin Nombre, para la condición sin proyecto, para de diseño y**
**Verificación.**

**Fuente: Elaboración propia.**

En el **Plano “Perfiles HEC-RAS Sin Proyecto”** adjunto en la presente entrega se presentan

los perfiles transversales de la modelación sin proyecto.

**4.5.2** **Resultados Modelación Con Proyecto**

Se realizó una simulación en el modelo que contempla por un lado la implementación de la

modificación de cauce y por otro lado el entubamiento del canal para el cruce del camino

por sobre esta obra hidráulica.

En la Figura 4.13 se muestra el modelo desarrollado en HEC-RAS que incluye las condiciones

de borde mencionadas en acápite 4.3.

30

**Figura 4.13 Vista 3D de modelo hidráulico de Estero Sin Nombre para condición con proyecto.**
**Fuente: Modelo hidráulico HEC-RAS.**

En este caso, se determina la capacidad de porteo de agua para el caso del caudal de diseño,

equivalente a 5.34 (m [3] /s). En la Figura 4.14 se muestra el eje hidráulico del tramo de estudio

del Estero Sin Nombre para el caudal de diseño y el caudal de verificación. En este caso con

proyecto pasa la misma situación de peralte del tirante hidráulico al final del Estero Sin

nombre, producto de la cota de inundación del Estero Potrerillo de las Yeguas. En este

contexto es importante comentar que este efecto no alcanza a intervenir en las obra del

puente o el desagüe de las aguas por parte del canal de desagüe proveniente de la planta

Crucero.

31

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Desague|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
||||||||||||||||||||
|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento|||||||
||||||||||||||||||||

**Figura 4.14 Eje Hidráulico Estero Sin Nombre, situación con proyecto para caudal de Diseño y Verificación.**

**Fuente: Modelo hidráulico HEC-RAS.**

Además en la figura a continuación se muestra la sección del entubamiento, y la carga

hidráulica de las tuberías proyectadas.

32

**Figura 4.15 Perfil Transversal Entubamiento Estero Sin Nombre, situación con proyecto para caudal de**

**Diseño.**

**Fuente: Modelo hidráulico HEC-RAS.**

Como se aprecia en el perfil de la figura 4.15, la cota del agua en la sección del

entubamiento, para el caso del caudal de diseño, es la 152.77 (m .s.n.m.), y la cota de

coronamiento de la clave superior de la tubería es la 153.1 (m .s.n.m.), es decir, hay una

altura libre de 0.31 (m), equivalente al 21% de la altura de la sección útil del entubamiento,

es decir, se respeta el diseño de utilizar como máximo el 80% de la altura (0,8*H).

En la Tabla 4.13 se muestran los principales resultados de la simulación hidráulica para el

tramo en estudio del Estero Sin Nombre, para la situación con proyecto. Se entregan los

valores del eje hidráulico, velocidad de escurrimiento, ancho superficial, y número de

Froude. Luego, en la Tabla 4.14, se entrega la misma información para el caudal de

verificación.

**Tabla 4.13 Resultados simulación hidráulica en situación con proyecto de Estero Sin Nombre para caudal de**

**diseño.**

|Perfil|Caudal|Cota<br>Fondo|Cota Pelo<br>de Agua|Velocidad<br>Media|Área<br>Mojada|Ancho<br>Superficial|Número de<br>Froude|
|---|---|---|---|---|---|---|---|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|<br>**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|4.47|152.33|153.13|1.14|3.91|9.88|0.58|

33

|km 0+020|4.47|152.18|152.95|1.07|4.16|10.93|0.56|
|---|---|---|---|---|---|---|---|
|km 0+040|4.47|152.03|152.72|1.43|3.13|5.46|0.6|
|km 0+060|4.47|151.6|152.71|0.62|7.2|12.09|0.25|
|km 0+070|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|
|km 0+080|4.47|151.6|152.37|1.19|3.75|7.25|0.53|
|km 0+100|4.47|151.41|152.2|1.19|3.76|9.76|0.61|
|km 0+120|4.47|151.36|152.12|0.79|5.71|12.17|0.36|
|km 0+140|4.47|151.21|151.99|1.11|4.09|9.45|0.52|
|km 0+160|4.47|151.01|151.63|1.65|2.71|10.56|1.02|
|km 0+180|4.47|150.61|151.43|0.83|5.41|12.21|0.39|
|km 0+200|4.47|150.47|151.28|1.18|3.82|8.92|0.56|
|km 0+220|4.47|150.12|151.24|0.66|6.82|12.28|0.28|
|km 0+240|5.34|149.86|151.23|0.54|9.82|12.08|0.19|
|km 0+260|5.34|149.93|151.18|0.76|7.08|10.55|0.28|
|km 0+280|5.34|149.74|151.17|0.49|11.08|11.81|0.16|
|km 0+300|5.34|149.6|151.13|0.71|7.58|11.21|0.27|
|km 0+320|5.34|149.53|151.12|0.44|12.93|15|0.13|

**Fuente: Modelo hidráulico Estero Sin Nombre, HEC-RAS.**

**Tabla 4.14 Resultados simulación hidráulica en situación con proyecto de Estero Sin Nombre para caudal de**

**verificación.**

|Perfil|Caudal|Cota Fondo|Cota Pelo<br>de Agua|Velocidad<br>Media|Área<br>Mojada|Ancho<br>Superficial|Número de<br>Froude|
|---|---|---|---|---|---|---|---|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|4.99|152.33|153.16|1.17|4.25|10.28|0.58|
|km 0+020|4.99|152.18|153|1.06|4.69|11.47|0.53|
|km 0+040|4.99|152.03|152.78|1.44|3.48|5.58|0.58|
|km 0+060|4.99|151.6|152.79|0.62|8.1|13.18|0.24|
|km 0+070|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|Entubamiento Puente|
|km 0+080|4.99|151.6|152.41|1.24|4.01|7.36|0.54|
|km 0+100|4.99|151.41|152.23|1.21|4.11|10.51|0.62|
|km 0+120|4.99|151.36|152.15|0.83|6.11|12.41|0.37|
|km 0+140|4.99|151.21|152.01|1.17|4.34|9.55|0.54|
|km 0+160|4.99|151.01|151.65|1.7|2.95|10.86|1.01|
|km 0+180|4.99|150.61|151.47|0.85|5.86|12.6|0.39|
|km 0+200|4.99|150.47|151.32|1.21|4.18|9.2|0.55|
|km 0+220|4.99|150.12|151.29|0.68|7.36|12.99|0.28|
|km 0+240|5.96|149.86|151.27|0.58|10.33|12.45|0.2|
|km 0+260|5.96|149.93|151.22|0.81|7.49|11.58|0.29|
|km 0+280|5.96|149.74|151.21|0.52|11.51|12.03|0.17|
|km 0+300|5.96|149.6|151.16|0.76|7.93|11.63|0.29|
|km 0+320|5.96|149.53|151.15|0.47|13.38|15|0.14|

**Fuente: Modelo hidráulico Estero Sin Nombre, HEC-RAS.**

34

En la Figura 4.16 se muestra los valores de velocidad media del flujo en el Estero Sin Nombre

para cada perfil. Tal como se produce en los dos casos modelados anteriormente, no hay

grandes variaciones de velocidades, asociados a pocos cambios de pendientes.

|Col1|Col2|
|---|---|
||Desague|
|||

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|Vdiseño<br>Vverificación<br>Entubamiento|Vdiseño<br>Vverificación<br>Entubamiento|Vdiseño<br>Vverificación<br>Entubamiento||

**Figura 4.16 Gráfico Velocidad de escurrimiento en Estero Sin Nombre, para la condición con proyecto para**
**caudal de diseño y verificación.**
**Fuente: Elaboración propia.**

Un reflejo del comportamiento homogéneo en el tramo de estudio es el número de Froude

que se mantiene en régimen de río para una condición con proyecto en todo el tramo de

estudio. Por otro lado se puede observar que las dos singularidades modeladas para esta

condición con proyecto, entubamiento y desagüe, no provocan un cambio en el régimen de

escurrimiento del estero.

35

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||Entubamiento||
|||||

**Figura 4.17 Gráfico número de Froude en Estero Sin Nombre, para la condición con proyecto para caudal de**
**diseño y verificación.**
**Fuente: Elaboración propia.**

#### 4.6 Modelación Canal de Desagüe de Aguas Lluvia

Como se menciona anteriormente, para la situación con proyecto se modela el canal de

desagüe de aguas lluvia. Este desagüe también existe para una condición sin proyecto, pero

el área aportante menor, y con coeficientes de escorrentía menores, por lo que el canal era

muy pequeño, en donde escurría agua superficialmente en muy pocas ocasiones.

Con la entrada en operación se agranda el sistema de drenaje natural, de manera de

conducir las descargas de aguas lluvia de manera eficiente y segura desde el punto de vista

hidráulico, lo anterior para evitar apozamiento en la zona de la planta.

36

En la tabla a continuación se muestran los resultados obtenidos para 100 y 200 años período

de retorno.

|Tabla 4.15 Resultados simulación hidráulica en situación con proyecto, Canal Desagüe, para caudal de diseño y verificación.|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|**Caudal Diseño (Q100)**|
|**Perfil**|**Caudal**|**Cota Fondo**|**Cota Pelo**<br>**de Agua**|**Velocidad**<br>**Media**|**Área**<br>**Mojada**|**Ancho**<br>**Superficial**|**Número**<br>**de Froude**|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|0.87|151.97|152.54|0.65|1.38|4.29|0.33|
|km 0+020|0.87|151.89|152.48|0.64|1.6|4.87|0.29|
|km 0+040|0.87|151.86|152.37|0.95|0.99|4.57|0.54|
|km 0+060|0.87|151.72|152.26|0.75|1.24|4.25|0.4|
|km 0+080|0.87|151.6|151.96|1.51|0.57|2.49|1.01|
|km 0+100|0.87|150.28|151.23|0.54|1.74|3.54|0.21|
|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|**Caudal Verificación (Q200)**|
|**Perfil**|**Caudal**|**Cota Fondo**|**Cota Pelo**<br>**de Agua**|**Velocidad**<br>**Media**|**Área**<br>**Mojada**|**Ancho**<br>**Superficial**|**Número**<br>**de Froude**|
|**Perfil**|**[m3/s]**|**[m.s.n.m.]**|**[m.s.n.m.]**|**[m/s]**|**[m2]**|**[m]**|**[m]**|
|km 0+000|0.97|151.97|152.56|0.68|1.48|4.48|0.34|
|km 0+020|0.97|151.89|152.51|0.67|1.71|4.95|0.3|
|km 0+040|0.97|151.86|152.39|0.98|1.09|4.69|0.54|
|km 0+060|0.97|151.72|152.28|0.78|1.33|4.36|0.4|
|km 0+080|0.97|151.6|151.98|1.55|0.62|2.65|1|
|km 0+100|0.97|150.28|151.27|0.56|1.89|3.56|0.21|

**Fuente: Modelo hidráulico Estero Sin Nombre, HEC-RAS.**

A simple vista se puede ver que el canal de desagüe, al tener baja pendiente, circula el agua

a una velocidad muy baja. Todo el tramo tiene una velocidad sub crítica, y solo en el perfil

km 0+080 alcanza la velocidad crítica.

En el **Plano “Perfiles HEC-RAS Con Proyecto”** adjunto en la presente entrega se presentan

los perfiles transversales de la modelación sin proyecto.

#### 4.7 Análisis Comparativo

37

Luego de analizar los resultados para las situaciones sin y con proyecto obtenidas con ayuda

del modelo hidráulico en HEC-RAS, es posible compararlas con el fin de determinar si existe

o no algún impacto en la entrada en operación del entubamiento. Antes de mostrar los

resultados, es importante hacer un análisis previo de las condiciones fluviométricas en cada

caso.

La modificación de cauce en estudio, es una solución muy utilizada para la construcción de

entubamientos para el flujo vehicular, la cual cuenta con buenos resultados operacionales.

Por otro lado, es importante comentar que el entubamiento cuenta con dos grandes

secciones de tubería de 1.5 metros de diámetro cada una, con material estructurante

debidamente compactado que le da firmeza a la solución implementada y además sujeción

al rodado para la circulación de vehículos sobre él. El hecho de tener secciones circularess

amplias ayuda para el caso de crecidas, en donde los lechos portan gran cantidad de sólidos,

pudiendo pasar sin problema a través del entubamiento, sin producir atascos, y por ende

un deterioro de la estructura y/o socavaciones.

En la Figura 4.18 se muestra el eje hidráulico del tramo en estudio del Estero Sin Nombre,

para el caudal de diseño, para la condición sin proyecto y la condición con proyecto. El largo

de ambos tramos es el mismo, por lo que no hay problemas compatibilidad en los perfiles.

38

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||Desague|Desague|Desague|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||Entubamiento|Entubamiento|Entubamiento|Entubamiento|Entubamiento||||||||||||
|||||||||||||||||||

**Figura 4.18** **Eje Hidráulico Estero Sin Nombre, Situaciones sin y con proyecto con operación para caudal de**

**diseño.**

**Fuente: Modelo hidráulico Estero Sin Nombre, HEC-RAS.**

Como se puede ver, para la instalación de las tuberías de entubamiento de 1500 (mm) de

diámetro, se hizo una pequeña profundización del cauce. Este cambio, sumado a la

singularidad misma del entubamiento provoca una pequeña influencia aguas arriba. Igual

así, la influencia es poco significativa, debido a que la sección es la sección del entubamiento

es suficientemente grande para dejar pasar el caudal de diseño. Distinto sería en el caso

que la sección del entubamiento sea menor, lo que causaría un peralte de agua en la sección

aguas arriba de la estructura debido a que el flujo es del tipo súper crítico (río).

Por otro lado se ve que la entrada en operación del canal de desagüe, aumenta el caudal al

interior de la caja del río. En estricto rigor, este aumento también existe para el caso sin

proyecto, solo que en una proporción un poco menor, debido a que parte del agua lluvia

que cae sobre la planta es infiltrada por el suelo, y el resto escurre por la misma parte por

39

donde se modela para la situación con proyecto, pero para hacer lo más conservador

posible, la situación sin proyecto se modela sin el aporte superficial de aguas por parte del

área aportante entre el entubamiento y el encuentro con el Estero Potrerillo de las Yeguas.

Como se menciona en el párrafo anterior, si bien hay un pequeño aumento en la cota del

eje hidráulico del estero sin nombre, esta no es significativa como para tener una influencia

significativa sobre el estero Potrerillo de las Yeguas, corroborando así el hecho de no

considerar como área de influencia este estero. Esto se ve en el eje hidráulico, en donde el

tirante hidráulico del Estero Sin nombre se peralta, pero no lo suficiente como para afectar

las obras en estudio.

La Figura 4.19 y Figura 4.20 muestran la comparación de velocidad media y número de

Froude respectivamente para las situaciones sin y con proyecto para el Estero Sin Nombre.

40

**Figura 4.19 Gráfico de comparación de velocidad de escurrimiento en Estero Sin Nombre, para situaciones**
**sin y con proyecto, para caudal de diseño.**
**Fuente: Elaboración propia.**

Respecto a las velocidades, los cambios de velocidad son poco significativos. Por un lado la

construcción del entubamiento significa una disminución de la velocidad de conducción en

la sección agua arriba. Esto se debe principalmente por el hecho de sobre excavar el lecho

del estero para la instalación de los tubos, provocando así una pequeña zona de

apozamiento en la sección agua arriba, lo que se acentúa por el hecho de contar con un

escurrimiento del tipo sub crítico.

Por otro lado, el desagüe tampoco provoca un cambio significativo en la velocidad de

escurrimiento del cauce, dejando casi sin cambio el hecho de portar un caudal mayor. Esto

último se debe principalmente a la baja pendiente del cauce en la zona de estudio.

Por último se compara el número de Froude para ambas condiciones de modelación,

resultados que se muestran en la siguiente figura.

41

|Col1|Col2|Col3|
|---|---|---|
||||
||||
|Entubamiento|Entubamiento||

**Figura 4.20** **Gráfico de comparación de número de Froude en Estero Sin Nombre, para situaciones sin y con**
**proyecto, para caudal de diseño.**
**Fuente: Elaboración propia.**

Los resultados de los números de Froude obtenidos, comprueban que no hay cambio de

régimen para la condición sin y con proyecto. Si bien hay pequeños cambios de velocidad

localmente, no son lo suficientemente significativos como para cambiar el régimen de

escurrimiento para el caso del caudal de diseño. Por otro lado en todos los modelos, la

condición de borde aguas abajo hace que el flujo se acelere en cierto sentido, llegando a la

condición crítica de escurrimiento.

42

### 5. SOCAVACIÓN LOCAL

La socavación es un fenómeno producido por un desequilibrio localizado entre la tasa a la

cual el sedimento es arrastrado por la corriente fuera de una determinada zona del lecho y

la tasa de sedimento alimentada hacia ella. Este desequilibrio de genera por la

concentración del flujo asociado a la presencia de un obstáculo o estructura implantada en

un lecho fluvial. El resultado es una profundización local del lecho, bajo la forma de una fosa

o cavidad en el entorno de la estructura, que se desarrolla durante un cierto tiempo hasta

que se restituye el equilibrio entre la tasa de entrada y de salida de sedimento a la fosa.

El proceso tiende a alcanzar una condición de régimen o de estabilización. Es esta condición

la que interesa principalmente cuantificar desde un punto de vista ingenieril. La fosa de

socavación que caracteriza la condición de régimen puede llegar a afectar la estabilidad de

estructuras y por lo tanto, se hace necesario predecirla como parte del diseño.

Para el caso en estudio, corresponde a la instalación de dos tuberías de HDPE de 1500 (mm)

de diámetro cada una, cuya salida está dispuesta a la cota de terreno en la ribera del estero

sin nombre. Dadas las condiciones de diseño, es necesario realizar un análisis de socavación

local, tal como se especifica en el Volumen 3 del Manual de Carreteras, capítulo

3.707.404.(3), “Socavación al Pie de Alcantarillas y Ductos de Descarga de Sección Circular”.

También se estudia la posibilidad de socavación local en el sector donde el canal de desague

de aguas lluvia intersecta al estero sin nombre. Para este caso se utiliza la misma

metodología, considerando que la esto se realiza con una tubería de diámetro similar al del

canal.

El fenómeno de socavación ocurre cuando un ducto desagua sobre un lecho móvil

erosionable, tal como se esquematiza en la Figura 5.1.

43

**Figura 5.1 Socavación local al pie de una descarga.**

**Fuente: Manual De Carreteras V3**

#### 5.1 Dimensiones Socavación

La socavación máxima dentro de la fosa se puede estimar a partir de la siguiente fórmula

genérica:

S
d [= AQ] d [y][x]

σ z
g

w [+ B]
D
50

Donde:

S: Socavación (m)
d: Diámetro del ducto (m)
Q: Caudal total descargado (m [3] /s)
σ g : Desviación estándar de sedimento del lecho erosionable (-)
D 50 : Diámetro 50% que pasa (mm)
A, B, X, y, z, w: Parámetros definidos en la Tabla 3.707.404.F del volumen 3 del Manual de
Carreteras.

44

**5.1.1** **Dimensiones en Planta de la Fosa de Socavación**

Para caracterizar la longitud y ancho de la fosa de socavación se recomienda emplear las

siguientes fórmulas desarrolladas por Abt et al., las cuales se muestran a continuación.

L s
d [= 9.3 Q] d [1.45][0.58]

B s
d [= 4.1 Q] d [1.65][0.66]

Donde:

L s : Largo de la fosa de socavación (m)
B s : Ancho de la fosa de socavación (m)
d: Diámetro del ducto (m)
Q: Caudal total descargado (m [3] /s)

#### 5.2 Resultados de Socavación Local

Se estimó la profundidad y dimensiones de la fosa de socavación al pie de la descarga

utilizando la metodología propuesta en este capítulo. Los valores utilizados se muestran a

continuación en la Tabla 5.1.

<!-- INICIO TABLA 5.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- utilizando la metodología propuesta en este capítulo. Los valores utilizados se muestran a continuación en la Tabla 5.1. -->

**Tabla 5.1: Valores utilizados para el análisis de socavación local para cada Quebrada****

| Col1 | Estero Sin Nombre |
| --- | --- |
|  | **Sector Entubamiento**<br>**Sector Canal de Desagüe** |
| Caudal Total [m3/s]<br>Número de Ductos<br>Caudal por Ducto (m3/s)<br>d [m]<br>D50[mm]<br>D84[mm] | 4.47<br>0.87<br>2 <br>1 <br>2.24<br>0.87<br>1.5<br>1.2<br>17<br>17<br>82<br>82 |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 45 D 16 [mm] 6 6 -->
<!-- FIN TABLA 5.1 -->


**Tabla 5.1 Valores utilizados para el análisis de socavación local para cada Quebrada**

|Col1|Estero Sin Nombre|
|---|---|
||**Sector Entubamiento**<br>**Sector Canal de Desagüe**|
|Caudal Total [m3/s]<br>Número de Ductos<br>Caudal por Ducto (m3/s)<br>d [m]<br>D50[mm]<br>D84[mm]|4.47<br>0.87<br>2 <br>1 <br>2.24<br>0.87<br>1.5<br>1.2<br>17<br>17<br>82<br>82|

45

D 16 [mm] 6 6

### σ g 3.70 3.70

**Fuente: Elaboración Propia.**

En la Tabla 5.2 se muestra distintos parámetros calibrados para este problema, expuestos

en el Manual de Carreteras - Volumen 3 para estimar la profundidad de la fosa de

socavación, y en la tabla 5.3 se muestran los resultados de la socavación obtenida para cada

metodología, en donde se toma el promedio de todos.

**Tabla 5.2 Parámetros utilizados en el cálculo y valores obtenidos de profundidad de socavación local.**

**BREUSERS**

**PARÁMETRO** **BOHAN**

**Y**

**RAUDKIVI**

**ABT** **RUFF**

**Fuente: Elaboración Propia.**

**Tabla 5.3 Valores obtenidos de profundidad de socavación local.**

|Col1|Breusers y<br>Bohan Abt Ruff Socavación<br>Raudkivi<br>Promedio|
|---|---|
|**Sector Entubamiento**<br>**Sector Canal de**<br>**Desagüe**|0.67<br>0.01<br>0.56<br>0.84<br>**0.52**<br>0.46<br>0.00<br>0.35<br>0.57<br>**0.35**|

**Fuente: Elaboración Propia.**

Los valores para la profundidad de socavación local promedio varían desde 0.01 [m] hasta

0.84 [m] para el caso del entubamiento del estero, y 0 [m] hasta 0.57 [m] para el caso del

encuentro del canal de desagüe al estero sin nombre.

46

Luego en la Tabla 5.4 se muestra las estimaciones para largo y ancho de la fosa de

socavación.

**Tabla 5.4 Valores obtenidos para longitud y ancho de la fosa de socavación local.**

|Col1|Estero Sin Nombre<br>Sector Entubamiento Sector Canal de Desagüe|
|---|---|
|**Largo Socavación (m)**<br>**Ancho Socavación (m)**|3.71<br>2.37<br>1.6<br>1.0|

**Fuente: Elaboración Propia.**

Si bien los resultados pueden parecer que no se requiera de una protección al lecho del río,

esto va a depender del criterio que se tome, por lo que sería necesario de revisar la

necesidad o no de proteger el lecho del estero sin nombre en estas dos singularidades.

47

### 6. CÁLCULO DE ENROCADO DE PROTECCIÓN

El enrocado se diseña tanto para el talud de fondo, que es donde golpea el agua al salir de

los ductos.

**6.1** **TALUDES DE FONDO**

Existen dos enfoques para abordar este análisis, el teórico y el práctico. El primero consta

de un equilibrio de fuerzas sobre un elemento del enrocado, como se muestra en la figura.

**Figura 6.1 Diagrama de cuerpo libre de un elemento del enrocado.**

**Fuente: Elaboración Propia.**

Donde:
Ws: Peso de la roca [Kg]
Fr: Fuerza de roce [N]
N: Fuerza Normal [N]
Fa: Fuerza de Arrastre [N]

48

Luego de reemplazar términos se llega a una relación entre la velocidad del flujo y el

diámetro equivalente del enrocado:

u [2] = [4]
3

RgD

C d

(μcos α−sin α)

Donde,
u: Velocidad del flujo [m/s]
R: (Peso esp. del sólido - Peso esp. del agua)/ P esp. del agua [-]
D: Diámetro equivalente del enrocado [m]
C d : Coeficiente de arrastre [-]
 Coeficiente de fricción [-]

Trabajando la expresión anterior, obtenemos una resolución en función del número de

Froude. Hay que tener en cuenta que se utiliza un coeficiente de fricción igual a 0,4.

(Régimen turbulento).

D
2
H [= 0.188F] [r]

Donde,

D: Diámetro equivalente del enrocado [m]
H: Carga hidráulica [m]
Fr: Número de Froude [-]

Por otro lado, se han desarrollado otras relaciones a partir de datos experimentales, las más

importantes se muestran a continuación:

 - **Maza & García:**

H
D [= [1.93] F r

~~]~~

2.86

49

Esta relación es válida para el rango de 0.4 a 10 metros de profundidad de agua y hasta 500

mm de diámetro equivalente de las partículas. Generalmente se ocupa para números de

Froude entre 1.35 y 1.6.

 - **Straub**

H
D [= 6.97] F 3

3

F r

- **Neill**

- **Isbash**

H
D [= 5.99] F r3

H
D [= 2.88Rcos α] F r [2]

En la Tabla 6.1 se presentan los valores utilizados y en la Tabla 9.2 los resultados obtenidos

para las distintas metodologías, para cada una de los sectores del estero sin nombre.

**Tabla 6.1 Parámetros Hidráulicos para calcular Socavación Local.**

**Estero Sin Nombre**

**Sector Entubamiento** **Sector Canal de Desagüe**

50

γ [N/m [3] ] 9800 9800

γ s [N/m [3] ] 25970 25970

R 1.65 1.65

**Fuente: Elaboración Propia.**

Los valores de profundidad del flujo (H), número de Froude (F r ) y pendiente longitudinal (α)

fueron obtenidos de los resultados de la modelación hidráulica en el perfil km 0+060 y en

el perfil km 0+240, para el caso del entubamiento y el canal de desagüe respectivamente,

seleccionando la situación con proyecto, para el periodo de retorno de 100 años por ser la

más conservadora. Para el peso específico de los sólidos, se escogió un valor conservador

dentro del rango habitual.

**Tabla 6.2 Resultados Socavación Local por Quebrada.**

|Método|Diámetro Equivalente (mm) (Estero Sin Nombre)|
|---|---|
|**Método**|**Sector Entubamiento**<br>**Sector Canal de Desagüe**|
|**Teórico**<br>**Maza & García**<br>**Straub**<br>**Neill**<br>**Ibash**|0.025<br>0.017<br>0.009<br>0.004<br>0.007<br>0.004<br>0.008<br>0.004<br>**0.028**<br>**0.030**|

**Fuente: Elaboración Propia.**

Como se aprecia en la tabla 6.2, la metodología que obtiene mayor diámetro de roca es el

de Isbash. Igual así, los diámetros equivalentes necesario para evitar socavación, son

pequeños con respecto a la misma granulometría de los lechos que conforman el estero sin

nombre. Por lo anterior se concluye que no es necesario hacer un enrocado de protección

en las dos secciones de estudio.

Si perjuicio de lo anterior, se estima conveniente continuar con una inspección visual del

lecho del estero en las zonas intervenidas, durante el tiempo de operación de estas. Lo

anterior con el fin de limpiarlas en el caso de ser necesario, para así no comprometer su

correcto funcionamiento, o para ver cualquier evidencia de socavación local o general en el

tramo afectado por las alcantarillas, evitando así consecuencias mayores en el caso de la

presencia de alguna particularidad.

51

### 7. CONCLUSIÓN

Las condiciones hidrológicas con las que se comprueba el diseño del entubamiento

proyectado sobre el estero Sin Nombre son para caudales de diseño, asociado a una crecida

de 100 años período de retorno, y se verifica para una crecida de 200 años. Los resultados

obtenidos del estudio hidrológico son dispares según los métodos de cálculo utilizados, por

lo anterior se decide utilizar caudales de crecidas conservadores, de manera de tener

factores de seguridad en el diseño del entubamiento.

Realizada la modelación del Estero Sin Nombre en la zona donde se emplaza el proyecto del

entubamiento y el desagüe de agua lluvia por parte del área aportante de la planta Crucero.

Con esta modelación se puede concluir que la entrada en operación de esta obra, no tiene

efectos significativos sobre el lecho del Estero Sin Nombre, desde el punto de vista de las

condiciones fluviométricas, y morfológicas del estero. Lo anterior se explica a que el

entubamiento proyectado cuenta con una sección útil lo suficientemente grande para

permitir el paso del caudal de diseño, considerando un área mojada disponible para portar

agua de 3.53 m2, dividida en dos secciones de 1.77 m2 c/u.

Se concluye también que el área de influencia de todo lo que involucra el proyecto de

ampliación de la planta crucero, no abarca el Estero Potrerillo de las Yeguas, lo anterior a

que las condiciones de escurrimiento para una condición sin y con proyecto son muy

similares. Por otro lado las velocidades de escurrimiento en el estero sin nombre son muy

bajas en todo el tramo de estudio, por lo que su impacto sobre el lecho natural del estero

es nulo en cuanto al potencial de socavación general o local según sea el caso.

52

Según lo revisado en terreno y en la cartografía, el área aportante del estero Sin Nombre se

encuentra altamente intervenida con caminos, entubamientos, siendo muy susceptible a la

presencia de basura y escombros. Estos pueden ser arrastrados por el caudal en un evento

de crecidas, pudiendo producir un estancamiento en la sección del entubamiento. El diseño

contempla la instalación de prefabricados de hormigón de gran sección que facilita el paso

de elementos que pueda portar el canal.

Según los resultados de enrocados requeridos para proteger el lecho del estero para, se

concluye que los diámetros equivalentes necesario para evitar socavación son pequeños

con respecto a la misma granulometría de los lechos que conforman el estero sin nombre,

no haciendo necesario implementar una protección del lecho del estero en las dos

secciones de estudio.

Sin perjuicio de lo anterior, se estima conveniente continuar con una inspección visual del

lecho del estero en las zonas intervenidas, durante el tiempo de operación de estas. Lo

anterior con el fin de limpiarlas en el caso de ser necesario, para así no comprometer su

correcto funcionamiento, o para ver cualquier evidencia de socavación local o general en el

tramo afectado por las alcantarillas, evitando así consecuencias mayores en el caso de la

presencia de alguna particularidad.

Por último recomendar al titular del proyecto crear una condición de escurrimiento más segura para

el caso del Estero Sin nombre en todo el tramo donde se emplaza la planta. Si bien la condición

natural del estero es capaz de portar el caudal de diseño, este lo hace naturalmente con un peralte

muy pequeño. Ante algún evento de precipitación extrema, fuera de los análisis comunes de un

estudio hidrológico, o producto de un atasco en el mismo canal, esto puede provocar un desborde

de agua en esta sección y causar algún daño a las instalaciones de la planta y en consecuencia alterar

la calidad de las aguas.

Para lograr una condición segura, se puede hacer un pretil de seguridad de 0,5 metros de alto,

realizado con material natural compactado debidamente, con pendiente del talud de 1:2 (H:V). Esto

no se tiene que hacer fuera del cauce del mismo canal, de manera que no comprenda una defensa

fluvial propiamente tal, ya que no interviene el lecho natural del estero.

53

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.2: Determinación del coeficiente de rugosidad de Manning por método de Cowan, Canal de Desagüe.****

| Descripción Coeficiente | Col2 | Cauce | Col4 | Ribera | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Descripción Coeficiente** | **Descripción Coeficiente** | **Justificación** | **Valor** | **Justificació**<br>**n ** | **Valor** |
| **n**<br>**0 ** | Material | Tierra | 0.020 | Tierra | 0.02 |
| **n**<br>**1 ** | Grado de Irregularidad Perímetro<br>Mojado | Moderado | 0.005 | Moderado | 0.005 |
| **n**<br>**2 ** | Variaciones de las Secciones | Moderado | 0.003 | Moderado | 0.003 |
| **n**<br>**3 ** | Efecto Relativo de las Obstrucciones | Leve | 0.012 | Leve | 0.012 |

**Tabla 4.3: Determinación del coeficiente de rugosidad de Manning por método de Cowan, Estero Potrerillo de****

| Descripción Coeficiente | Col2 | Cauce | Col4 | Ribera | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Descripción Coeficiente** | **Descripción Coeficiente** | **Justificación** | **Valor** | **Justificación** | **Valor** |
| **n0** | Material | Tierra | 0.020 | Tierra | 0.02 |
| **n1** | Grado de Irregularidad Perímetro Mojado | Moderado | 0.005 | Moderado | 0.005 |
| **n2** | Variaciones de las Secciones | Moderado | 0.003 | Moderado | 0.003 |
| **n3** | Efecto Relativo de las Obstrucciones | Leve | 0.012 | Leve | 0.012 |
| **n4** | Densidad de Vegetación | baja | 0.005 | Alta | 0.02 |
| **m ** | Sinuosidad y Frecuencia de Meandros | Leve | 1.1 | Media | 1.1 |
| **n ** | **Rugosidad de Manning Río Pitreño** | **Manning** | **0.050** | **Manning** | **0.066** |

**Tabla 4.4: Resumen de condiciones de contorno calibradas para la modelación hidráulica de Estero Sin****

| Variables | Descripción |
| --- | --- |
| Geometría | Levantamiento realizado en la zona de estudio. |
| Coeficiente de<br>Rugosidad de Manning | Cauce principal: n = 0.045<br>Planicies de inundación: n = 0.052 |
| Tipo de Modelación | Flujo Permanente en Escurrimiento Mixto |
| Condición de Borde<br>Aguas Arriba y Abajo | Estero Sin Nombre: Pendiente fondo A. Arriba 0.9 [%]<br>Estero Sin Nombre: Unión con Estero Potrerillo de las<br>Yeguas |

**Tabla 4.5: Resumen de condiciones de contorno calibradas para la modelación hidráulica del Canal de****

| Variables | Descripción |
| --- | --- |
| Geometría | Levantamiento realizado en la zona de estudio. |
| Coeficiente de<br>Rugosidad de Manning | Cauce principal: n = 0.045<br>Planicies de inundación: n = 0.045 |
| Tipo de Modelación | Flujo Permanente en Escurrimiento Mixto |

**Tabla 4.6: Resumen de condiciones de contorno calibradas para la modelación hidráulica del Estero Potrerillo****

| Variables | Descripción |
| --- | --- |
| Geometría | Levantamiento realizado en la zona de estudio. |
| Coeficiente de<br>Rugosidad de Manning | Cauce principal: n = 0.05<br>Planicies de inundación: n = 0.066 |
| Tipo de Modelación | Flujo Permanente en Escurrimiento Mixto |
| Condición de Borde<br>Aguas Arriba y Abajo | Estero Sin Nombre: Pendiente fondo A. Arriba 0.92 [%]<br>Estero Sin Nombre: Pendiente fondo A. Abajo 0.92 [%] |

**Tabla 4.9: Resultados simulación hidráulica Estero Potrerillo de las Yeguas para caudal de Diseño.****

| Perfil | Caudal | Cota<br>Fondo | Cota Pelo<br>de Agua | Velocidad<br>Media | Área<br>Mojada | Ancho<br>Superficial | Número<br>de Froude |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **[m3/s]** | **[m.s.n.m.]** | **[m.s.n.m.]** | **[m/s]** | **[m2]** | **[m]** | **[m]** |
| km 0+000 | 27.68 | 149.23 | 151.26 | 2.14 | 13.85 | 11.37 | 0.56 |
| km 0+020 | 27.68 | 149.11 | 151.27 | 1.29 | 21.52 | 14.09 | 0.33 |
| km 0+040 | 27.68 | 149.33 | 151.14 | 1.67 | 17.49 | 14.88 | 0.44 |
| km 0+060 | 27.68 | 149.2 | 151.12 | 1.36 | 22.97 | 17.14 | 0.33 |
| km 0+080 | 33.02 | 149.18 | 150.93 | 1.89 | 17.48 | 13.82 | 0.54 |
| km 0+100 | 33.02 | 149.16 | 150.71 | 2.16 | 15.28 | 11.39 | 0.6 |

**Tabla 4.10: Resultados simulación hidráulica Estero Potrerillo de las Yeguas para caudal de Verificación.****

| km 0+000 | 32.06 | 149.23 | 151.38 | 2.27 | 15.23 | 12.08 | 0.58 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| km 0+020 | 32.06 | 149.11 | 151.4 | 1.38 | 23.29 | 14.52 | 0.35 |
| km 0+040 | 32.06 | 149.33 | 151.26 | 1.78 | 19.22 | 15.49 | 0.45 |
| km 0+060 | 32.06 | 149.2 | 151.23 | 1.46 | 24.96 | 18 | 0.35 |
| km 0+080 | 37.05 | 149.18 | 151.05 | 1.94 | 19.09 | 14.26 | 0.54 |
| km 0+100 | 37.05 | 149.16 | 150.82 | 2.25 | 16.5 | 11.51 | 0.6 |

**Tabla 4.11: Resultados simulación hidráulica en situación sin proyecto de Estero Sin Nombre para caudal de****

| Col1 | Col2 | Col3 | Diseño. | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **Caudal** | **Cota Fondo** | **Cota Pelo**<br>**de Agua** | **Velocidad**<br>**Media** | **Área**<br>**Mojada** | **Ancho**<br>**Superficial** | **Número de**<br>**Froude** |
| **Perfil** | **[m3/s]** | **[m.s.n.m.]** | **[m.s.n.m.]** | **[m/s]** | **[m2]** | **[m]** | **[m]** |
| km 0+000 | 4.47 | 152.33 | 153.13 | 1.13 | 3.94 | 9.91 | 0.57 |
| km 0+020 | 4.47 | 152.18 | 152.97 | 1.03 | 4.35 | 11.16 | 0.53 |
| km 0+040 | 4.47 | 152.03 | 152.57 | 1.93 | 2.32 | 5.17 | 0.92 |
| km 0+060 | 4.47 | 151.6 | 152.51 | 0.89 | 5.05 | 9.31 | 0.38 |
| km 0+080 | 4.47 | 151.6 | 152.37 | 1.19 | 3.75 | 7.25 | 0.53 |
| km 0+100 | 4.47 | 151.41 | 152.2 | 1.19 | 3.76 | 9.76 | 0.61 |

**Tabla 4.12: Resultados simulación hidráulica en situación sin proyecto de Estero Sin Nombre para caudal de****

| Perfil | Caudal | Cota Fondo | Cota Pelo<br>de Agua | Velocidad<br>Media | Área<br>Mojada | Ancho<br>Superficial | Número de<br>Froude |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **[m3/s]** | **[m.s.n.m.]** | **[m.s.n.m.]** | **[m/s]** | **[m2]** | **[m]** | **[m]** |
| km 0+000 | 4.49 | 152.33 | 153.13 | 1.14 | 3.95 | 9.92 | 0.58 |
| km 0+020 | 4.49 | 152.18 | 152.97 | 1.03 | 4.36 | 11.16 | 0.53 |
| km 0+040 | 4.49 | 152.03 | 152.57 | 1.93 | 2.32 | 5.18 | 0.92 |
| km 0+060 | 4.49 | 151.6 | 152.52 | 0.89 | 5.07 | 9.33 | 0.38 |
| km 0+080 | 4.49 | 151.6 | 152.38 | 1.2 | 3.76 | 7.26 | 0.53 |
| km 0+100 | 4.49 | 151.41 | 152.2 | 1.19 | 3.78 | 9.79 | 0.61 |
| km 0+120 | 4.49 | 151.36 | 152.12 | 0.79 | 5.73 | 12.18 | 0.36 |
| km 0+140 | 4.49 | 151.21 | 151.99 | 1.11 | 4.1 | 9.45 | 0.52 |
| km 0+160 | 4.49 | 151.01 | 151.63 | 1.66 | 2.72 | 10.57 | 1.02 |
| km 0+180 | 4.49 | 150.61 | 151.43 | 0.83 | 5.4 | 12.2 | 0.4 |
| km 0+200 | 4.49 | 150.47 | 151.27 | 1.21 | 3.75 | 8.87 | 0.57 |
| km 0+220 | 4.49 | 150.12 | 151.23 | 0.67 | 6.68 | 12.08 | 0.29 |
| km 0+240 | 4.49 | 149.86 | 151.22 | 0.46 | 9.76 | 12.03 | 0.16 |
| km 0+260 | 4.49 | 149.93 | 151.19 | 0.63 | 7.17 | 10.77 | 0.23 |
| km 0+280 | 4.49 | 149.74 | 151.18 | 0.4 | 11.23 | 11.86 | 0.13 |
| km 0+300 | 4.49 | 149.6 | 151.16 | 0.57 | 7.88 | 11.57 | 0.22 |
| km 0+320 | 4.49 | 149.53 | 151.15 | 0.35 | 13.38 | 15 | 0.11 |

**Tabla 4.13: Resultados simulación hidráulica en situación con proyecto de Estero Sin Nombre para caudal de****

| Perfil | Caudal | Cota<br>Fondo | Cota Pelo<br>de Agua | Velocidad<br>Media | Área<br>Mojada | Ancho<br>Superficial | Número de<br>Froude |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **[m3/s]** | **[m.s.n.m.]** | **[m.s.n.m.]** | <br>**[m/s]** | **[m2]** | **[m]** | **[m]** |
| km 0+000 | 4.47 | 152.33 | 153.13 | 1.14 | 3.91 | 9.88 | 0.58 |

**Tabla 4.14: Resultados simulación hidráulica en situación con proyecto de Estero Sin Nombre para caudal de****

| Perfil | Caudal | Cota Fondo | Cota Pelo<br>de Agua | Velocidad<br>Media | Área<br>Mojada | Ancho<br>Superficial | Número de<br>Froude |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **[m3/s]** | **[m.s.n.m.]** | **[m.s.n.m.]** | **[m/s]** | **[m2]** | **[m]** | **[m]** |
| km 0+000 | 4.99 | 152.33 | 153.16 | 1.17 | 4.25 | 10.28 | 0.58 |
| km 0+020 | 4.99 | 152.18 | 153 | 1.06 | 4.69 | 11.47 | 0.53 |
| km 0+040 | 4.99 | 152.03 | 152.78 | 1.44 | 3.48 | 5.58 | 0.58 |
| km 0+060 | 4.99 | 151.6 | 152.79 | 0.62 | 8.1 | 13.18 | 0.24 |
| km 0+070 | Entubamiento Puente | Entubamiento Puente | Entubamiento Puente | Entubamiento Puente | Entubamiento Puente | Entubamiento Puente | Entubamiento Puente |
| km 0+080 | 4.99 | 151.6 | 152.41 | 1.24 | 4.01 | 7.36 | 0.54 |
| km 0+100 | 4.99 | 151.41 | 152.23 | 1.21 | 4.11 | 10.51 | 0.62 |
| km 0+120 | 4.99 | 151.36 | 152.15 | 0.83 | 6.11 | 12.41 | 0.37 |
| km 0+140 | 4.99 | 151.21 | 152.01 | 1.17 | 4.34 | 9.55 | 0.54 |
| km 0+160 | 4.99 | 151.01 | 151.65 | 1.7 | 2.95 | 10.86 | 1.01 |
| km 0+180 | 4.99 | 150.61 | 151.47 | 0.85 | 5.86 | 12.6 | 0.39 |
| km 0+200 | 4.99 | 150.47 | 151.32 | 1.21 | 4.18 | 9.2 | 0.55 |
| km 0+220 | 4.99 | 150.12 | 151.29 | 0.68 | 7.36 | 12.99 | 0.28 |
| km 0+240 | 5.96 | 149.86 | 151.27 | 0.58 | 10.33 | 12.45 | 0.2 |
| km 0+260 | 5.96 | 149.93 | 151.22 | 0.81 | 7.49 | 11.58 | 0.29 |
| km 0+280 | 5.96 | 149.74 | 151.21 | 0.52 | 11.51 | 12.03 | 0.17 |
| km 0+300 | 5.96 | 149.6 | 151.16 | 0.76 | 7.93 | 11.63 | 0.29 |
| km 0+320 | 5.96 | 149.53 | 151.15 | 0.47 | 13.38 | 15 | 0.14 |

**Tabla 5.3: Valores obtenidos de profundidad de socavación local.****

| Col1 | Breusers y<br>Bohan Abt Ruff Socavación<br>Raudkivi<br>Promedio |
| --- | --- |
| **Sector Entubamiento**<br>**Sector Canal de**<br>**Desagüe** | 0.67<br>0.01<br>0.56<br>0.84<br>**0.52**<br>0.46<br>0.00<br>0.35<br>0.57<br>**0.35** |

**Tabla 5.4: Valores obtenidos para longitud y ancho de la fosa de socavación local.****

| Col1 | Estero Sin Nombre<br>Sector Entubamiento Sector Canal de Desagüe |
| --- | --- |
| **Largo Socavación (m)**<br>**Ancho Socavación (m)** | 3.71<br>2.37<br>1.6<br>1.0 |

**Tabla 6.2: Resultados Socavación Local por Quebrada.****

| Método | Diámetro Equivalente (mm) (Estero Sin Nombre) |
| --- | --- |
| **Método** | **Sector Entubamiento**<br>**Sector Canal de Desagüe** |
| **Teórico**<br>**Maza & García**<br>**Straub**<br>**Neill**<br>**Ibash** | 0.025<br>0.017<br>0.009<br>0.004<br>0.007<br>0.004<br>0.008<br>0.004<br>**0.028**<br>**0.030** |
