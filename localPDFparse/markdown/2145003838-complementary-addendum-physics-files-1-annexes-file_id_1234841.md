---
title: Sin título
author: Keith Massey
date: D:20200811115815-04'00'
language: es
type: report
pages: 18
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 1.0 RESUMEN DE LOS MODELOS DE CODELCO DMH DEL SISTEMA DE AGUA SUBTERRÁNEA
-->

CORPORACION NACIONAL DEL COBRE

# ANEXO 1.0 RESUMEN DE LOS MODELOS DE CODELCO DMH DEL SISTEMA DE AGUA SUBTERRÁNEA

ADENDA COMPLEMENTARIA DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO “AUMENTO MOVIMIENTOS

MINA”

_Anexo 1.0_Resumen global de los modelos_

**ÍNDICE DE CONTENIDO**

Resumen de los modelos de Codelco DMH del sistema de agua subterránea ............................................ 3

1. Introducción ...................................................................................................................................... 3

2. Propósito de los modelos.................................................................................................................. 3

3. Etapas principales en el desarrollo de un modelo ............................................................................ 5

Etapa 1 - Recopilación y revisión de datos ........................................................................................... 5

Etapa 2 - Preparación del modelo conceptual ..................................................................................... 5

Etapa 3 - Construcción y calibración del modelo numérico ................................................................. 6

4. Descripción de los modelos operados por Codelco DMH................................................................. 8

Modelo regional de la Cuenca de Calama (Pampa Talabre) en Modflow 2000 ................................... 8

Modelo regional de la Cuenca de Calama (Pampa Talabre) en Modflow USG ................................... 12

Modelo Operacional del Rajo DMH en MINEDW ............................................................................... 14

**ÍNDICE DE TABLAS**

Tabla 1. Historial de la modelación de Codelco relevante al Proyecto “Aumento Movimientos Mina” ...... 8
Tabla 2. Unidades Hidrogeológicas del Área de Estudio............................................................................... 9

**ÍNDICE DE FIGURAS**

Figura 1. Dominios del modelo regional en Modflow y el modelo operacional del Rajo DMH en MINEDW

...................................................................................................................................................................... 4

Figura 2. Distribución de pozos de drenaje al noreste del Rajo DMH ........................................................ 11

Figura 3. Ejemplo de una malla Quadtree con densificación de las celdas en zonas de particular interés 13

Figura 4. Refinamiento de la malla triangular en el modelo MINEDW para representar el detalle de los

bancos del Rajo DMH y las estructuras de relevancia hidrogeológica y geotécnica .................................. 16

Figura 5 Distribución de pozos de drenaje al noreste del Rajo DMH en el Modelo Operacional ........ 17

Figura 6 Distribución de drenes pasivos y el túnel del Rajo DMH en el Modelo Operacional ............. 18

Página 2 de 18

_Anexo 1.0_Resumen global de los modelos_

## Resumen de los modelos de Codelco DMH del sistema de agua subterránea

### 1. Introducción

Existen 3 modelos numéricos relevantes a la estimación de la tasa de drenaje del Rajo DMH, construidos

con distintos códigos numéricos, dos versiones de Modflow (Modflow 2000 y Modflow USG), publicado

por el Servicio de Geología de los Estados Unidos [ _United States Geological Survey_ (USGS)] y MINEDW,

publicado por Itasca. Los tres modelos son:

 - Modelo regional en Modflow 2000 de la Cuenca de Calama (Pampa Talabre).

 - Modelo regional en Modflow USG (versión actual del modelo regional).

 - Modelo operacional del Rajo DMH en MINEDW.

La Figura 1 es un mapa que muestra la extensión geográfica de estos modelos.

La evaluación ambiental del Proyecto en Evaluación reportada en la Adenda I de la DIA, se base en

simulaciones predictivas realizadas con el modelo regional en Modflow 2000 de la Cuenca de Calama.

En 2020, la empresa consultora Arcadis, hizo la translación de Modelo en Modflow 2000 al código

Modflow USG. Además, se logró mejoras en la calibración del modelo en la zona de la cabecera del río

San Salvador. Este trabajo está resumido más adelante en este documento.

El Anexo 1 de la Adenda Complementaria del DIA “Aumento Movimientos Mina” incluye copias de

informes relevantes sobre los modelos conceptuales y numéricos que el Titular ha desarrollado a través

de la historia del Proyecto DMH.

### 2. Propósito de los modelos

Existen decenas de miles de modelos de sistemas de agua subterránea [1] en todo el mundo. Se desarrollan

modelos para usarlos como herramientas para apoyar en la protección de recursos hídricos y la gestión

de su utilización sustentable.

