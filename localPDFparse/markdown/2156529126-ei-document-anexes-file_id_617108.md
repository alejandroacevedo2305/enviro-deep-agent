---
title: Sin título
author: Matias Gargiulo Rosa
date: D:20220718082900-04'00'
language: es
type: report
pages: 24
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - EVALUACIÓN DEL ÁREA DE INFLUENCIA EN EL SEDIMENTO PROYECTO: “Modificación de biomasa del cultivo de Salmón Atlántico, RCA 371/2008, CES Leucayec, Código de Centro 110860” SOLICITANTE: SALMONES CAMANCHACA S.A. EJECUTOR: IA Consultores SpA.
-->

# EVALUACIÓN DEL ÁREA DE INFLUENCIA EN EL SEDIMENTO PROYECTO: “Modificación de biomasa del cultivo de Salmón Atlántico, RCA 371/2008, CES Leucayec, Código de Centro 110860” SOLICITANTE: SALMONES CAMANCHACA S.A. EJECUTOR: IA Consultores SpA.

Junio de 2022

Innovación Ambiental Consultores Spa.

Manuel Ojeda 1476, Castro

Cel.: +56 9 96797610

[mgargiulo@iacspa.cl](mailto:mgargiulo@iacspa.cl)
[https://www.innovacionambiental.cl/](https://www.innovacionambiental.cl/)

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**TABLA DE CONTENIDO**

1 Introducción ................................................................................................................................................ 3

2 Metodología y Supuestos ........................................................................................................................... 4

2.1 NewDepomod .................................................................................................................................... 4
2.2 Definición del Área de Influencia (AI) ................................................................................................ 9
3 Objetivos de la modelación ...................................................................................................................... 10

4 Datos de entrada del modelo ................................................................................................................... 12

5 Descripción del área de estudio ............................................................................................................... 12

5.1 Batimetría ........................................................................................................................................ 12

5.2 Hidrodinámica del área .................................................................................................................... 14
5.2.1 Filtrado y selección de capas de la correntometría ................................................................. 14
6 Antecedentes de la modelación ............................................................................................................... 15

6.1 Grilla de Modelación ........................................................................................................................ 15
6.2 Cálculo de los valores de flujo diario y flujo anual de carbono ........................................................ 15
6.3 Cálculo del Índice de Impacto (Findlay - Watling) ........................................................................... 16
7 Resultados ............................................................................................................................................... 18

7.1 Extensión y magnitud del Área de Influencia (AI) del proyecto. ...................................................... 18
7.2 Evaluación del Impacto ................................................................................................................... 20
8 Conclusiones ............................................................................................................................................ 22

23

9 Anexos (adjuntos en formato digital) ........................................................................................................ 24

3. Archivos de correntometría utilizada para la modelación ......................................................................... 24

P á g i n a | **2**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**1** **Introducción**

NewDEPOMOD es un software de modelado de rastreo de partículas, desarrollado por la

Asociación Escocesa de Ciencias del Mar (SAMS), en conjunto con la industria de la

acuicultura y la Agencia Escocesa de Protección del Medio Ambiente (SEPA).

El tamaño de los centros de cultivo de acuicultura marinos está directamente relacionado

con la escala y el grado de los impactos de los alimentos no consumidos y las heces de

peces que caen al fondo marino. A medida que estos componentes se asientan, pueden

causar cambios en la química y la biología del fondo marino. Si el tamaño del centro no se

ajusta bien al entorno en el que se encuentra, el lecho marino puede contaminarse,

afectando negativamente a la fauna bentónica y afectando la capacidad de la comunidad

de sedimentos para procesar los desechos. Utilizando un enfoque de gestión informado,

estos impactos pueden mantenerse dentro de los límites permitidos.

Los desechos descargados de los centros de cultivo (heces de peces, desperdicios de

alimentos y tratamientos químicos) se acumulan en el fondo del mar, causando

enriquecimiento orgánico y acumulación de residuos, lo que puede conducir a condiciones

tóxicas para la vida marina. SEPA monitorea y regula las descargas de acuicultura y

especifica los Estándares de Calidad Ambiental (EQS) para los sedimentos del fondo

marino, que se aplican para todos los sitios de acuicultura en Escocia. Sin embargo,

predecir cómo las descargas de las operaciones de acuicultura nuevas (o alteradas)

afectarán la calidad ambiental del fondo marino (y las consecuencias para la fauna

biológica) es difícil debido a las complejas condiciones específicas del sitio que existen.

DEPOMOD, AutoDEPOMOD y NewDEPOMOD son modelos desarrollados por “The

Scottish Association for Marine Science” (SAMS). Estos modelos predicen el impacto de las

descargas de centros de cultivo de acuicultura en el fondo marino de manera tal de

optimizar la operación de los sitios de acuicultura para que coincida con la capacidad

ambiental. SEPA adoptó AutoDEPOMOD como una etapa obligatoria en el proceso de

consentimiento para la planificación de la acuicultura en Escocia, y también se utilizó en

otros 25 países en todo el mundo. En 2017, comisionado por el gobierno escocés, SAMS

produjo la siguiente generación del modelo, NewDEPOMOD, el que ahora ha sido adoptado

como el nuevo estándar de la industria (SAMS 2019 [1] ).

1 SAMS Research Services Limited, NewDepomod Team, 2019-2020, NewDepomod User Guide

P á g i n a | **3**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**2** **Metodología y Supuestos**

**2.1 NewDepomod**

El modelo incorpora una gama de procesos, que en conjunto simulan el destino de las

partículas de desechos individuales producidas en las jaulas del centro de cultivo. Al simular

el destino de las partículas durante un período de semanas a años, e incluir factores

ambientales como la batimetría (forma del fondo marino) y las corrientes de agua, es posible

crear una imagen de cómo es probable que se distribuyan los productos de desecho en el

entorno bentónico (fondo marino) de los centros de cultivo de acuicultura. El entorno

bentónico (fondo marino). Aunque el modelo no incorpora actualmente una unidad de

biogeoquímica, los usuarios pueden hacer sus propias asociaciones entre el flujo calculado

y los impactos de interés (por ejemplo, Normas de Calidad Ambiental (EQS) especificadas

por el regulador).

Los distintos procesos del modelo se resumen en la siguiente figura. A la derecha de la

figura se indica además qué módulos fueron activados en la presente modelación y cuales

no lo fueron.

|MÓDULO|ACTIVO|
|---|---|
|Generación de<br>Grilla|SI|
|Producción de<br>deshechos|SI|
|Trazado de<br>partículas|SI|
|Módulo del<br>sedimento|NO|
|Consolidación|NO|
|Degradación del<br>Carbono|NO|
|Erosión|NO|
|Resuspensión|NO|
|Módulo<br>Bentónico|NO|

**Figura 1.** Diagrama de flujo que representa las entradas, módulos y procesos del modelo
NewDEPOMOD. En la tabla de la derecha se identifican los módulos que fueron desactivados en la
presente modelación.

P á g i n a | **4**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

A continuación, se describen los procesos que afectan el destino de las partículas del

modelo, de manera secuencial y en el orden en que tienen lugar dentro de cada subsección.

A continuación, se presentan los diagramas y ecuaciones que introducirán los parámetros

claves.

**Generación de deshechos**

La primera etapa en el modelo es la producción de partículas de desechos. Esto se lleva a

cabo desde jaulas que ocupan un volumen fijo debajo de la superficie del agua. A las jaulas

se les asigna una densidad de población (kg m-3) y una serie de tiempo que describe los

insumos de alimentación. El nivel de almacenamiento y la información de las entradas de

alimentación permiten una serie temporal que describe la cantidad de partículas de

desechos que salen de las jaulas del centro de cultivo que se simulará. Las partículas de

desechos que caen de los centros de cultivo se agrupan en dos categorías:

 - Residuos de alimento

 - Fecas

Estas dos clases de partículas difieren en sus características: tamaño, densidad y

composición (proporción de masa compuesta de carbono, agua y residuos químicos), lo

que afecta su velocidad de sedimentación. En realidad, no hay dos partículas exactamente

iguales, y el modelo representa esta variabilidad seleccionando tamaños de partículas y

tasas de sedimentación de una distribución. Estas características alteran cómo se mueve

una partícula individual en cada etapa posterior de la ejecución del modelo. A lo largo de

una simulación, las partículas se liberan continuamente de las jaulas del centro de cultivo

modelo y comienzan su viaje hacia el fondo marino.

**Transporte de partículas en suspensión: asentamiento y advección**

Una vez que las partículas salen de las jaulas, su movimiento está sujeto a las condiciones

que encuentran cuando se asientan ("Módulo de seguimiento de partículas", figura 1). Las

partículas pueden moverse horizontal y verticalmente, sujetas a las corrientes de agua

(advección), procesos difusivos y hundimiento. De manera predeterminada, la columna de

agua se representa en 3 dimensiones como una cuadrícula que consta de celdas cuadradas

regulares horizontalmente y una serie de capas definidas por los datos del medidor actual

suministrados y la información de batimetría. El movimiento "horizontal" de las partículas es

verdaderamente lateral (perpendicular a vertical), en lugar de seguir la forma del fondo

P á g i n a | **5**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

marino. En términos generales, los sólidos de interés (en términos de impactos bentónicos)

no son flotantes; en ausencia de fuerza externa, se hunden hacia el fondo del mar. Como

se señaló anteriormente, la velocidad de hundimiento puede variar entre las partículas, pero

permanece constante para una partícula dada durante su vida útil en el modelo. Las

corrientes de agua varían con la profundidad y generalmente son más altas cerca de la

superficie del agua. Esta variación se representa en los registros de series temporales

actuales que se recopilan en los centros de cultivo, por lo que se recomienda tener una

medición de superficie (alrededor de 0.1 x profundidad de la columna de agua), una

medición de profundidad media (alrededor de 0.5 x profundidad de la columna de agua) y

un Medición cercana al lecho (alrededor de 0,95 x profundidad de la columna de agua). La

velocidad horizontal para una partícula dada se obtiene interpolando linealmente las

corrientes a profundidades por encima y por debajo de la profundidad de partícula actual.

Las partículas también están sujetas a lo que colectivamente se denominan "procesos

difusivos". Debido a las fluctuaciones a pequeña escala en las corrientes y los movimientos

del agua debido a la turbulencia, las partículas que se mueven en el agua tienden

naturalmente a separarse unas de otras. Esto tiene lugar tanto horizontal como

verticalmente, y se representa en el modelo mediante pequeñas adiciones aleatorias a (o

sustracciones de) los movimientos que las partículas realizan debido al hundimiento o las

corrientes horizontales. La magnitud de esta dispersión aleatoria está representada por tres

dimensiones, x, y (ambas horizontales) y z (vertical). El tipo de caminata aleatoria

implementada se puede definir en el modelo como una de dos ecuaciones:

1. Reticular:

2. Uniforme

donde _x_ _i,t_ y _y_ _i,t_ son las ubicaciones de una partícula i en los ejes este y norte (en m) en el

tiempo t (por lo tanto, el subíndice t + Δt indica la ubicación después de un paso de tiempo

de longitud Δt). u y v son las velocidades de corriente este y norte (en m s-1) en la ubicación

de la partícula, y el término adicional incorpora el efecto de difusión horizontal, basado en

P á g i n a | **6**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

el paso de tiempo, el parámetro de escala k (x, y). R = +1 o -1, y U es un número aleatorio

uniforme entre -1 y 1

Del mismo modo, el movimiento vertical puede estar representado por una de las siguientes

dos ecuaciones:

1. Reticular:

2. Uniforme

donde _z_ _i,t_ es la posición vertical de la partícula, _k_ _z_ es el coeficiente de difusión vertical y _V_ _sink,i_

es la velocidad de hundimiento de la partícula i. El período de tiempo para que una partícula

llegue al fondo marino depende de la profundidad del agua, la forma del fondo marino y la

velocidad de hundimiento de la partícula. Finalmente, la partícula interceptará el fondo

marino. Esto generalmente ocurre entre dos puntos de tiempo de modelo. En el caso de

que se calcule una nueva posición de partículas por debajo del fondo marino, un algoritmo

de interpolación busca identificar el momento preciso en el que la partícula llegó al fondo

marino, y la partícula se coloca en el fondo marino en ese punto y tiempo. Una

representación de este escenario se da en la figura 2.

**Figura 2.** Representación de la interacción de partículas con el fondo marino.

Los altos caudales reducen las tasas de sedimentación de partículas y, en casos extremos,

les permiten mostrar velocidades de sedimentación negativas, lo que les permite tener una

flotabilidad positiva. Esto puede representarse en el modelo habilitando el "asentamiento

modificado por cizallamiento", que altera el _v_ _sink_ de acuerdo con la velocidad de fricción local,

fv:

P á g i n a | **7**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

donde α es un parámetro de ajuste. Una referencia adicional a esto, entregando rango

adecuado de valores, se puede encontrar en el paper de Black et al. (2016). Se proporciona

una opción adicional para habilitar o prevenir la flotabilidad en este caso. De acuerdo a lo

indicado por el fabricante del modelo, en la mayoría de los casos, no es necesario o

recomendable el uso de asentamiento modificado por cizallamiento o habilitación de

flotabilidad, motivo por el cual no fue activado en la presente modelación.

**Procesos en el sedimento**

El proceso de lecho y el módulo de resuspensión en NewDEPOMOD representa un

desarrollo significativo de AutoDEPOMOD, proporcionando un manejo más refinado de este

aspecto del proceso de depósito. Una vez que una partícula alcanza el fondo marino, se

deposita en una capa de sedimento en la superficie del fondo marino. Después de que las

partículas han estado en el fondo marino por un cierto tiempo (definido por un parámetro

modelo), se produce la consolidación, lo que significa que la capa de partículas depositadas

se convierte en parte del fondo marino y puede estar cubierta por nuevas partículas que se

depositan sobre ellos. Las partículas en el fondo marino pueden sufrir degradación

(descomposición del carbono y / o concentraciones químicas). Las partículas en la

superficie del fondo marino son susceptibles a la erosión. Esto significa que, si el esfuerzo

cortante en el fondo marino es suficientemente alto, las partículas se eliminan del fondo

marino y vuelven a entrar en la columna de agua. Este proceso se representa en la figura

3. El fondo marino dentro de una unidad horizontal dada se modela como una serie de

capas. La capa superior (en la superficie del fondo marino) es la capa que recibe partículas

depositadas de la columna de agua. Cuando se depositan las partículas, comienzan a

formar una nueva capa, que cubre las capas establecidas. La dureza de las capas en el

fondo marino aumenta con el tiempo. Como las capas depositadas más recientemente

están en la superficie del fondo marino, esto significa que la dureza aumenta al aumentar

la profundidad debajo de la superficie del fondo marino (zb), y que el esfuerzo cortante

requerido para erosionar las capas más profundas es mayor que para las capas poco

profundas. Cuando se agrega una nueva capa, la capa debajo de ella aumenta en dureza

(su esfuerzo crítico de cizallamiento por erosión “tcrit, z” aumenta), acercándose a una

dureza máxima de lecho de equilibrio. La configuración de las capas en el modelo de fondo

y su dureza se muestran en la figura 3.

P á g i n a | **8**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**Figura 3.** Representación del movimiento de partículas en el modelo de fondo desde la deposición (a la

izquierda), hasta la consolidación (centro) y la erosión (derecha).

La materia en el fondo marino se degrada con el tiempo. Esto significa que la masa química

se elimina de la masa depositada de acuerdo con las velocidades definidas para la

ejecución del modelo particular (se utilizan valores predeterminados razonables). El modelo

también puede permitir la degradación del carbono a lo largo del tiempo, aunque se

requieren pruebas adicionales de este proceso tanto para el material lábil como para el

refractario, a fin de tener en cuenta los cambios en este proceso con la temperatura, la

profundidad y, por lo tanto, el oxígeno (SAMS, 2019 [2] ). Debido a ello, el módulo de

sedimento no fue activado en la presente modelación.

**2.2 Definición del Área de Influencia (AI)**

Se define el Área de Influencia del proyecto (AI) siguiendo para ello lo indicado en la “Guía

para la Descripción del Área de Influencia”, publicado por el SEA. Como AI se define al

área comprendida dentro de la isolínea de los 700 gC/m2/año de sedimentación. Este valor

es seleccionado debido a que un número relevante de publicaciones especializadas

identifican un valor similar como el límite inferior a partir del cual el impacto ambiental

producto de la sedimentación de fecas y alimento, aunque no necesariamente significativo,

sí comienza a ser detectable (Cromey et.al, 2002 [3], Hargrave 2010 [4] )

2 SAMS Research Services Limited, NewDepomod Team, 2019-2020, NewDepomod User Guide
3 Cromey CJ, Nickell TD, Black KD (2002). DEPOMOD--modelling the deposition and biological effects of waste solids from marine
cage farms. Aquaculture 214, 211 -239
4 Hargrave BT (2010) Empirical relationships describing benthic impacts of salmon aquaculture. Aquacult Environ Interact 1: 33−46

P á g i n a | **9**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**3** **Objetivos de la modelación**

El presente informe se construye con el objetivo de entregar los antecedentes suficientes

que permitan a las autoridades descartar que las modificaciones propuestas por el titular

sean de consideración, tanto en extensión del impacto ambiental como en su magnitud y

duración, al alero de los dispuesto en el artículo 2 letra g. 3) del D.S. 40/2013 del Ministerio

