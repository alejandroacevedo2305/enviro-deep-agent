---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 50
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO HIDRÁULICO PROYECTO “LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 8”
-->

Informe Técnico

2024

# ESTUDIO HIDRÁULICO PROYECTO “LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 8”

www.flujoing.cl /+562 29798241/ info@flujoing.cl

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### CONTENIDO

1. ANTECEDENTES Y ALCANCES ................................................................................................. 3

2. METODOLOGÍA ................................................................................................................................ 6

2.1. Fundamentos de la modelación con Iber ........................................................ 6

2.2. Geometría ...................................................................................................... 8

2.3. Malla de cálculo ............................................................................................ 9

2.4. Rugosidad ...................................................................................................... 11

2.5. Condiciones de contorno e internas .............................................................. 12

2.6. Condiciones iniciales ..................................................................................... 14

2.7. Simulación y postproceso .............................................................................. 14

3. RESULTADOS Y ANÁLISIS DE INUNDACIONES ............................................................ 14

4. Estudio de socavaciones ........................................................................................................... 19

4.1. Fundamentos del módulo de transporte de sedimentos ................................ 20

4.2. Granulometría de sedimentos ........................................................................ 21

4.3. Parametros de transporte de sedimentos ...................................................... 22

4.4. Resultados de Socavaciones ......................................................................... 23

5. APLICABILIDAD PERMISOS AMBIENTALES SECTORIALES.................................. 26

6. CONCLUSIÓN ................................................................................................................................. 29

7. BIBLIOGRAFÍA ............................................................................................................................... 32

8. SUBANEXOS .................................................................................................................................... 33

www.flujoing.cl / info@flujoing.cl

1

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### Índice de Tablas

Tabla 1. Caudales líquidos quebradas de estudio. ........................................................ 5

Tabla 2. Caudales detríticos quebradas de estudio. ...................................................... 5

Tabla 3. Rugosidad método de Cowan. ........................................................................ 11

Tabla 4. Caudales de condiciones de contorno de entrada. ........................................ 13

Tabla 5. Curva granulométrica utilizada. .................................................................... 22

Tabla 6. Condiciones método de transporte en suspensión Iber. ................................. 23

Tabla 7. Condiciones método de transporte de fondo Iber. ........................................ 23

### Índice de Figuras

Figura 1. Área de estudio. .............................................................................................. 3

Figura 2. Quebradas aportantes al área de estudio. .................................................... 4

Figura 3. Geometría del modelo. .................................................................................. 8

Figura 4. Malla de cálculo de modelo. ........................................................................ 10

Figura 5. Distribución de tamaños de los elementos de la malla de cálculo (acumulado).

.................................................................................................................................... 10

Figura 6. Condiciones de contorno aplicadas al modelo. ............................................ 13

Figura 7. Zonas de inundación total T-100 años. .......................................................... 15

Figura 8. Profundidades de flujo inundación Parte 1 ..................................................... 16

Figura 9. Profundidades de flujo inundación Parte 2 .................................................... 17

Figura 10. Velocidades de flujo inundación Parte 1 ....................................................... 18

Figura 11. Velocidades de flujo inundación Parte 2 ....................................................... 18

Figura 12: Curva granulométrica utilizada. .................................................................. 22

Figura 13. Socavaciones escenario T-150 años Parte 1. ................................................. 25

Figura 14. Socavaciones escenario T-150 años Parte 2. ................................................ 25

Figura 15. Profundidades inundación zona recinto principal proyecto BH8. ................ 27

Figura 16. Profundidades inundación zona recinto secundario proyecto BH8. ............. 28

www.flujoing.cl / info@flujoing.cl

2

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### 1. ANTECEDENTES Y ALCANCES

En el presente informe se desarrolla el estudio hidráulico en el marco del proyecto “Línea

de transmisión y central BESS Halcón 8”, en adelante “el Proyecto”, considerando sus

respectivos aspectos metodológicos, análisis de resultados y principales conclusiones.

El Proyecto se encuentra emplazado en la comuna de Huasco, Región de Atacama, y

consiste en un proyecto de construcción y operación de una central de almacenamiento

de energía eléctrica en base a baterías de ion litio (BESS) junto con una línea de alta

tensión de 110 kV .

El área definida para este estudio tiene una superficie aproximada de 328 hectáreas, y

considera la zona de emplazamiento de las obras del proyecto, más una superficie

suficientemente amplia para analizar el comportamiento hidráulico para las crecidas de

los cauces de interés y su influencia sobre las obras del proyecto.

**Figura 1. Área de estudio.**

**Fuente: Elaboración propia, plataforma SIG.**

www.flujoing.cl / info@flujoing.cl

3

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Es importante destacar que este trabajo considera como antecedente el documento

“Estudio Hidráulico e Hidrológico proyecto Línea de Transmisión y Central BESS Halcón

8”, en el cual se desarrolló la caracterización hidrológica y estimación de caudales de

crecida, en el marco de este proceso de evaluación ambiental.

Por lo tanto, las condiciones hidrológicas consideradas para el presente estudio son

análogas a las desarrolladas en dicho trabajo, siendo de particular interés los escenarios

con periodo de retorno T-100 y T-150 años.

En el estudio hidrológico antecedente se identificaron 3 quebradas aportantes al área

de estudio cuyas áreas aportantes se definieron en 80.19 km [2], 3.45 km [2 ] y 0.28 km [2], para

las cuencas 1, 2 y 3 respectivamente. La _Figura 2_ presenta una vista detallada de estas

quebradas con relación al área de estudio.

**Figura 2. Quebradas aportantes al área de estudio.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8.**

www.flujoing.cl / info@flujoing.cl

4

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

La Tabla 1 y Tabla 2 ilustran los caudales máximos instantáneos y los caudales detríticos

obtenidos en dicho estudio para los distintos periodos de retorno, siendo importante

destacar que para la obtención de los caudales asociados al periodo de retorno de 150

años se ha utilizado la extrapolación de los caudales por medio de ajustes logarítmicos

(ver SubAnexo N°4 “Extrapolación de caudales”).

|Caudal (m3/s)<br>Periodo de retorno (años)<br>Cuenca 1 Cuenca 2 Cuenca 3|Col2|Col3|Col4|
|---|---|---|---|
|Periodo de retorno (años)<br>Caudal (m3/s)<br>Cuenca 1<br>Cuenca 2<br>Cuenca 3|Cuenca 1|Cuenca 2|Cuenca 3|
|10|0.64|0.09|0.04|
|25|0.86|0.09|0.05|
|50|1.02|0.12|0.07|
|75|1.09|0.16|0.08|
|100|1.19|0.18|0.08|
|150|1.27|0.19|0.09|

