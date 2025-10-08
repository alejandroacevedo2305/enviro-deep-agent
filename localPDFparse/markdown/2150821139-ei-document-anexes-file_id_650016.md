---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: manual
pages: 33
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Grupo Estelar SpA Anexo 6 Estudio de Campos electromagnéticos
-->

# Grupo Estelar SpA Anexo 6 Estudio de Campos electromagnéticos

## Declaración de Impacto Ambiental del Proyecto “Parque Fotovoltaico Fénix”

### Región de Atacama

Febrero, 2021

Elaborado por:

**Gestión Ambiental Consultores S.A.**

General del Canto 421, Piso 6, Providencia,

Santiago, Chile - Fono: +56 2 2719 5600

www.gac.cl

#### ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PARQUE FOTOVOLTAICO FÉNIX

##### Nelson Morales Osorio Febrero 2021

2

**CONTENIDO**

1 Objetivo y alcance del estudio .................................................................................................... 4

2 Características del proyecto ........................................................................................................ 4

2.1 Centros de Transformación ................................................................................................. 5

2.2 Punto de Evacuación ........................................................................................................... 5

2.3 Línea de interconexión de Media Tensión .......................................................................... 6

3 Normativa de referencia para Radio interferencia ..................................................................... 6

_4_ Normas de referencia para campos electromagnéticos de 50 Hz .............................................. 7

5 Campo magnético de centros de transformación....................................................................... 8

6 Modelamiento de Línea de transmisión de 23 kV ...................................................................... 9

7 radio interferencia por fenómeno corona ................................................................................ 13

8 EFECTOS SINÉRGICOS con paralelismo DE LÍNEAS ....................................................................... 14

9 Zona de Influencia ..................................................................................................................... 17

10 Conclusiones.......................................................................................................................... 18

11 Referencias ............................................................................................................................ 19

ANEXO ............................................................................................................................................... 20

Estudio de radio interferencia para la línea ...................................................................................... 20

**LISTADO DE TABLAS**

Tabla 1 Nivel de perturbación radiofónica aceptable a 0,5 MHz ....................................................... 7

Tabla 2 Variación de la inducción magnética con distancia al transformador................................... 8

Tabla 3 Valores de campo en el borde de la franja y confrontación con norma ............................. 13

Tabla 4 Magnitud de radio interferencia y confrontación con norma ............................................. 14

Tabla 5 Valores de campo electromagnético en paralelismo de líneas ........................................... 17

3

**LISTADO DE FIGURAS**

Figura 1 Parque Solar Fénix y línea de conexión ................................................................................ 5

Figura 2 Esquema de estructura tipo de la línea de Media Tensión .................................................. 6

Figura 3 Reducción de la densidad de flujo magnético de equipos con la distancia ........................ 9

Figura 4 Malla de elementos finitos ................................................................................................ 10

Figura 5 Distribución de líneas equipotenciales eléctricas .............................................................. 11

Figura 6 Campo eléctrico a 1m sobre el suelo bajo torre ................................................................ 11

Figura 7 Distribución de líneas equipotenciales magnéticas ........................................................... 12

Figura 8 Inducción magnética 1m sobre el suelo bajo torre ............................................................. 12

Figura 9 Radio interferencia vs distancia a la línea ........................................................................... 14

Figura 10 Malla de elementos finitos en zona de paralelismo......................................................... 15

Figura 11 Distribución de equipotenciales eléctricas ....................................................................... 15

Figura 12 Campo eléctrico a 1m sobre el suelo en zona de paralelismo ......................................... 16

Figura 13 Distribución de equipotenciales magnéticas ................................................................... 16

Figura 14 Inducción magnética a 1m sobre el suelo en zona de paralelismo .................................. 17

4

**1** **OBJETIVO Y ALCANCE DEL ESTUDIO**

El propósito de este estudio es estimar la magnitud de los campos

electromagnéticos de baja y alta frecuencia provocados por la operación del Parque

Fotovoltaico Fénix y su línea de evacuación en 23 kV.

Se presenta en este documento información recogida de la literatura técnica

respecto de emisión provocada por los centros de transformación y resultados de una

simulación de la línea de evacuación de 23 kV; la simulación se efectúa con apoyo del

software QuickField [1] que utiliza el método de elementos finitos para obtener campo

eléctrico y campo magnético generados en la vecindad de conductores energizados.

Los valores obtenidos con los equipos y conductores operando en el voltaje

indicado, se confrontan posteriormente con las recomendaciones y límites admisibles

