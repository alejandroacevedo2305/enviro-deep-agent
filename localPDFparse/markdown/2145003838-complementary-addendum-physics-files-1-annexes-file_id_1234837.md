---
title: Formato Informe y Cubierta
author: Itasca
date: D:20190927204120-03'00'
language: es
type: report
pages: 90
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe ITASCA-4026.004-2019-01
  - A partir de las tareas desarrolladas se puede concluir lo siguiente:
  - Finalmente, el modelo numérico construido y calibrado se encuentra disponible para realizar
-->

|Col1|Nombre del estudio<br>Actualización a Julio 2019 del<br>Modelo Numérico<br>Hidrogeológico 3D Rajo Ministro<br>Hales|
|---|---|
|~~**INFORME**~~<br>**ITASCA-INF-**<br>**4026.004.01**<br>**Rev.2 **<br> <br>|~~**INFORME**~~<br>**ITASCA-INF-**<br>**4026.004.01**<br>**Rev.2 **<br> <br>|
|<br>Preparada para:<br> <br>**CODELCO, División Ministro**<br>**Hales**|<br>Preparada para:<br> <br>**CODELCO, División Ministro**<br>**Hales**|
|Preparado por<br>**Andrea Castro**<br>Revisada por<br>**Martin Brown**|Preparado por<br>**Andrea Castro**<br>Revisada por<br>**Martin Brown**|
|<br>**Itasca Chile SpA**<br>**Av. Pedro de Valdivia 291, Segundo**<br>**Piso, Providencia, C.P. 750-0524**<br>**Santiago de Chile**<br> <br>** (56) 224 341 300**<br>** itascachile@itasca.cl**<br>**www.itasca.cl**<br>|<br>**Itasca Chile SpA**<br>**Av. Pedro de Valdivia 291, Segundo**<br>**Piso, Providencia, C.P. 750-0524**<br>**Santiago de Chile**<br> <br>** (56) 224 341 300**<br>** itascachile@itasca.cl**<br>**www.itasca.cl**<br>|
|||

# Informe ITASCA-4026.004-2019-01

**Actualización a Julio 2019 del Modelo Numérico**

**Hidrogeológico 3D Rajo Ministro Hales**

Preparado para:
**CODELCO, División Ministro Hales**

|Revisión|Preparado<br>por|Revisado<br>por|Fecha|Observaciones|
|---|---|---|---|---|
|**1 **|Andrea Castro|~~Martin~~<br>Brown|~~Septiembre,~~<br>2019||

**Av. Pedro de Valdivia 291, Segundo Piso, Providencia, Santiago de Chile**

 **(56) 224 341 300**  **itascachile@itasca.cl**

**Web: www.itasca.cl**

Actualización a Julio 2019 del Modelos Numérico Hidrogeológico
3D Rajo Ministro Hales

CODELCO, División Ministro Hales

**Actualización del Modelo Numérico Hidrogeológico 3D**
**Rajo Ministro Hales**

**Tabla de Contenidos**

**INFORME ...................................................................................................................................................... I**

**INTRODUCCIÓN .................................................................................................................................. 1**

1.1 O BJETIVOS Y A LCANCES .............................................................................................................................. 2

**ACTUALIZACIÓN DEL MODELO DE FLUJO 3D CON** _**MINEDW**_ **................................................................ 4**

2.1 E L C ÓDIGO N UMÉRICO _MINEDW_ ............................................................................................................... 5

2.2 D OMINIO DEL M ODELO Y C ONDICIONES DE C ONTORNO ................................................................................... 5

2.3 D ISCRETIZACIÓN E SPACIAL Y T EMPORAL ........................................................................................................ 6

2.4 U NIDADES H IDROGEOLÓGICAS ................................................................................................................... 11

2.5 M ODELO E STRUCTURAL ........................................................................................................................... 12

2.6 N IVELES I NICIALES ................................................................................................................................... 14

2.7 P OZOS DE O BSERVACIÓN .......................................................................................................................... 14

2.8 I NCORPORACIÓN DEL P LAN DE E XPLOTACIÓN ................................................................................................ 14

2.9 Z ONA DE R ELAJACIÓN (ZOR) ..................................................................................................................... 16

2.10 P OZOS DE B OMBEO ............................................................................................................................ 19

2.11 S ISTEMA DE D RENAJE .......................................................................................................................... 20

**CALIBRACIÓN DEL MODELO HIDROGEOLÓGICO................................................................................ 21**

3.1 C ALIBRACIÓN DEL M ODELO _MINEDW_ E STACIONARIO ................................................................................... 21

_3.1.1_ _Periodo de Calibración .............................................................................................................. 21_

_3.1.2_ _Ajuste de Parámetros ............................................................................................................... 21_

_3.1.3_ _Balance de Masas ..................................................................................................................... 22_

_3.1.4_ _Calibración de Niveles Piezométricos........................................................................................ 23_

3.2 C ALIBRACIÓN DEL M ODELO _MINEDW_ T RANSIENTE ...................................................................................... 25

_3.2.1_ _Periodo de Calibración .............................................................................................................. 25_

_3.2.2_ _Ajuste de Parámetros ............................................................................................................... 25_

_3.2.3_ _Balance de Masas ..................................................................................................................... 27_

_3.2.4_ _Calibración de Niveles Piezométricos........................................................................................ 35_

_3.2.5_ _Calibración de Zonas de Seepage ............................................................................................. 35_

**COMENTARIOS FINALES Y CONCLUSIONES ....................................................................................... 39**

**REFERENCIAS .................................................................................................................................... 40**

**ANEXO 1 GRÁFICOS DE CALIBRACIÓN DE PIEZÓMETROS ........................................................................... 42**

Septiembre, 2019 **ii**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización a Julio 2019 del Modelos Numérico Hidrogeológico
3D Rajo Ministro Hales

CODELCO, División Ministro Hales

**ÍNDICE DE FIGURAS**

Figura 1: Localización del rajo Ministro Hales. ..................................................................... 2
Figura 2: Bordes definidos para el modelo numérico hidrogeológico 3D del Rajo Ministro

Hales. ...................................................................................................................................... 7

Figura 3: Discretización horizontal del modelo numérico. .................................................... 9
Figura 4: Discretización vertical del modelo numérico. ....................................................... 10
Figura 5: Unidades hidrogeológicas del modelo numérico actualizado. .............................. 12
Figura 6: Modelo estructural 2019 representado en la actualización del modelo numérico
MINEDW del rajo DMH. ..................................................................................................... 13
Figura 7: Pozos de observación del rajo DMH utilizados para la calibración del modelo

actualizado. ........................................................................................................................... 15

Figura 8: Geometría de la ZOR para el modelo actualizado del rajo DMH. ........................ 18
Figura 9: Valores de las conductividades hidráulicas para cada unidad hidrogeológica de las
dos capas de la ZOR del modelo numérico actualizado. ...................................................... 18
Figura 10: Pozos de bombeo para el modelo MINEDW actualizado del rajo DMH. .......... 19
Figura 11: Sistema de drenaje del modelo actualizado MINEDW para el rajo DMH. ........ 20
Figura 12: Valores calibrados de las conductividades hidráulicas para cada unidad
hidrogeológica del modelo numérico estacionario actualizado. ........................................... 22
Figura 13: Balance de masas de la calibración estacionaria del modelo MINEDW. ........... 23
Figura 14: Resultado de la calibración de niveles obtenida en el modelo estacionario. ...... 23
Figura 15: Valores de conductividad hidráulica calibrados en el modelo numérico actualizado
(color azul). En rojo se indican los valores máximos y mínimos de las permeabilidades
definidas en el modelo conceptual. ...................................................................................... 27
Figura 16: Caudal de seepage total estimado por el modelo numérico transiente actualizado
del rajo DMH. ....................................................................................................................... 29
Figura 17: Caudal de seepage que aflora en las unidades hidrogeológicas que corresponden
a grava, roca y fallas, en el modelo numérico actualizado del rajo DMH............................ 29
Figura 18: Porcentaje de caudal de seepage que aporta la unidad de gravas. ...................... 30
Figura 19: Caudal de seepage y excavación del rajo DMH, a medida que transcurre el tiempo

de simulación. ....................................................................................................................... 30

Figura 20: Unidades hidrogeológicas expuestas en el rajo DMH durante enero y marzo de

