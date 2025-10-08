---
title: Anexo 7 Estudio de campos electromagnéticos
author: María Paz Lagos Avid
date: D:20201217151742-03'00'
language: es
type: report
pages: 29
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Farol Solar SpA Anexo 7 Estudio de campos electromagnéticos
-->

# Farol Solar SpA Anexo 7 Estudio de campos electromagnéticos

## Declaración de Impacto Ambiental “Parque Fotovoltaico Farol”

### Región de Antofagasta

Rev.0 - Diciembre, 2020

Elaborado para:

**Gestión Ambiental Consultores S.A.**

General del Canto 421 Piso 6, Providencia

Santiago, Chile - Fono: +56 2 2719 5600

www.gac.cl

#### ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PARQUE FOTOVOLTAICO FAROL

##### Nelson Morales Osorio Diciembre 2020

2

**CONTENIDO**

1 Objetivo y alcance del estudio .................................................................................................... 3

2 Características del proyecto ........................................................................................................ 3

2.1 Centros de Transformación ................................................................................................. 4

2.2 Punto de Evacuación ........................................................................................................... 5

2.3 Línea de interconexión de Media Tensión .......................................................................... 5

3 Normativa de referencia para Radio interferencia ..................................................................... 6

_4_ Normas de referencia para campos electromagnéticos de 50 Hz .............................................. 7

5 Campo magnético de centros de transformación....................................................................... 7

6 Modelamiento de Línea de transmisión de 23 kV ...................................................................... 9

7 radio interferencia por fenómeno corona ................................................................................ 13

8 Zona de Influencia ..................................................................................................................... 13

9 Conclusiones.............................................................................................................................. 14

10 Referencias ............................................................................................................................ 15

ANEXO 1 ............................................................................................................................................ 16

Estudio de radio interferencia para la línea ...................................................................................... 16

**LISTADO DE FIGURAS**

Figura 1 Parque Fotovoltaico Farol .................................................................................................... 4

Figura 2 Parque Fotovoltaico Farol y línea de interconexión ............................................................. 5

Figura 3 Esquema de estructura tipo de la línea de Media Tensión .................................................. 6

Figura 4 Reducción de la densidad de flujo magnético de equipos con la distancia ........................ 9

Figura 5 Malla de elementos finitos ................................................................................................ 10

Figura 6 Distribución de líneas equipotenciales eléctricas .............................................................. 11

Figura 7 Campo eléctrico a 1m sobre el suelo bajo torre ................................................................ 11

Figura 8 Distribución de líneas equipotenciales magnéticas ........................................................... 12

Figura 9 Inducción magnética 1m sobre el suelo bajo torre ............................................................. 12

**LISTADO DE TABLAS**

Tabla 1 Nivel de perturbación radiofónica aceptable a 0,5 MHz ....................................................... 6

Tabla 2 Variación de la inducción magnética con distancia al transformador................................... 8

Tabla 3 Valores de campo en el borde de la franja y confrontación con norma ............................. 13

3

**1** **OBJETIVO Y ALCANCE DEL ESTUDIO**

El propósito de este estudio es estimar la magnitud de los campos

electromagnéticos de baja y alta frecuencia provocados por la operación del Parque

Fotovoltaico Farol y su línea de evacuación en 23 kV.

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

El Proyecto se ubica en el sector rural de la Comuna de Mejillones, Provincia de

Antofagasta, Región de Antofagasta, aproximadamente a 52 km al norte de la ciudad de

Antofagasta y a 9 km al oriente de Mejillones. Corresponde a un proyecto de pequeños

medios de generación distribuida (PMGD) a través de energías renovables no

convencionales (ERNC), que generará energía limpia a través de la construcción de una

central de generación de energía eléctrica.

La Planta Fotovoltaica, está conformada por Bloques o conjuntos de paneles

solares los que suman un total de 9 MW AC. Cada Bloque cuenta con un Centro de

Transformación, siendo en total 6 Centros de transformación que recibe la corriente

generada por los paneles solares para adecuarla y enviarla mediante cableado soterrado

4

hasta el Centro de Seccionamiento, donde converge la energía de bloques, para ser

enviada mediante una línea aérea de media tensión (23 KV), hasta el punto de

interconexión, donde se entregará la energía al Sistema Eléctrico Nacional (SEN).