de Medio Ambiente. Para ello se define el Área de Influencia (AI) sobre el sedimento y se

evalúa el nivel de impacto dentro del AI, siguiendo para ello la “Guía para la Descripción del

Área de Influencia”, publicado por el SEA.

**Tabla 1.** Análisis realizados en el presente estudio.

**Escenarios de biomasa y**
**estructuras evaluados**

**RCA 371 / 2008.**

**20 jaulas cuadradas**

**de 30x30x15 m.**

**Biomasa 5.000 Ton.**

**Alternativa 1**

**18 jaulas cuadradas**

**de 40x40x20 m.**
**Biomasa 7.435** **[5]** **Ton.**

**Alternativa 2**

**32 jaulas cuadradas de**

**30x30x15 m. Biomasa**

**7.435** **[6]** **Ton.**

**Escenarios de corrientes** **Sicigia**

**Cuadratura**

**Correntometría completa**

**Extensión del Impacto**
**(Área de Influencia)**

Evaluación mediante análisis NewDEPOMOD de la extensión de impacto ambiental y
comparación entre ambos escenarios.

**Magnitud y evaluación del**
Evaluación mediante combinación de DEPOMOD y modelo Findlay - Watling de la
**Impacto**
magnitud del impacto y comparación entre ambos escenarios.