2012. ..................................................................................................................................... 31

Figura 21: Unidades hidrogeológicas expuestas en el rajo DMH durante junio de 2013 y abril

de 2015. ................................................................................................................................ 31

Figura 22: Unidades hidrogeológicas expuestas en el rajo DMH durante mayo y septiembre

de 2017. ................................................................................................................................ 32

Figura 23: Caudal estimado de evaporación según el modelo numérico actualizado. ......... 33

Septiembre, 2019 **iii**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización a Julio 2019 del Modelos Numérico Hidrogeológico
3D Rajo Ministro Hales

CODELCO, División Ministro Hales

Figura 24: Caudal de los pozos de bombeo simulados en el modelo de régimen transiente.

.............................................................................................................................................. 34

Figura 25: Comportamiento del % residual para cada periodo de cálculo del modelo numérico

actualizado. ........................................................................................................................... 34

Figura 26: Vista desde Mirador oeste hacia noreste del rajo DMH en visita de julio de 2019
y comparación con resultado de seepage entregado por MINEDW para esta misma fecha. 37
Figura 27: Vista desde Mirador norte hacia sureste del rajo DMH en visita de julio de 2019
y comparación con resultado de seepage entregado por MINEDW para esta misma fecha. 38

**ÍNDICE DE TABLAS**

Tabla 1: Modificaciones llevadas a cabo en la actualización del modelo numérico

hidrogeológico de DMH. ........................................................................................................ 4
Tabla 2: Asignación de las nuevas UH del modelo UGTB19, a unidades existentes en el

modelo MINEDW del año 2018. .......................................................................................... 11

Tabla 3: Multiplicadores de permeabilidad para la ZOR. .................................................... 17
Tabla 4. Criterios de error empleados para valorar la calibración de niveles. ..................... 24
Tabla 5. Valores de los índices de calibración obtenidos para el modelo estacionario. ....... 24
Tabla 6: Valores de los parámetros hidráulicos calibrados para cada unidad hidrogeológica,
para los modelos del rajo DMH de diciembre de 2018 y julio de 2019. .............................. 26
Tabla 7: Porcentajes de caudal aportante y de afloramiento de seepage en el modelo, de las
unidades de grava, roca y fallas. ........................................................................................... 32
Tabla 8: Valores de los índices de calibración obtenidos para el modelo transiente

actualizado. ........................................................................................................................... 35

Tabla 9: Valores de índices de calibración obtenidos para el modelo de diciembre de 2018 y
para el modelo actualizado de julio de 2019. ....................................................................... 35

Septiembre, 2019 **iv**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**Actualización del Modelo Numérico Hidrogeológico 3D Rajo**

**Ministro Hales**

**INTRODUCCIÓN**

En el presente informe se describen los trabajos realizados por Itasca Chile SpA (en adelante
Itasca) para la Corporación Nacional de Cobre de Chile (Codelco), División de Ministro Hales
(DMH), para la actualización del “Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales”.

Este documento incluye las características de la actualización del modelo numérico construido
para el entorno del Rajo de DMH con el _software_ _MINEDW_, así como los resultados obtenidos
durante la calibración de este mismo. Dichas actualizaciones, que incorporan los nuevos datos
obtenidos desde diciembre del año 2018 hasta julio del año 2019 para el rajo DMH, cumplen con
los objetivos descritos en las Bases Técnicas (BBTT) publicadas por la Superintendencia de
Geotecnia, perteneciente a la Gerencia de Recursos Mineros y Desarrollo (GRMD) de la DMH,

Codelco.

DMH es un yacimiento de cobre que se encuentra en desarrollo desde el año 2011. Se ubica dentro
de la cuenca media del río Loa o cuenca de Calama, aproximadamente a 8 km al norte de Calama,
en la región de Antofagasta, a una altitud de 2.400 m.s.n.m. (Figura 1).

Debido a su ubicación, las instalaciones de DMH están sometidas a unas condiciones hidrológicas
e hidrogeológicas naturales especiales. Si a estas les sumamos la alta antropización de la zona,
entorno minero que genera importantes recargas de carácter antrópico, hace que el agua
subterránea juegue un rol muy importante en las labores mineras realizadas en el rajo de DMH. Es
por lo que ambos regímenes de flujo, natural y antrópico, requieren ser estudiados y analizados en
detalle para garantizar unas condiciones de seguridad, estabilidad de taludes, y de operatividad

adecuadas.

Septiembre, 2019 **1**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 1: Localización del rajo Ministro Hales.**_

**1.1 Objetivos y Alcances**

El principal objetivo de este proyecto consiste en actualizar y calibrar el modelo numérico 3D
existente en el _software MINEDW_ (Itasca Denver, INC, 2018) utilizando las descripciones del
sistema hidrogeológico presentes en el entorno y definidas en el modelo conceptual y en sus
actualizaciones vigentes, incorporando toda la nueva información generada desde diciembre del
año 2018, hasta julio de 2019.

La actualización de este modelo permitirá contar con una herramienta de modelación más robusta,
que represente de la forma más realista posible los procesos hidrogeológicos que ocurren en el
dominio del rajo de DMH, desde el inicio de la explotación en 2011, hasta julio del año 2019. De
esta manera, el modelo será una herramienta sólida para la evaluación de los principales aspectos
hidrogeológicos relacionados con la implementación y avance del plan de explotación y de
distintos planes de drenaje y despresurización. Esto, al contener la última información
hidrogeológica del área, que posee un mayor entendimiento del medio y un mayor número de
observaciones de terreno de referencia para la calibración.

Septiembre, 2019 **2**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

De esta manera, los trabajos a llevar a cabo son los siguientes:

CODELCO, División Ministro Hales

**I.** **Revisión de Información:**

a. Revisión minuciosa y análisis crítico del conjunto de información disponible y
facilitada por DMH, que será incorporada al nuevo modelo _MINEDW._

**II.** **Actualización del Modelo Numérico 3D en** _**MINEDW**_ **:**

a. Incorporar nuevo modelo estructural.
b. Modificar la geometría y parámetros hidráulicos de las unidades hidrogeológicas.
c. Añadir topografías desde enero hasta julio de 2019.
d. Actualizar las series de datos de niveles piezométricos medidos en piezómetros
existentes, a julio de 2019.
e. Considerar los datos de caudales del balance hídrico conceptual.

**III.** **Calibración del Modelo Numérico:**

a. Considera la modificación de los parámetros hidráulicos para lograr el ajuste de los
niveles modelados con los medidos en campo, de acuerdo con los rangos de valores
definidos en el modelo conceptual, reproduciendo también las tendencias de los

datos.

b. Analizar las zonas de afloramientos superficiales en el área a modelar, en especial
dentro del rajo de DMH.
c. Se llevará a cabo en dos etapas: calibración del modelo en estado estacionario y del

modelo en estado transiente.

**IV.** **Análisis de Sensibilidad del Modelo** _**MINEDW**_ **:**

a. Determinar los parámetros con mayor influencia en los resultados del modelo

numérico.

b. Evaluar el efecto que tiene la variación de los parámetros más inciertos del modelo.
**V.** **Simulación de Alternativas de Drenaje y Despresurización:**
a. Creación de planes de despresurización mediante la incorporación de distintos
sistemas de drenaje para las fases a simular en el modelo _MINEDW_ .

Cabe destacar que la actualización y calibración del modelo numérico existente se realizará
considerando los estándares establecidos en la “Guía para el uso de modelos de aguas subterráneas
en el SEIA” (Servicio de Evaluación Ambiental, SEA, 2012).

Septiembre, 2019 **3**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**ACTUALIZACIÓN DEL MODELO DE FLUJO 3D CON** _**MINEDW**_

El modelo numérico hidrogeológico _MINEDW_ del rajo DMH realizado hasta diciembre de 2018,
ha sido actualizado con información disponible a julio de 2019. Esta actualización ha utilizado
como base el modelo realizado durante el año 2018, cambiando algunas características
constructivas, como la discretización de la malla, geometría de unidades hidrogeológicas, modelo
estructural, y otras diferencias en la información utilizada, que se muestran en la siguiente tabla:

_**Tabla 1: Modificaciones llevadas a cabo en la actualización del modelo numérico**_
_**hidrogeológico de DMH.**_