**Figura 1 Parque Fotovoltaico Farol**

Fuente: Esquema entregado por Titular del Proyecto

**2.1** **Estación Inversora Transformadora (EIT)**

Cada Estación Inversora Transformadora (EIT) consiste en la integración inversor +

transformador, la cual toma la corriente eléctrica para adecuarla y enviarla mediante

cableado soterrado hasta el centro de seccionamiento al interior del parque, para ser

enviada mediante una línea aérea de media tensión (23 KVA), hasta el punto de

interconexión al SEN.

Los inversores son equipos diseñados para trasformar la corriente continua

procedente del campo de paneles en corriente alterna compatible con la forma de

5

corriente de la red. Los transformadores son equipos diseñados para transformar el nivel

de tensión de la electricidad proveniente de los inversores desde un nivel a otro, para

luego ser inyectada a la red.

**2.2** **Punto de Evacuación o Centro de seccionamiento**

Consiste en un contenedor que incorpora todos los equipos eléctricos necesarios

para recibir la energía desde los Estación Inversora Transformadora (EIT) y que se evacuan

a través de la línea de interconexión que inicia en este lugar. El Proyecto no contará con

una subestación eléctrica, sino que se conectará directamente a la red de distribución

perteneciente al SEN.

**2.3** **Línea de interconexión de Media Tensión**

La evacuación de la energía eléctrica producida en el parque fotovoltaico se

realizará mediante un tendido eléctrico aéreo de 23 kV de tensión nominal, que conectará

el punto de evacuación de la planta con el punto de conexión a la red de distribución

distante aproximadamente 8,1 km. Las estructuras de soporte de los conductores serán

postes simples de hormigón armado o postes metálicos ensamblados (tejidos) según

corresponda. En la se muestra un esquema de una estructura tipo a utilizar en la línea

eléctrica.

**Figura 2 Parque Fotovoltaico Farol y línea de interconexión**

Fuente: Esquema entregado por Titular del Proyecto.

6

**Figura 3 Esquema de estructura tipo de la línea de Media Tensión**

Fuente: Esquema entregado por Titular del Proyecto.

La faja de la línea de evacuación tendrá un ancho total de 7m.

**3** **NORMATIVA DE REFERENCIA PARA RADIO INTERFERENCIA**

La referencia 3 indica el nivel de perturbación radio eléctrica aceptable generada

por líneas de transmisión o subestaciones, a una frecuencia de 0,5 MHz, Tabla siguiente:

**Tabla 1 Nivel de perturbación radiofónica aceptable a 0,5 MHz**

|Tensión eléctrica<br>nominal entre fases (kV)|Radio interferencia<br>[dB /1 μV/m]|
|---|---|
|Bajo 70|43|
|70 - 200|49|
|200 - 300|53|
|300 - 400|56|
|400 - 600|60|

7

Sobre 600 63

Fuente: Referencia [3]

Para una línea, los valores están definidos a 15 m de distancia lateral de la fase

externa. Para una subestación, los valores están definidos a 15 m del borde. Para una

instalación de 23 kV, el límite correspondiente es 43 [dB/ (1V/m)].

_**4**_ **NORMAS DE REFERENCIA PARA CAMPOS ELECTROMAGNÉTICOS DE 50 HZ**

En nuestro país no existe reglamentación relativa a los valores límites permitidos

de exposición de las personas a los campos electromagnéticos de frecuencia industrial. No

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

_Japón, Reino de Suecia y Confederación Suiza. Para la utilización de las normas de_

_referencia, se priorizará aquel Estado que posea similitud en sus componentes_

_ambientales, con la situación nacional y/o local, lo que será justificado razonablemente_

_por el proponente._

La recomendación de uso más frecuente para público general y exposición

permanente, es la publicada por la ICNIRP [4], organismo no gubernamental reconocido

por la Organización Mundial de la Salud como referente en el tema, que establece 5.000

[V/m] para el campo eléctrico y 200 [micro Tesla], equivalente a 2.000 [mili Gauss] para la

inducción magnética, valores que han sido acogidos por la normativa de diversos países

incluidos en la nómina anterior.

**5** **CAMPO MAGNÉTICO DE CENTROS DE TRANSFORMACIÓN**