**Tabla 1. Caudales líquidos quebradas de estudio.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8.**

|Caudal (m3/s)<br>Periodo de retorno (años)<br>Cuenca 1 Cuenca 2 Cuenca 3|Col2|Col3|Col4|
|---|---|---|---|
|Periodo de retorno (años)<br>Caudal (m3/s)<br>Cuenca 1<br>Cuenca 2<br>Cuenca 3|Cuenca 1|Cuenca 2|Cuenca 3|
|10|0.91|0.13|0.06|
|25|1.23|0.13|0.07|
|50|1.46|0.17|0.10|
|75|1.56|0.23|0.11|
|100|1.70|0.26|0.11|
|150|1.82|0.27|0.13|

**Tabla 2. Caudales detríticos quebradas de estudio.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8.**

La metodología de este estudio hidráulico corresponde a modelación numérica

bidimensional mediante el software Iber, ampliamente utilizado para la simulación de

flujos en ríos y estuarios. Dicho modelo es aplicable a condiciones donde las hipótesis

de distribución hidrostática de presiones y distribución uniforme de la velocidad en la

profundidad sean representativas de las condiciones dominantes, como es el caso de los

escurrimientos someros en el área de estudio.

Se realiza también un estudio de socavaciones por medio de modelación de lecho móvil

utilizando el módulo de transporte de sedimentos del software Iber. Se detallan en este

informe los fundamentos y aspectos metodológicos respectivos al modelo, así como los

resultados obtenidos.

www.flujoing.cl / info@flujoing.cl

5

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Los alcances de este proyecto corresponden entonces al análisis de inundaciones para

los escenarios extraordinarios T-100 y T-150 años en el área de estudio, determinando las

zonas inundables y sus principales variables hidráulicas (profundidad, velocidad,

caudales específicos). Se considera también el análisis de socavaciones para el

escenario más desfavorable (T-150 años), determinando la respuesta mecánico fluvial a

las condiciones hidráulicas de interés, con particular énfasis en el fenómeno de

socavaciones. Se considera el análisis de la relación de los fenómenos evaluados con

las obras del proyecto.

### 2. METODOLOGÍA

En este capítulo se detallan los aspectos metodológicos relacionados al estudio de

modelación hidráulica realizado, definiendo los fundamentos y limitaciones del modelo,

lo relativo a la construcción del modelo (geometría, malla de cálculo, rugosidad), las

condiciones de modelación (condiciones de contorno, condiciones internas, condiciones

meteorológicas) y también aspectos de la simulación y postproceso.

2.1. FUNDAMENTOS DE LA MODELACIÓN CON IBER

El modelo utilizado está basado en el software Iber, en su versión 3.3, el cual es un

modelo numérico de simulación de flujo turbulento en lámina libre en régimen no

permanente, y de procesos medioambientales en hidráulica fluvial. Dicho software

cuenta actualmente con una gran variedad de módulos para distintas aplicaciones,

pasando a ser un modelo que permite simular múltiples procesos ambientales de base

hidrodinámica. Se destaca en este caso la utilización del módulo hidrodinámico,

considerando también el módulo de procesos hidrológicos para la incorporación de las

condiciones de precipitación en el área de estudio.

El módulo de hidrodinámica de Iber permite predecir los valores que toman las variables

hidráulicas del flujo (profundidad, velocidad, caudal, etc.) resolviendo las ecuaciones

de Saint-Venant de forma bidimensional, es decir, se resuelven las ecuaciones en las dos

www.flujoing.cl / info@flujoing.cl

6

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

direcciones horizontales y promediadas en la profundidad, según se muestra en las

siguientes expresiones.

∂h

∂h∂t [+ ∂hU] ∂x [x]

[x]

∂x [+ ∂hU] [y]

= 0,
∂y

[∂]

∂y [(hU] [x] [U] [y] [) = −gh ∂Z] ∂x [b]

∂x [b] [+ τ] [s,x]

[s,x]

ρ [−τ] ρ [b,x]

2

[∂]

∂x [(hU] [x]

[2] [∂]

2 ~~[)]~~ [ +]

∂ [∂]
∂t [(hU] [x] [) +]

2 + g [h] [2]

[x]

∂x [x] ~~[)]~~ [ +] [∂]

∂y [∂] [(θ] [t] [h ∂U] ∂y [x]

[x]

∂y ~~[)]~~ [,]

[b,x] [∂]

ρ [+]

∂x [∂] [(θ] [t] [h ∂U] ∂x [x]

∂y [b] [+ τ] ρ [s,][y]

[s,][y]

ρ [−τ] [b,] ρ [y]

[2]

2 [) = −gh ∂Z] ∂y [b]

∂y [∂] [(θ] [t] [h ∂U] ∂y [y]

[y]

∂y ~~[)]~~ [,]

∂ [∂]
∂t [(hU] [y] [) +]

[∂] [∂]

∂x [(hU] [x] [U] [y] [) +]

2

[∂]

∂y [(hU] [y]

2 + g [h] [2]

∂x [y] [) +] [∂]

[b,][y] [∂]

ρ [+]

[∂]