|Característica|Modelo diciembre-2018|Modelo julio-2019|
|---|---|---|
|~~Número de~~<br>Nodos <br>|1.434.985|2.271.748|
|~~Número de~~<br>Elementos <br>|2.810.340|4.443.338|
|~~Tamaño de~~<br>Malla (Zona_pit_) <br>|15 a 18 m de lado|15 a 18 m de lado|
|~~Profundidad~~<br>Máxima<br>Discretizada|1.400 m.s.n.m. <br>|1.400 m.s.n.m.<br>|
|Condiciones de<br>Borde <br>|~~Flujo constante noreste (2.410 m.s.n.m.)~~<br>y suroste (2.220 m.s.n.m.). Flujo nulo<br>por este y oeste.|~~Flujo constante noreste (2.410 m.s.n.m.)~~<br>y suroste (2.220 m.s.n.m.). Flujo nulo<br>por este y oeste.|
|~~Condiciones~~<br>Iniciales <br>|Premina 2.375 m.s.n.m. (31-01-2011) <br>|Premina 2.375 m.s.n.m. (31-01-2011)<br>|
|~~Parámetros~~<br>Hidráulicos|~~Fallas con conductividades hidráulicas~~<br>diferentes (conductoras y barreras)|~~Fallas con conductividades hidráulicas~~<br>diferentes (conductoras y barreras)|
|Modelo UGTB <br>|Año 2018, 12 UH|Julio de 2019, 12 UH|
|~~Modelo~~<br>Estructural|Año 2018, 149 fallas. <br>|Julio-2019, 179 fallas. <br>|
|_ZOR _<br>|~~Proporcional con la profundidad del~~~~_pit_. ~~<br>2 zonas. Factores = 1000-100-5-2|~~Proporcional con la profundidad del~~~~_pit_. ~~<br>2 zonas. Factores = 1000-100-5-2|
|~~Periodo de~~<br>Calibración <br>|Enero de 2011 a diciembre de 2018 <br>|Enero de 2011 a julio de 2019<br>|
|~~Pozos de~~<br>Bombeo<br>|~~Caudales pozos de bombeo hasta~~<br>diciembre de 2018<br>|~~Caudales pozos de bombeo hasta julio~~<br>de 2019|
|~~Sistema de~~<br>Drenaje|~~Todos los drenes hasta diciembre de~~<br>2018|Todos los drenes hasta julio de 2019|

Septiembre, 2019 **4**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

A continuación, se describe el proceso de actualización del modelo numérico del rajo DMH, con
respecto al modelo _MINEDW_ del año 2018.

**2.1 El Código Numérico** _**MINEDW**_

_MINEDW_ es un programa que fue desarrollado para analizar el flujo subterráneo y las condiciones
hidrogeológicas específicamente en minas, por lo que cuenta con una serie de atributos a la hora
de representar condiciones asociadas a los procesos mineros. Este _software_ resuelve la ecuación
de flujo tridimensional con una superficie no-confinada o confinada usando el método de
elementos finitos. El código de modelación ha sido verificado por el _Sandia National Laboratory_
(1998) y es utilizado en numerosos proyectos asociados a mineria en todo el mundo.

El programa permite incluir aspectos importantes en la simulación del modelamiento
hidrogeológico de minas a rajo abierto o subterráneas, tales como el colapso de la malla y el
movimiento de la topografía de acuerdo con el plan minero de explotación, la implementación de
zonas que cambian las propiedades hidráulicas en el tiempo para simular fenómenos como el
_caving_, la inclusión de zonas de alteración superficial ( _ZOR_ ), o la simulación de _pit lake._

La actualización del modelo se realizó con la última versión del _software_ _MINEDW_ (Itasca Denver
Inc. 2018), correspondiente a la 3.05, que incluye mayores capacidades de pre y postprocesamiento, soluciona algunos problemas gráficos, e incluye un nuevo _solver_ _SAMG_ el cual
resuelve la ecuación de flujo de forma más rápida y precisa.

**2.2 Dominio del Modelo y Condiciones de Contorno**

La actualización del modelo _MINEDW_ ha sido realizada utilizando coordenadas mina, sistema de

referencia utilizado por DMH para todos sus elementos georreferenciados.

El área del modelo actualizado, así como las condiciones de contorno de este, se han mantenido

con respecto al modelo _MINEDW_ del año 2018. De esta manera, el área modelada corresponde a
una forma irregular que presenta unas dimensiones de aproximadamente 6 km en la dirección EW por unos 9 km en dirección N-S, donde el rajo se encuentra en posición aproximadamente

centrada.

Las condiciones de borde del modelo han sido establecidas como flujo constante en los bordes
noreste y suroeste, y de flujo nulo para los límites este y oeste, según las condiciones hidráulicas
definidas en el modelo conceptual. Esta condición del código calcula para cada paso de tiempo el
caudal que ingresa o sale de los contornos utilizando la conductividad hidráulica de las unidades
hidrogeológicas y el nivel piezométrico inicial definido, a través de una solución analítica para un

Septiembre, 2019 **5**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

acuífero semi-infinito acoplada al borde. De esta manera, no se permite el ingreso por los bordes
de un volumen irrealmente alto de agua, como pasaría en el caso de contornos de nivel fijo muy
cercanos al rajo.

Además, el límite inferior del modelo se ha profundizado hasta la cota 0 m s.n.m. para que el
espesor del modelo fuera suficientemente grande y no interferir en el régimen hídrico modelado,
incluso en las etapas en las que el rajo alcanza su mayor profundidad.

 - Borde de nivel constante 2410 m.s.n.m. Este borde representa la principal entrada de agua
al modelo numérico, proveniente del norte y noreste

 - Borde de nivel constante 2220 m.s.n.m. Este borde representa la salida de agua del modelo
numérico por el suroeste.

 - Bordes de flujo nulo o borde impermeable. Estos son obtenidos a partir de altos

topográficos que separan cuencas locales del área de estudio, por el este y el oeste.

En la Figura 2 es posible ver las condiciones de contorno definidas para la actualización del

modelo.

**2.3 Discretización Espacial y Temporal**

El mallado del modelo actualizado fue modificado con respecto al modelo anterior. El detalle de
la discretización en planta del nuevo modelo se puede observar en la Figura 3, mientras que el
detalle en sentido vertical se muestra en la Figura 4.

La discretización espacial se ha realizado mediante el método de elementos finitos resulto por
_MINEDW_, generando prismas de base triangular en toda la extensión del modelo. Para esto se han
considerado los siguientes criterios:

 - En la extensión máxima del Rajo DMH, definida por la topografía del PND2019 hasta el
año 2041, los elementos tienen un tamaño de lado de entre 15 a 18 metros.

 - A lo largo de toda la traza de la Falla Oeste, que cruza el modelo de Norte a Sur, los

elementos tienen un tamaño de lado de entre 15 a 18 metros.

 - En los bordes del modelo los elementos tienen entre 250 a 350 metros de lado.

Septiembre, 2019 **6**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 2: Bordes definidos para el modelo numérico hidrogeológico 3D del Rajo Ministro**_

_**Hales.**_

Septiembre, 2019 **7**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

La diferencia entre los dos mallados reside en la extensión de la zona más refinada, donde en la

actualización del modelo se amplió hasta el área donde se ubican los pozos de drenaje en norte del
rajo, con el objetivo de tener un modelo más detallado y que represente de mejor forma los
procesos que ocurren en esa zona del modelo.

La discretización vertical también fue modificada con respecto a la original. Mientras que el
modelo _MINEDW_ del año 2018 para DMH contaba con 23 capas verticales principales con
espesores de 250 m. en las capas más profundas y 50 m. en las capas más someras, la actualización
de este modelo posee 32 capas verticales principales cuyos espesores varían entre 500 y 15 metros
en las capas más profundas y superficiales, respectivamente.

Asimismo, al igual que en el modelo anterior, en la zona del rajo se ha aplicado una mayor
discretización vertical en las 27 capas más superficiales ( _pinchout_ ) que ha permitido obtener
elementos de espesor de aproximadamente 15 metros. Este espesor se considera adecuado para
poder representar, con suficiente resolución, la geometría de los bancos existentes.