Los primeros modelos numéricos fueron desarrollados en la segunda parte de la década de los sesenta [2] .

Durante las décadas subsecuentes, su utilización para simular sistemas de agua subterránea creció, y para

la década de los ochenta llegaron a ser una herramienta indispensable para los estudios hidrogeológicos.

En vista de su importancia para la evaluación de los efectos que la actividad humana pueda producir sobre
los recursos hídricos, el Servicio de Evaluación Ambiental (SEA) publicó una guía [3] sobre el uso de modelos

en evaluaciones de impacto ambiental.

1 Un sistema de agua subterránea o sistema hidrogeológico pueda incluir uno o más acuíferos separados por
unidades de menor permeabilidad denominadas acuitardos.

2 Yangxiao, Z & A Wenpeng, L (2011). A review of regional groundwater flow modeling
https://www.sciencedirect.com/science/article/pii/S167498711100020X

3 SEA (2012). Guía Para el Uso de Modelos de Aguas Subterráneas en el SEIA. ISBN 978-956-9076-12-1
[https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_aguas_subterraneas_seia.pdf](https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_aguas_subterraneas_seia.pdf)

_Anexo 1.0_Resumen global de los modelos_ _Página 3 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Figura 1. Dominios del modelo regional en Modflow y el modelo operacional del Rajo DMH en MINEDW**

_Anexo 1.0_Resumen global de los modelos_ _Página 4 de 18_

_Anexo 1.0_Resumen global de los modelos_

Los modelos utilizados por Codelco DMH en soporte de la DIA del Proyecto “Aumento Movimientos Mina”

tienen escalas de interés y propósitos distintos, como se resume a continuación:

 - El modelo regional en el código numérico Modflow USG (y anteriormente en Modflow 2000)

cubre un área de estudio amplia (Figura 1) que corresponde a una escala de interés regional o

distrital. Su propósito es simular el comportamiento del sistema de agua subterránea a esta

escala, con zonas de interés particular que incluyen:

~ Tranque Talabre y la demás infraestructura minera de Codelco en la zona, incluyendo las

instalaciones de DMH.

~ Los salares Brinckerhoff y Rudolph.

~ El río Loa y sus afluentes en la zona, incluyendo los ríos Salado y San Salvador.

~ El Oasis de Calama.

 - El modelo operacional, implementado en el código numérico MINEDW, es a una escala local, muy
detallada (Figura 1). Codelco DMH lo utiliza como una herramienta en apoyo de la gestión

hidro-geotécnica del Rajo DMH. Permite optimizar la seguridad y eficiencia de la operación

minera, asegurando que las presiones de poros de las fases espaciales del yacimiento, próximas

a excavarse, están debidamente drenadas (despresurizadas) para evitar derrumbes de la pared

del rajo. La revisión y planificación continúa de la implementación en terreno del plan de drenaje

del Rajo DMH, al que este modelo aporta, además permite que Codelco DMH extraiga solamente

el caudal de agua necesario (agua del minero) para garantizar la seguridad de los trabajadores

desempeñándose en el rajo y su entorno inmediato.

### 3. Etapas principales en el desarrollo de un modelo

-
Etapa 1 Recopilación y revisión de datos

La primera etapa durante el desarrollo de un modelo es la revisión de toda la información

hidrogeológicamente relevante y la identificación y obtención de datos adicionales que se requieren para

formar un entendimiento robusto del funcionamiento de un sistema de agua subterránea.

-
Etapa 2 Preparación del modelo conceptual

Posteriormente, en base a la información recopilada, se prepara un modelo conceptual que describe y

explica los aspectos relevantes del sistema hidrogeológico. El modelo conceptual incluirá:

 - Mapas y secciones geológicas e hidrogeológicas.

 - Una base de datos de la información relevante, que puede incluir:

`o` Las observaciones registradas en terreno de nivel y calidad química de las aguas

subterráneas.

`o` Las observaciones registradas en terreno de caudal y calidad química de las aguas

superficiales.

_Anexo 1.0_Resumen global de los modelos_ _Página 5 de 18_

_Anexo 1.0_Resumen global de los modelos_

`o` Los datos registrados en estaciones meteorológicas dentro del dominio del modelo y en

cercanía geográfica a él, incluyendo precipitación y evaporación potencial.

`o` La información disponible del mapeo geológico e hidrogeológico de las perforaciones,

sondajes y pozos en el dominio del modelo.

`o` La información disponible sobre el diseño de pozos en el dominio del modelo, que detalla

los tramos donde la tubería de revestimiento está en contacto con el sistema de agua

subterránea (secciones de tubería ranuradas), los tramos donde la tubería de