8

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
|Inducción magnética B[micro<br>|12,5|1,56|0,46|0,20|0,10|
|~~Tesla]~~<br>Inducción magnética B[mili Gauss]|125|15,6|4,6|2,0|1,0|

Fuente: Elaboración propia

Se observa que a partir de 5m del transformador, la inducción magnética se reduce

a un valor inferior a 1,0 [micro Tesla] o equivalentemente, 10 [mili Gauss]. Por lo tanto, el

área de influencia para el campo magnético de cada transformador de 2.500 kVA abarca

aproximadamente 5m en torno al transformador.

La referencia [5] también entrega un ábaco que se reproduce en la Figura

siguiente, correspondiente a valores medidos en transformadores y switchgear de HV y

MV.

9

**Figura 4 Reducción de la densidad de flujo magnético de equipos con la distancia**

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

son Volt por metro [V/m] o Kilovolt por metro [kV/m] en alta tensión; en el caso en

estudio, 23 kV entre fases y 23/√3 KV fase a tierra.

10

El campo magnético se debe a la corriente que circula por los conductores y no

depende del nivel de voltaje de la línea, pero sí del consumo. Para este estudio se

consideró una potencia nominal a transmitir por la línea de 12,5 MVA, lo que en 23 kV

define 314 Amperes como corriente nominal por fase. La magnitud representativa del

campo magnético es la “inducción Magnética” o “densidad de flujo Magnético” B **,** que
tiene como unidad de medida práctica el mili Gauss (1 mG = 10 [-3] Gauss) o el micro Tesla

(1T = 10 [-6] Tesla ) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra

caracterizar al campo eléctrico y el campo magnético cerca de una instalación de alta

tensión por el concepto “Campo a nivel del suelo”, que corresponde al campo eléctrico o

magnético medido o calculado a 1 metro de altura sobre el suelo, en ausencia de otros

objetos.

El análisis mediante elementos finitos para el concepto campo a nivel del suelo, se

presenta a continuación para la estructura mostrada en la Figura 2.

**Figura 5 Malla de elementos finitos**

Fuente: Elaboración propia

11

**Figura 6 Distribución de líneas equipotenciales eléctricas**

Fuente: Elaboración propia

**Figura 7 Campo eléctrico a 1m sobre el suelo bajo torre**

Fuente: Elaboración propia

12

**Figura 8 Distribución de líneas equipotenciales magnéticas**

Fuente: Elaboración propia

**Figura 9 Inducción magnética 1m sobre el suelo bajo torre**

Fuente: Elaboración propia

13

En la Tabla siguiente se presenta los valores obtenidos a 1m de altura sobre el

suelo en el borde de la franja de seguridad, considerada con un ancho total de 7m y la

confrontación con los límites señalados por la ICNIRP [4].

**Tabla 3 Valores de campo en el borde de la franja y confrontación con norma**

|Col1|Campo<br>eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Inducción<br>magnética<br>[mili Gauss]|
|---|---|---|---|
|Estructura|248|1,16|11,6|
|Límite<br>ICNIRP|5.000|200|2.000|
|Cumple|SI|SI|SI|

Fuente: Elaboración propia

**7** **RADIO INTERFERENCIA POR FENÓMENO CORONA**

La descarga corona en líneas de alta tensión corresponde a descargas eléctricas

parciales en el aire alrededor de los conductores, generadas por alto campo eléctrico, que

provoca ionización del aire. Este fenómeno emite campos electromagnéticos desde

frecuencias de audio hasta alta frecuencia que pueden provocar perturbaciones en la

banda de frecuencia de radio y televisión.

Mediante la aplicación del software LINEAS, de elaboración propia, se determina el campo

eléctrico en la superficie de los conductores y la radio interferencia emitida por la

estructura de la línea de 23 kV. El programa ocupa el Método de Simulación de Cargas [2]

para determinar el campo eléctrico superficial y el procedimiento CIGRE para evaluar nivel

de interferencia [2]. En el ANEXO se presenta el listado de salida del programa, para la

estructura analizada. La magnitud de radio interferencia calculada para la estructura

analizada, a 0,5 MHz y a 15m de distancia lateral desde el conductor externo, resulta

negativa y confrontada con el valor límite establecido por la norma, este valor es superior.

**8** **ZONA DE INFLUENCIA**