La nueva discretización espacial realizada ha dado como resultado un total de 2.271.748 nodos y
4.443.338 elementos en el modelo _MINEDW_, a diferencia del modelo anterior, que estaba
compuesto por 1.434.985 nodos y 2.810.340 elementos, lo que entrega un detalle mucho mayor al

nuevo modelo actualizado.

En ambos modelos la discretización temporal es en tiempos de cálculo regulares de cadencia
mensual. El régimen estacionario se ha modelado con fecha enero de 2011, cuando no había
desarrollos mineros aún, mientras que la etapa de calibración transiente del modelo actualizado se
ha llevado a cabo entre las fechas de enero de 2011 a julio de 2019.

Septiembre, 2019 **8**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

El tamaño de los

elementos en el área

del rajo es de entre

15 a 18 metros.

El tamaño de los

elementos a lo largo

de la Falla Oeste es

de entre 15 a 18

metros.

_**Figura 3: Discretización horizontal del modelo numérico.**_

Septiembre, 2019 **9**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

_**Figura 4: Discretización vertical del modelo numérico.**_

Septiembre, 2019 **10**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**2.4 Unidades Hidrogeológicas**

Las unidades hidrogeológicas (UH) fueron creadas directamente mediante la combinación entre
las diferentes alteraciones y mineralizaciones, las cuales, junto con las estructuras principales
conforman las unidades de mayor interés hidrogeológico.

Las UH integradas en la actualización del modelo numérico han sido obtenidas del modelo
UGTB19, que incluye 16 UH, 4 adicionales con respecto al modelo UGTB18, siendo este último
el utilizado para la construcción del modelo numérico en _MINEDW_ del año 2018 de DMH.

Estas 4 nuevas UH corresponden a subunidades de unidades anteriormente descritas en el modelo
hidrogeológico conceptual planteado por Itasca (Itasca Chile Spa, 2018b), con características
bastante similares a UH previamente definidas, por lo que cada una será incorporada a una UH ya
existente con el objetivo de simplificar la modelación y calibración del modelo.

Las nuevas unidades presentes en el modelo UGTB19, así como la unidad que las representará en
el modelo _MINEDW_ actualizado, se exponen en la Tabla 2.

_**Tabla 2: Asignación de las nuevas UH del modelo UGTB19, a unidades existentes en el**_

_**modelo MINEDW del año 2018.**_

|Unidad Modelo UGTB19|Unidad modelo MINEDW|
|---|---|
|~~UVOALT~~<br>|~~UVO~~<br>|
|~~GMMALT~~<br>|~~GMM~~<br>|
|~~UGPC~~<br>|~~UGP~~<br>|
|~~ARE~~|~~UVO~~|

A partir de esto, la actualización del modelo numérico hidrogeológico de DMH incluye las mismas
12 UH que el modelo de año 2018, sin embargo, la distribución espacial ha sido modificada, según
lo actualizado en el modelo UGTB19, con respecto al UGTB18. Adicionalmente, se incluyen 3
UH que corresponden a las estructuras presentes en la zona de estudio.

La distribución de las unidades hidrogeológicas en el modelo numérico actualizado puede ser
observada en la Figura 5, en la que se muestra una vista en planta del modelo construido, tanto en
toda su extensión, como enfocado en el rajo.

Septiembre, 2019 **11**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 5: Unidades hidrogeológicas del modelo numérico actualizado.**_

**2.5 Modelo Estructural**

El modelo numérico _MINEDW_ actualizado para el rajo DMH, muestra variaciones en cuanto a las
estructuras, con respecto al modelo realizado para diciembre de 2018. Las zonas de falla del

modelo numérico actualizado, han sido definidas de acuerdo al modelo estructural del año 2019,

el cual cuenta con 178 estructuras definidas en el sector del rajo DMH, a diferencia del modelo
estructural del año 2018, utilizado para construir el modelo numérico en _MINEDW_ de DMH a
diciembre de 2018, que contaba con 149 fallas.

Todas las estructuras han sido ingresadas y representadas de forma explícita en el modelo
numérico, es decir, asignando las propiedades de las fallas a elementos.

En el modelo actualizado, al igual que en el anterior, se exhibe la Falla Oeste con un carácter
hidráulico de tipo barrera y correspondiente a una falla regional, por lo que ha sido incorporada
como una unidad hidrogeológica independiente que cruza todo el modelo numérico de norte a sur.

Septiembre, 2019 **12**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

A partir de la relación entre el comportamiento hidráulico y la dirección de la falla de las
estructuras que contaban con esta información, fue posible clasificar el resto de las fallas del
modelo entre dos unidades hidrogeológicas según su potencial hidráulico. Estas dos unidades
corresponden a Zonas de Fallas Barreras (ZF1) y Zonas de Fallas Conductoras (ZF2), como
muestra la Figura 6.

Cabe destacar que en el modelo desarrollado a diciembre de 2018, las fallas ubicadas al este de la
falla oeste consideraron una permeabilidad similar a la del medio en el cual se situaban. Esto fue
modificado en el modelo actualizado de julio de 2019, con el objetivo de generar un modelo más
representativo de la realidad.

_**Figura 6: Modelo estructural 2019 representado en la actualización del modelo numérico**_
_**MINEDW del rajo DMH.**_

Septiembre, 2019 **13**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**2.6 Niveles Iniciales**

Para la simulación del estado transiente del modelo de flujo, fue necesario definir una condición
de nivel inicial de aguas subterráneas. Esta condición inicial se generó a partir de una simulación
en régimen estacionario, considerando como resultados válidos aquellos que se obtuvieron una vez
transcurrido el período de estabilización.

**2.7 Pozos de Observación**

La actualización del modelo numérico considera los mismos pozos de observación que el modelo
_MINEDW_ del rajo DMH del año 2018.

Dentro de estos piezómetros se incluyen 26 de tipo Casagrande y 37 de cuerda vibrante, a los
cuales se les actualizarán las series medidas hasta julio de 2019, para ser considerados en la

calibración del modelo transiente actualizado.

En la Figura 7 se muestran todos los pozos de observación incluidos en ambos modelos.

**2.8 Incorporación del Plan de Explotación**

El nuevo modelo de flujo ha sido actualizado incorporando las topografías consecutivas mensuales
de enero a junio del año 2019, correspondiendo esta última al fin del modelo transiente.

El modelo actualizado considera la topografía original antes de la excavación del rajo, así como
las topografías consecutivas mensuales hasta diciembre del año 2018, utilizadas en el modelo
_MINEDW_ del rajo DMH del año 2018.

Septiembre, 2019 **14**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 7: Pozos de observación del rajo DMH utilizados para la calibración del modelo**_

_**actualizado.**_

Septiembre, 2019 **15**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**2.9 Zona de Relajación (ZOR)**

La Zona de Relajación (ZOR) es una región superficial paralela al rajo, donde la permeabilidad
hidráulica de las unidades hidrogeológicas que la componen aumenta. Esto se justifica mediante
la descompresión que sufren las diferentes unidades, incluyendo rocas y fallas, al estar expuestas
a la descarga continua de materiales producto del avance de explotación del rajo, y está relacionado
directamente con el “factor de daño D” definido en los modelos geomecánicos de estabilidad de
taludes (Itasca, 2014).

La extensión de la ZOR puede ser estimada usando modelos mecánicos y consiste en una estrecha
“zona de daño” por explosión, cuyo daño puede ser observable (Hoek _et al_ ., 2010) y abarcar un
espesor variable entre 5 a 40 m. (Beale, 2011), que se sitúa sobre una “zona de descarga” que
puede tener cientos de metros de espesor dependiendo de la geología, _stress in-situ_, el método de
excavación, entre otros (Sullivan, 2007).

El efecto de la ZOR en la permeabilidad ha sido estimado por varios autores. Beale (2011) sugiere
que el daño por explosión puede incrementar la permeabilidad hasta 3 órdenes de magnitud o más
en rocas frágiles no alteradas, mientras que Rutqvist _et al_ . (2009) han calculado un incremento en
la permeabilidad de 1 a 3 órdenes de magnitud, en diferentes métodos para estimar la
permeabilidad en deformación en túneles en granitos. Este aumento en la conductividad hidráulica
se debe también a la apertura de fracturas presentes en la ZOR, que se genera por la descompresión
de las unidades producto de la descarga de materiales del rajo.