revestimiento está sin ranuras (casing ciego) y los intervalos de filtros y sellos emplazados

en el espacio anular alrededor del revestimiento del pozo.

`o` Los registros disponibles de la extracción real de agua subterránea de pozos en el dominio

del modelo, y la información acerca de los derechos de aprovechamiento de agua

asociados con estos.

`o` Datos e interpretaciones geofísicas del terreno.

`o` Datos isotópicos.

 - Un balance hídrico que describe los flujos de agua subterránea entrando y saliendo del dominio

del modelo, incluyendo la interacción entre los sistemas de agua subterránea y superficial.

-
Etapa 3 Construcción y calibración del modelo numérico

Se implementa el modelo conceptual como un modelo numérico, utilizando un código apropiado, por

ejemplo, una de las versiones de Modflow, MINEDW, Feflow, o varios otros códigos con un historial de

aplicación en la hidrogeología. El modelo numérico es una representación del modelo conceptual, y por

lo tanto, es una representación del sistema real. Como tal, el modelo numérico debería poder reproducir

a un nivel de precisión adecuada al comportamiento observado del sistema real. Para lograr esta

habilidad, se sujeta el modelo numérico a un proceso de calibración, en la cual el modelo numérico tiene

que reproducir datos observados en terreno, principalmente niveles de agua subterránea, registrado en

pozos de monitoreo dentro del dominio del modelo. La calibración de modelos numéricos está
ampliamente tratada en la literatura científica, por ejemplo, por Anderson et al (2015) [4] . Hay dos etapas

en el proceso de calibración, como se describe a continuación.

La primera etapa es la calibración del modelo en _régimen permanente_ . Esta busca que el modelo replique

un conjunto de niveles representativos de las condiciones hidrogeológicas iniciales en el sistema

hidrogeológico, antes de cualquier perturbación de las condiciones, por ejemplo, debido a actividades

humanas o cambios de clima. Como se describe en la guía del SEA mencionada arriba, se califica la

precisión con la cual el modelo logra reproducir un nivel real o _target_, por calcular el residual, también

conocido como el error, que es:

nivel observado
Residual =

nivel observado nivel simulado por elen terreno modelo numérico

modelo numérico

4 Anderson M, Woessner W, & Hunt R (2015). Applied Groundwater Modeling - Simulation of Flow and Advective
Transport (2nd Edition). Academic Press. ISBN 9780120581030.

_Anexo 1.0_Resumen global de los modelos_ _Página 6 de 18_

_Anexo 1.0_Resumen global de los modelos_

Los niveles medidos en terreno tienen unidades de metros sobre el nivel del mar (msnm) y el residual está

en metros. Cómo se explica en la guía del SEA, se puede usar el conjunto de residuales para determinar

otras estadísticas, incluyendo:

 - El error medio absoluto (MAE, _mean absolute error_ )

 - La raíz del error cuadrático medio (RMSE, _root mean absolute error_ )

 - El error cuadrático medio normalizado (NRMS o NRMSE, _normalized root mean absolute error_ )

Estas estadísticas permiten describir la bondad de la calibración del modelo numérico con respecto a los

datos observados en terreno. El modelo regional en Modflow USG, por ejemplo, tiene un NRMS inferior

a 5%, considerando un conjunto de 255 puntos de calibración, como se describe en el informe incluido en

el Anexo 1.8 de esta Adenda Complementaria. Por lo tanto, la bondad de la calibración del modelo

regional se puede considerar como buena.

Posteriormente a la calibración en régimen permanente, se procede a realizar la calibración en régimen

transitoria. Durante la calibración en régimen transitoria se busca reproducir la variación histórica que ha

sido registrada en terreno del nivel de agua subterránea en un conjunto de pozos. En esta etapa, se trata

de replicar las _tendencias_ de nivel que se observan en el hidrograma de niveles de agua subterránea,

registrado en terreno en cada pozo del conjunto de calibración. Un modelo numérico con una buena

calibración en régimen transitoria, simulará hidrogramas de nivel en sus puntos de calibración que

reproducen las tendencias (fluctuaciones temporales) observadas en el hidrograma de niveles medidos

en terreno.

Si, al final del proceso de la calibración en régimen permanente, un pozo queda con un residual cerca de

cero metros, entonces, el hidrograma simulado por el modelo numérico será sobrepuesto al hidrograma

de niveles medidos en terreno. Mientras, si el residual del pozo al final del proceso de calibración en

régimen permanente tiene cierta magnitud, por ejemplo 5 m, entonces, el hidrograma simulado por el

modelo numérico será paralelo a, pero distanciado u _offset_ de, el hidrograma observado en terreno. Esta