∂x [(θ] [t] [h ∂U] ∂x [y]

en donde h es el calado o profundidad, Ux y Uy son las velocidades horizontales

promediadas en profundidad, g es la aceleración de gravedad, ρ es la densidad del

agua, Z b es la cota del fondo, τ s es la fricción en la superficie libre debido al rozamiento

producido por el viento, τ b es la fricción debido al rozamiento del fondo y θ t es la

viscosidad turbulenta (Bladé, 2012).

La fricción de fondo se evalúa mediante la fórmula de Manning como:

τ b,x = ρgh [n] [2] [U] h [4 3][x ] ⁄ [|U|] [2] ~~,~~

[|U|] [2]
τ b,y = ρgh [n] [2] [U] h [4 3][y] ⁄ ~~,~~

Dichas ecuaciones asumen una distribución de presión hidrostática y una distribución

relativamente uniforme de la velocidad en profundidad. La hipótesis de presión

hidrostática se cumple razonablemente en el flujo en ríos y aguas someras. Asimismo, la

hipótesis de distribución uniforme de velocidad en profundidad se cumple habitualmente

en aguas someras, aunque pueden existir zonas en las que dicha hipótesis no se cumpla

debido a flujos locales tridimensionales.

Dichas ecuaciones se resuelven mediante esquemas numéricos estables y robustos, sobre

un dominio espacial discretizado con volúmenes finitos en mallas no estructuradas,

formadas por elementos triangulares (de tres nodos) y cuadrangulares (de cuatro

nodos).

Según lo especificado por sus autores, algunas aplicaciones del modelo, particularmente

del módulo hidrodinámico, corresponden a:

www.flujoing.cl / info@flujoing.cl

7

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

 Simulación del flujo en lámina libre en cauces naturales.

 Evaluación de zonas inundables. Cálculo de las zonas de flujo preferente.

 - Cálculo hidráulico de encauzamientos.

 - Cálculo hidráulico de redes de canales en lámina libre.

 - Cálculo de corrientes de marea en estuarios.

2.2. GEOMETRÍA

La construcción de la geometría del área de estudio es una de las etapas más

importantes del modelo, ya que permite caracterizar la morfología que determina el

movimiento del fluido. Para la elaboración de la geometría se utilizó la topografía del

área de estudio, de 328 hectáreas de extensión, disponiendo de una superficie ráster

que puede ser incorporada al modelo mediante distintas herramientas de la interfaz. La

_Figura 3_ muestra el modelo de elevación digital construido en base a este proceso.

**Figura 3. Geometría del modelo.**

**Fuente: Elaboración propia, plataforma SIG.**

www.flujoing.cl / info@flujoing.cl

8

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Es importante destacar que para este estudio se ha considerado una ampliación

significativa del levantamiento topográfico en la zona noroeste del área de estudio, con

el fin de obtener un modelamiento más realista de la quebrada N°1, evitando que se vea

limitada por la extensión topográfica.

2.3. MALLA DE CÁLCULO

Para que el modelo pueda llevar a cabo la resolución de las ecuaciones gobernantes

por el método de volúmenes finitos, es necesario realizar previamente una discretización

espacial del dominio a estudiar. Para ello se divide el dominio de estudio en celdas o

elementos de tamaño relativamente pequeño, a la que se le denomina malla de cálculo.

La generación de la malla de cálculo es una de las etapas que requiere mayor tiempo y

esfuerzo a la hora de desarrollar un estudio de simulación numérica del flujo, ya que se

requiere determinar un tipo de malla que se adapte y represente adecuadamente la

geometría del problema y con una selección y distribución de tamaños adecuados para

lograr independizar de esta variable los resultados obtenidos, al mismo tiempo que

permitir eficiencia para la modelación.

El modelo Iber presenta distintas herramientas internas para la creación del mallado,

siendo indispensable hacer un análisis de sensibilidad para independizar los resultados

de esta variable. Para el caso de estudio se utilizó una malla irregular no estructurada

generada por medio de la herramienta Rfast, distribuida con distintos tamaños según las

características de la geometría y las zonas de mayor interés de análisis.

La _Figura 4_ ilustra la malla utilizada para las modelaciones, mientras que la _Figura 5_

refleja la respectiva distribución de tamaños de los elementos.

www.flujoing.cl / info@flujoing.cl

9

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

**Figura 4. Malla de cálculo de modelo.**

**Fuente: Elaboración propia.**

**Figura 5. Distribución de tamaños de los elementos de la malla de cálculo (acumulado).**

**Fuente: Elaboración propia, Iber.**

www.flujoing.cl / info@flujoing.cl

10

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

2.4. RUGOSIDAD

Para la aplicación de la rugosidad, el modelo permite asignar distintos valores conforme

a la identificación de usos de suelo. En el caso de estudio se considera la aplicación de

un único uso de suelo, conforme a lo definido en el estudio antecedente de la

Declaración de Impacto Ambiental.

Se utilizó el método de Cowan descrito en el MC V3, el que se basa en la siguiente

expresión:

n= m× (n 0 + n 1 + n 2 + n 3 + n 4 )

Donde:

n 0 = Rugosidad base.

n 1 = Rugosidad adicional por irregularidades perímetro mojado.

n 2 = Rugosidad adicional por variación de forma.

n 3 = Rugosidad adicional por obstrucciones.

n 4 = Rugosidad adicional por presencia de vegetación.

m= Factor de corrección por efecto sinuosidad.

Conforme a lo definido para las condiciones del área de estudio, se definió un

coeficiente de rugosidad de Manning equivalente a 0.0275, según lo expuesto en la

Tabla 3.

|Condición Valor|Col2|Col3|
|---|---|---|
|Material del lecho|n0|0.0225|
|Grado de irregularidad P.M.|n1|0.0000|
|Variaciones de secciones|n2|0.0000|
|Efecto relativo de las obstrucciones|n3|0.0000|
|Densidad de vegetación|n4|0.0050|
|Sinuosidad y frecuencia de meandros|m|1.0000|
|n|n|0.0275|

**Tabla 3. Rugosidad método de Cowan.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8(2023).**

www.flujoing.cl / info@flujoing.cl

11

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

2.5. CONDICIONES DE CONTORNO E INTERNAS

Iber permite la asignación de condiciones de borde de entrada y salida, además de

condiciones internas como fuentes y sumideros. Para las condiciones de entrada es

posible asignar un caudal total, un caudal especifico o una cota de agua, junto con el

régimen y condiciones específicas en función de este. Para las condiciones de salida, es

necesario definir el régimen, donde en el caso de régimen supercrítico/critico no se

requieren mayores detalles de condiciones a diferencia del régimen subcrítico.

El tratamiento de estas condiciones debe ser cuidadosamente analizado, con el fin de

minimizar las influencias sobre los resultados del modelo, especialmente en las zonas de

interés, lo cual se realiza en este estudio por medio de un proceso de iteraciones y

extensión suficiente del área de estudio.

El modelo permite también la asignación de condiciones internas, como estructuras

perdidas locales, fuentes y sumideros en cualquier parte del dominio de cálculo.

Para las condiciones de contorno de entrada se utilizaron escenarios estacionarios con

los caudales detríticos definidos en los antecedentes de este informe (Tabla 2), para los

periodo de retorno de 100 y 150 años, obtenidos de los antecedentes de esta tramitación

ambiental (“Estudio Hidráulico e Hidrológico proyecto Línea de Transmisión y Central

BESS Halcón 8”).

Se consideraron los caudales detríticos con el fin de evaluar los escenario de caudales

más desfavorable considerando el aumento volumétrico de dicha condición.

Se determinó que de acuerdo con las características del área de estudio y las quebradas

aportantes, la condición de entrada más apropiada es por medio de caudales en

régimen subcrítico, para lo cual se definieron los límites de entrada en función del

trazado de las quebradas delimitadas, la topografía e imágenes aéreas de alta

definición. En la _Tabla 4_ se detallan los caudales utilizados para cada condición de

entrada y para cada periodo de retorno.

www.flujoing.cl / info@flujoing.cl

12

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

|Q detrítico T-100 Q detrítico T-150<br>Entrada Quebrada asociada<br>(m3/s) (m3/s)|Col2|Col3|Col4|
|---|---|---|---|
|**E-1**|Cuenca 1|1.70|1.82|
|**E-2**|Cuenca 2|0.26|0.27|
|**E-3**|Cuenca 3|0.11|0.13|

**Tabla 4. Caudales de condiciones de contorno de entrada.**

**Fuente: Elaboración propia.**

Para las condiciones de contorno de salida se establecieron condiciones

supercríticas/criticas, y se definieron sus límites según la misma metodología indicada en

el párrafo anterior, utilizando contornos de salida de gran amplitud al sur del área de

estudio.

Las Figura 6 ilustran las condiciones de contorno de entrada y salida incorporadas al

modelo, especificando la numeración de las distintas entradas. Se destaca que de

acuerdo con los requerimientos del estudio no fue necesaria la incorporación de

condiciones internas al modelo.

**Figura 6. Condiciones de contorno aplicadas al modelo.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

13

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

2.6. CONDICIONES INICIALES

Las condiciones iniciales del modelo, es decir los valores de partida de las variables de

cota o calado en las celdas del dominio, se asignaron como condición seca, aplicando

valores nulos de calado en todas las celdas; siendo relevante utilizar un calentamiento

apropiado del modelo en las respectivas simulaciones para permitir que los resultados

se independicen de esta condición inicial.

2.7. SIMULACIÓN Y POSTPROCESO

Para la aplicación del modelo se realizaron simulaciones de escenarios de caudales

estacionarios durante un tiempo suficiente para lograr un comportamiento estacionario

del flujo hidráulico.

Para las simulaciones se consideró un coeficiente de Courant-Friedrich-Levy (CFL) de

0.45, para condicionar la variación pasos de tiempo para la resolución de las

ecuaciones, buscando evitar inestabilidades en la solución.

Se definió un límite seco-mojado de 0.01m. Dicho valor corresponde a la profundidad

bajo la cual se pierde relevancia para los análisis en relación con la magnitud y

características de los cauces y los objetivos del estudio.

Para analizar el comportamiento hidráulico del área de estudio en los distintos

escenarios simulados, se estudiaron los resultados en la interfaz de postproceso de Iber

y exportándolos en formato ráster a una plataforma GIS, enfocándose en las principales

variables hidráulicas de interés.

### 3. RESULTADOS Y ANÁLISIS DE INUNDACIONES

En este capítulo se detallan los aspectos relacionados a los resultados del estudio,

determinando las áreas de inundación, sus principales características hidráulicas

(profundidad y velocidad) y su influencia sobre la zona del proyecto y sus obras.

www.flujoing.cl / info@flujoing.cl

14

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

En el SubAnexo N°1 “Mapas de modelación hidráulica” se entregan los resultados de

calado (profundidad) y velocidad en el área de estudio, para las condiciones de

escenario caudal detrítico T-100 y T-150 años modeladas.

Las _Figura 7_ ilustra los resultados de zonas de inundación obtenidas para el escenario

T-100 años. Como es posible observar, los recintos de obras permanentes y temporales

se proyectan fuera de los límites de inundación de la crecida centenaria de los cauces

identificados dentro del área de influencia. Se identifican algunas postaciones que se

emplazan cercanos a los límites de la inundación, mientras que el camino de acceso

cruza en algunos puntos flujos secundarios provenientes de la Cuenca 1.

**Figura 7. Zonas de inundación total T-100 años.**

**Fuente: Elaboración propia.**

Las Figura 8 y Figura 9 ilustran de forma más detallada las áreas de inundación y sus

profundidades del flujo. Como es posible observar, se tienen profundidades bajas de

escurrimiento, en general inferiores a 0.25, con excepción de algunas zonas del

escurrimiento principal de la Cuenca 1, y donde existen depresiones topográficas que

generan acumulación de los escurrimientos.

www.flujoing.cl / info@flujoing.cl

15

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

En las zonas donde las postaciones se emplazan cercanas a los límites de la inundación,

y en las zonas donde el camino de acceso interactúa con la inundación, se observan

escasas profundidades de escurrimiento, inferiores a 0.25 m, que no generan afectación

alguna para estas obras.

**Figura 8. Profundidades de flujo inundación Parte 1**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

16

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

**Figura 9. Profundidades de flujo inundación Parte 2**

**Fuente: Elaboración propia.**

Las Figura 10 y Figura 11 ilustran los resultados de velocidad para el mismo escenario. Se

observa que las distintas quebradas producen escasas velocidades, inferiores a 0.5 m/s,

que superan este valor solo en algunas zonas puntuales del escurrimiento.

En las zonas donde las postaciones se emplazan cercanas a los límites de la inundación,

y en las zonas donde el camino de acceso interactúa con la inundación, se observan

velocidades inferiores a 0.5 m/s, las cuales no tienen potencial erosivo que pueda

afectar estas componentes.

www.flujoing.cl / info@flujoing.cl

17

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

**Figura 10. Velocidades de flujo inundación Parte 1**

**Fuente: Elaboración propia.**

**Figura 11. Velocidades de flujo inundación Parte 2**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

18

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Adicionalmente, según se presenta en las cartografías anexas para el escenario T-150

años, no existen diferencias significativas en el área de inundación, profundidades y

velocidades para dicho caso, verificando que las obras tampoco no se verán afectadas

ante esas condiciones.

Considerando lo anterior, se tiene que los recintos de obras permanentes y temporales

del proyecto se emplazan fuera de los límites de los cauces naturales identificados en el

AI, sin requerir obras de defensa u otras obras adicionales que los intervengan.

En este sentido, es importante aclarar que el presente estudio hidráulico utilizó un

levantamiento topográfico significativamente más amplio en comparación con el estudio

hidráulico precedente en la evaluación ambiental, permitiendo un modelamiento

hidráulico más realista del flujo de la Cuenca 1. Al modelar dicha quebrada en toda su

amplitud transversal se obtuvo que la mayor parte del caudal de esta quebrada escurre

al sur del recinto donde se emplazan las baterías del proyecto, y que dicho recinto no

será afectado por la crecida centenaria.

Finalmente, las únicas obras y componentes del proyecto que se emplazan en zonas

inundables de estos cauces para el escenario T-100 años, corresponden al camino de

acceso. Sin embargo, se tiene que los flujos que enfrentan estas componentes son de

escaza magnitud, con profundidades inferiores a 0.25 m y velocidades inferiores a 0.5

m/s, descartando que se requieran obras adicionales que intervengan los cauces.

### 4. ESTUDIO DE SOCAVACIONES

En relación con lo solicitado en el ICSARA Complementario de la evaluación ambiental

del Proyecto, se realiza en este capítulo un análisis de socavaciones para los cauces del

AI, con el fin de analizar si las obras emplazadas en zonas inundables (camino de

acceso y postaciones) serán afectadas por este fenómeno, analizando la eventual

necesidad de obras de protección y sus permisos ambientales sectoriales aplicables.

Los alcances de este análisis corresponden a la evaluación del efecto de socavación en

los cauces y en las obras emplazadas en zonas inundables para el escenario más

www.flujoing.cl / info@flujoing.cl

19

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

desfavorable, correspondiente a los caudales detríticos para el periodo de retorno T-150

años.

La metodología para este estudio de mecánica fluvial corresponde a modelación de

lecho móvil utilizando el módulo de transporte de sedimentos del software Iber, donde

las condiciones de geometría, malla de cálculo, rugosidades, y en general las

condiciones de simulación hidráulica son análogas a las descritas en el capítulo 2. Se

detallan en este capítulo los fundamentos y aspectos metodológicos respectivos al

modelo de transporte de sedimentos del modelo, así como los resultados obtenidos.

4.1. FUNDAMENTOS DEL MÓDULO DE TRANSPORTE DE SEDIMENTOS

De acuerdo con lo indicado por los desarrolladores del modelo (E. Bladé et al, 2014),

en el módulo de transporte de sedimentos de Iber se resuelven las ecuaciones de

transporte por carga de fondo y por carga en suspensión. Teniendo en cuenta ambos

modos de transporte se calcula la evolución de la cota del fondo debido a procesos de

sedimentación y erosión mediante la ecuación de Exner. Se consideran granulometrías

uniformes, incluyendo en las actualizaciones más recientes la posibilidad de incorporar

granulometrías mixtas.

El caudal sólido de fondo se calcula mediante formulaciones empíricas en función de la

tensión de fondo. El módulo de transporte de sedimentos por carga de fondo incluye las

siguientes características:

 - Umbral de movimiento de Shields.

 Formulaciones para caudal sólido de fondo.

 Meyer Peter-Müller con corrección de Wong-Parker (D = 2-30 mm).

 Van Rijn (D = 0,2-2 mm).

 Corrección por pendiente de fondo en inicio del arrastre (tensión crítica en talud).

 Corrección por pendiente de fondo en transporte sólido (magnitud y dirección).

 Separación de tensiones de Einstein por formas de fondo y grano.

 Condiciones de contorno tipo sedimentograma (caudal sólido de fondo variable

en tiempo).

www.flujoing.cl / info@flujoing.cl

20

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

 Condición de cota de fondo no erosionable (puntos fijos).

El transporte en suspensión se calcula resolviendo la ecuación de convección-difusión

promediada en profundidad para la concentración de sedimento, incluyendo un término

de deposición/resuspensión que modela el intercambio de sedimento entre el lecho y la

carga en suspensión. Las principales características de este módulo son:

 Incorporación de transporte por difusión turbulenta.

 Término de deposición/resuspensión.

 Cálculo de la concentración de sedimento en suspensión según las formulaciones

de: Van Rijn, Smith McLean y Ariathurai.

 Cálculo de la velocidad de sedimentación de las partículas según Van Rijn.

 Condición de contorno de concentración de sedimento en suspensión variable en

tiempo.

4.2. GRANULOMETRÍA DE SEDIMENTOS

Para utilizar el módulo de transporte de sedimentos del modelo se requiere en primer

lugar caracterizar los sedimentos representativos de los cauces. Para esto se considera

adecuado utilizar una condición de granulometría uniforme, siendo necesario incorporar

el D50 representativo de los sedimentos del área de estudio.

Se definió como granulometría representativa la curva granulométrica definida en la

Tabla 5 y Figura 12, a partir de la cual es posible identificar un material arenoso, con un

D50 de 0.31 mm, D65 de 0.45mm y D90 de 2.60 mm. Dicha granulometría corresponde

a la curva granulométrica de una calicata realizada en el área de estudio y su

correspondiente análisis granulométrico, según se presenta en el SubAnexo N°3 “Ensayo

de mecánica de suelos”.

www.flujoing.cl / info@flujoing.cl

21

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

|Tamiz (mm) Porcentaje que pasa (%)|Col2|
|---|---|
|25|100.00|
|20|99.00|
|10|96.00|
|5|94.00|
|2|89.00|
|0.5|71.00|
|0.08|25.00|

**Tabla 5. Curva granulométrica utilizada.**

**Fuente: Elaboración propia.**

**Figura 12: Curva granulométrica utilizada.**

**Fuente: Elaboración propia.**

4.3. PARAMETROS DE TRANSPORTE DE SEDIMENTOS

En relación con los parámetros del módulo, para la estimación del transporte en

suspensión se utiliza el método de Van Rajn (Van Rajn, 1984), definiendo los siguientes

parámetros:

www.flujoing.cl / info@flujoing.cl

22

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

|Parámetro Valor|Col2|
|---|---|
|Diámetro Sed. Susp.(m)|0.001|
|Porosidad TS|0.4|
|Densidad Relativa TS|2.65|
|Coeficiente de difusión (m2/s)|0.001|
|Schmidt num|0.7|

**Tabla 6. Condiciones método de transporte en suspensión Iber.**

**Fuente: Elaboración propia.**

Por otro lado, en relación con el transporte de fondo, se utiliza el método de Meyer

Peter & Müller con corrección de Wong-Parker (M. Wong, G. Parker, 2006), apropiado

para los sedimentos granulares en estudio. Los parámetros correspondientes al

transporte de fondo se definen en la siguiente tabla.

|Parámetro Valor|Col2|
|---|---|
|D50 (m)|0.00031|
|Porosidad TF|0.4|
|Densidad Relativa TF|2.65|
|Ángulo de fricción RF (rad)|0.55|

**Tabla 7. Condiciones método de transporte de fondo Iber.**

**Fuente: Elaboración propia.**

Se establece además la condición que todo el lecho de la geometría en estudio es

erosionable.

Adicionalmente, dado que no existen antecedentes para asumir condiciones de entrada

de sedimentos en suspensión ni por arrastre de fondo al modelo, se utiliza por defecto

una condición de agua clara, atendiendo a los objetivos del análisis que es evaluar las

tendencias del lecho dentro del área de estudio.

4.4. RESULTADOS DE SOCAVACIONES

En este capítulo se detallan los aspectos relacionados a los resultados del estudio de

socavaciones, determinando las extensiones y magnitudes del fenómeno, y su influencia

sobre la zona del proyecto y sus obras.

En primer lugar, es importante destacar que en el SubAnexo N°2 “Mapas de

Socavaciones” se entregan los resultados de socavaciones en el área de estudio, para

las condiciones de escenarios de caudal detrítico 150 años modeladas.

www.flujoing.cl / info@flujoing.cl

23

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

La Figura 13 y Figura 14 ilustra los resultados de los efectos de socavación a partir de la

modelación con lecho móvil para el escenario T-150 años.

Como es posible observar, los efectos de socavación obtenidos son prácticamente

inexistentes, teniendo que en la mayor parte de las zonas de inundación las socavaciones

son nulas. Este fenómeno se limita a zonas específicas de los escurrimientos de mayor

relevancia y zonas puntuales, con magnitudes inferiores a 5 cm, lo cual se considera

poco significativo para la naturaleza del fenómeno analizado.

Los insignificantes efectos de socavación observados en el área de estudio son

consistentes con los bajos caudales determinados para el estudio hidráulico, y las

escasas profundidades y velocidades de los escurrimientos que estos generan, los cuales

no generan tensiones cortantes suficientes para generar arrastre de sedimentos y

socavaciones de magnitudes relevantes.

Adicionalmente, las obras del proyecto que se determinaron emplazadas en los límites

de zonas inundables (camino de acceso), no serán afectadas por el fenómeno de

socavación para el escenario T-150 años analizado, ya que se ubican en zonas donde

las socavaciones estimadas son nulas, descartando la afectación para estas

componentes.

Se determina por lo tanto que las obras y componentes del proyecto no serán afectadas

por el fenómeno de socavación de los cauces analizados y que no se requieren ni

proyectan obras que los intervengan.

www.flujoing.cl / info@flujoing.cl

24

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

**Figura 13. Socavaciones escenario T-150 años Parte 1.**

**Fuente: Elaboración propia.**

**Figura 14. Socavaciones escenario T-150 años Parte 2.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

25

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### 5. APLICABILIDAD PERMISOS AMBIENTALES SECTORIALES

A partir de lo desarrollado en el presente estudio, particularmente los resultados

presentados en los capítulos 3 y 4, se analiza en este acápite la aplicabilidad de los

permisos ambientales sectoriales correspondientes a cauces naturales, específicamente,

los Permisos Ambientales Sectoriales 156 y 157.

En primer lugar, se considera que el permiso para efectuar modificaciones de cauce

(PAS 156) se fundamenta en los artículos 41 y 171 inciso 1o del D.F.L. No 1.122, de 1981, del

Ministerio de Justicia, Código de Aguas. En este sentido, es de particular importancia lo

dispuesto en los incisos 1° y 2° del artículo 41, donde se establece que:

_“El proyecto y construcción de las modificaciones que fueren necesarias realizar en_

_cauces naturales o artificiales, con motivo de la construcción de obras, urbanizaciones y_

_edificaciones que puedan causar daño a la vida, salud o bienes de la población o que_

_de alguna manera alteren el régimen de escurrimiento de las aguas, serán de_

_responsabilidad del interesado y deberán ser aprobadas previamente por la Dirección_

_General de Aguas de conformidad con el procedimiento establecido en el párrafo 1 del_

_Título I del Libro Segundo del Código de Aguas. La Dirección General de Aguas_

_determinará mediante resolución fundada cuáles son las obras y características que se_

_encuentran en la situación anterior”._

_“Se entenderá por modificaciones no solo el cambio de trazado de los cauces mismos,_

_sino también la alteración o sustitución de cualquiera de sus obras de arte y la_

_construcción de nuevas obras, como abovedamientos, pasos sobre o bajo nivel o_

_cualesquiera otras de sustitución o complemento”._

Adicionalmente, el permiso para efectuar obras de regularización o defensa de cauces

naturales (PAS 157) se fundamenta en el inciso del artículo 171 que indica: _“Cuando se_

_trate de obras de regularización o defensa de cauces naturales, los proyectos respectivos_

_deberán contar, además, con la aprobación de la Dirección de Obras Hidráulicas del_

_Ministerio de Obras Públicas”._

www.flujoing.cl / info@flujoing.cl

26

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Según se establece en la guía ambiental del permiso para efectuar modificaciones de

cauce (PAS 156), las obras de regularización o defensa de cauces naturales se exceptúan

de la aplicabilidad del PAS 156, correspondiendo para este tipo de obras la

presentación del Permiso Ambiental Sectorial 157.

Considerando todo lo anterior, se analiza en primer lugar la aplicabilidad de estos

permisos para los recintos del proyecto. En este sentido, en el capítulo 3 se estableció

que los recintos de obras permanentes y temporales se proyectan fuera de los límites de

inundación de la crecida centenaria de los cauces identificados dentro del área de

influencia, sin requerir obras de defensa u otras obras adicionales que los intervengan.

Las Figura 15 y Figura 16 presentadas a continuación profundizan dicha información,

entregando una vista detallada de estas zonas.

**Figura 15. Profundidades inundación zona recinto principal proyecto BH8.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

27

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

**Figura 16. Profundidades inundación zona recinto secundario proyecto BH8.**

**Fuente: Elaboración propia.**

En este sentido, es importante aclarar que el presente estudio hidráulico utilizó un

levantamiento topográfico significativamente más amplio en comparación con el estudio

hidráulico precedente en la evaluación ambiental, permitiendo un modelamiento

hidráulico más realista del flujo de la Cuenca 1. Al modelar dicha quebrada en toda su

amplitud transversal se obtuvo que la mayor parte del caudal de esta quebrada escurre

al sur del recinto donde se emplazan las baterías del proyecto, y que dicho recinto no

será afectado por la crecida centenaria, desafectando la necesidad de la obra de

defensa y respectivo PAS 157 previamente presentado.

Por otro lado, en el capítulo 3 se identificó que el camino de acceso cruza en algunos

puntos flujos secundarios provenientes de la Cuenca 1. Estos resultados son consistentes

con el estudio hidráulico precedente. Sin embargo, los flujos que enfrentan estas

componentes son de escasa magnitud, con profundidades inferiores a 0.25 m y

velocidades inferiores a 0.5 m/s, descartando así la necesidad de obras adicionales que

intervengan los cauces.

www.flujoing.cl / info@flujoing.cl

28

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Adicionalmente, de acuerdo con lo solicitado en el ICSARA Complementario de la

evaluación ambiental del Proyecto, en este estudio se realizó un análisis de socavaciones

para los cauces del AI. El objetivo fue determinar si las obras emplazadas en zonas

inundables (camino de acceso) serían afectadas por este fenómeno, y analizar la

eventual necesidad de obras de protección y los permisos ambientales sectoriales

aplicables.

Los resultados de este análisis se presentaron en el acápite 4.4, estableciendo que las

obras del proyecto que se determinaron emplazadas en los límites de zonas inundables

(camino de acceso), no serán afectadas por el fenómeno de socavación para el

escenario T-150 años analizado, ya que se ubican en zonas donde las socavaciones

estimadas son nulas, descartando la afectación para estas componentes.

A partir de todo lo anterior, se descarta que se requieran obras de defensa,

regularización identificados en el Área de Influencia, desafectando entonces para el

Proyecto la aplicabilidad del permiso ambiental sectorial 157, respectivos a cauces

naturales.

Independiente de lo anterior, y a modo conservador como medida de resguardo, se

proponen obras tipo badén en las zonas inundables del camino de acceso, donde se

requerirán intervención y modificación del cauce, por lo tanto, se presenta en la actual

Adenda el permiso ambiental sectorial 156 de modificación de cauces.

### 6. CONCLUSIÓN

Conforme a los objetivos y alcances de este estudio, utilizando como referencia las guías

y manuales aplicables y vigentes en Chile para la realización de estudios hidráulicos

para proyectos en el Sistema de Evaluación Ambiental, se desarrolló en el presente

informe el estudio hidráulico de inundaciones del área de interés del proyecto.

Se desarrollaron los análisis de inundaciones para el escenario extraordinario T-100 y T

150 años en el área de estudio, determinando las zonas inundables y sus principales

variables hidráulicas (profundidades y velocidades).

www.flujoing.cl / info@flujoing.cl

29

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

Se obtuvo en primer lugar que los recintos de obras permanentes y temporales del

proyecto se emplazan fuera de los límites de los cauces naturales identificados en el AI,

sin requerir obras de defensa u otras obras que los intervengan.

En este sentido, se aclara que el presente estudio hidráulico realizó un modelamiento

hidráulico más realista del flujo de la Cuenca 1 en comparación con el estudio hidráulico

precedente en la evaluación ambiental, producto de la ampliación topográfica

desarrollada. Al modelar dicha quebrada en toda su amplitud transversal se obtuvo que

la mayor parte del caudal de esta quebrada escurre al sur del recinto donde se

emplazan las baterías del proyecto, resultando en que dicho recinto no será afectado

por la crecida centenaria, por lo tanto, se desafecta la necesidad de la obra de defensa

y el PAS 157 previamente presentado.

Por otro lado, las únicas obras y componentes del proyecto que se emplazan en zonas

inundables de estos cauces para los escenario T-100 y T-150 años, corresponden al

camino de acceso. Sin embargo, se tiene que los flujos que enfrentan estas componentes

son de escasa magnitud, con profundidades inferiores a 0.25 m y velocidades inferiores

a 0.5 m/s, sin generar ninguna afectación para estas obras, por lo tanto, no requieren

obras de protección u de otro tipo que intervengan estos cauces.

Adicionalmente, según fue solicitado en el ICSARA Complementario, se desarrolló un

estudio de socavaciones en el área de estudio, considerando el escenario más

desfavorable (T-150 años). Se obtuvo que los efectos de socavación para dicho escenario

son prácticamente inexistentes, y que las obras del proyecto que se determinaron

emplazadas en los límites de zonas inundables (camino de acceso) no serán afectadas

por este fenómeno, ya que se emplazan en zonas donde las socavaciones estimadas son

nulas, descartando la afectación para estas componentes.

Por lo tanto, se descarta que se requieran obras de defensa o regularización de los

cauces identificados en el Área de Influencia, desafectando entonces la aplicabilidad

del permiso ambiental sectorial 157 respectivos a cauces naturales para el Proyecto.

De todos modos, de forma conservadora como medida de resguardo, se proponen

obras tipo badén en las zonas inundables del camino de acceso, donde se requerirán

www.flujoing.cl / info@flujoing.cl

30

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

intervención y modificación del cauce, por lo tanto, se presenta en la actual Adenda el

permiso ambiental sectorial 156 de modificación de cauces.

www.flujoing.cl / info@flujoing.cl

31

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### 7. BIBLIOGRAFÍA

DGA-MOP. (2016). _Guías Metodológicas para Presentación y Revisión Técnica de_

_Proyectos de Modificación de Cauces Naturales y Artificiales._ Santiago, Chile:

Departamento de administración de recursos hídricos.

Dirección de Vialidad - MOP. (2021). _Manual de Carreteras._ Chile: MOP-DGOP.

Dirección General de Aguas. (1991). _Precipitaciones máximas en 1, 2 y 3 días._ Chile:

CIRH-DGA.

Dirección General de Aguas. (1995). _Manual de cálculo de crecidas y caudales mínimos_

_en cuencas sin información fluviométrica._ Chile: CIRH-DGA.

Instituto Geográfico Militar. (1922). _Instituto Geográfico Militar de Chile_ . Obtenido de

https://www.igm.cl/

Ministerio de Bienes Nacionales. (2023). _IDE Chile_ . Obtenido de Infraestructura de

Datos Geoespaciales: https://www.ide.cl/

MOP. (1981). _Código de Aguas - DFL No1.122._ Santiago, Chile.

SEA. (2017). _Guía para la descripción del área de influencia._

SEA. (2021). _Criterio de evaluación en la SEIA: Contenidos técnicos para la evaluación_

_ambiental del Recurso Hídrico._

SERNAGEOMIN. (2003). _Mapa Geológico de Chile._

Te Chow, V., R. Maidment, D., & W. Mays, L. (1994). _Hidrología Aplicada._ Illinois:

McGraw-Hill.

United States Department of Agriculture. (1986). _Urban Hydrology for Small Watersheds_

_TR-55._ Washington DC: Conservation Engineering Division.

www.flujoing.cl / info@flujoing.cl

32

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### 8. SUBANEXOS

www.flujoing.cl / info@flujoing.cl

33

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

## SUBANEXO No1 (Mapas de hidráulica )

www.flujoing.cl / info@flujoing.cl

34

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### SUBANEXO No2 “MAPAS DE SOCAVACIONES”

info@flujoing.cl / www.flujoing.cl

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### SUBANEXO No3 “ENSAYO DE MECÁNICA DE SUELOS”

info@flujoing.cl / www.flujoing.cl

Copiapó, 11 de Abril de 2024 **Informe No 111826** **Correlativo No 1**
LEPUCV S.A. - Avenida Copayapu 5184, Copiapó

**INFORME DE ENSAYOS: ÁREA MECÁNICA DE SUELOS**

**1 de 1**

|Obra: BESS Halcón 3 / BFSS Halcón 8|Solicitante/Cliente: Oenergy Development SpA|
|---|---|
|Ubicación:<br>**Tierra Amarilla - Región de Atacama**|Dirección:<br>**Apoquindo N°3910 - Oficina N°201 - Las**<br>**Condes - Región Metropolitana de Santiago**|

|IDENTIFICACIÓN DE LA MUESTRA|Col2|
|---|---|
|Fecha ingreso muestra:<br>**09.04.2024**|No orden de trabajo:<br>**106634**|
|Responsable extracción:<br>**Cliente**|Responsable ensayo:<br>**Mario Reinoso**|

|No|Descripción visual del suelo|Tipo de material|Procedencia y ubicación de la muestra|
|---|---|---|---|
|1|Arena limosa color café claro|Existente|BH8|

**RESULTADOS ENSAYOS**

|ANÁLISIS GRANULOMÉTRICO - % QUE PASA EN EL TAMIZ<br>(Suelos. Método para determinar la Granulometría 8.102.1 (MC-V8, Diciembre 2003))|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**No**|**Fecha ensayo**|**3''**|**2 1/2''**|**2''**|**1 1/2''**|**1''**|**3/4''**|**3/8''**|**No4**|**No10**|**No40**|**No200**|
|1|10.04.2024|-|-|-|-|100|99|96|94|89|71|25|

Notas: (1) Los resultados entregados en el presente informe se relacionan solamente con los ítems sometidos a ensayo.

**(2) Los antecedentes proporcionados y las condiciones de extracción de la muestra, son de exclusiva responsabilidad del cliente.**

**(3) Contacto Solicitante: Cristóbal Ebensperger - cristobal.ebensperger@oenergy.cl**

**Jefe Laboratorio Regional**
**LePUCV S.A.**

RIE-11/V19/28.03.22

www.lepucv.cl
LA INFORMACIÓN CONTENIDA EN ESTE DOCUMENTO NO DEBE SER REPRODUCIDA O TRANSMITIDA SIN LA AUTORIZACIÓN PREVIA Y POR ESCRITO DE LEPUCV S.A.

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

### SUBANEXO No4 “EXTRAPOLACIÓN CAUDALES DE MODELACIÓN”

info@flujoing.cl / www.flujoing.cl

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

|Caudal (m3/s)<br>Periodo de retorno (años)<br>Cuenca 1 Cuenca 2 Cuenca 3|Col2|Col3|Col4|
|---|---|---|---|
|**Periodo de retorno (años)**<br>**Caudal (m3/s)**<br>Cuenca 1<br>Cuenca 2<br>Cuenca 3|Cuenca 1|Cuenca 2|Cuenca 3|
|10|0.64|0.09|0.04|
|25|0.86|0.09|0.05|
|50|1.02|0.12|0.07|
|75|1.09|0.16|0.08|
|100|1.19|0.18|0.08|

**Tabla SA-1. Caudales líquidos quebradas de estudio.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8.**

**Figura SA-1. Ajuste logarítmico Caudales Cuenca 1**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl
1

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

**Figura SA-2. Ajuste logarítmico Caudales Cuenca 2**

**Fuente: Elaboración propia.**

**Figura SA-3. Ajuste logarítmico Caudales Cuenca 3**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl
2

| ESTUDIO HIDRÁULICO BESS HALCÓN 8

|Caudal (m3/s)<br>Periodo de retorno (años)<br>Cuenca 1 Cuenca 2 Cuenca 3|Col2|Col3|Col4|
|---|---|---|---|
|**Periodo de retorno (años)**<br>**Caudal (m3/s)**<br>Cuenca 1<br>Cuenca 2<br>Cuenca 3|Cuenca 1|Cuenca 2|Cuenca 3|
|10|0.64|0.09|0.04|
|25|0.86|0.09|0.05|
|50|1.02|0.12|0.07|
|75|1.09|0.16|0.08|
|100|1.19|0.18|0.08|
|150|1.27|0.19|0.09|

**Tabla SA-2. Caudales líquidos quebradas de estudio con extrapolación.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8.**

|Caudal (m3/s)<br>Periodo de retorno (años)<br>Cuenca 1 Cuenca 2 Cuenca 3|Col2|Col3|Col4|
|---|---|---|---|
|**Periodo de retorno (años)**<br>**Caudal (m3/s)**<br>Cuenca 1<br>Cuenca 2<br>Cuenca 3|Cuenca 1|Cuenca 2|Cuenca 3|
|10|0.91|0.13|0.06|
|25|1.23|0.13|0.07|
|50|1.46|0.17|0.10|
|75|1.56|0.23|0.11|
|100|1.70|0.26|0.11|
|150|1.82|0.27|0.13|

**Tabla SA-3. Caudales detríticos quebradas de estudio con extrapolación.**

**Fuente: Estudio hidrológico e Hidráulico BESS Halcón 8.**

info@flujoing.cl / www.flujoing.cl
3

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Caudales líquidos quebradas de estudio.****

| Caudal (m3/s)<br>Periodo de retorno (años)<br>Cuenca 1 Cuenca 2 Cuenca 3 | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Periodo de retorno (años)<br>Caudal (m3/s)<br>Cuenca 1<br>Cuenca 2<br>Cuenca 3 | Cuenca 1 | Cuenca 2 | Cuenca 3 |
| 10 | 0.91 | 0.13 | 0.06 |
| 25 | 1.23 | 0.13 | 0.07 |
| 50 | 1.46 | 0.17 | 0.10 |
| 75 | 1.56 | 0.23 | 0.11 |
| 100 | 1.70 | 0.26 | 0.11 |
| 150 | 1.82 | 0.27 | 0.13 |

**Tabla 3.**

| Condición Valor | Col2 | Col3 |
| --- | --- | --- |
| Material del lecho | n0 | 0.0225 |
| Grado de irregularidad P.M. | n1 | 0.0000 |
| Variaciones de secciones | n2 | 0.0000 |
| Efecto relativo de las obstrucciones | n3 | 0.0000 |
| Densidad de vegetación | n4 | 0.0050 |
| Sinuosidad y frecuencia de meandros | m | 1.0000 |
| n | n | 0.0275 |