El programa _MINEDW_ permite incorporar una zona de relajación (ZOR) superficial compuesta
por una o varias capas con una extensión creciente, ajustándose al área del rajo existente en cada
fecha, donde los elementos que la componen aumentan la conductividad hidráulica en función de
su profundidad. De esta manera, esta zona se mueve automáticamente con la topografía de igual
manera que progresa el plan de explotación en el modelamiento.

En la actualización del modelo hidrogeológico no se ha variado la ZOR, con respecto al modelo
2018. En ambos casos se tiene un espesor total de 1⁄4 la profundidad del rajo para cada tiempo de
cálculo, manteniendo en todo momento 2 capas de una potencia del 50% del espesor total.
Asimismo, los multiplicadores de la conductividad hidráulica de cada UH también se mantienen
con respecto al modelo anterior. De esta manera, la zona de relajación se crea para todas las
unidades hidrogeológicas, a excepción de los materiales aluviales.

Los multiplicadores de la conductividad hidráulica asociados a la ZOR, así como la geometría de
definida para la actualización del modelo del rajo de DMH para esta misma, se muestran en la
Tabla 3 y Figura 8.

Septiembre, 2019 **16**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

La Figura 9 expone los valores de las conductividades hidráulicas mínimas y máximas de cada
unidad hidrogeológica a partir de las pruebas realizadas en cada unidad, así como los valores
otorgados para cada una en las dos capas de la ZOR. En esta figura es posible observar que todos
los valores de permeabilidad de todas las unidades se encuentran dentro de los límites conceptuales
definidos, con excepción de la unidad Conglomerado Brechoso Negro (CBN), el cual cuenta con
muy pocas pruebas hidráulicas y cuyos valores de permeabilidad de la ZOR se encuentran dentro
de lo que indica la literatura para este tipo de roca.

_**Tabla 3: Multiplicadores de permeabilidad para la ZOR.**_

|Unidad Hidrogeológica|Capa 1|Capa 2|
|---|---|---|
|~~UGP~~<br>|~~1 ~~<br>|~~1 ~~<br>|
|~~UGS~~<br>|~~1 ~~<br>|~~1 ~~<br>|
|~~CBN~~<br>|~~1000~~<br>|~~100~~<br>|
|~~CBMM~~<br>|~~1000~~<br>|~~100~~<br>|
|~~CBR~~<br>|~~1000~~<br>|~~100~~<br>|
|~~UVO~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~ARG~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~HSA~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~BGM~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~GMM~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~BAS~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~PMM~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~FW~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~ZF1~~<br>|~~5 ~~<br>|~~2 ~~<br>|
|~~ZF2~~|~~5 ~~|~~2 ~~|

Septiembre, 2019 **17**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

1E-01

1E-02

1E-03

1E-04

1E-05

1E-06

1E-07

1E-08

1E-09

1E-10

1E-11

_**Figura 8: Geometría de la ZOR para el modelo actualizado del rajo DMH.**_

Conductividad Hidráulica ZOR Modelo Transiente (cm/s)

UGS UGP CBN CBMM CBR UVO ARG HSA BGM GMM BAS PMM FW

Valor Mínimo Valor Máximo ZOR Capa 1 ZOR Capa 2

_**Figura 9: Valores de las conductividades hidráulicas para cada unidad hidrogeológica de las**_
_**dos capas de la ZOR del modelo numérico actualizado.**_

Septiembre, 2019 **18**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**2.10 Pozos de Bombeo**

Los pozos de bombeo considerados en la actualización del modelo _MINEDW_ del rajo DMH se
muestran en la Figura 10. Estos corresponden a los mismos pozos considerados en el modelo del
año 2018 para este rajo, sin embargo, los caudales de bombeo han sido actualizados a julio de

2019.

La implementación del sistema de drenaje consiste principalmente en interceptar y drenar las aguas
subterráneas de las unidades de gravas (UGS y UGP), en el sector noreste del rajo, de manera de
evitar un aumento de las presiones de poros en las paredes producto de infiltraciones de la recarga
que se produce aguas arriba.

_**Figura 10: Pozos de bombeo para el modelo MINEDW actualizado del rajo DMH.**_

Septiembre, 2019 **19**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**2.11 Sistema de Drenaje**

El sistema de drenaje del modelo actualizado no incorpora nuevos drenes, en comparación con el
modelo _MINEDW_ de diciembre de 2018, por lo tanto, todos los drenes incluidos en este modelo
fueron incorporados en la actualización descrita en este informe.

El _software MINEDW_ detecta de manera automática los drenes que se encuentran sobre la
topografía, y, por ende, que ya no se encuentran en funcionamiento. Esto ocurre con los drenes del
sector este y sureste del rajo DMH, que actualmente se encuentran destruidos, pero de todas formas
fueron incorporados al modelo debido a su funcionamiento previo, cuando aún se encontraban

activos.

Los drenes considerados en la actualización del modelo _MINEDW_ del rajo DMH se muestran en
la Figura 11.

_**Figura 11: Sistema de drenaje del modelo actualizado MINEDW para el rajo DMH.**_

Septiembre, 2019 **20**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**CALIBRACIÓN DEL MODELO HIDROGEOLÓGICO**

La calibración del modelo hidrogeológico actualizado lleva asociada la realización simultánea de
dos procesos de calibración: el balance de masas y los niveles piezométricos:

 - Por un lado, se ha realizado la calibración del balance de masas para representar lo más
fehacientemente posible el modelo conceptual existente y las observaciones de campo
descritas por el personal de la división.

 - Por otro lado, se ha fijado como objetivo que los puntos de observación del modelo
muestren niveles lo más cercanos posibles a los medidos en el piezómetro correspondiente.

Al mismo tiempo, con la finalidad de validar y dar robustez a la calibración obtenida en la
actualización del modelo hidrogeológico, se realiza un análisis de error de calibración, el cual se
hace siguiendo los lineamientos de Barnett et al., (2012) definidos para la _Australian Groundwater_
_Modelling Guidlines_, y el criterio de la _“Guía Para el Uso de Modelos de Aguas Subterráneas en_
_el SEIA”_ (SEA, 2012) Para esto, los datos medidos son comparados en su misma fecha con los
simulados por el modelo, y los niveles piezométricos son contrastados en términos de _RMS_ (Error
Cuadrático Medio), S _RMS_ (Error Cuadrático Medio Estandarizado) y _MAE_ (Error Medio
Absoluto).

**3.1 Calibración del Modelo** _**MINEDW**_ **Estacionario**

El proceso de calibración en régimen estacionario se realiza con el objetivo de estimar los
parámetros hidráulicos (conductividad hidráulica) iniciales de las unidades hidrogeológicas, los
cuales representan el estado pre-minería del sistema hidrogeológico del área de estudio.

3.1.1 Periodo de Calibración

Los datos utilizados para la calibración del régimen estacionario han sido los de 16 piezómetros
ubicados en la zona de estudio, que contienen información de niveles medidos durante el estado
de pre-minería, siendo la gran mayoría de enero de 2011.

3.1.2 Ajuste de Parámetros

Los valores de las conductividades hidráulicas obtenidos en el proceso de calibración se pueden
ver en la Figura 12, junto con los límites mínimos y máximos de cada unidad, determinados a
partir de los ensayos realizados y definidos en la actualización del modelo conceptual (Itasca,
2018). Se observa que todos los valores calibrados se encuentran dentro de estos límites
conceptuales.

Septiembre, 2019 **21**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 12: Valores calibrados de las conductividades hidráulicas para cada unidad**_
_**hidrogeológica del modelo numérico estacionario actualizado.**_

3.1.3 Balance de Masas

La variación en el almacenamiento ha sido suficientemente pequeña en los cálculos finales para
considerarlo despreciable (<0.00 L/s) y alcanzar la condición de modelo estacionario con variación
del almacenamiento nulo. En la Figura 13 se muestra el balance de masas obtenido en la
calibración estacionaria del modelo. Como se puede observar, el agua entra al modelo por la
condición de borde ubicada al norte, con un caudal estabilizado de 59.3 l/s, mientras que salida al
sur está en equilibrio con un caudal de -59.3 l/s. Esto es coherente con lo estimado en el modelo
conceptual, que indica un caudal de entrada dentro del rango de 50 y 75 l/s.