para establecer una conclusión respecto de la emisión electromagnética de baja

frecuencia provocada por la operación de los equipos.

Similarmente se realiza una estimación del nivel perturbador a frecuencias de radio

generado por los conductores de la línea de transmisión debido al fenómeno corona y se

compara con valores límites establecidos por recomendaciones internacionales. El cálculo

de nivel de perturbación a frecuencias de radio se determina aplicando métodos

aproximados de conocimiento general [2].

**2** **CARACTERÍSTICAS DEL PROYECTO**

El Parque Solar se ubica al costado norte de la ruta C-351, de acceso al puerto de

Caldera, y su línea de evacuación va paralela a esta ruta y a la línea Galleguillos Caldera

1x110kV; ambas acceden a la Subestación Caldera.

La Planta Fotovoltaica, está conformada por Bloques o conjuntos de paneles

solares los que suman un total de 9 MW AC. Cada Bloque cuenta con un Centro de

Transformación o Estación Inversora Transformadora que recibe la corriente generada

por los paneles solares para adecuarla y enviarla mediante cableado soterrado hasta el

Centro de Seccionamiento, donde converge la energía de bloques, para ser enviada

mediante una línea aérea de media tensión (23 KVA), hasta el punto de interconexión,

donde se entregará la energía al Sistema Eléctrico Nacional (SEN).

5

**Figura 1 Parque Solar Fénix y línea de conexión**

Fuente: Esquema entregado por Titular del Proyecto.

**2.1** **Centros de Transformación**

Cada Centro de Transformación contendrá un conjunto de uno o más inversores

que en total suman 2500 kW o más de potencia nominal. Adicionalmente, habrá un

transformador para convertir de Baja a Media Tensión, por cada Centro de

Transformación, elevando la tensión a un nivel de 23 kV de tensión, además de otros

equipos eléctricos pertinentes y usuales en dicho tipo de instalaciones, tal como

interruptores, relés y puesta a tierra.

Los inversores son equipos diseñados para trasformar la corriente continua

procedente del campo de paneles en corriente alterna compatible con la forma de

corriente de la red. Los transformadores son equipos diseñados para transformar el nivel

de tensión de la electricidad proveniente de los inversores desde un nivel a otro, para

luego ser inyectada a la red.

**2.2** **Punto de Evacuación**

Consiste en un contenedor que incorpora todos los equipos eléctricos necesarios

para recibir la energía desde los Centros de Transformación y que se evacuan a través de

la línea de interconexión que inicia en este lugar. El Proyecto no contará con una

6

subestación eléctrica, sino que se conectará directamente a la red de distribución

perteneciente al SEN.

**2.3** **Línea de interconexión de Media Tensión**

La evacuación de la energía eléctrica producida en el parque fotovoltaico se

realizará mediante un tendido eléctrico aéreo de 23 kV de tensión nominal, que conectará

el punto de evacuación de la planta con el punto de conexión. Las estructuras de soporte

de los conductores serán postes simples de hormigón armado o postes metálicos

ensamblados (tejidos) según corresponda. En la se muestra un esquema de una

estructura tipo a utilizar en la línea eléctrica.

**Figura 2 Esquema de estructura tipo de la línea de Media Tensión**

Fuente: Esquema entregado por Titular del Proyecto.

**3** **NORMATIVA DE REFERENCIA PARA RADIO INTERFERENCIA**

La referencia 3 indica el nivel de perturbación radio eléctrica aceptable generada

por líneas de transmisión o subestaciones, a una frecuencia de 0,5 MHz, Tabla siguiente:

7

**Tabla 1 Nivel de perturbación radiofónica aceptable a 0,5 MHz**

|Tensión eléctrica<br>nominal entre fases (kV)|Radio interferencia<br>[dB /1 μV/m]|
|---|---|
|Bajo 70|43|
|70 - 200|49|
|200 - 300|53|
|300 - 400|56|
|400 - 600|60|
|Sobre 600|63|
|Para una línea, valores a 15 m de distancia lateral de la fase externa<br>Para una subestación, valores a 15 m del borde|Para una línea, valores a 15 m de distancia lateral de la fase externa<br>Para una subestación, valores a 15 m del borde|

Fuente: Referencia [3]

Para una instalación de 23 kV, el límite correspondiente es 43 [dB/ (1V/m)] .

_**4**_ **NORMAS DE REFERENCIA PARA CAMPOS ELECTROMAGNÉTICOS DE 50 HZ**