es la situación que se observa en algunos de los hidrogramas simulados por el modelo regional en

Modflow USG.

Posterior a la calibración del modelo en régimen transitoria, se revisará la calibración periódicamente, por

ejemplo, cada 2 años, actualizándola con la incorporación de nuevos datos observados en terreno durante

el tiempo acumulado desde la finalización de la calibración inicial. Además, se puede _validar_ el modelo

periódicamente. La validación del modelo involucra la comparación de los niveles simulados por el

modelo, con datos observados en terreno. Si hay un buen acuerdo entre los datos simulados y los datos

medidos en terreno, se confirma que el modelo sigue como una representación adecuada del sistema

real. Si el proceso de validación no rinde un buen resultado, entonces esto indica que el Modelador

debería revisar si hubo cambios en el sistema real (por ejemplo, el inicio de una actividad humana que

falta aún incluir en el modelo conceptual e incorporar en el modelo numérico). Sí es necesario, se procede

a optimizar la calibración del modelo en régimen transitorio, relativa al historial completo de datos

observados en terreno.

_Anexo 1.0_Resumen global de los modelos_ _Página 7 de 18_

_Anexo 1.0_Resumen global de los modelos_

### 4. Descripción de los modelos operados por Codelco DMH

A continuación, se describen los modelos utilizados por Codelco DMH para la gestión del recurso hídrico

y para apoyar en la óptima y segura operación de su recinto minero.

La presentar un listado de los modelos que son relevantes al Proyecto “Aumento Movimientos Mina”.

Junto con una descripción del modelo, la tabla indica el autor del estudio, su año de emisión y el número

de anexo de esta Adenda Complementaria en lo cual se incluye una copia del informe en cuestión.

**Tabla 1. Historial de la modelación de Codelco relevante al Proyecto “Aumento Movimientos Mina”**

|Descripción|Autor|Año|N°<br>Anexo|
|---|---|---|---|
|Modelo numérico en soporte de EIA del Proyecto Mansa Mina|CPH Consultores Ltda|2005|1.1|
|Modelo conceptual Pampa Talabre|Knight Piésold Consulting|2009|1.2|
|Modelo numérico Pampa Talabre|Knight Piésold Consulting|2010|1.3|
|Actualización de la calibración del modelo numérico de 2010 de Knight<br>Piésold|Hidromas|2012|1.4|
|Actualización de la calibración del modelo numérico de 2012 de Hidromas|Hidromas|2015|1.5|
|Actualización de la calibración del modelo numérico de 2015 de Hidromas|Montgomery &<br>Associates|2018|1.6|
|Simulaciones en soporte la DIA con el modelo numérico de Montgomery &<br>Associates de 2018|Codelco|2019|1.7|
|Actualización de la calibración del modelo numérico de 2015 de<br>Montgomery & Associates de 2018 y traslación del modelo de Modflow<br>2000 a Modflow USG.|Arcadis|2020|1.8|
|Modelo conceptual hidro-geotécnico local operacional del Rajo DMH|Itasca|2019|1.9|
|Modelo numérico hidro-geotécnico local operacional del Rajo DMH|Itasca|2019|1.10|

**Modelo regional de la Cuenca de Calama (Pampa Talabre) en Modflow 2000**

Este modelo numérico fue construido y calibrado por Knight Piésold en base a su modelo conceptual del

año 2009. Posteriormente, la empresa consultora Hidromas (2012), lo actualizó. El modelo está

implementado en el código numérico a diferencias finitas, _Modflow 2000_, publicado por el Servicio de
Geología de los Estados Unidos [United States Geological Survey (USGS)]. [5]

5 _Harbaugh AW, Banta ER, Hill MC & McDonald MG. Modflow 2000, The U.S. Geological Survey Modular_

_Ground-Water Model - User Guide to Modularization Concepts and the Ground-Water Flow Process. Open-_
_[File Report 2000-92. https://doi.org/10.3133/ofr200092](https://doi.org/10.3133/ofr200092)_

_Anexo 1.0_Resumen global de los modelos_ _Página 8 de 18_

_Anexo 1.0_Resumen global de los modelos_

La familia de códigos Modflow es considerado un estándar mundial para la simulación de sistemas de

agua subterránea y sus interacciones con cuerpos de aguas superficiales y actividades antrópicas. El

modelo fue construido usando la plataforma de diseño _Visual Modflow 2009_, publicado por la empresa
canadiense, Waterloo Hydrogeologic Inc. [6]

En el año 2015, Hidromas extendió el dominio del modelo hacia el oeste, así incorporando la mayor parte

del Oasis de Calama, y se actualizó la calibración del modelo. En 2018, la empresa consultora, Montgomery

& Associates actualizó la calibración del modelo. Durante 2020, Arcadis ha actualizado la calibración del

modelo. La secuencia de informes preparados para Codelco Norte y DMH es como sigue:

1) CPH y Asociados (jul 2005). Modelo hidrogeológico integrado sector Calama Pampa Talabre.