Septiembre, 2019 **22**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

|Col1|Variación<br>Almacenamiento<br>ΔS ≈ 0 L/s|Col3|
|---|---|---|
||||

_**Figura 13: Balance de masas de la calibración estacionaria del modelo MINEDW.**_

3.1.4 Calibración de Niveles Piezométricos

La Figura 14 muestra los resultados obtenidos en la calibración estacionaria de la actualización del
modelo _MINEDW_ del rajo DMH.

_**Figura 14: Resultado de la calibración de niveles obtenida en el modelo estacionario.**_

Para valorar de forma cuantitativa la calibración obtenida, se han calculado los tres índices que
comparan los errores obtenidos en los niveles modelados con los niveles observados. Los índices
utilizados y su formulación se muestran en la Tabla 4.

Septiembre, 2019 **23**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

Los valores obtenidos para estos índices se muestran en la Tabla 5, donde se puede ver que la
calibración cumple con el estándar recomendado en la “ _Australian Groundwater Modelling_
_Guidelines_ ” (Barnett et al, 2012) y en la “ _Guía Para el Uso de Modelo de Aguas Subterráneas en_
_el SEIA”_ (SEA, 2012).

_**Tabla 4. Criterios de error empleados para valorar la calibración de niveles.**_

|Criterio de Error|Fórmula|
|---|---|
|Valor Cuadrático Medio del Residual (RMS):|R<br>R= ඩ1<br>n෍ri<br>2<br>n<br>i=1<br>|
|Valor Cuadrático Medio del Residual<br>Normalizado (SRMS):|SS<br>= 100<br>∆Hඩ1<br>n෍(ri−R)2<br>n<br>i=1<br> <br>|
|Error Medio Absoluto (MAE):<br>|MM= 1<br>n෍ቚhoo,i−hss,iቚ<br>~~n~~<br>i=1<br>|

_**Tabla 5. Valores de los índices de calibración obtenidos para el modelo estacionario.**_

|Criterio de Error|Valor Obtenido|Valor Recomendado|
|---|---|---|
|~~Valor Cuadrático Medio del~~<br>Residual (RMS): <br>|~~11.3 m~~<br>|~~- ~~<br>|
|~~Valor Cuadrático Medio del~~<br>Residual Normalizado (SRMS): <br>|~~6.4 %~~<br>|~~< 10 %~~<br>|
|~~Error Medio Absoluto (MAE):~~<br>|~~9.3 m~~|~~< 25.5 m~~|

Septiembre, 2019 **24**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

**3.2 Calibración del Modelo** _**MINEDW**_ **Transiente**

El proceso de calibración en estado transiente se ha realizado tanto con los datos piezométricos de
la red de monitoreo como con los datos de _seepage_ producido en el rajo. Esto ha permitido
reproducir en el modelo el _stress_ hídrico generado por procesos hidrogeológicos históricos
conocidos y cuantificados que han sucedido en la zona de estudio, modificando los parámetros de

entrada.

Para la calibración de niveles en régimen transiente se han utilizado todos los piezómetros
disponibles, cuya ubicación se puede ver en la Figura 7. Los gráficos de calibración para cada uno
de estos piezómetros con sus sensores se presentan en el Anexo I de este informe.

Esta calibración ha permitido obtener los parámetros de los coeficientes de almacenamiento
específico ( _Ss_ ) y porosidad efectiva ( _Sy_ ) de las diferentes unidades hidrogeológicas, así como los
valores de conductividad hidráulica (K). Esto con el objetivo de obtener un modelo confiable y
robusto que pueda ser utilizado en las simulaciones predictivas con la menor incertidumbre
posible.

En este caso, se ha fijado el objetivo que los puntos de observación del modelo muestren una
variación temporal de niveles lo más cercanos posibles a los medidos en el piezómetro
correspondiente, así como reproducir su tendencia.

3.2.1 Periodo de Calibración

La actualización del modelo hidrogeológico del rajo DMH en _MINEDW_ se ha calibrado en régimen
transiente entre las fechas enero de 2011 (antes de la excavación del rajo) a julio de 2019.

3.2.2 Ajuste de Parámetros

Las propiedades hidráulicas de partida para la calibración del modelo actualizado para cada UH,
fueron obtenidas del modelo _MINEDW_ del año 2018. A partir de estos datos se ha realizado el
proceso de calibración que ha permitido reproducir las variables de estado medidas en campo.

El comportamiento hidráulico de todas las estructuras del modelo se definió de la siguiente

manera:

 - Fallas con orientación este-oeste muestran un carácter de tipo conductoras.

 - Fallas con orientación norte-sur poseen un carácter principalmente de tipo barreras.

Septiembre, 2019 **25**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

La Tabla 6 muestra los valores de las propiedades hidráulicas del modelo numérico _MINEDW_ del
rajo DMH de diciembre de 2018, y los parámetros finales obtenidos en el proceso de calibración
en la actualización de este modelo numérico a julio de 2019 _._ A partir de esta tabla se desprende
que las permeabilidades, así como el almacenamiento específico y la porosidad drenable, se
mantuvieron constantes con respecto a los valores utilizados en el modelo de diciembre de 2018.

_**Tabla 6: Valores de los parámetros hidráulicos calibrados para cada unidad hidrogeológica,**_
_**para los modelos del rajo DMH de diciembre de 2018 y julio de 2019.**_

|Modelo|DMH diciembre 2018|Col3|Col4|DMH Actualizado julio 2019|Col6|Col7|
|---|---|---|---|---|---|---|
|**Unidades**|**K (cm/s)**|**Ss (1/m)**|**Sy**|**K (cm/s)**|**Ss (1/m)**|**Sy**|
|UGP|2.89E-03|1.00E-05|0.3|2.89E-03|1.00E-05|0.3|
|UGS|8.10E-03|1.00E-05|0.3|8.10E-03|1.00E-05|0.3|
|CBN|9.44E-05|1.00E-07|1.00E-05|9.44E-05|1.00E-07|1.00E-05|
|CBMM|6.02E-09|1.00E-07|1.00E-05|6.02E-09|1.00E-07|1.00E-05|
|CBR|7.06E-08|1.00E-07|1.00E-05|7.06E-08|1.00E-07|1.00E-05|
|UVO|6.94E-08|1.00E-07|1.00E-05|6.94E-08|1.00E-07|1.00E-05|
|ARG|2.31E-08|1.00E-07|1.00E-05|2.31E-08|1.00E-07|1.00E-05|
|HSA|2.89E-07|1.00E-07|1.00E-05|2.89E-07|1.00E-07|1.00E-05|
|BGM|2.78E-08|1.00E-07|1.00E-05|2.78E-08|1.00E-07|1.00E-05|
|GMM|3.70E-08|1.00E-07|1.00E-05|3.70E-08|1.00E-07|1.00E-05|
|BAS|3.36E-08|1.00E-07|1.00E-05|3.36E-08|1.00E-07|1.00E-05|
|PMM|1.16E-07|1.00E-07|1.00E-05|1.16E-07|1.00E-07|1.00E-05|
|FW|1.16E-11|1.00E-07|1.00E-05|1.16E-11|1.00E-07|1.00E-05|
|Conductoras|1.16E-06|1.00E-07|1.00E-05|1.16E-06|1.00E-07|1.00E-05|
|Barrera|1.16E-08|1.00E-07|1.00E-05|1.16E-08|1.00E-07|1.00E-05|

La Figura 15 muestra de manera gráfica los valores máximos y mínimos de permeabilidad
reportados para cada unidad hidrogeológica en el modelo conceptual, y que provienen de los
ensayos de terreno, junto con los valores calibrados para cada una de las unidades definidas. Se
observa que todos los valores calibrados se encuentran dentro de los límites conceptuales.

Septiembre, 2019 **26**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 15: Valores de conductividad hidráulica calibrados en el modelo numérico actualizado**_
_**(color azul). En rojo se indican los valores máximos y mínimos de las**_
_**permeabilidades definidas en el modelo conceptual.**_

3.2.3 Balance de Masas

El balance de masas de la actualización del modelo transiente del rajo DMH, será analizado en
función de los caudales de _seepage_, pozos de bombeo, caudal de entrada del modelo y evaporación.