Se modelan por lo tanto 3 escenarios diferentes en cuanto a su biomasa y

estructuras de cultivo y 3 escenarios diferentes en cuanto a las corrientes utilizadas,

resultando un total de 9 modelaciones diferentes, según se detalla a continuación.

**Tabla 1.** Identificación de escenarios modelados.

**Escenario** **Estructuras** **Biomasa** **Corrientes**

20 jaulas cuadradas de 30x30x15 5.000 ton 30 días

**RCA**

20 jaulas cuadradas de 30x30x15 5.000 ton Cuadratura

20 jaulas cuadradas de 30x30x15 5.000 ton Sicigia

**1** 18 jaulas cuadradas de 40x40x15 7.435 ton 30 días

5 Valor calculado según Artículo 2 letra n) del Reglamento Ambiental para la Acuicultura Dct N°20/2001
6 Valor calculado según Artículo 2 letra n) del Reglamento Ambiental para la Acuicultura Dct N°20/2001

P á g i n a | **10**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**2**

18 jaulas cuadradas de 40x40x15 7.435 ton Cuadratura

18 jaulas cuadradas de 40x40x15 7.435 ton Sicigia

32 jaulas cuadradas de 30x30x15 7.435 ton 30 días

32 jaulas cuadradas de 30x30x15 7.435 ton Cuadratura

