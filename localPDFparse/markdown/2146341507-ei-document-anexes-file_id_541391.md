---
title: Sin título
author: Nelson MO
date: D:20200415180019-04'00'
language: es
type: report
pages: 17
has_toc: False
has_tables: True
extraction_quality: high
---

## INFORME ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PROYECTO PARQUE FOTOVOLTAICO TRUPÁN Nelson Morales Osorio Abril 2020

2

**CONTENIDO**

1 Objetivos y Alcance del Estudio .................................................................................................. 3

2 Descripción del Proyecto ............................................................................................................. 3

3 Campo magnético de transformadores ...................................................................................... 5

4 Análisis del campo electromagnético de la línea ........................................................................ 7

_5_ Normativa de referencia para Radio interferencia ................................................................... 12

_6_ Normas de referencia para campos electromagnéticos de 50 Hz ............................................ 13

7 Conclusiones.............................................................................................................................. 14

8 Referencias ................................................................................................................................ 15

Anexo Cálculo de radio interferencia generada por la línea ............................................................. 16

**LISTADO DE FIGURAS**

Figura 1 Parque Fotovoltaico Trupán y Línea de evacuación ............................................................. 4

Figura 2 Esquema de estructura tipo de la línea de Media Tensión .................................................. 5

Figura 3 Reducción de la densidad de flujo magnético de equipos con la distancia ........................ 6

Figura 4 Distribución de líneas equipotenciales eléctricas ................................................................ 8

Figura 5 Campo eléctrico a 1m sobre el suelo, bajo la línea .............................................................. 9

Figura 6 Distribución de líneas equipotenciales magnéticas ........................................................... 10

Figura 7 Inducción magnética a 1m sobre el suelo, bajo la línea ..................................................... 11

Figura 8 Radio interferencia de línea de 66 kV; distancia desde el eje ............................................. 12

**LISTADO DE TABLAS**

Tabla 1 Variación de la inducción magnética con distancia al transformador................................... 6

Tabla 2 Nivel de perturbación radiofónica aceptable a 0,5 MHz ..................................................... 12

Tabla 3 Valores finales para Planta fotovoltaica San Bernardo Trupán ........................................... 14

3

**1** **Introducción**

Este Informe presenta una estimación de los campos electromagnéticos de baja y alta

frecuencia que pueden presentarse en el entorno de las instalaciones del Proyecto Parque

Fotovoltaico Trupán, durante su operación.

**2** **Objetivos y Alcance del Estudio**

El objetivo del presente informe es estimar las emisiones de campos electromagnéticos y

verificar si cumplen con los límites establecidos en la norma de referencia utilizada.

Respecto de los alcances, Se entrega información respecto del campo electromagnético

generado por centros de transformación y los resultados de una simulación para el campo

eléctrico y el campo magnético en el entorno de la línea de transmisión. Para determinar la

magnitud de estos campos, se utiliza un programa computacional que aplica el método de

elementos finitos [1] para modelar la configuración a estudiar y resolver la ecuación

diferencial parcial que rige el comportamiento de los campos en la región a estudiar.

Los valores indicados se confrontan con las recomendaciones y límites admisibles [2] para

establecer finalmente una conclusión respecto al impacto ambiental de las instalaciones del

Parque, desde el punto de vista técnico de la emisión electromagnética de baja frecuencia.

Similarmente se realiza una estimación del nivel perturbador a frecuencias de radio

generado por la línea de transmisión debido al fenómeno corona, en base a expresiones

simplificadas de uso habitual, y se compara con valores límites establecidos por

recomendaciones internacionales [3].

**3** **Descripción del Proyecto**

El Proyecto PARQUE FOTOVOLTAICO TRUPÁN consiste en un parque fotovoltaico de 7,016

MW de potencia instalada, configurándose como un Pequeño Medio de Generación

(PMGD) emplazado en la Comuna de Tucapel, Región de Bío Bío.

La generación de energía eléctrica se realiza mediante paneles solares con 28.056 unidades

de celdas fotovoltaicas. El Parque consta de 6 subestaciones inversoras y 2 subestaciones

transformadoras. Contará con una línea eléctrica aérea de 23 kV, para realizar

4

posteriormente la inyección de la energía generada a la red de distribución en la postación:

160547

En la Figura 1 se muestra la ubicación del Parque Fotovoltaico Trupán y la línea eléctrica de

23 kV.

Fuente: Elaboración propia.

**Figura 1 Parque Fotovoltaico Trupán y Línea de evacuación**

La línea usará una postación de 11,5m de altura, similar a la mostrada en la Figura siguiente,
con conductor Alliance AAAC para 23KV - 6MWac; 125mm [2] de sección; 14,31 mm de

diámetro total.

5

Fuente: Imagen referencial.

**Figura 2 Esquema de estructura tipo de la línea de Media Tensión**

**4** **Campo magnético de Subestaciones Transformadoras**

El Parque consta de dos subestaciones de transformación, que al considerarlas

similares, tendrán una capacidad de 3,5MVA. La densidad de flujo B está muy relacionada

con la potencia aparente nominal de un transformador. En base a una serie de experiencias

y resultados obtenidos en una amplia gama de potencias, en la referencia [4] se sugiere

una relación simple para el valor efectivo de la inducción magnética en la vecindad de un

transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla]

P N : Potencia Nominal del transformador [kVA]

r: Distancia desde el centro del transformador [m]

k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA]

Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

6

Esta expresión indica que la densidad de flujo magnético de transformadores

decrece rápidamente al alejarse del transformador (relación inversa con la tercera potencia

de la distancia). De acuerdo a esta expresión, con un transformador de 3.500 KVA para cada

Centro de Transformación, la densidad de flujo magnético B a una distancia D desde el

centro del transformador es la siguiente:

**Tabla 1 Variación de la inducción magnética con distancia al transformador**

|Distancia D[m]|2|4|6|8|10|
|---|---|---|---|---|---|
|Inducción magnética B [micro Tesla]|17,5|2,19|0,65|0,27|0,14|

Fuente: Elaboración propia

Se observa que a partir de 6m de cada transformador, la inducción magnética se

reduce a un valor inferior a 1,0 [micro Tesla]. Por lo tanto, el área de influencia para el

campo magnético de un transformador de 3.500 kVA abarca menos de 6m en torno al

transformador.

La referencia [4] también entrega un ábaco que se reproduce en la Figura siguiente,

de valores medidos en transformadores y switchgear de HV y MV.

**Figura 3 Reducción de la densidad de flujo magnético de equipos con la distancia**

Fuente: Referencia [4]

7

Por lo tanto, el campo magnético generado por la Subestación Transformadora,

incluyendo transformador y equipos anexos, a pesar de que puede ser intenso en la

proximidad inmediata de los Centros, decrece rápidamente siendo no relevante a 8 m de

distancia, pues decae a menos de 1 [micro Tesla], no representando impacto hacia el

exterior del Parque.

**5** **ANÁLISIS DEL CAMPO ELECTROMAGNÉTICO DE LA LÍNEA**

En la vecindad de una línea aérea de alta tensión, el campo eléctrico se debe a que

el conductor de alta tensión está directamente expuesto al aire (no existe aislamiento

sólido, el aislamiento está definido por espaciamientos de aire) y sobre dicho conductor

está aplicado alto voltaje respecto de tierra, que actúa como conductor de referencia a

potencial cero. Sus unidades son Volt por metro (V/m) o Kilo Volt por metro (KV/m) en alta

tensión; en el caso en estudio, 23 kV entre fases y 23/√3 KV fase a tierra.

El campo magnético se debe a la corriente que circula por los conductores y no

depende del nivel de voltaje de la línea pero sí del consumo. Para este estudio se consideró

una corriente nominal a transmitir por la línea de 180 Amperes por fase. La magnitud

representativa del campo magnético es la “inducción Magnética” o “densidad de flujo
Magnético” B **,** que tiene como unidad de medida práctica el mili Gauss (1 mG = 10 [-3] Gauss)

o el micro Tesla (1T = 10 [-6] Tesla ) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra

caracterizar al campo eléctrico y el campo magnético cerca de una instalación de alta

tensión por el concepto “Campo a nivel del suelo”, que corresponde al campo eléctrico o

magnético medido o calculado a 1 metro de altura sobre el suelo, en ausencia de otros

objetos.

A continuación se presenta el resultado del estudio mediante el programa de