2) Knight Piésold (dic 2009). Modelamiento Hidráulico Tranque Talabre y su Relación con los

Acuíferos y Cauces Superficiales. Elaboración del Modelo Conceptual. Knight Piésold Ref:
N°SA202-00039/20-9.

3) Knight Piésold. (2010). Modelamiento Hidráulico Tranque Talabre y su Relación con los Acuíferos

y Cauces Superficiales. Elaboración del Modelo Numérico.

4) Hidromas (dic 2012). Servicio de Construcción y Validación de Modelamiento Numérico.

Modelación Hidrogeológica del Acuífero de Calama.

5) Hidromas (dic 2015). Informe Final Modelo Numérico de Flujo Efecto de Drenaje del Rajo DMH.

6) Montgomery & Associates Consultores Ltda (ago 2018). Actualización Modelo Numérico Cuenca

Calama - Drenaje Rajo División Ministro Hales.

7) Arcadis (may 2020). Actualización Modelo Hidrogeológico Numérico 3D de Flujo y Transporte de

Sulfatos - Tranque Talabre. Simulaciones Para Evaluar Efectos del Desagüe Futuro del Rajo de

DMH. Arcadis Ref: N°5228-0000-RH-INF-002_B.

El modelo regional en Modflow 2000 incluye 3 capas ( _layers_ ) para su discretización espacial vertical que

permite representar la geometría de las unidades hidrogeológicas del área de estudio, resumidas en la

Tabla 2.

**Tabla 2. Unidades Hidrogeológicas del Área de Estudio**

|Unidad<br>Hidrogeológica|Descripción|Notas|
|---|---|---|
|UH-1|Sedimentos recientes (gravas y arenas no<br>consolidadas)|Generalmente seca, si no forma una<br>extensión vertical del Acuífero Superior|
|UH-2|Calizas y areniscas calcáreas de la Formación<br>El Loa|Acuífero Superior|
|UH-4|Limos y arcillas de la Formación El Loa|Acuítardo|
|UH-5|Acuífero de Gravas de la Formación Calama|Acuífero Inferior|
|UH-6|Basamento de rocas pre-Terciarias|Acuícludo|