32 jaulas cuadradas de 30x30x15 7.435 ton Sicigia

P á g i n a | **11**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**4** **Datos de entrada del modelo**

Para la modelación de los distintos escenarios descritos en la Tabla 2, se detalla a

continuación la configuración productiva utilizada para alimentar el modelo.

**Tabla 2.** Configuración productiva a partir de la cual se alimentó el modelo de dispersión
NewDEPOMOD. El calibre utilizado de 12 mm corresponde al máximo calibre a utilizar en el proyecto.

**Escenario 1**

**18 jaulas**
**cuadradas de**

**40x40x15**

**Escenario 2.**

**32 jaulas**
**cuadradas de**

**30x30x15 m**

**Unidad**

**RCA.**

**20 jaulas**
**cuadradas de**

**30x30x15 m**

**Meses ciclo** Meses 18 18 18

**Numero de Jaulas** Jaulas 20 18 32

**dimensiones** Metros 30x30x15 40x40x15 20x30x15

**Toneladas a Cosechar** Ton 5.000 7.435 7.435

**Toneladas de mortalidad (15%)** Ton 292,8 435 435

**Toneladas de Alimento** Ton 4.908 7.361 7.361

**Digestibilidad Alimento** % 92,1 92,1 92,1

**FCR** - 1,1 1,1 1,1

% 1 1 1

**Pérdida de alimento**

Ton 49 74 74

% 8 8 8

**Pérdida de fecas**

384
Ton 576 576

**Contenido agua en alimento** % 9 9 9

**% Carbono en alimento** % 46,1 46,1 46,1

**% Carbono en fecas** % 30 30 30

**Módulo de Resuspensión y de** - Inactivo Inactivo Inactivo
**fondo**

**Calibre alimento** mm 12 12 12

**Velocidad hundimiento pellets** m/s 0,125 0,125 0,125

**Velocidad hundimiento fecas** m/s 0,032 0,032 0,032

**5** **Descripción del área de estudio**

**5.1 Batimetría**

Para el modelo se utilizó la batimetría del sector, a partir de la cual se definió el tamaño del

Dominio de modelación, esto quiere decir que el modelo es capaz de representar la

sedimentación que se genere dentro de esta área. El dominio utilizado debe permitir

representar el área de sedimentación completa.

P á g i n a | **12**

**Figura 4.** Vista bidimensional de la Batimetría del dominio de Modelación en Leucayec. Concesión
otorgada en color rojo.

Las profundidades bajo la concesión se distribuyen entre los 22 y los 85 metros de

profundidad aproximadamente (profundidades corregidas al nivel de reducción de sondas).

**Figura 5.** Configuración de Jaulas dentro de la concesión. Izquierda: 20 jaulas cuadradas de 30x30x15
m según RCA 371 / 2008. Al centro 18 jaulas de 40x40x15 y a la derecha 32 jaulas de 30x30x15 según
nueva solicitud.