elementos finitos para la línea, exponiendo los resultados mediante perfiles de campo

transversales a la línea.

La línea transversal en las Figuras 5 y 7 representa el plano de tierra; el símbolo ⇩

en los gráficos señala la ubicación de la línea. Las líneas rojas representan los bordes de la

franja de seguridad, que para este caso se estimó en 10m hacia cada lado del eje, con 20m

totales.

8

**Figura 4 Distribución de líneas equipotenciales eléctricas**

Fuente: Elaboración propia

9

**Figura 5 Campo eléctrico a 1m sobre el suelo, bajo la línea**

Fuente: Elaboración propia

10

**Figura 6 Distribución de líneas equipotenciales magnéticas**

Fuente: Elaboración propia

11

**Figura 7 Inducción magnética a 1m sobre el suelo, bajo la línea**

Fuente: Elaboración propia

12

**Figura 8 Radio interferencia de línea de 66 kV; distancia desde el eje**

Fuente: Elaboración propia

La línea verde indica el valor a la distancia de norma, -5,50 [dB/uV/m].

_**6**_ **NORMATIVA DE REFERENCIA PARA RADIO INTERFERENCIA**

La referencia 2 indica el nivel de perturbación radio eléctrica aceptable generada

por líneas de transmisión o subestaciones, a una frecuencia de 0,5 MHz, y a 15 m de

distancia lateral de la fase externa, tabla que se reproduce a continuación:

**Tabla 2 Nivel de perturbación radiofónica aceptable a 0,5 MHz**

|Tensión eléctrica<br>nominal entre fases (kV)|Radio interferencia<br>[dB /1 μV/m]|
|---|---|
|Bajo 70|43|
|70 - 200|49|
|200 - 300|53|
|300 - 400|56|
|400 - 600|60|
|Sobre 600|63|
|Para una línea, valores a 15 m de distancia lateral de la fase externa<br>Para una subestación, valores a 15 m del borde|Para una línea, valores a 15 m de distancia lateral de la fase externa<br>Para una subestación, valores a 15 m del borde|

Fuente: Elaboración propia.

Para una instalación de 66 kV, el límite correspondiente es 43 [dB/ (1V/m)] .

13

_**7**_ **NORMAS DE REFERENCIA PARA CAMPOS ELECTROMAGNÉTICOS DE 50 HZ**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de

exposición de las personas a los campos electromagnéticos de frecuencia industrial. No

obstante, la regulación ambiental que rige el tema de emisiones señala que de no existir

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

_Japón, Reino de Suecia y Confederación Suiza. Para la utilización de las normas de referencia,_

_se priorizará aquel Estado que posea similitud en sus componentes ambientales, con la_

_situación nacional y/o local, lo que será justificado razonablemente por el proponente._

La recomendación de uso más frecuente es la publicada por la ICNIRP (Comisión

Internacional de Protección de Radiación no Ionizante) [2], que establece para público

general y exposición permanente **5.000 [V/m]** para el campo eléctrico y **200 [micro Tesla]**

para la inducción magnética. Este organismo no gubernamental ha sido reconocido por la

Organización Mundial de la Salud (OMS) como referente respecto de este tema y sus

recomendaciones han sido recogidas por la normativa de varios países de la nómina

anterior.

14

**8** **Conclusiones**

Del análisis efectuado se obtuvo los siguientes valores característicos:

**Tabla 3 Valores finales para Planta fotovoltaica San Bernardo Trupán**

|Col1|Campo eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Radio<br>Interferencia<br>[dB/uV/m]|
|---|---|---|---|
|Transformador<br>3,5MVA|-|<1|A 6m del equipo|
|Inversor-<br>transformador|-|<1|A 8m del equipo|
|Valor máximo|270|0,33|2,94|
|Valor en borde franja|155|0,117|-5,50|
|Valor límite|5.000|200|43|
|Cumplimiento|SI|SI|SI|

De acuerdo a lo mostrado en la Tabla anterior, se concluye que las instalaciones del

Parque Fotovoltaico Trupán, satisfacen la normativa vigente respecto de la componente

campos electromagnéticos de baja frecuencia y de radio interferencia.

15

**9** **Referencias**

[1] Students' QuickField (TM) Finite Element Analysis System