La Figura 16 muestra el comportamiento del caudal de _seepage_ estimado por el modelo numérico
a lo largo de todo el periodo de simulación, donde se observa un valor máximo de 71.7 l/s durante
julio de 2013 y un valor aproximado de 40 l/s para julio de 2019.

El caudal de _seepage_ que aflora en las unidades hidrogeológicas correspondientes a gravas, roca y
fallas, se muestra en la Figura 17, de donde se desprende que el _seepage_ que aflora por las gravas
desde el año 2012 a 2015, es bastante superior al que aflora por la unidades de roca y fallas, y
donde también es posible observar un mayor afloramiento de _seepage_ para las unidades
compuestas de roca, en comparación con las otras unidades, desde el año 2015 hasta 2017, para
continuar con un aumento abrupto en el afloramiento de _seepage_ de las gravas, en julio de 2017.
Con estos datos ha sido posible calcular la relación del caudal de _seepage_ que aflora por las

Septiembre, 2019 **27**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

unidades de gravas, en comparación al total, obteniéndose el gráfico de la Figura 18, donde se
puede ver que para julio de 2019 el afloramiento por las gravas corresponde aproximadamente a

un 60% del total.

El caudal de afloramiento de _seepage_ tiene relación con la excavación de las unidades
hidrogeológicas presentes en el rajo DMH (Figura 19). En particular se observan grandes aumentos
de caudal de _seepage_ cuando se excavan las unidades de grava, que es donde se encuentra la mayor
fuente de agua subterránea. Esto ocurre, por ejemplo, en las etapas tempranas de la excavación del
rajo DMH, como muestra la Figura 19 y la Figura 20, donde se presentan las unidades expuestas
durante enero y agosto del año 2012, cuando se lleva a cabo excavación principalmente en las
unidades de gravas y aumenta drásticamente el caudal de _seepage_ del rajo de 0 a 60 l/s. Esto mismo
se observa durante mayo y septiembre de 2017, donde el caudal de _seepage_ del rajo aumenta de
23 a 52 l/s, debido a la excavación y expansión del rajo hacia el este, profundizando en la unidad
de grava superior (Figura 19 y Figura 22).

Por el contrario, cuando se profundiza mucho el rajo, el caudal de _seepage_ disminuye, ya que se
expone más área de roca, en comparación con la superficie expuesta de las gravas. Un ejemplo de
esto se observa durante junio de 2013 y abril de 2015, donde existe una disminución del caudal de
_seepage_ en todo el rajo de 74 a 39 l/s (Figura 19). La Figura 21 muestra el rajo de DMH para estas
fechas, donde es posible notar una gran profundización del centro y norte del rajo y una mayor
exposición de las unidades de roca. Al mismo tiempo, también se observa una mayor excavación
de las gravas en el sector sur, que son las responsables de que aún exista un caudal significativo
de _seepage_ aflorando en el rajo, a pesar de su disminución en el tiempo.

Cabe destacar que el agua que aflora ( _seepage_ ) en el modelo numérico por las unidades de grava,
roca y fallas, no corresponde necesariamente al agua que aportan las distintas unidades, ya que el
porcentaje de agua que aportan las gravas y las rocas, por la condición de borde de caudal constante
al noreste ha sido estimado en 97.5 y 2.5 %, respectivamente, siendo el caudal aportante de las
gravas bastante superior al que se observa como afloramiento en el rajo, en estas mismas unidades
(Tabla 7). Esto se debe probablemente a la existencia e implementación en el modelo numérico de
la ZOR, la cual genera que el agua proveniente de las gravas aflore por una unidad de roca
subyacente a esta, debido al aumento de permeabilidad de esta última, en la zona del rajo. Esto es
coherente con lo observado en la realidad, donde la mayor parte de afloramiento de _seepage_ se ve
en el límite del contacto entre las gravas y la roca.

Septiembre, 2019 **28**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 16: Caudal de seepage total estimado por el modelo numérico transiente actualizado**_
_**del rajo DMH.**_

_**Figura 17: Caudal de seepage que aflora en las unidades hidrogeológicas que corresponden a**_
_**grava, roca y fallas, en el modelo numérico actualizado del rajo DMH.**_

Septiembre, 2019 **29**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 18: Porcentaje de caudal de seepage que aporta la unidad de gravas.**_

_**Figura 19: Caudal de seepage y excavación del rajo DMH, a medida que transcurre el tiempo**_

_**de simulación.**_

Septiembre, 2019 **30**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 20: Unidades hidrogeológicas expuestas en el rajo DMH durante enero y marzo de**_

_**2012.**_

_**Figura 21: Unidades hidrogeológicas expuestas en el rajo DMH durante junio de 2013 y abril**_

_**de 2015.**_

Septiembre, 2019 **31**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 22: Unidades hidrogeológicas expuestas en el rajo DMH durante mayo y septiembre de**_

_**2017.**_

_**Tabla 7: Porcentajes de caudal aportante y de afloramiento de seepage en el modelo, de las**_
_**unidades de grava, roca y fallas.**_

|Unidad|Aporte por Condición de<br>Borde Flujo Constante<br>(Norte)|Afloramiento de Seepage|
|---|---|---|
|~~Gravas~~<br>|~~97.5%~~<br>|~~57%~~<br>|
|~~Roca~~<br>|~~2.5%~~<br>|~~41%~~<br>|
|~~Fallas~~<br>|~~0%~~|~~2%~~|

En la Figura 23 es posible observar el caudal de evaporación calculado por el modelo numérico
actualizado, a medida que transcurre el tiempo de simulación, donde se desprende que el caudal
de evaporación del rajo de DMH, a julio de 2019, es de aproximadamente 23 l/s. Este incremento
en el caudal de evaporación a medida que transcurre el tiempo de simulación se debe al aumento
del área de exposición de zonas de _seepage_, a medida que se excava el rajo.

Además, en la Figura 24 se muestra el caudal de los pozos de bombeo que se modelaron en el rajo
de DMH, cuyos valores han sido impuestos según los valores de caudal de extracción real. En esta
figura es posible notar que el caudal de extracción a julio de 2019 es de aproximadamente 28 l/s.

Septiembre, 2019 **32**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

Al mismo tiempo, el caudal que ingresa por el extremo noreste del modelo, mediante la condición
de borde de nivel de agua fijo (Figura 2), corresponde a 76 l/s, siendo coherente con lo estimado
en el modelo conceptual del rajo DMH.

Por último, en la Figura 25 se expone el comportamiento del residual del modelo numérico
actualizado, que representa el equilibrio del balance de masas para cada tiempo de cálculo, el cual
según la “ _Australian Groundwater Modelling Guidelines_ ” (Barnett _et al_, 2012) al ser menor a 1%

se considera como un modelo estabilizado numéricamente.

_**Figura 23: Caudal estimado de evaporación según el modelo numérico actualizado.**_

Septiembre, 2019 **33**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

_**Figura 24: Caudal de los pozos de bombeo simulados en el modelo de régimen transiente.**_

_**Figura 25: Comportamiento del % residual para cada periodo de cálculo del modelo numérico**_

_**actualizado.**_

Septiembre, 2019 **34**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

3.2.4 Calibración de Niveles Piezométricos

CODELCO, División Ministro Hales

Para realizar la evaluación del error en la calibración del modelo en régimen transiente, se han
utilizado todos los datos medidos disponibles de los piezómetros. Estas medidas se comparan por
fecha con la misma que entrega el modelo numérico, y los niveles son contrastados en términos de
los indicadores presentados anteriormente en la Tabla 4.

Los valores obtenidos para estos índices se muestran en la Tabla 8, donde se puede ver que la
calibración cumple con el estándar recomendado en la “ _Australian Groundwater Modelling_
_Guidelines_ ” (Barnett et al, 2012) y en la “ _Guía Para el Uso de Modelo de Aguas Subterráneas en_
_el SEIA”_ (SEA, 2012).

_**Tabla 8: Valores de los índices de calibración obtenidos para el modelo transiente actualizado.**_

|Criterio de Error|Valor Obtenido|Valor Recomendado|
|---|---|---|
|~~Valor Cuadrático Medio del~~<br>Residual (RMS): <br>|26.7 m|-|
|~~Valor Cuadrático Medio del~~<br>Residual Normalizado (SRMS): <br>|5.2 %<br>|< 10 %<br>|
|~~Error Medio Absoluto (MAE):~~|~~20.1 m~~|~~< 25.5 m~~|