P á g i n a | **13**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**5.2 Hidrodinámica del área**

La medición de corrientes se realizó durante 30 días consecutivos, desde el 23 de abril al

23 de mayo del 2019, contemplando dos períodos de sicigia (04 y 18 de mayo) y dos

períodos de cuadratura lunar (26 de abril y 11 de mayo) respectivamente, utilizando para

ello un Correntómetro ADCP, modelo Nortek 600 KHz. En anexo VIII de la DIA se adjunta

el informe de correntometría para mayor detalle.

**Tabla 3.** Descripción de los 3 períodos de correntometría utilizados para modelar.

**Cuadratura** **Sicigia** **Correntometría completa**

Inicio periodo 26-04-2019 04-05-2019 23-04-2019

N° de registros 577 577 4.319

Intervalo de mediciones 600 600 600

Velocidad promedio (cm/s) 7,6 15,16 12,08

Velocidad mínima (cm/s) 0,4 0,6 0,4

Capa de fondo

Velocidad Máxima (cm/s) 31,1 46,9 61

Dev. St. (cm/s) 4,41 9,14 8,43

% de registros >9,4 cm/s 29% 70% 54%

Según el análisis de velocidades de corrientes, en la capa de fondo ( **tabla 3** ) el 54% de las

velocidades de fondo registradas durante el período de medición completo superan los 9,4

cm/s, lo que clasifica a este centro como **dispersivo** (dispersivos son aquellos con >50%

de registros con velocidades superiores a 9,4 cm/s, según Keeley et.al., 2013 [7] ).

**5.2.1 Filtrado y selección de capas de la correntometría**

En todas las modelaciones realizadas, se utilizó el 100% de las capas de medición de

corrientes entre los -6 y los -70 m de profundidad. Se eliminaron las 2 capas más

superficiales: -2 y -4 m, por ser consideradas por la autoridad [8] como capas no

representativas para el proceso de modelación de la dispersión del alimento y fecas

procedentes de la biomasa de salmón.