Version 5.8 User's Guide

Copyright (C) Tera Analysis Company, 2010.

2 International Commission on Non‐Ionizing Radiation Protection

ICNIRP Publication - 2010

ICNIRP Guidelines for limiting exposure to time‐varying electric and magnetic fields

(1 hz - 100 kHz)

Published in: Health Physics 99(6):818‐836; 2010

[3] Association canadienne de normalisation, Valeurs limites et methods de mesure du

bruit électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant

alternatif. CAN3- C108.3.1 - M84. Octobre 1984.

[4] Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power

Substations Gerhard Bräunlich, Reinhold Bräunlich. ETH Zürich, Switzerland; FKH

Fachkommission für Hochspannungsfragen. Proceedings, 20th Int. Zurich

Symposium on EMC, Zurich 2009

16

**Anexo Cálculo de radio interferencia generada por la línea**

A continuación se entrega el listado de salida del programa LINEAS, de elaboración

propia, que modela la distribución espacial de conductores de una línea y entrega el campo

eléctrico superficial en cada conductor y la magnitud de radio interferencia.

Nota: El programa usa punto decimal en vez de coma y no utiliza tildes

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 3_

_Numero de conductores activos : 3_

_Numero de cables de guardia : 0_

|Fase|1|2|3|
|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_0.7155_|_0.7155_|_0.7155_|
|_Ubicacion lateral del conductor (m)_|_-1.32_|_0.00_|_1.32_|
|_ Altura conductor sobre el suelo (m)_|_11.50_|_11.50_|_11.50_|

_Matriz de coeficientes (amplif. por (2 πƐ_ _0_ _))_

_8.0754 2.8595 2.1713_

_2.8595 8.0754 2.8595_

_2.1713 2.8595 8.0754_

_Matriz de capacitancias (amplif. por 1/(2 πƐ_ _0_ _))_

_.1455 -.0431 -.0239_

_-.0431 .1543 -.0431_

_-.0239 -.0431 .1455_

_Potenciales de conductores ( KVolts)_

_( 13.2790, 0.0000 ) 13.2790_
_( -6.6395, -11.5000 ) 13.2790_
_( -6.6395, 11.5000 ) 13.2790_

_Cargas en conductores (Cb)/( 2 πƐ_ _0_ _)_

_( 2.3766, 0.2208 ) 2.3868_
_( -1.3107, -2.2701 ) 2.6213_
_( -0.9971, 2.1686 ) 2.3868_

17

_Gradientes superficiales (kVef./cm)_

_( 3.3215, 0.3086 ) 3.3358_
_( -1.8318, -3.1728 ) 3.6636_
_( -1.3935, 3.0308 ) 3.3358 ._

_Radio interferencia_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|-8,92|-6,89|-7,0162||-5,50|

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Variación de la inducción magnética con distancia al transformador****

| Distancia D[m] | 2 | 4 | 6 | 8 | 10 |
| --- | --- | --- | --- | --- | --- |
| Inducción magnética B [micro Tesla] | 17,5 | 2,19 | 0,65 | 0,27 | 0,14 |

**Tabla 2: Nivel de perturbación radiofónica aceptable a 0,5 MHz****

| Tensión eléctrica<br>nominal entre fases (kV) | Radio interferencia<br>[dB /1 μV/m] |
| --- | --- |
| Bajo 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 300 - 400 | 56 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |
| Para una línea, valores a 15 m de distancia lateral de la fase externa<br>Para una subestación, valores a 15 m del borde | Para una línea, valores a 15 m de distancia lateral de la fase externa<br>Para una subestación, valores a 15 m del borde |

**Tabla 3: Valores finales para Planta fotovoltaica San Bernardo Trupán****

| Col1 | Campo eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Radio<br>Interferencia<br>[dB/uV/m] |
| --- | --- | --- | --- |
| Transformador<br>3,5MVA | - | <1 | A 6m del equipo |
| Inversor-<br>transformador | - | <1 | A 8m del equipo |
| Valor máximo | 270 | 0,33 | 2,94 |
| Valor en borde franja | 155 | 0,117 | -5,50 |
| Valor límite | 5.000 | 200 | 43 |
| Cumplimiento | SI | SI | SI |