De los resultados indicados, se desprende que la zona de influencia de la

componente campos electromagnéticos para la línea de transmisión de 23 kV, puede

14

definirse en 7 m totales, 3,5 m hacia cada lado del eje de la línea. Con respecto al Parque,

se estima solamente en el área comprometida por el Parque, en todo su perímetro.

**9** **CONCLUSIONES**

De acuerdo a los resultados obtenidos en la investigación bibliográfica y en la

modelación de campos electromagnéticos, se concluye que:

 - La magnitud máxima de campo eléctrico existente a un metro de altura sobre el

suelo en torno a la línea operando en 23 kV es 258 [Volt/m] y en el borde del Área

de Influencia es 248 [V/m]; estos valores son muy inferiores al límite de 5.000

[V/m] considerado internacionalmente como seguro para personas.

 - La magnitud máxima de inducción magnética existente a un metro de altura sobre

el suelo en torno a la línea operando en 23 kV es 1,20 [micro Tesla] (equivalente a
12 [mili Gauss] y en el borde del Área de Influencia es 1,16 [micro Tesla]

(equivalente a 11,6 [mili Gauss], inferior al límite de 200 [micro Tesla] o 2.000 [mili

Gauss], considerado internacionalmente como seguro.

 - La radio interferencia generada por la línea no alcanza a un valor positivo a la

distancia de norma (15m desde el conductor externo), por lo tanto cumple esta

norma.

Por lo tanto, las instalaciones del Proyecto Parque Fotovoltaico Farol satisfacen los

valores establecidos por la normativa vigente, respecto de campos electromagnéticos de

baja y alta frecuencia.

15

**10** **REFERENCIAS**

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

[5] Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power

Substations

Gerhard Bräunlich, Reinhold Bräunlich

ETH Zürich, Switzerland

FKH Fachkommission für Hochspannungsfragen

Proceedings, 20th Int. Zurich Symposium on EMC, Zurich 2009

16

**ANEXO 1**

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
|Numero de subconductores|1|1|1|
|Radio del subconductor (cm)|0.9150|0.9150|0.9150|
|Ubicacion lateral del conductor (m)|-1.200|0.600|1.2000|
|Altura conductor sobre el suelo (m)|10.00|10.00|10.00|

##### Matriz de coeficientes (amplif. por (2 ¶ ε 0 ))

7.6897 2.4120 2.1274

2.4120 7.6897 3.5070

2.1274 3.5070 7.6897

##### Matriz de capacitancias (amplif. por 1/(2 ¶ ε 0 ))

.1479 -.0350 -.0250

-.0350 .1725 -.0690

-.0250 -.0690 .1684

17

Potenciales de conductores ( KVolts)

( 13.2790, 0.0000 ) 13.2790

( -6.6395, -11.5000 ) 13.2790

( -6.6395, 11.5000 ) 13.2790

##### Cargas en conductores (Cb)/(2 ¶ ε 0 )

( 2.3626, 0.1157 ) 2.3654

( -1.1523, -2.7768 ) 3.0064

( -0.9915, 2.7299 ) 2.9044

Gradientes superficiales (kVef./cm)

( 2.5821, 0.1265 ) 2.5852

( -1.2593, -3.0347 ) 3.2857

( -1.0836, 2.9835 ) 3.1742

#### INFORME LINEA DE BASE CAMPO ELECTROMAGNÉTICO PARQUE FOTOVOLTAICO FAROL

**Nelson Morales Osorio**

**Diciembre 2020**

2

**CONTENIDO**

1. Objetivo ....................................................................................................................................... 3

2. Descripción .................................................................................................................................. 3

3. Metodología ................................................................................................................................ 4

4. Resultados ................................................................................................................................... 4

4.1 Punto 1 ...................................................................................................................................... 4

4.2 Punto 2 ..................................................................................................................................... 6

4.3 Punto 3 ...................................................................................................................................... 7

5.- Conclusiones .................................................................................................................................. 8

Referencias ...................................................................................................................................... 9

ANEXO ............................................................................................................................................... 10

Instrumento y Procedimiento de medida ......................................................................................... 10

A.1 Medida de campo eléctrico .................................................................................................... 10

A.2 Medida de campo magnético ................................................................................................. 11

**LISTADO DE FIGURAS**

Figura 1 Ubicación Parque Fotovoltaico Farol ................................................................................... 3

Figura 2 Trayectoria y sentido de medida ........................................................................................... 5

Figura 3 Campo eléctrico a 1m sobre el suelo en trayectoria de medida ........................................... 5

Figura 4 Inducción magnética a 1m sobre el suelo en trayectoria de medida .................................. 6

Figura 2 Sector de ubicación de Parque Fotovoltaico Farol ................................................................ 6

Figura 3 Trayectoria en punto de conexión ....................................................................................... 7

Figura 4 Campo eléctrico a 1m sobre el suelo ................................................................................... 7

Figura 5 Inducción magnética a 1m sobre el suelo ............................................................................. 8

**LISTADO DE TABLAS**

Tabla 1 Coordenadas punto de medida ............................................................................................. 4

Tabla 2 Máximos valores medidos ...................................................................................................... 8

3

**1.** **Objetivo**

El propósito de este documento es entregar los resultados de la medición de

campo eléctrico y campo magnético de frecuencia industrial, generado por fuentes

existentes en el lugar de instalación del Parque Fotovoltaico Farol, con el propósito de

caracterizar la Línea de Base de la componente Campos Electromagnéticos del Proyecto.

**2.** **Descripción**

El Parque Fotovoltaico Farol se ubica en la Comuna de Mejillones, Provincia de

Antofagasta, Región de Antofagasta, a aproximadamente a 52 km al norte de la ciudad de

Antofagasta y al costado oriente de la ruta sur de ingreso a Mejillones.

**Figura 1 Ubicación Parque Fotovoltaico Farol**

4

Como se observa en la Figura, saliendo del Parque, su línea de evacuación

atraviesa seis líneas de transmisión, que son de poniente a oriente, de acuerdo con la

información aportada por el Coordinador Eléctrico:

- Línea de 1x220kV Atacama Esmeralda, 197,4 MVA

- Línea 1x110kV Mejillones - Antofagasta, 91,45 MVA

- Línea 1x220kV Mejillones O ́Higgins, 260,6 MVA

- Línea 1x220kV Chacaya - Mantos Blancos, 304 MVA

- Línea 2x220kV Atacama - O ́Higgins, 245,4 MVA

- Línea 2x220kV Chacaya - El Cobre, 350 MVA

**3.** **Metodología**

Se realizó mediciones de acuerdo a la norma IEEE Standard 644-1994 "IEEE

Standard Procedure for Measurements of Power Frequency Electric and Magnetic Fields

from AC Power Lines". El procedimiento establecido por la norma indica que los campos

deben medirse a 1 metro de altura sobre el nivel del suelo. Los puntos considerados para

caracterizar la Línea de Base son los de coordenadas:

**Tabla 1 Coordenadas punto de medida**

|Col1|Ubicación|Coordenadas|Col4|
|---|---|---|---|
|Punto 1|Camino a relleno sanitario|19 K 353785 m E|7441763 m S|
|Punto 2|Parque Fotovoltaico|19K 353248 m E|7440200 m S|
|Punto 3|Punto de conexión|19K 352142 m E|7443547 m S|

El equipo utilizado para las medidas es el medidor EFM 130 Electric Field Meter y

EFM131 Magnetic Field Meter. Las medidas se efectuaron el 20 de enero del 2020. El

detalle del procedimiento e instrumento de medida se incluye en Anexo **.**

**4.** **Resultados**

**4.1 Punto 1**

5

La fotografía siguiente muestra la trayectoria seguida para cubrir todas las líneas,

en dirección de poniente a oriente.

**Figura 2 Trayectoria y sentido de medida**

Y los resultados se presentan en los gráficos siguientes. El símbolo ⇩ indica la

posición de una línea.

**Figura 3 Campo eléctrico a 1m sobre el suelo en trayectoria de medida**

6

**Figura 4 Inducción magnética a 1m sobre el suelo en trayectoria de medida**

**Comentario:** Ambos gráficos, de campo eléctrico y magnético, evidencian el efecto de las

líneas presentes, con incremento de valores. Los máximos valores encontrados en esta

trayectoria son:

Campo eléctrico: 2.350 [V/m]

Inducción magnética: 29,31 [mili Gauss]

**4.2 Punto 2**

En el sector de instalación del Parque Fotovoltaico Farol no existe fuente de campo

electromagnético cercana. Una vista hacia dicho sector se muestra en la imagen siguiente:

**Figura 5 Sector de ubicación de Parque Fotovoltaico Farol**

7

Los valores medidos de campo eléctrico y campo magnético resultan nulos:

Campo eléctrico: 0,0 [V/m]

Inducción magnética: 0,0 [mili Gauss]

**4.3 Punto 3**

El tercer Punto de medida corresponde al punto de conexión de la línea de

evacuación.

**Figura 6 Trayectoria en punto de conexión**

**Figura 7 Campo eléctrico a 1m sobre el suelo**

8

**Figura 8 Inducción magnética a 1m sobre el suelo**

**Comentario:**

En los gráficos de campo aparece bien marcada la presencia de la línea; los

máximos valores encontrados en esta trayectoria son:

Campo eléctrico: 75,5 [V/m]

Inducción magnética: 1,03[mili Gauss]

**5.- Conclusiones**

Se ha logrado identificar mediante medidas directas en terreno, valores

característicos del campo eléctrico y del campo magnético de fuentes existentes, para

definir la Línea de Base de la componente campos electromagnéticos para el Proyecto

Parque Fotovoltaico Farol.

Los máximos valores medidos se indican en la Tabla a continuación:

**Tabla 2 Máximos valores medidos**

|Col1|Col2|Ubicación|
|---|---|---|
|Campo eléctrico<br>[V/m]|2.350|Bajo Línea 1x220kV Chacaya - Mantos Blancos|
|Inducción magnética<br>[mili Gauss]|29,31|Bajo Línea 1x110kV Mejillones - Antofagasta|

9

Ninguno de los valores medidos supera los máximos tolerables para las personas,

definidos por la ICNIRP [2], que corresponden a 5.000 [Volts/m] para el campo eléctrico y

2.000 [mili Gauss] para el campo magnético. La ICNIRP es un organismo experto de

consulta en temas de radiaciones no ionizantes reconocida por la Organización Mundial

de la Salud, OMS, la Organización Internacional del Trabajo (International Labour

Organization - ILO) y la Unión Europea.

En consecuencia, el campo electromagnético no supera los máximos tolerables

para las personas, definidos por la ICNIRP [2], que corresponden a 5.000 [Volts/m] para el

campo eléctrico y 2.000 [mili Gauss] para el campo magnético. La ICNIRP es un organismo

experto de consulta en temas de radiaciones no ionizantes reconocida por la Organización

Mundial de la Salud, OMS, la Organización Internacional del Trabajo (International Labour

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

**ANEXO**

**Instrumento y Procedimiento de medida**

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

11

El medidor utilizado es el EFM 131 de EFM Company, Stockbridge. La sonda o

sensor de campo eléctrico, definido como “de cuerpo libre”, consiste en un dipolo en

forma de cajas rectangulares, con dimensiones de 7 por 20 centímetros. El detector es un

voltímetro digital. La sonda y el detector son introducidos en el campo eléctrico con un

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

**Tabla 1: Coordenadas punto de medida****

| Col1 | Ubicación | Coordenadas | Col4 |
| --- | --- | --- | --- |
| Punto 1 | Camino a relleno sanitario | 19 K 353785 m E | 7441763 m S |
| Punto 2 | Parque Fotovoltaico | 19K 353248 m E | 7440200 m S |
| Punto 3 | Punto de conexión | 19K 352142 m E | 7443547 m S |

**Tabla 2: Máximos valores medidos****

| Col1 | Col2 | Ubicación |
| --- | --- | --- |
| Campo eléctrico<br>[V/m] | 2.350 | Bajo Línea 1x220kV Chacaya - Mantos Blancos |
| Inducción magnética<br>[mili Gauss] | 29,31 | Bajo Línea 1x110kV Mejillones - Antofagasta |

**Tabla 3: Valores de campo en el borde de la franja y confrontación con norma****

| Col1 | Campo<br>eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Inducción<br>magnética<br>[mili Gauss] |
| --- | --- | --- | --- |
| Estructura | 248 | 1,16 | 11,6 |
| Límite<br>ICNIRP | 5.000 | 200 | 2.000 |
| Cumple | SI | SI | SI |