7 Keeley N.B., Cromey C.J., Goodwin E.O., Gibbs M.T., Macleod C.M., 2013. Predictive depositional modelling of the
interactive effect of current flow and resuspension on ecological impacts beneath salmon farms. Aquacult Environ Interact.
Vol. 3: 275-291, 2013
8 Subsecretaría de Pesca y Acuicultura. Adendas DIA en proyectos de acuicultura (p. ej.
[https://infofirma.sea.gob.cl/DocumentosSEA/MostrarDocumento?docId=c6/2c/3aa9df82c7f400d4598cf6a3a081d9af2f30)](https://infofirma.sea.gob.cl/DocumentosSEA/MostrarDocumento?docId=c6/2c/3aa9df82c7f400d4598cf6a3a081d9af2f30)

P á g i n a | **14**

|Evaluac<br>Junio-2022<br>Proyecto 220|ión Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_<br>_Evaluac_<br>_Proyecto 220_|_54_|_54_|

Las capas utilizadas para modelar corresponden por lo tanto a las siguientes profundidades:

-70,-68,-66,-64,-62,-60,-58,-56,-54,-52,-50,-48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,

24,-22,-20,-18,-16,-14,-12,-10,-8 y -6.

**6** **Antecedentes de la modelación**

**6.1 Grilla de Modelación**

Para la generación del modelo se utilizó una Grilla con malla con cuadrantes de 10x10 m,

con un offset mínimo (desfase respecto de la concesión) de 200 metros (Figura 6).

**Figura 6.** Esquematización de grilla utilizada para la modelación, junto con la disposición espacial
estructurada de los elementos dentro del área modelada. Concesión otorgada en rojo.

**6.2 Cálculo de los valores de flujo diario y flujo anual de carbono**

El modelo NewDepomod fue alimentado en primer lugar con la información del ciclo

productivo de 18 meses que se describe en la DIA (ver Tabla 2). Es importante recalcar que

la información que entrega el modelo corresponde al flujo acumulado de carbono durante

todo el período de modelación, es decir **18 meses** en este caso. Esto es posible verificarlo

revisando el archivo generado automáticamente por el software, ubicado en la carpeta del

presente informe: **Anexo 2_Archivos modelaciones / “nombre modelación” como**

**“E1_LEUCAYEC_C1” u otro / Depomod / results / E1_LEUCAYEC_C1-18JAULAS-**

P á g i n a | **15**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**NONE-N-carbon-g0.** Al abrir el archivo, se observan 3 columnas, las que corresponden de

izquierda a derecha a: eje X, eje Y, gramos de Carbono / m2 (ver Figura 7).

**Figura 7.** Resultados de flujo de carbono extraídos de NewDepomod. De izquierda a derecha: columnas
eje X, eje Y y carbono acumulado por m2.

La naturaleza del resultado obtenido es por lo tanto un valor acumulado, no

asociado de forma explícita a una unidad de tiempo, que representa la acumulación

de carbono a lo largo de todo el ciclo productivo modelado. Por lo tanto, se debe en

primer lugar conocer el período de tiempo que representan los valores de carbono

obtenidos, con el objetivo de poder obtener un valor de flujo de carbono por unidad

de tiempo, por ejemplo diario (gC/m2/día) o anual (gC/m2/año).

Por lo tanto, dado que el ciclo productivo representado es de 18 meses, se debe en

primer lugar dividir cada uno de los valores de carbono acumulado por el número

de días que hay en 18 meses. Ello nos permite obtener el valor de flujo de carbono

diario (gC/m2/día), el cálculo para obtener el valor de flujo diario de carbono es el

siguiente:

**(g carbono / m2) / (n° días en 18 meses** )

Como es lógico, para transformar este valor a un flujo de carbono anual, se deberá

multiplicar por 365 el resultado anterior.

**6.3 Cálculo del Índice de Impacto (Findlay - Watling)**

Con los resultados del “NewDEPOMOD”, y los datos de corrientes y oxígeno es posible

elaborar un índice de evaluación de impacto ambiental (Findlay - Watling, 1997). Este

índice entrega el balance entre la demanda de oxígeno necesaria para la oxidación del

P á g i n a | **16**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

carbono orgánico, y el oxígeno intersticial teóricamente disponible. Si la disponibilidad es

mayor que la demanda, el índice tendrá un valor mayor a 1, y los impactos serían mínimos,

dado que el carbono orgánico tendría disponibilidad de oxígeno suficiente para oxidarse y

no se producirían condiciones anaeróbicas.

Sin embargo, si la disponibilidad y la demanda son equivalentes, el índice sería cercano a

1 y los impactos moderados. Por otra parte, si la demanda es mayor que la disponibilidad,

los valores del índice serán menores a 1 lo que tendría como consecuencia sedimentos

hipóxicos y anaeróbicos, por lo que en el sector de impacto se observarían notables

cambios en la estructura ecológica de las especies presentes en el fondo del sector

sedimentado. El cálculo del índice se realiza según la siguiente ecuación:

Donde: X = Promedio menor de 2 horas de las Velocidades de Corrientes en la capa de Fondo.

Y = Concentración de carbono en mmol/m2/día.

**Es importante aclarar que el impacto ambiental sobre el sedimento es evaluado**

**exclusivamente en base al flujo de carbono modelado, específicamente el flujo diario**

**de carbono, por lo que el presente índice se entrega a modo complementario.**

Para generar el índice de impacto en fondo se calculó el mínimo promedio de 2 horas de

duración en la capa más cercana al fondo (Capa 35), de acuerdo a lo indicado por Findlay

et.al, 1997, modelo que fue validado con corrientes a 1 m de distancia del fondo. El valor

obtenido para estos efectos fue distinto dependiendo del ciclo mareal, según se indica a

continuación.

**Tabla 4.** Valores del promedio mínimo de 2 horas de duración, calculado en cada uno de los ciclos
mareales utilizados para modelar.

**Ciclo mareal** **Promedio mínimo de 2 horas**

30 días 3,9 cm/s

Sicigia 5,4 cm/s

Cuadratura 3,9 cm/s

P á g i n a | **17**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**7** **Resultados**

**7.1 Extensión y magnitud del Área de Influencia (AI) del proyecto.**

En la Tabla 5 se comparan las superficies de las AI de los escenarios modelados. De esta

comparación se desprende que existe escasa variabilidad en las áreas totales de las AI

entre los nuevos escenarios modelados.

**Tabla 5.** Comparación entre las áreas de sedimentación de carbono de los escenarios modelados.

|Tasa de<br>Sedimentación<br>g C / m2 / año|30 días<br>20 jaulas 30x30x15 m 18 jaulas 40x40x15 m 32 jaulas 30x30x15 m<br>% Cobertura % Cobertura % Cobertura<br>Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l<br>sedimentada sedimentada sedimentada|CUADRATURA<br>20 jaulas 30x30x15 m 18 jaulas 40x40x15 m 32 jaulas 30x30x15 m<br>% Cobertura % Cobertura % Cobertura<br>Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l<br>sedimentada sedimentada sedimentada|SICIGIA<br>20 jaulas 30x30x15 m 18 jaulas 40x40x15 m 32 jaulas 30x30x15 m<br>% Cobertura % Cobertura % Cobertura<br>Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l<br>sedimentada sedimentada sedimentada|
|---|---|---|---|
|701 - 1000<br>1001 - 1500<br>1501 - 2000<br>2001 - 2500<br>**Área Total**<br>**(m2)**<br>**Área fuera de**<br>**la concesión**<br>**(m2)**<br>**% fuera de la**<br>**concesión**|20,661<br> <br>69.1%<br>29,369<br> <br>40.1%<br>37,600<br> <br>48.4%<br>9,251<br> <br>30.9%<br>43,662<br> <br>59.6%<br>40,145<br> <br>51.6%<br>207<br> <br>0.3%<br>**29,912**<br> <br>**73,239**<br> <br>**77,745**<br> <br>44<br> <br>9,875<br> <br>11,125<br> <br>0.15%<br>13.5%<br>14.3%|13,835<br> <br>33.5%<br>20,387<br> <br>28.1%<br>31,717<br> <br>39.0%<br>17,739<br> <br>43.0%<br>47,313<br> <br>65.3%<br>46,398<br> <br>57.1%<br>9,008<br> <br>21.8%<br>4,797<br> <br>6.6%<br>3,128<br> <br>3.9%<br>692<br> <br>1.7%<br>**41,275**<br> <br>**72,498**<br> <br>**81,243**<br> <br>1,106<br> <br>10,876<br> <br>13,370<br> <br>2.68%<br>15.0%<br>16.5%|17,165<br> <br>89.2%<br>51,684<br> <br>88.7%<br>43,102<br> <br>75.2%<br>2,070<br> <br>10.8%<br>6,554<br> <br>11.3%<br>13,856<br> <br>24.2%<br>347<br> <br>0.6%<br>**19,235**<br> <br>**58,239**<br> <br>**57,306**<br> <br>4,529<br> <br>28,819<br> <br>31,592<br> <br>23.5%<br>49.5%<br>55.1%|

En cuanto a las concentraciones de Carbono en el sedimento, las concentraciones máximas

anuales alcanzadas están en torno a los **2.106 g C/m2/año** en el escenario de la RCA (5.000

Ton), en período de cuadratura (Tabla 7)

**Tabla 6.** Áreas de deposición y concentraciones máximas de deposición de carbono.

**Área AI (m2)** **gC/m2/día** **gC/m2/año**

RCA 30 días 29,912 3.93 1,434

RCA Cuadratura 41,275 5.77 2,106

RCA Sicigia 19,235 3.08 1,124

E1_7.435 Ton. 30 días 73,239 4.38 1,599

E1_7.435 Ton. Cuadratura 72,498 4.74 1,730

E1_7.435 Ton. Sicigia 58,239 3.36 1,228

E2_7.435 Ton. 30 días 77,745 4.17 1,522

E2_7.435 Ton. Cuadratura 81,243 4.72 1,723

E2_7.435 Ton. Sicigia 57,306 4.33 1,579

P á g i n a | **18**

30 días CUADRATURA SICIGIA

**Figura 8.** Flujo diario de carbono. Tasa de sedimentación en gC/m2/día. Fila superior: Escenario RCA;
20 jaulas de 30x30x15 m y 5.000 Ton; Fila del centro, escenario 1 (E1): 18 jaulas de 40x40x15 m y 7.435
Ton. Fila inferior, escenario 2 (E2): 32 jaulas de 30x30x15 m y 7.435 Ton. De izquierda a derecha:
escenarios de 30 días de corriente, cuadratura y sicigia; Concesión otorgada en rojo.

P á g i n a | **19**

30 días CUADRATURA SICIGIA

**Figura 9.** Flujo anual de carbono. Tasa de sedimentación en gC/m2/año. Fila superior: Escenario
RCA; 20 jaulas de 30x30x15 m y 5.000 Ton; Fila del centro, escenario 1 (E1): 18 jaulas de 40x40x15 m y
7.435 Ton. Fila inferior, escenario 2 (E2): 32 jaulas de 30x30x15 m y 7.435 Ton. De izquierda a derecha:
escenarios de 30 días de corriente, cuadratura y sicigia; Concesión otorgada en rojo.

_**7.2 Evaluación del Impacto**_

Los valores máximos de flujo diario de carbono en el nuevo escenario, son de apenas 4,74

gC/m2/día, lo que es inferior a los valores máximos recomendados en algunas de las

publicaciones que establecen los límites de carbono más restrictivos (Chang et.al., 2014 [9],

9 Chang BD, Page FH, Losier, RJ, McCurdy EP (2014) Organic enrichment at salmon farms in the Bay of Fundy, Canada: DEPOMOD
predictions versus observed sediment sulfide concentrations. Aquacult Environ Interact. Vol. 5: 185-208.

P á g i n a | **20**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

Hargrave et al. 2008 [10], Hargrave 2010 [11] ) donde se postula que recién a partir de

concentraciones superiores a los 5 gC/m2/día existe el riesgo de impactos ambientales

diversos. **Ello permite concluir que, bajo los parámetros modelados, el nivel de**

**impacto en el AI del nuevo proyecto no es significativo** .

A partir de los resultados de sedimentación de Carbono sobre el fondo se calculó

adicionalmente el índice de Impacto propuesto por Findlay - Watling,1997 (Tabla 8).

La evaluación del nivel de impacto en el AI de los escenarios modelados muestra valores

del Índice de Findlay - Watling muy superiores a 1, por lo que no se presentaría déficit de

oxígeno para la oxidación de la materia orgánica en ninguno de los escenarios modelados.

**Tabla 7.** Valores mínimos de Índice de Impacto en cada escenario.

**Escenario** **Índice Findlay - Watling**

RCA 30 días 4.21

RCA Cuadratura 2.78

RCA Sicigia 5.52

E1_7.435 Ton. 30 días 3.74

E1_7.435 Ton. Cuadratura 3.43

E1_7.435 Ton. Sicigia 5.00

E2_7.435 Ton. 30 días 3.95

E2_7.435 Ton. Cuadratura 3.45

E2_7.435 Ton. Sicigia 3.79

10 Hargrave BT, Holmer M, Newcombe CP (2008) Towards a classification of organic enrichment in marine sediments based on
biogeochemical indicators. Mar Pollut Bull 56: 810−824
11 Hargrave BT (2010) Empirical relationships describing benthic impacts of salmon aquaculture. Aquacult Environ Interact 1: 33−46

P á g i n a | **21**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**8** **Conclusiones**

**Cuantificación del impacto:** se define el Área de Influencia del proyecto (AI) como el área

comprendida dentro de la isolínea de los 700 gC/m2/año de sedimentación de acuerdo a lo

descrito en el numeral 2.2. Se describen a continuación las áreas de sedimentación y las

concentraciones máximas de carbono del AI.

**-** **Área de Influencia** : los resultados muestran un AI anual máxima de 81.243 m2 en el

nuevo escenario de 7.435 Ton de biomasa total, en período de cuadratura en el E2. El

nuevo AI es mayor al AI del proyecto actualmente aprobado, el que tiene una AI máxima

de 41.275 m2 en 30 cuadratura.

En cuanto al área de sedimentación del AI que sale fuera de la concesión, el área

máxima corresponde al E2 de 32 jaulas de 30x30x15 metros con 31.592 m [2] en el

escenario de sicigia, con la nueva biomasa de 7.435 Ton, lo que equivale al 55% del AI

fuera de la concesión.

**-** **Concentraciones de carbono** : los valores de flujo diario de carbono se mantienen en

todos los casos para este proyecto de ampliación, por debajo del flujo 5 gC/m2/día.

**Tabla 8.** Resumen de los valores críticos modelados: máximas concentraciones de carbono, máximos
tiempos de recuperación, valores mínimos del Índice de Impacto.

Escenario

Área

sedimentación

(m2)

g C / m2 / día g C / m2 / año Índice Findlay

**RCA 30 días** 29,912 3.93 1,434 4.21

**RCA Cuadratura** 41,275 5.77 2,106 2.78

**RCA Sicigia** 19,235 3.08 1,124 5.52

**E1_7.435 Ton. 30 días** 73,239 4.38 1,599 3.74

**E1_7.435 Ton. Cuadratura** 72,498 4.74 1,730 3.43

**E1_7.435 Ton. Sicigia** 58,239 3.36 1,228 5.00

**E2_7.435 Ton. 30 días** 77,745 4.17 1,522 3.95

**E2_7.435 Ton. Cuadratura** 81,243 4.72 1,723 3.45

**E2_7.435 Ton. Sicigia** 57,306 4.33 1,579 3.79

P á g i n a | **22**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**Evaluación del impacto** . Como ya se indicó, es importante destacar que los valores

máximos de flujo diario de carbono en el nuevo escenario, son de apenas 4,74 gC/m2/día,

lo que es inferior a los valores máximos recomendados en algunas de las publicaciones

que establecen los límites de carbono más restrictivos (Chang et.al., 2014 [12], Hargrave et al.

2008 [13], Hargrave 2010 [14] ) donde se postula que a partir de concentraciones superiores a los

5 gC/m2/día existe el riesgo de impactos ambientales diversos.

Se concluye que la modificación de una estructura de 20 jaulas cuadradas de 30x30x15 m

a estructuras de 18 jaulas cuadradas de 40x40x15 metros o 32 jaulas cuadradas de

40x40x15 metros, con un aumento de biomasa de 5.000 Ton a 7.435 Ton., no generará

impactos adicionales significativos en el área de influencia del proyecto, teniendo en cuenta

los parámetros productivos utilizados para cada modelación. Es más, el flujo de carbono

diario se ve disminuido en relación al actual proyecto aprobado en RCA 371/2008, debido

principalmente a las nuevas ubicaciones propuestas de los trenes de jaulas y sus

dimensiones.

Informe elaborado por:

Modelaciones:

Matías E. Gargiulo

Biólogo Marino

Informe:

Beyssi Jofre S.

Ingeniero Civil Ambiental

IA Consultores

12 Chang BD, Page FH, Losier, RJ, McCurdy EP (2014) Organic enrichment at salmon farms in the Bay of Fundy, Canada: DEPOMOD
predictions versus observed sediment sulfide concentrations. Aquacult Environ Interact. Vol. 5: 185-208.
13 Hargrave BT, Holmer M, Newcombe CP (2008) Towards a classification of organic enrichment in marine sediments based on
biogeochemical indicators. Mar Pollut Bull 56: 810−824
14 Hargrave BT (2010) Empirical relationships describing benthic impacts of salmon aquaculture. Aquacult Environ Interact 1: 33−46

P á g i n a | **23**

|Junio-2022|Evaluación Área de Influencia (AI) en sedimento<br>Centro Leucayec|Col3|
|---|---|---|
|_Junio-2022_|_Proyecto 22054_|_Proyecto 22054_|

**9** **Anexos (adjuntos en formato digital)**

1. Archivos AutoCAD georreferenciados en WGS84 de los escenarios modelados con

tasa de sedimentación diaria y anual.

2. Archivos de Modelaciones NewDepomod.

3. Archivos de correntometría utilizada para la modelación

P á g i n a | **24**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5.: ** Comparación entre las áreas de sedimentación de carbono de los escenarios modelados.**

| Tasa de<br>Sedimentación<br>g C / m2 / año | 30 días<br>20 jaulas 30x30x15 m 18 jaulas 40x40x15 m 32 jaulas 30x30x15 m<br>% Cobertura % Cobertura % Cobertura<br>Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l<br>sedimentada sedimentada sedimentada | CUADRATURA<br>20 jaulas 30x30x15 m 18 jaulas 40x40x15 m 32 jaulas 30x30x15 m<br>% Cobertura % Cobertura % Cobertura<br>Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l<br>sedimentada sedimentada sedimentada | SICIGIA<br>20 jaulas 30x30x15 m 18 jaulas 40x40x15 m 32 jaulas 30x30x15 m<br>% Cobertura % Cobertura % Cobertura<br>Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l Área m2 r áe rs ep ae c toto ta a l l<br>sedimentada sedimentada sedimentada |
| --- | --- | --- | --- |
| 701 - 1000<br>1001 - 1500<br>1501 - 2000<br>2001 - 2500<br>**Área Total**<br>**(m2)**<br>**Área fuera de**<br>**la concesión**<br>**(m2)**<br>**% fuera de la**<br>**concesión** | 20,661<br> <br>69.1%<br>29,369<br> <br>40.1%<br>37,600<br> <br>48.4%<br>9,251<br> <br>30.9%<br>43,662<br> <br>59.6%<br>40,145<br> <br>51.6%<br>207<br> <br>0.3%<br>**29,912**<br> <br>**73,239**<br> <br>**77,745**<br> <br>44<br> <br>9,875<br> <br>11,125<br> <br>0.15%<br>13.5%<br>14.3% | 13,835<br> <br>33.5%<br>20,387<br> <br>28.1%<br>31,717<br> <br>39.0%<br>17,739<br> <br>43.0%<br>47,313<br> <br>65.3%<br>46,398<br> <br>57.1%<br>9,008<br> <br>21.8%<br>4,797<br> <br>6.6%<br>3,128<br> <br>3.9%<br>692<br> <br>1.7%<br>**41,275**<br> <br>**72,498**<br> <br>**81,243**<br> <br>1,106<br> <br>10,876<br> <br>13,370<br> <br>2.68%<br>15.0%<br>16.5% | 17,165<br> <br>89.2%<br>51,684<br> <br>88.7%<br>43,102<br> <br>75.2%<br>2,070<br> <br>10.8%<br>6,554<br> <br>11.3%<br>13,856<br> <br>24.2%<br>347<br> <br>0.6%<br>**19,235**<br> <br>**58,239**<br> <br>**57,306**<br> <br>4,529<br> <br>28,819<br> <br>31,592<br> <br>23.5%<br>49.5%<br>55.1% |