En la Tabla 9 se muestra la comparación de los valores de RMS, SRMS y MAE obtenidos para el
modelo actual y el modelo realizado para diciembre del año 2018 por Itasca, donde se puede
observar que los valores son bastante similares en ambos modelos, siendo levemente inferiores
para los valores de RMS y SRMS, y levemente superior para el índice de MAE.

_**Tabla 9: Valores de índices de calibración obtenidos para el modelo de diciembre de 2018 y**_
_**para el modelo actualizado de julio de 2019.**_

|Modelo MINEDW|RMS (m)|SRMS (%)|MAE (m)|
|---|---|---|---|
|~~Diciembre 2018~~<br>|~~27.4~~<br>|~~5.3~~<br>|~~19.3~~<br>|
|~~Julio 2019~~<br>|~~26.7~~|~~5.2~~|~~20.1~~|

3.2.5 Calibración de Zonas de _Seepage_

Además de la calibración de niveles y del balance de masas, se han tenido en cuenta las zonas de
_seepage_ observadas en el rajo en la visita realizada en julio de 2019, además de las históricas que
se han podido observar a través de _Google Earth._

Septiembre, 2019 **35**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo
Ministro Hales

CODELCO, División Ministro Hales

Los resultados del modelo en comparación con las observaciones de campo se muestran en la
Figura 26 y la Figura 27, de las que se puede concluir que el modelo numérico actualizado logra
reproducir las zonas de afloramiento, especialmente las que se encuentran en el contacto grava
roca.

Septiembre, 2019 **36**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

_**Figura 26: Vista desde Mirador oeste hacia noreste del rajo DMH en visita de julio de 2019 y comparación con resultado de**_
_**seepage entregado por MINEDW para esta misma fecha.**_

Septiembre, 2019 **37**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

_**Figura 27: Vista desde Mirador norte hacia sureste del rajo DMH en visita de julio de 2019 y comparación con resultado de**_
_**seepage entregado por MINEDW para esta misma fecha.**_

Septiembre, 2019 **38**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro
Hales

**COMENTARIOS FINALES Y CONCLUSIONES**

# A partir de las tareas desarrolladas se puede concluir lo siguiente:

CODELCO, División Ministro Hales

 El modelo numérico ha sido actualizado utilizando el modelo UGTB 2019, modelo

estructural 2019, y modelo conceptual actualizado por Itasca en 2018.

 Se ha incorporado el plan de explotación real desde enero de 2019 hasta julio de 2019,
así como el plan utilizado en el modelo del año 2018, que incluye abril de 2011 a

diciembre 2018 de forma mensual.

 - El modelo estacionario actualizado fue calibrado satisfactoriamente con base en 16

piezómetros con medida disponible para 2011, el índice SRMS para la calibración

estacionaria es de 6.4%, considerado como bueno de acuerdo con la “ _Australian_

_Groundwater Modelling Guidelines_ ” (Barnett _et al_, 2012).

 El modelo transiente actualizado fue calibrado con todos lo piezómetros disponibles,
tanto abiertos como de cuerda vibrante, desde enero de 2011 a julio de 2019,
entregando un índice SRMS de 5.2%, considerado como bueno de acuerdo con la
“ _Australian Groundwater Modelling Guidelines_ ” (Barnett _et al_, 2012).

 El modelo transiente actualizado logra reproducir el balance de masas, entregando un
valor de _seepage_ para julio de 2019 aproximado de 40 l/s.

 - Las zonas de _seepage_ observadas en campo también son reproducidas por el modelo

numérico.

A modo de recomendación, se aconseja incluir para la siguiente actualización del modelo
hidrogeológico del rajo DMH, una revisión exhaustiva del comportamiento de las fallas
según lo observado en los piezómetros, así como la existencia de las mismas. Esto con el
objetivo de lograr un modelo que represente aún más los procesos que ocurren en la realidad,
sobre todo en zonas con piezómetros que se encuentran construidos sobre estructuras, y cuyos
niveles calculados pueden estar aún mejor ajustados a los niveles observados.

# Finalmente, el modelo numérico construido y calibrado se encuentra disponible para realizar

las simulaciones predictivas necesarias, pudiendo evaluar distintos escenarios de drenaje y/o
distintos planes de explotación para el rajo.

Septiembre, 2019 **39**
ITASCA - INF - 4026.004.01 ITASCA Chile

|

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro
Hales

CODELCO, División Ministro Hales

**REFERENCIAS**

Barnet B., Townley LR., Post V., Evans RE., Hunt RJ., Peeters L., Richardson S., Werner
AD., Knapton A and Boronkay A., (2012) “Australian Groundwater Modelling
Guidelines”, June 2012. National Water Commission Australia, Waterlines Report

Series No. 82, ISBN:978-1-921853-91-3.

Beale, G. (2011) “Creation of a Conceptual Model of Pore Pressures in a Fractured Rock
Slope,” Draft Report to Large Open Pit Project.

Beale, G., and Read, J. (2013) “Guidelines for Evaluating Water in Pit Slope Stability”,
CSIRO Publishing, Collingwood, Australia.

Hoek, E., J. Hutchinson, K. Kalenchuk and M. Diederichs. (2010) “Appendix 3 -- Influence
of In Situ Stresses on Open Pit Design,” in _**Guidelines for Open Pit Design**_, pp. 437445. J. Read and P. Stacey Eds. Collingwood, Vic., Australia: CSIRO Publishing.

Itasca Chile SpA. (2014) “Descripción de Información de Entrada Utilizada por Itasca en

Estudios de Modelamiento Numérico 3D” Informe ISA-536.003/2014-02

Itasca Chile SpA. (2018) “4026.002 - Actualización Modelo Conceptual_Rev0”.

Itasca Chile SpA. (2019) “4026.002 - Modelo Numérico Hidrogeológico 3D Rajo Ministro

Hales”.

Itasca Consulting Group, Inc. (2012) “Assessment of the Effect of Water Pressures on the
Stability of Closely Jointed Rock”.

Itasca Denver, Inc., (2018). MINEDW - 3D Groundwater Flow Code, Version 3.05. Denver:

Itasca.

Rutqvist, J., L. Bogesson, M. Chijimatsu, J.Hernelind, L. Jing, A. Kobayashi and S. Nguyen.
(2009) “Modeling of Damage, Permeability Changes and Pressure Responses during

Excavation of the TSX Tunnel in Granitic Rock at URL, Canada,” _Environ. Geol.,_

_**57**_, 1263-1274.

Servicio de Evaluación Ambiental, SEA, (2012) “Guía Para el Uso de Modelos de Agua
Subterránea en el SEIA”, Santiago, Chile.

Septiembre, 2019 **40**
ITASCA - INF - 4026.004.01 ITASCA Chile

|

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro
Hales

CODELCO, División Ministro Hales

Sullivan, T. D. (2007) “Hydromechanical Coupling and Pit Slope Movements,” in _Slope_
_Stability 2007 (Proceedings, 2007 International Symposium, Rock Slope Stability in_
_Open Pit Mining and Civil Engineering, Perth, Australia, September 2007)_, Keynote
Address, pp. 3-43. Y. Potvin, Ed. Perth: Australian Centre for Geomechanics.

Septiembre, 2019 **41**
ITASCA - INF - 4026.004.01 ITASCA Chile

|

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro
Hales

CODELCO, División Ministro Hales

**ANEXO 1 GRÁFICOS DE CALIBRACIÓN DE PIEZÓMETROS**

Septiembre, 2019 **42**
ITASCA - INF - 4026.004.01 ITASCA Chile

|

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **43**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **44**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **45**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **46**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **47**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **48**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **49**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **50**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **51**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **52**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **53**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **54**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **55**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **56**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **57**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **58**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **59**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **60**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **61**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **62**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **63**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **64**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **65**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **66**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **67**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **68**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **69**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **70**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **71**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **72**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **73**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **74**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **75**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **76**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **77**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **78**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **79**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **80**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **81**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **82**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **83**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **84**
ITASCA - INF - 4026.004.01 ITASCA Chile

Actualización del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales CODELCO, División Ministro Hales

Septiembre, 2019 **85**
ITASCA - INF - 4026.004.01 ITASCA Chile