6 [https://www.waterloohydrogeologic.com/](https://www.waterloohydrogeologic.com/)

_Anexo 1.0_Resumen global de los modelos_ _Página 9 de 18_

_Anexo 1.0_Resumen global de los modelos_

La UH-6 no está simulada explícitamente en el modelo regional, donde el techo de la UH-6 se considera

como una condición de borde de no flujo. No obstante, el modelo operacional local en MINEDW simula

el basamento rocoso de la UH-6 para poder determinar la distribución de presiones de poro, y como éstas

evolucionarán a través de la vida operacional y el periodo post cierre del Rajo DMH.

La grilla numérica del modelo regional en Modflow 2000 está orientada norte-sur, es decir que es sin

rotación. Usa una discretización espacial variable para mayor eficiencia computacional. Esto permite

obtener un mayor nivel de detalle (mayor densidad geográfica de niveles y flujos simulados) en sectores

de particular interés, tales como el rajo DMH y los cauces de los ríos Loa y San Salvador. En el sector del

Rajo DMH, la grilla del modelo consiste en celdas de 90 m x 90 m. Afuera de estos sectores, la grilla del

modelo es de 180 m x 180 m.

La discretización temporal aplicada en las simulaciones predictivas realizadas con el modelo regional en

Modflow 2000, considera períodos de estrés, o _stress periods,_ anuales (intervalos de tiempo dentro de los

cuales, las condiciones de borde matemáticas de la simulación se mantienen constantes). Se subdivide

cada período de estrés en 10 pasos de tiempo, o _time steps_, para permitir el desarrollo eficiente de la

simulación numérica.

El modelo usa una variedad de condiciones de borde:

 - El modelo incorpora zonas de recarga meteórica y antrópica, según corresponda, sobre toda su

extensión geográfica.

 - Se usan condiciones de borde de tipo nivel conocido ( _constant head cells_ ) para representar flujos

de agua subterránea que entran y salen de los límites geográficos del dominio del modelo.

 - Pozos de bombeo dentro del dominio del modelo, tales como los pozos de desagüe perimetrales
del rajo DMH, ubicados al norte y noreste del rajo (Figura 2), están representados por la condición

de borde de tipo pozo ( _well_ ) en el modelo.

 - Condiciones de borde de tipo dren ( _drain cells_ ) representan zonas de descarga de agua

subterránea, por ejemplo, en la cabecera del río San Salvador, las vertientes del Oasis de Calama

y en el Rajo DMH. La magnitud del flujo está condicionada por la _conductancia_ del dren, que

depende de la conductividad hidráulica vertical del medio hidrogeológico. Las celdas dren

solamente permiten la descarga de agua subterránea.

 - Condiciones de borde de tipo río ( _river cells_ ) representan el río Loa, permitiendo el intercambio

de agua entre el río y el sistema de agua subterránea, en función de la relación entre la cota del

espejo de agua del río ( _river stage_ ) y la elevación de la superficie piezométrica en la celda del

modelo que contiene está condición de borde. De modo similar a las celdas dren, la magnitud del

flujo está condicionada por una conductancia, en este caso del lecho del río. A diferencia de las

celdas dren, que solamente permiten la salida de agua desde el sistema de agua subterránea, las

celdas río permiten que agua salga del sistema de agua subterránea al río (tramo de río ganador)

o entre al sistema de agua subterránea desde el río (tramo de río perdedor).

_Anexo 1.0_Resumen global de los modelos_ _Página 10 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Figura 2. Distribución de pozos de drenaje al noreste del Rajo DMH**

_Anexo 1.0_Resumen global de los modelos_ _Página 11 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Modelo regional de la Cuenca de Calama (Pampa Talabre) en Modflow USG**

La actualización del modelo regional por Arcadis en mayo de 2020, incluye la traslación del modelo de
Modflow 2000 a _Modflow USG_ . [7]

Modflow USG ofrece varias ventajas sobre versiones anteriores de Modflow, entre las más destacadas

están:

(i) El uso de mallas no estructuradas para refinar la grilla en zonas de interés, permitiendo lograr

mayor eficiencia en las simulaciones numéricas y obtener una mayor densidad de niveles y flujos

simulados en las zonas de interés.

(ii) Reduce los problemas de convergencia numérica asociados al secado y rehumectación de celdas

en acuíferos libres, producto de variaciones en el tiempo de la elevación de la superficie freática.

(iii) Permite introducir discontinuidades de unidades hidrogeológicas (acuñamientos), eliminando la

necesidad de tener capas numéricas continuas.

(iv) Permite no incluir celdas inactivas (celdas de no flujo) en las matrices de la simulación numérica,

que mejora la eficiencia computacional de la simulación numérica.

(v) Permite simular pozos que están abiertos en múltiples capas del modelo, con el proceso

_Connected Linear Network_ (CLN); esto además permite la opción de reducir automáticamente las

tasas de bombeo cuando el sistema de agua subterránea no es capaz de sustentarlas.

Se usó la plataforma de diseño, Groundwater Vistas 7, publicada por Environmental Simulations Inc, para
facilitar este trabajo [8] .

En el modelo regional en Modflow USG, se utiliza un esquema de refinamiento de la grilla, denominado

malla _Quadtree_ . Esto se basa en el concepto que cualquier celda cuadrilátera puede dividirse en cuatro

celdas de igual tamaño, para aumentar la densidad de celdas en zonas de particular interés. En versiones

de Modflow anteriores a Modflow USG, para lograr el refinamiento en una zona de interés, la única opción

es achicar columnas y filas enteras en la malla del modelo. Esto es poco eficiente, porque produce

aumentos en la cantidad de celdas afuera de la zona de interés. La Figura 3 muestra como el proceso

Quadtree permite aumentar la densidad de la malla en zonas geográficamente restringidas.

7 _Panday, Sorab, Langevin, C.D., Niswonger, R.G., Ibaraki, Motomu, and Hughes, J.D., 2017, Modflow USG_

_version 1.4.00: An unstructured grid version of Modflow for simulating groundwater flow and tightly_

_coupled processes using a control volume finite-difference formulation. United States Geological Survey_

_(27 October 2017)_

_[https://dx.doi.org/10.5066/F7R20ZFJ](https://dx.doi.org/10.5066/F7R20ZFJ)_

8 [http://www.groundwatermodels.com/ESI_Software.php](http://www.groundwatermodels.com/ESI_Software.php)

_Anexo 1.0_Resumen global de los modelos_ _Página 12 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Figura 3. Ejemplo de una malla Quadtree con densificación de las celdas en zonas de particular interés**

En el caso del modelo regional de la Cuenca de Calama:

 - En el sector del rajo DMH, el modelo usa celdas cuadradas de 100 m x 100 m en planta.

 - En la zona de la cabecera del río San Salvador, se aplican celdas cuadradas de 50 m x 50 m.

 - La malla fuera de estas zonas está compuesta de celdas cuadradas de 200 m x 200 m.

El modelo utiliza 3 capas para su discretización espacial vertical, lo que permite simular el flujo de agua

subterránea en las siguientes unidades hidrogeológicas:

 - Acuífero superior (calizas y sedimentos no consolidados)

 - Acuitardo intermedio (depósitos limo-arcillosos)

 - Acuífero inferior (gravas)

A diferencia del modelo regional en Modflow 2000, que utiliza celdas dren para representar la descarga

de agua subterránea al rajo DMH, el modelo regional en Modflow USG aplica las tasas de descarga

determinadas por la simulación del Modelo Operacional del Rajo DMH en _MINEDW_, descrito a

continuación. Esta descarga es la suma de:

 - Las tasas de bombeo de los pozos de desagüe perimetrales del rajo DMH, ubicados al norte y

noreste del rajo (Figura 2).

 - La tasa de descarga de agua subterránea al rajo DMH, por la condición de borde tipo dren o

seepage node; estos caudales representan las descargas de agua subterránea desde drenes

pasivos y estructuras discretas en la pared del rajo, además de filtraciones difusas desde las caras

de las unidades hidrogeológicas expuestas en la pared del rajo.

_Anexo 1.0_Resumen global de los modelos_ _Página 13 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Modelo Operacional del Rajo DMH en MINEDW**

El Modelo Operacional del Rajo DMH está implementado en el código de elementos finitos, MINEDW [9],

publicado por Itasca. MINEDW es un programa que fue desarrollado del código FEMFLOW3D, para simular

el flujo de agua subterránea y las condiciones hidrogeológicas en minas, por lo que cuenta con una serie

de atributos para representar condiciones asociadas a los procesos mineros. Este software resuelve la

ecuación de flujo tridimensional, considerando condiciones hidráulicas no-confinadas o confinadas.

MINEDW ha sido verificado por el _Sandia National Laboratory_ (1998) y es utilizado en numerosos

proyectos mineros en todo el mundo. El Sandia National Laboratory, ubicado en Albuquerque, New

Mexico, es uno de los tres laboratorios de investigación científica y desarrollo de la Administración

Nacional de Seguridad Nuclear de los Estados Unidos.

La versión actual del modelo operación del Rajo DMH está implementada en MINEDW versión 3.05,
la última versión del software que incluye un nuevo _solver_ (paquete de solución) denominado SAMG

( _Algebraic Multigrid Processes for Systems_ ) que permite resolver de manera altamente eficiente grandes

sistemas de ecuaciones lineales durante las computaciones numéricas.

El modelo contiene 4.443.338 elementos triangulares. En la zona del rajo DMH la dimensión máxima de

estos elementos en planta varía entre 15 a 18 m (Figura 4). Afuera de esta zona de enfoque, la dimensión

máxima de los elementos alcanza 250 a 350 m.

La discretización vertical del modelo considera 32 capas, con espesores que van desde los 500 m en las

capas más profundas, hasta los 15 m aproximadamente en las capas más superficiales. En la zona del rajo,

se ha aplicado una mayor discretización vertical ( _pinchout_ ) que ha permitido obtener elementos de

espesor de aproximadamente 15 metros. Este espesor se considera adecuado para poder representar,

con suficiente resolución, la geometría de los bancos mineros individuales en este modelo operacional

muy detallado.

La discretización temporal de las simulaciones con el Modelo Operacional del Rajo DMH en MINEDW es

mensual.

Los pozos de desagüe del Rajo DMH, se distribuyen al norte y noreste del rajo (Figura 5). Estos están
representados en Modelo Operacional del Rajo DMH mediante la condición de borde pozo (well) en

MINEDW. Los drenes pasivos y el túnel del Rajo DMH (Figura 6) están implementados mediante la

condición de borde dren ( _seepage node_ ) en MINEDW.

La calibración del modelo utiliza niveles piezométricos registrados en terreno en:

 - 37 piezómetros de tipo cuerda vibrante, instalados en columnas de lechada de cemento con

bentonita en sondajes diamantinas

 - 26 pozos de observación y piezómetros de tipo Casagrande

9 Itasca Denver, Inc (2018). MINEDW - 3D Groundwater Flow Code, Version 3.05.

[https://www.itascadenver.com/software/MINEDW](https://www.itascadenver.com/software/MINEDW)

_Anexo 1.0_Resumen global de los modelos_ _Página 14 de 18_

_Anexo 1.0_Resumen global de los modelos_

La calibración en régimen estacionario (régimen permanente) es para la configuración de la superficie

piezométrica de enero de 2011, cuando no había desarrollos mineros aún.

La calibración transiente del modelo corresponde al periodo entre las fechas de enero de 2011 a julio de

2019.

La representación muy detallada del Rajo DMH y su entorno inmediato por el Modelo Operacional del

Rajo DMH en MINEDW, permite la simulación del sistema hidrogeológico-geotécnico del sector del

Rajo DMH con un nivel de precisión extremadamente alto.

El uso de las estimaciones de los caudales de desagüe y drenaje del Rajo DMH como dato de entrada al

Modelo Regional en Modflow USG, permite una representación superior del caudal asociado con el

drenaje y desagüe del rajo DMH en el modelo regional en Modflow USG, relativa a lo que se pudo lograr

con el Modelo Regional en Modflow 2000. Esto se debe a que el Modelo Operacional del Rajo DMH en

MINEDW tiene una discretización espacial en planta y vertical, mucha más fina que el Modelo Regional

en Modflow 2000.

_Anexo 1.0_Resumen global de los modelos_ _Página 15 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Figura 4. Refinamiento de la malla triangular en el modelo MINEDW para representar el detalle de los bancos del Rajo DMH y las estructuras**

**de relevancia hidrogeológica y geotécnica**

Fuente: ITASCA (sep 2019). _Actualización a Julio 2019 del Modelo Numérico Hidrogeológico 3D Rajo Ministro Hales_ . Informe interno de Codelco.

Ref Itasca: Informe-4026.004-2019-01.

_Anexo 1.0_Resumen global de los modelos_ _Página 16 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Figura 5** **Distribución de pozos de drenaje al noreste del Rajo DMH en el Modelo Operacional**

Fuente: ITASCA (sep 2019). _Actualización a Julio 2019 del Modelo Numérico Hidrogeológico 3D Rajo_

_Ministro Hales_ . Informe interno de Codelco. Ref Itasca: Informe-4026.004-2019-01.

_Anexo 1.0_Resumen global de los modelos_ _Página 17 de 18_

_Anexo 1.0_Resumen global de los modelos_

**Figura 6** **Distribución de drenes pasivos y el túnel del Rajo DMH en el Modelo Operacional**

Fuente: ITASCA (sep 2019). _Actualización a Julio 2019 del Modelo Numérico Hidrogeológico 3D Rajo_

_Ministro Hales_ . Informe interno de Codelco. Ref Itasca: Informe-4026.004-2019-01.

_Anexo 1.0_Resumen global de los modelos_ _Página 18 de 18_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Historial de la modelación de Codelco relevante al Proyecto “Aumento Movimientos Mina”****

| Descripción | Autor | Año | N°<br>Anexo |
| --- | --- | --- | --- |
| Modelo numérico en soporte de EIA del Proyecto Mansa Mina | CPH Consultores Ltda | 2005 | 1.1 |
| Modelo conceptual Pampa Talabre | Knight Piésold Consulting | 2009 | 1.2 |
| Modelo numérico Pampa Talabre | Knight Piésold Consulting | 2010 | 1.3 |
| Actualización de la calibración del modelo numérico de 2010 de Knight<br>Piésold | Hidromas | 2012 | 1.4 |
| Actualización de la calibración del modelo numérico de 2012 de Hidromas | Hidromas | 2015 | 1.5 |
| Actualización de la calibración del modelo numérico de 2015 de Hidromas | Montgomery &<br>Associates | 2018 | 1.6 |
| Simulaciones en soporte la DIA con el modelo numérico de Montgomery &<br>Associates de 2018 | Codelco | 2019 | 1.7 |
| Actualización de la calibración del modelo numérico de 2015 de<br>Montgomery & Associates de 2018 y traslación del modelo de Modflow<br>2000 a Modflow USG. | Arcadis | 2020 | 1.8 |
| Modelo conceptual hidro-geotécnico local operacional del Rajo DMH | Itasca | 2019 | 1.9 |
| Modelo numérico hidro-geotécnico local operacional del Rajo DMH | Itasca | 2019 | 1.10 |

**Tabla 2.**

| Unidad<br>Hidrogeológica | Descripción | Notas |
| --- | --- | --- |
| UH-1 | Sedimentos recientes (gravas y arenas no<br>consolidadas) | Generalmente seca, si no forma una<br>extensión vertical del Acuífero Superior |
| UH-2 | Calizas y areniscas calcáreas de la Formación<br>El Loa | Acuífero Superior |
| UH-4 | Limos y arcillas de la Formación El Loa | Acuítardo |
| UH-5 | Acuífero de Gravas de la Formación Calama | Acuífero Inferior |
| UH-6 | Basamento de rocas pre-Terciarias | Acuícludo |