En nuestro país no existe reglamentación relativa a los valores límites permitidos

de exposición de las personas a los campos electromagnéticos de frecuencia industrial. No

obstante, la regulación ambiental que rige el tema de emisiones señala que, de no existir

una regulación nacional, debe aplicarse como norma de referencia aquella que se

encuentre vigente en estados específicos. El Decreto No 40 del Ministerio del Medio

Ambiente, “Aprueba Reglamento del Sistema de Evaluación de Impacto Ambiental”,

publicado el 12-08-2013, y que entró en vigencia el 24-12-2013, indica en su Artículo 11:

_“Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los_

_efectos de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos_

_adversos señalados en la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes_

_en los siguientes Estados: República Federal de Alemania, República Argentina, Australia,_

_República Federativa del Brasil, Canadá, Reino de España, Estados Unidos Mexicanos,_

_Estados Unidos de América, Nueva Zelandia, Reino de los Países Bajos, República Italiana,_

_Japón, Reino de Suecia y Confederación Suiza. Para la utilización de las normas de_

_referencia, se priorizará aquel Estado que posea similitud en sus componentes_

_ambientales, con la situación nacional y/o local, lo que será justificado razonablemente_

_por el proponente._

8

La recomendación de uso más frecuente para público general y exposición

permanente, es la publicada por la ICNIRP [4], organismo no gubernamental reconocido

por la Organización Mundial de la Salud como referente en el tema, que establece 5.000

[V/m] para el campo eléctrico y 200 [micro Tesla], equivalente a 2.000 [mili Gauss] para la

inducción magnética, valores que han sido acogidos por la normativa de diversos países

incluidos en la nómina anterior.

**5** **CAMPO MAGNÉTICO DE CENTROS DE TRANSFORMACIÓN**

La densidad de flujo B está muy relacionada con la potencia aparente nominal de

un transformador. En base a una serie de experiencias y resultados obtenidos en una

amplia gama de potencias, en la referencia [5] se sugiere una relación simple para el valor

efectivo de la inducción magnética en la vecindad de un transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla]

P N : Potencia Nominal del transformador [kVA]

r: Distancia desde el centro del transformador [m]

k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA]

Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

Esta expresión indica que la densidad de flujo magnético de transformadores

decrece rápidamente al alejarse del transformador (relación inversa con la tercera

potencia de la distancia). De acuerdo a esta expresión, con un transformador de 2.500

KVA de cada Centro de Transformación, la densidad de flujo magnético B a una distancia D

desde el centro del transformador es la siguiente:

**Tabla 2 Variación de la inducción magnética con distancia al transformador**

|Distancia D[m]|2|4|6|8|10|
|---|---|---|---|---|---|
|Inducción magnética B[micro Tesla]|12,5|1,56|0,46|0,20|0,10|
|Inducción magnética B[mili Gauss]|125|15,6|4,6|2,0|1,0|

Fuente: Elaboración propia

Se observa que a partir de 5m del transformador, la inducción magnética se reduce

a un valor inferior a 1,0 [micro Tesla] o equivalentemente, 10 [mili Gauss]. Por lo tanto, el

área de influencia para el campo magnético de cada transformador de 1.500 kVA abarca

aproximadamente 5m en torno al transformador.

9

La referencia [5] también entrega un ábaco que se reproduce en la Figura

siguiente, correspondiente a valores medidos en transformadores y switchgear de HV y

MV.

**Figura 3 Reducción de la densidad de flujo magnético de equipos con la distancia**

Fuente: Referencia [5]

Por lo tanto, el campo magnético generado por los Centros de Transformación,

incluyendo transformador y equipos anexos, a pesar de que puede ser intenso en la

proximidad inmediata de los Centros, decrece rápidamente siendo no relevante a 8 m de

distancia, pues decae a menos de 1 [micro Tesla] (equivalente a 10 [mili Gauss], no

representando impacto hacia el exterior del Parque.

**6** **MODELAMIENTO DE LÍNEA DE TRANSMISIÓN DE 23 KV**

En la vecindad de una línea aérea, el campo eléctrico se debe a que el conductor

está directamente expuesto al aire (no existe aislamiento sólido, el aislamiento está

definido por espaciamientos de aire) y sobre dicho conductor está aplicado alto voltaje

respecto de tierra, que actúa como conductor de referencia a potencial cero. Sus unidades

10

son Volt por metro [V/m] o Kilovolt por metro [kV/m] en alta tensión; en el caso en

estudio, 23 kV entre fases y 23/√3 KV fase a tierra.

El campo magnético se debe a la corriente que circula por los conductores y no

depende del nivel de voltaje de la línea pero sí del consumo. Para este estudio se

consideró una potencia nominal a transmitir por la línea de 9 MVA, lo que en 23 kV define

226 Amperes como corriente nominal por fase. La magnitud representativa del campo

magnético es la “inducción Magnética” o “densidad de flujo Magnético” B **,** que tiene

como unidad de medida práctica el mili Gauss (1 mG = 10 [-3] Gauss) o el micro Tesla (1T =
10 [-6] Tesla ) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra

caracterizar al campo eléctrico y el campo magnético cerca de una instalación de alta

tensión por el concepto “Campo a nivel del suelo”, que corresponde al campo eléctrico o

magnético medido o calculado a 1 metro de altura sobre el suelo, en ausencia de otros

objetos. El análisis mediante elementos finitos para el concepto campo a nivel del suelo,

se presenta a continuación para la estructura mostrada en la Figura 2.

**Figura 4 Malla de elementos finitos**

Fuente: Elaboración propia

11

**Figura 5 Distribución de líneas equipotenciales eléctricas**

Fuente: Elaboración propia

**Figura 6 Campo eléctrico a 1m sobre el suelo bajo torre**

Fuente: Elaboración propia

12

**Figura 7 Distribución de líneas equipotenciales magnéticas**

Fuente: Elaboración propia

**Figura 8 Inducción magnética 1m sobre el suelo bajo torre**

Fuente: Elaboración propia

13

En la Tabla siguiente se presenta los valores obtenidos a 1m de altura sobre el

suelo en el borde de la franja de seguridad, considerada con un ancho total de 20m y la

confrontación con los límites señalados por la ICNIRP [4].

**Tabla 3 Valores de campo en el borde de la franja y confrontación con norma**

|Col1|Campo<br>eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Inducción<br>magnética<br>[mili Gauss]|
|---|---|---|---|
|Poste|108|0,30|3,0|
|Límite<br>ICNIRP|5.000|200|2.000|

Fuente: Elaboración propia

**7** **RADIO INTERFERENCIA POR FENÓMENO CORONA**

La descarga corona en líneas de alta tensión corresponde a descargas eléctricas

parciales en el aire alrededor de los conductores, generadas por alto campo eléctrico, que

provoca ionización del aire. Este fenómeno emite campos electromagnéticos desde

frecuencias de audio hasta alta frecuencia que pueden provocar perturbaciones en la

banda de frecuencia de radio.

Mediante la aplicación del software LINEAS, de elaboración propia, se determina el

campo eléctrico en la superficie de los conductores y la radio interferencia emitida por la

estructura de la línea de 23 kV. El programa ocupa el Método de Simulación de Cargas [2]

para determinar el campo eléctrico superficial y el procedimiento CIGRE para evaluar nivel

de interferencia [2]. En el ANEXO A se presenta el listado de salida del programa, para la

estructura analizada; a continuación, se incluye el gráfico de variación con la distancia al

eje de la estructura. La línea verde señala la distancia de norma.

14

**Figura 9 Radio interferencia vs distancia a la línea**

Fuente: Elaboración propia

La Tabla siguiente resume la magnitud de radio interferencia calculada para la

estructura analizada, a 0,5 MHz y a 15m de distancia lateral desde el conductor externo,

según norma canadiense [3], y confrontada con el valor límite establecido por la norma.

**Tabla 4 Magnitud de radio interferencia y confrontación con norma**

|Col1|RI [dB/uV/m]|
|---|---|
|Poste|18,8|
|Límite norma canadiense|43|
|Cumplimiento|SI|

Fuente: Elaboración propia

**8 EFECTOS SINÉRGICOS CON PARALELISMO DE LÍNEAS**

De acuerdo con la información aportada por el Coordinador Eléctrico, la línea de

evacuación del Parque es paralela a la línea de transmisión Galleguillos - Tap ImpulsiónCaldera de 1x110kV, 69 MVA. La separación entre los ejes de ambas líneas es 20m, según

Google Earth.

Para evaluar el efecto sinérgico que se produce por el paralelismo de líneas, se

aplica la metodología de elementos finitos, con apoyo del software QuickField ya

mencionado, que permite evaluar campos en un plano transversal a las líneas.

15

**Figura 10 Malla de elementos finitos en zona de paralelismo**

**Figura 11 Distribución de equipotenciales eléctricas**

16

**Figura 12 Campo eléctrico a 1m sobre el suelo en zona de paralelismo**

**Figura 13 Distribución de equipotenciales magnéticas**

17

**Figura 14 Inducción magnética a 1m sobre el suelo en zona de paralelismo**

La Tabla siguiente resume los valores máximos encontrados en el borde de la

franja de la línea.

**Tabla 5 Valores de campo electromagnético en paralelismo de líneas**

|Campo eléctrico<br>[V/m]|Col2|Inducción magnética<br>[mili Gauss]|Col4|
|---|---|---|---|
|Máximo|Borde franja|Máximo|Borde franja|
|1.570|1.570|3,27|1,62|

Fuente: Elaboración propia

**9** **ZONA DE INFLUENCIA**

De los resultados indicados, se desprende que la zona de influencia de la

componente campos electromagnéticos para la línea de transmisión de 23 kV, puede

definirse en 25 m totales, 12,5 m hacia cada lado del eje de la línea a lo largo de toda la

18

línea. Con respecto al Parque, se estima en el área comprometida por el Parque,

extendida en 10m hacia el exterior en todo su perímetro.

**10** **CONCLUSIONES**

De acuerdo a los resultados obtenidos en la investigación bibliográfica y en la

modelación de campos electromagnéticos, se concluye que:

 - La magnitud máxima de campo eléctrico existente a un metro de altura sobre el

suelo en torno a la línea operando en 23 kV es 258 [Volt/m] y en el borde del Área

de Influencia es 108 [V/m]; estos valores son muy inferiores al límite de 5.000

[V/m] considerado internacionalmente como seguro para personas.

 - La magnitud máxima de inducción magnética existente a un metro de altura sobre

el suelo en torno a la línea operando en 23 kV es 2,51 [micro Tesla] (equivalente a
25,1 [mili Gauss] y en el borde del Área de Influencia es 0,30 [micro Tesla]

(equivalente a 3,0 [mili Gauss], inferior al límite de 200 [micro Tesla] o 2.000 [mili

Gauss], considerado internacionalmente como seguro.

 - La magnitud de radio interferencia generada por la línea a la distancia y frecuencia

de norma es 18,80 [dB/uV/m], inferior al límite establecido por la norma

canadiense, de 43 [dB/uV/m].

Por lo tanto, las instalaciones del Proyecto Parque Fotovoltaico Fénix satisfacen los

valores establecidos por la normativa vigente, respecto de campos electromagnéticos de

baja y alta frecuencia.

Con respecto a los valores de campo eléctrico en la zona de paralelismo de líneas,

dada la proximidad entre ambas líneas, dichos valores quedan definidos por la línea de

mayor tensión, siendo muy superiores a los generados por la línea de 23 kV, pero

inferiores a los límites establecidos por la ICNIRP; los valores de campo magnético sin

embargo son comparables, pero también resultan inferiores a los límites establecidos por

la ICNIRP.

19

**11** **REFERENCIAS**

[1] Students' QuickField (TM) Finite Element Analysis System

Version 5.8 User's Guide

Copyright (C) Tera Analysis Company, 2010.

[2] N. Morales, "Fenómeno corona en líneas de transmisión y sus efectos".

Publicación T(P)/9, Departamento de Ingeniería Eléctrica. Noviembre 1986.

[3] Association canadienne de normalisation, Valeurs limites et methods de mesure du

bruit électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant

alternatif. CAN3- C108.3.1 - M84. Octobre 1984.

4 International Commission on Non‐Ionizing Radiation Protection

ICNIRP Publication - 2010

ICNIRP Guidelines for limiting exposure to time‐varying electric and magnetic fields

(1 hz - 100 kHz)

Published in: Health Physics 99(6):818‐836; 2010

[5] Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power Substations

Gerhard Bräunlich, Reinhold Bräunlich ETH Zürich, Switzerland

FKH Fachkommission für Hochspannungsfragen

Proceedings, 20th Int. Zurich Symposium on EMC, Zurich 2009

20

**ANEXO A**

**ESTUDIO DE RADIO INTERFERENCIA PARA LA LÍNEA**

Se presenta a continuación el listado de salida del programa LINEAS, que calcula

campo eléctrico superficial en conductores de línea de alta tensión y radio interferencia,

aplicado a la estructura en estudio.

NOTA: El programa utiliza punto decimal (.) en lugar de coma (,). No incluye tilde

de acentos.

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 3_

_Numero de conductores activos : 3_

_Numero de cables de guardia : 0_

|Fase|1|2|3|
|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_0.9150_|_0.9150_|_0.9150_|
|_Ubicacion lateral del conductor (m)_|_-1.200_|_0.000_|_1.2000_|
|_ Altura conductor sobre el suelo (m)_|_10.500_|_10.500_|_10.500_|

_Matriz de coeficientes (amplif. por (2 πƐ_ _0_ _))_

_7.7385 2.8638 2.1755_

_2.8638 7.7385 2.8638_

_2.1755 2.8638 7.7385_

_Matriz de capacitancias (amplif. por 1/( 2 πƐ_ _0_ _))_

_.1540 -.0475 -.0257_

_-.0475 .1644 -.0475_

_-.0257 -.0475 .1540_

_Potenciales de conductores ( KVolts)_

_( 13.2790, 0.0000 ) 13.2790_

_( -6.6395, -11.5000 ) 13.2790_

_( -6.6395, 11.5000 ) 13.2790_

_Cargas en conductores (Cb)/( 2 πƐ_ _0_ _)_

21

_( 2.5314, 0.2501 ) 2.5438_

_( -1.4065, -2.4362 ) 2.8131_

_( -1.0491, 2.3173 ) 2.5438_

_Gradientes superficiales (kVef./cm)_

_( 2.7666, 0.2733 ) 2.7801_

_( -1.5372, -2.6625 ) 3.0744_

_( -1.1466, 2.5326 ) 2.7801_

_Radio Interferencia_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|_17,34_|_17,27_|_17,43_||_18,804_|

##### Apéndice 6.1 LINEA DE BASE DE CAMPOS ELECTROMAGNÉTICOS PARQUE FOTOVOLTAICO FÉNIX Nelson Morales Osorio Febrero 2021

2

##### CONTENIDO

1. Objetivo ....................................................................................................................................... 3

2. Descripción .................................................................................................................................. 3

3. Metodología ................................................................................................................................ 3

4. Resultados ................................................................................................................................... 4

4.1 Planta Fotovoltaica .............................................................................................................. 4

4.2 Línea Galleguillos - Caldera................................................................................................. 5

4.3 Subestación Caldera ............................................................................................................ 7

5.- Conclusiones .................................................................................................................................. 8

Referencias ...................................................................................................................................... 9

ANEXO Instrumento y Procedimiento de medida ............................................................................ 10

A.1 Medida de campo eléctrico .................................................................................................... 10

A.2 Medida de campo magnético ................................................................................................. 11

##### LISTADO DE FIGURAS

Figura 1 Instalaciones Proyecto Solar Fénix ....................................................................................... 3

Figura 2 Sector ubicación Planta Fotovoltaica .................................................................................... 5

Figura 3 Trayectoria de medida Líneas Galleguillos - Caldera............................................................. 5

Figura 4 Campo eléctrico a 1m sobre el suelo bajo línea ................................................................... 6

Figura 5 Inducción magnética a 1m sobre el suelo bajo línea ........................................................... 6

Figura 6 Trayectoria de medida en SE Caldera ................................................................................... 7

Figura 7 Campo eléctrico a 1m sobre el suelo en trayectoria ............................................................ 7

Figura 8 Inducción magnética a 1m sobre el suelo en trayectoria .................................................... 8

Figura A 1 Medidor y dipolo detector de campo eléctrico; medida con pértiga aislante ................ 10

**Figura A 2** **Medidor y bobina detectora de campo magnético unixial orientada en tres**

**direcciones** ........................................................................................................................................ 11

**LISTADO DE TABLAS**

Tabla 1 Coordenadas puntos de medida ............................................................................................ 4

Tabla 2 Resumen de valores medidos ................................................................................................ 8

3

**1.** **Objetivo**

El propósito de este documento es entregar los resultados de la medición de

campo eléctrico y campo magnético de frecuencia industrial, generado por fuentes

existentes que afecten las instalaciones del Parque Fotovoltaico Fénix, con el propósito de

caracterizar la Línea de Base de la componente Campos Electromagnéticos del Proyecto.

**2.** **Descripción**

La Planta Fotovoltaica se ubica al costado norte de la ruta C-351, de acceso al puerto

de Caldera, y su línea de evacuación va paralela a esta ruta y accede a la Subestación

Caldera.

**Figura 1 Instalaciones Parque Fotovoltaico Fénix**

El trazado de la línea de evacuación es paralelo a la línea Galleguillos Caldera

1x110kV.

**3.** **Metodología**

Se realizó mediciones de acuerdo a la norma IEEE Standard 644-1994 "IEEE

Standard Procedure for Measurements of Power Frequency Electric and Magnetic Fields

from AC Power Lines" para caracterizar los campos generados por la línea paralela, en el

4

lugar de instalación de la planta fotovoltaica y en el punto de conexión de la línea de

evacuación. Los puntos considerados para caracterizar la Línea de Base son los siguientes:

**Tabla 1 Coordenadas puntos de medida**

|Punto|Ubicación|Coordenadas|Col4|
|---|---|---|---|
|1|Planta Fotovoltaica|19 J 328296 m E|7001854 m S|
|2|Línea Galleguillos - Caldera|19 J 327885 m E|7001553 m S|
|3|Subestación Caldera|19 J 321291 m E|7002387 m S|

El procedimiento establecido por la norma [1] indica que los campos deben

medirse a 1 metro de altura sobre el nivel del suelo. El equipo utilizado para las medidas

es el medidor de campo eléctrico EFM 130 Electric Field Meter y el medidor de campo

magnético EFM131 Magnetic Field Meter. El detalle del procedimiento e instrumento de

medida se incluye en Anexo **.**

**4.** **Resultados**

Las medidas se realizaron el día 6 de febrero de 2020. En los gráficos se identifica

con el símbolo ⇩ la ubicación de la línea.

**4.1** **Planta Fotovoltaica**

En el sector de ubicación de la planta fotovoltaica no existen fuentes de campo

electromagnético, como se aprecia en la Figura siguiente:

5

**Figura 2 Sector ubicación Planta Fotovoltaica**

Por lo tanto, el campo medido fue nulo:

Campo eléctrico: 0,0 [V/m]

Inducción magnética: 0,0 [mili Gauss]

**4.2** **Línea Galleguillos - Caldera**

**Figura 3 Trayectoria de medida Líneas Galleguillos - Caldera**

6

**Figura 4 Campo eléctrico a 1m sobre el suelo bajo línea**

**Figura 5 Inducción magnética a 1m sobre el suelo bajo línea**

**Comentario:**

Ambos perfiles se aprecian bastante definidos, dado que no existen otras

perturbaciones y el terreno es de relieve parejo. Los máximos valores medidos en esta

línea son:

Campo eléctrico: 1.060 [V/m]

Inducción magnética: 5,38 [mili Gauss

7

**4.3** **Subestación Caldera**

**Figura 6 Trayectoria de medida en SE Caldera**

**Figura 7 Campo eléctrico a 1m sobre el suelo en trayectoria**

8

**Figura 8 Inducción magnética a 1m sobre el suelo en trayectoria**

**Comentario:**

Los mayores valores, tanto de campo eléctrico como de campo magnético, se

obtienen en el acceso de la línea Galleguillos - Caldera. Los máximos valores medidos en

este punto son:

Campo eléctrico: 286 [V/m]

Inducción magnética: 1,85 [mili Gauss]

Estos valores resultan inferiores a los medidos en el trayecto de la misma línea, por

la mayor altura de los conductores y la distinta disposición de conductores en este caso.

**5.- Conclusiones**

Se ha identificado mediante medidas directas en terreno, valores característicos

del campo eléctrico y del campo magnético de fuentes existentes, para definir la Línea de

Base de la componente campos electromagnéticos para el Proyecto Fotovoltaico Fénix.

**Tabla 2 Resumen de valores medidos**

|Ubicación|Campo eléctrico<br>[V/m]|Inducción magnética<br>[mili Gauss]|
|---|---|---|
|Planta Fotovoltaica|0,0|0,0|
|Línea Galleguillos - Caldera|1.060|5,38|
|Subestación Caldera|286|1,85|

9

Ninguno de los valores medidos supera los máximos tolerables para las personas,

definidos por la ICNIRP [2], que corresponden a 5.000 [Volts/m] para el campo eléctrico y

1.000 [mili Gauss] para el campo magnético. La ICNIRP es un organismo experto de

consulta en temas de radiaciones no ionizantes reconocida por la Organización Mundial

de la Salud, OMS, la Organización Internacional del Trabajo (International Labour

Organization - ILO) y la Unión Europea.

**Referencias**

[1] IEEE Standard 644-1994 "IEEE Standard Procedure for Measurements of Power

Frequency Electric and Magnetic Fields from AC Power Lines".

[2] ICNIRP Guidelines for limiting exposure to time varying electric and magnetic fields

(1 Hz - 100 kHz)

Published in: Health Physics 99(6):818 - 836; 2010

International Commission on Non-Ionizing Radiation Protection

ICNIRP Publication - 2010

10

**ANEXO Instrumento y Procedimiento de medida**

De acuerdo a norma [1], la caracterización del campo eléctrico y del campo

magnético en líneas aéreas y subestaciones se realiza mediante perfiles medidos a un

metro de altura sobre el suelo.

**A.1 Medida de campo eléctrico**

El campo eléctrico generado por instalaciones de frecuencia industrial, por la

naturaleza conductiva del terreno a esa frecuencia y las alturas típicas de conductores

aéreos, es perpendicular al terreno hasta una altura aproximada de 2 metros, por lo que

sólo es necesario conocer la componente vertical del campo eléctrico. Los medidores de

tipo caja-dipolo están diseñados con el dipolo en sentido vertical. Se debe considerar el

valor del campo eléctrico no perturbado (es decir, el campo que existiría en ausencia de

personas u objetos); también el cuerpo humano es conductor, de modo que se utiliza una

pértiga aislante para sostener el equipo de medida evitando alterar el campo natural.

**Figura A 1 Medidor y dipolo detector de campo eléctrico; medida con pértiga aislante**

El medidor utilizado es el EFM 131 de EFM Company, Stockbridge. La sonda o

sensor de campo eléctrico, definido como “de cuerpo libre”, consiste en un dipolo en

forma de cajas rectangulares, con dimensiones de 7 por 20 centímetros. El detector es un

voltímetro digital. La sonda y el detector son introducidos en el campo eléctrico con un

11

mango aislante pues el observador debe estar lo suficientemente alejado de la sonda para

evitar perturbaciones del campo en la vecindad.

**A.2 Medida de campo magnético**

Para la medición del campo magnético existen menos mecanismos de perturbación

y errores comparado con el caso del campo eléctrico. El cuerpo humano y el terreno son

absolutamente permeables al campo magnético, luego la sonda puede ser sujeta con un

mango dieléctrico corto sin afectar las mediciones. En este caso se requiere conocer las

tres componentes del campo y evaluar vectorialmente la magnitud de la inducción.

El medidor de campo magnético consiste igualmente de dos partes, la sonda o

elemento sensor de campo, y el medidor, el cual procesa la señal de la sonda e indica el

valor efectivo (rms) de la inducción magnética en un display digital. La sonda de inducción

magnética consiste de una bobina eléctricamente blindada (elemento sensor uniaxial) y

embebida en resina.

**Figura A 2** **Medidor y bobina detectora de campo magnético unixial orientada en tres**

**direcciones**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Coordenadas puntos de medida****

| Punto | Ubicación | Coordenadas | Col4 |
| --- | --- | --- | --- |
| 1 | Planta Fotovoltaica | 19 J 328296 m E | 7001854 m S |
| 2 | Línea Galleguillos - Caldera | 19 J 327885 m E | 7001553 m S |
| 3 | Subestación Caldera | 19 J 321291 m E | 7002387 m S |

**Tabla 2: Resumen de valores medidos****

| Ubicación | Campo eléctrico<br>[V/m] | Inducción magnética<br>[mili Gauss] |
| --- | --- | --- |
| Planta Fotovoltaica | 0,0 | 0,0 |
| Línea Galleguillos - Caldera | 1.060 | 5,38 |
| Subestación Caldera | 286 | 1,85 |

**Tabla 3: Valores de campo en el borde de la franja y confrontación con norma****

| Col1 | Campo<br>eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Inducción<br>magnética<br>[mili Gauss] |
| --- | --- | --- | --- |
| Poste | 108 | 0,30 | 3,0 |
| Límite<br>ICNIRP | 5.000 | 200 | 2.000 |

**Tabla 4: Magnitud de radio interferencia y confrontación con norma****

| Col1 | RI [dB/uV/m] |
| --- | --- |
| Poste | 18,8 |
| Límite norma canadiense | 43 |
| Cumplimiento | SI |

**Tabla 5: Valores de campo electromagnético en paralelismo de líneas****

| Campo eléctrico<br>[V/m] | Col2 | Inducción magnética<br>[mili Gauss] | Col4 |
| --- | --- | --- | --- |
| Máximo | Borde franja | Máximo | Borde franja |
| 1.570 | 1.570 | 3,27 | 1,62 |
