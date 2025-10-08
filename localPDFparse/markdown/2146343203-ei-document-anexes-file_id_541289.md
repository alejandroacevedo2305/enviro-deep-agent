---
title: Tipo de Informe o Capítulo
author: admin@gac.cl
date: D:20200416112152-04'00'
language: es
type: report
pages: 32
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 13 Estudio de Campos Electromagnéticos
-->

## PV Power Chile Spa

# Anexo 13 Estudio de Campos Electromagnéticos

### Declaración de Impacto Ambiental “Parque Fotovoltaico Chinchorro”

#### Región de Arica y Parinacota

Abril, 2020

Elaborado por Nelson Morales Osorio

Para:

**Gestión Ambiental Consultores S.A.**

General del Canto 421, Piso 6, Providencia

Fono: +56 2 2719 5600

www.gac.cl

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**INDICE GENERAL**

**1** **OBJETIVO Y ALCANCE DEL ESTUDIO ........................................................................................ 1**

**2** **CARACTERÍSTICAS DEL PROYECTO .......................................................................................... 1**

2.1 Línea de evacuación de energía de Media Tensión ......................................................................... 4

**3** **Metodología para Estudio con modelaciones .......................................................................... 5**

**4** **Campo magnético de Centros de transformación .................................................................... 6**

**5** **Modelamiento de Línea de transmisión de 13,2 kV ................................................................. 8**

**6** **Radio interferencia por fenómeno corona ............................................................................ 11**

**7** **Cruce con línea DE MT existente ........................................................................................... 12**

**8** **Estudio de paralelismo de líneas de 13,2kV........................................................................... 15**

**9** **Conclusiones ........................................................................................................................ 18**

**10** **Referencias .......................................................................................................................... 19**

**APÉNDICE 1 RESULTADOS DE LINEA DE BASE**

**Apéndice 2 ESTUDIO DE RADIO INTERFERENCIA PARA LA LÍNEA**

**INDICE DE TABLAS**

Tabla 2-1. Características técnicas transformador referencial ..................................................................... 3

Tabla 4-1. Variación de la inducción magnética con distancia al transformador ......................................... 6

Tabla 5-1. Valores de campo en el borde de la franja y confrontación con norma .................................... 11

Tabla 6-1. Magnitud de radio interferencia y confrontación con norma ................................................... 11

Tabla 9-1. Resumen de valores representativos ......................................................................................... 18

**INDICE DE FIGURAS**

Figura 2-1 Planta fotovoltaica Chinchorro y línea de evacuación ................................................................. 2

Figura 2-2. Postes simples de hormigón armado (Figura referencial) .......................................................... 4

Figura 4-1. Reducción de la densidad de flujo magnético de equipos con la distancia ................................ 7

Figura 5-1. Malla de elementos finitos .......................................................................................................... 8

Figura 5-2. Distribución de líneas equipotenciales eléctricas ....................................................................... 9

Figura 5-3. Campo eléctrico a 1m sobre el suelo bajo poste ........................................................................ 9

Figura 5-4. Distribución de líneas equipotenciales magnéticas .................................................................. 10

Figura 5-5. Inducción magnética 1m sobre el suelo bajo poste .................................................................. 10

Figura 6-1. Radio interferencia vs distancia para línea en estructura ......................................................... 12

Figura 7-1. Malla de elementos finitos ........................................................................................................ 13

Figura 7-2. Distribución de equipotenciales eléctricas ............................................................................... 13

Figura 7-3. Campo eléctrico bajo cruce de líneas ....................................................................................... 14

Figura 7-4. Inducción magnética bajo cruce de líneas ................................................................................ 14

Figura 8-1. Paralelismo de líneas de MT ..................................................................................................... 15

i

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

Figura 8-2. Líneas equipotenciales eléctricas .............................................................................................. 16

Figura 8-3. Campo eléctrico a 1m sobre el suelo entre líneas .................................................................... 16

Figura 8-4. Líneas equipotenciales magnéticas ........................................................................................... 17

Figura 8-5. Inducción magnética a 1m sobre el suelo ................................................................................. 17

ii

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

###### 1 OBJETIVO Y ALCANCE DEL ESTUDIO

El propósito de este documento es:

a) Evaluar la magnitud de los campos electromagnéticos de frecuencia industrial generados por

fuentes existentes en el lugar de instalación del Parque fotovoltaico y en el trazado de la línea

de evacuación, con el propósito de caracterizar la Línea de Base de la componente Campos

Electromagnéticos del Proyecto.

b) Estimar la magnitud de los campos electromagnéticos de baja y alta frecuencia provocados por

la operación del Parque Fotovoltaico Chinchorro y de su línea de evacuación en 13,2 kV.

###### 2 CARACTERÍSTICAS DEL PROYECTO

El Proyecto Parque Fotovoltaico Chinchorro tiene por objetivo proporcionar energía eléctrica a

través de energías renovables no convencionales (ERNC), por medio de la construcción y

operación de un parque fotovoltaico para inyectar energía al Sistema Eléctrico Nacional (SEN).

1

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 2-1 Planta fotovoltaica y línea de evacuación**

El Proyecto se emplaza en sector Rural de la comuna de Arica, en la Provincia de Arica de la Región

de Arica y Parinacota, a aproximadamente a 3.400 m del límite urbano de la ciudad de Arica y

corresponde a un proyecto de pequeños medios de generación distribuida (PMGD) a través de

energías renovables no convencionales (ERNC), que generará energía limpia a través de la

construcción de una central de 10,52 MW AC, los que serán inyectados al Sistema Eléctrico

Nacional (SEN) mediante una línea de evacuación de 13,2 kV.

El Proyecto comprende un parque fotovoltaico de 24.192 módulos, diez (10) subestaciones

inversoras, dos (2) subestaciones transformadoras y una línea de evacuación de 13,2 kV que

empalmará al SEN. El Proyecto no contará con una subestación eléctrica, sino que se conectará

directamente a la red de distribución perteneciente al Sistema Interconectado.

2

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Módulos fotovoltaicos**

Existirán 288 estructuras de soporte, cada una compuesta por 84 módulos con celdas

fotovoltaicas, lo que suma un total de 24.192 módulos fotovoltaicos. Cada módulo tendrá una

potencia de 435 Wp, en corriente continua (CC), resultando en una potencia instalada de 10,52

MW AC, inyectando 9,0 MW AC al Sistema Eléctrico Nacional.

**Subestación Inversora**

Existirán diez (10) subestaciones inversoras que recibirán la energía generada por los módulos

fotovoltaicos en corriente directa (DC) y la convertirán en corriente alterna (AC), de modo que se

pueda inyectar al sistema de distribución, SEN.

**Subestación transformadora**

Este equipo corresponde al transformador de potencia, donde se recibirá toda la energía

generada en el parque fotovoltaico y se adecuará al nivel de voltaje requerido para su inyección

a la red de distribución. Serán dos (2) subestaciones transformadoras de 5,5 MVA cada una. Cada

subestación transformadora cuenta con un transformador con las siguientes características

principales:

**Tabla 2-1. Características técnicas transformador referencial**

|Parámetros|Valor|
|---|---|
|Potencia nominal del primario|5.500 kVA|
|Frecuencia|50 Hz|
|Tensión nominal del primario|13,2 kV|

Fuente: Elaboración propia en base a ingeniería

3

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

###### 2.1 Línea de evacuación de energía de Media Tensión

La evacuación de la energía eléctrica producida en el parque fotovoltaico se realizará mediante un tendido

eléctrico aéreo de 13,2 kV de tensión nominales, que conectará el punto de evacuación de la planta con

el punto de conexión a la red de distribución. Este tendido eléctrico tendrá una longitud aproximada de

5.883,9 m. Las estructuras de soporte de los conductores serán postes simples de hormigón armado.

Tendrán una altura de 11,5 m y un ancho de 2,14 m en su parte más ancha, que es donde se sustentan los

conductores ( **Figura 2-2** ).

**Figura 2-2. Postes simples de hormigón armado (Figura referencial)**

4

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

###### 3 METODOLOGÍA PARA ESTUDIO CON MODELACIONES

Se presenta en primer lugar información recogida de la literatura técnica respecto de emisión

provocada por los Centros de Transformación y los resultados de una simulación de la línea de

evacuación de 13,2 kV en operación singular, en paralelismo y en el cruce con otra línea de

13,2kV; la simulación se efectúa con apoyo del software QuickField [1] que utiliza el método de

elementos finitos para obtener campo eléctrico y campo magnético generados en la vecindad de

conductores energizados.

Los valores obtenidos con los equipos y conductores operando en el voltaje indicado, se

confrontan posteriormente con las recomendaciones y límites admisibles para establecer una

conclusión respecto de la emisión electromagnética de baja frecuencia provocada por la

operación de los equipos.

Similarmente se realiza una estimación del nivel perturbador a frecuencias de radio generado por

los conductores de la línea de transmisión debido al fenómeno corona y se compara con valores

límites establecidos por recomendaciones internacionales. El cálculo de nivel de perturbación a

frecuencias de radio se determina aplicando métodos aproximados de conocimiento general [2].

5

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

###### 4 CAMPO MAGNÉTICO DE CENTROS DE TRANSFORMACIÓN

La densidad de flujo B está muy relacionada con la potencia aparente nominal de un

transformador. En base a una serie de experiencias y resultados obtenidos en una amplia gama

de potencias, en la referencia [7] se sugiere una relación simple para el valor efectivo de la

inducción magnética en la vecindad de un transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla]

P N : Potencia Nominal del transformador [kVA].

r: Distancia desde el centro del transformador [m].

k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA].

Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

Esta expresión indica que la densidad de flujo magnético de transformadores decrece

rápidamente al alejarse del transformador (relación inversa con la tercera potencia de la

distancia). De acuerdo a esta expresión, con un transformador de 5,5 MVA del Centro de

Transformación, la densidad de flujo magnético B a una distancia D desde el centro del

transformador es la siguiente:

**Tabla 4-1. Variación de la inducción magnética con distancia al transformador**

|Distancia D[m]|2|4|6|8|10|
|---|---|---|---|---|---|
|Inducción magnética B[micro Tesla]|25,0|3,12|0,92|0,40|0,20|

Fuente: Elaboración propia

Se observa que a partir de 5m del transformador, la inducción magnética se reduce a un valor

inferior a 1,0 [micro Tesla]. Por lo tanto, el área de influencia para el campo magnético de cada

transformador de 5,5 MVA abarca menos de 5m en torno al transformador.

La referencia [6] también entrega un ábaco que se reproduce en la Figura siguiente,

correspondiente a valores medidos en transformadores y switchgear de HV y MV.

6

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 4-1. Reducción de la densidad de flujo magnético de equipos con la distancia**

Fuente: Referencia [6]

Por lo tanto, el campo magnético generado por cada Centro de Transformación, incluyendo

transformador y equipos anexos, a pesar de que puede ser intenso en la proximidad inmediata

de los Centros, decrece rápidamente siendo no relevante a 10 m de distancia, pues decae a menos

de 1 [micro Tesla], no representando impacto hacia el exterior del Parque.

7

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

###### 5 MODELAMIENTO DE LÍNEA DE TRANSMISIÓN DE 13,2 KV

En la vecindad de una línea aérea, el campo eléctrico se debe a que el conductor está

directamente expuesto al aire (no existe aislamiento sólido, el aislamiento está definido por

espaciamientos de aire) y sobre dicho conductor está aplicado alto voltaje respecto de tierra, que

actúa como conductor de referencia a potencial cero.

El campo magnético se debe a la corriente que circula por los conductores y no depende del nivel

de voltaje de la línea, pero sí del consumo. Para este estudio se consideró una potencia nominal

a transmitir por la línea de 9 MVA, lo que en 13,2 kV define 394 Amperes como corriente nominal

por fase.

El análisis mediante elementos finitos para el concepto campo a nivel del suelo, se presenta a

continuación para la estructura mostrada en la Figura 2.

**Figura 5-1. Malla de elementos finitos**

Fuente: Elaboración propia

8

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 5-2. Distribución de líneas equipotenciales eléctricas**

Fuente: Elaboración propia

**Figura 5-3. Campo eléctrico a 1m sobre el suelo bajo poste**

Fuente: Elaboración propia

9

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 5-4. Distribución de líneas equipotenciales magnéticas**

Fuente: Elaboración propia

**Figura 5-5. Inducción magnética 1m sobre el suelo bajo poste**

Fuente: Elaboración propia

10

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

En la Tabla siguiente se presenta los valores obtenidos a 1m de altura sobre el suelo en el borde

de la franja de seguridad, considerada con un ancho total de 20m y la confrontación con los límites

señalados por la ICNIRP [4].

**Tabla 5-1. Valores de campo en el borde de la franja y confrontación con norma**

|Col1|Campo<br>eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Inducción<br>magnética<br>[mili Gauss]|
|---|---|---|---|
||95|0,80|8,0|
|Límite<br>ICNIRP|5.000|200|2.000|

Fuente: Elaboración propia

###### 6 RADIO INTERFERENCIA POR FENÓMENO CORONA

La descarga corona corresponde a descargas eléctricas parciales (ionización) en el aire alrededor

de los conductores, generadas por alto campo eléctrico. Este fenómeno emite campos

electromagnéticos desde frecuencias de audio hasta alta frecuencia que pueden provocar

perturbaciones en la banda de frecuencia de radio y televisión.

Mediante la aplicación del software LINEAS, de elaboración propia, se determina el campo

eléctrico en la superficie de los conductores y la radio interferencia emitida por el poste de la

línea de 13,2 kV. El programa ocupa el Método de Simulación de Cargas [2] para determinar el

campo eléctrico superficial y el procedimiento CIGRE para evaluar nivel de interferencia [2]. En

el Apéndice 1 se presenta el listado de salida del programa.

La Tabla siguiente resume la magnitud de radio interferencia calculada para 0,5 MHz y a 15m de

distancia lateral desde el conductor externo, según norma canadiense [5], y confrontada con el

valor límite establecido por la norma.

**Tabla 6-1. Magnitud de radio interferencia y confrontación con norma**

|Col1|RI [dB/uV/m]|
|---|---|
|Estructura|-10,2|
|Límite norma canadiense|43|

Fuente: Elaboración propia

11

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

La Figura siguiente muestra gráficamente la variación de la radio interferencia con la distancia al

eje de la línea. La línea verde indica el valor de norma.

**Figura 6-1. Radio interferencia vs distancia para línea en estructura**

Fuente: Elaboración propia

###### 7 CRUCE CON LÍNEA DE MT EXISTENTE

En el punto de coordenadas (19 K 365700,5 mE ; 7960855,5 m S) se producirá el cruce con una

línea de media tensión, la cual se asume corresponde a una línea de 13,2kV. La situación se analiza

con apoyo del software QuickField, ya comentado anteriormente.

12

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 7-1. Malla de elementos finitos**

Fuente: Elaboración propia

**Figura 7-2. Distribución de equipotenciales eléctricas**

Fuente: Elaboración propia

13

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 7-3. Campo eléctrico bajo cruce de líneas**

Fuente: Elaboración propia

**Figura 7-4. Inducción magnética bajo cruce de líneas**

Fuente: Elaboración propia

14

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Comentario:**

Comparado con la situación de la línea singular, el campo eléctrico sube fuertemente a 190 [V/m]

en el borde de franja y el campo magnético se incrementa en mayor proporción a 1,60 [micro

Tesla].

###### 8 ESTUDIO DE PARALELISMO DE LÍNEAS DE 13,2KV

La línea eléctrica que evacúa la energía generada por el Parque se mantiene paralela a una línea

de media tensión previo a su conexión (Ver Figura 8). A continuación se presenta el estudio para

la situación de paralelismo, también mediante el apoyo de QuickField.

Para el estudio del campo magnético se consideran ambas líneas con la misma potencia, lo que

supone un criterio conservador.

**Figura 8-1. Paralelismo de líneas de MT**

Fuente: Elaboración propia

15

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 8-2. Líneas equipotenciales eléctricas**

Fuente: Elaboración propia

**Figura 8-3. Campo eléctrico a 1m sobre el suelo entre líneas**

Fuente: Elaboración propia

16

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Figura 8-4. Líneas equipotenciales magnéticas**

Fuente: Elaboración propia

**Figura 8-5. Inducción magnética a 1m sobre el suelo**

Fuente: Elaboración propia

17

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Comentario:**

Comparado con la situación de la línea singular, el campo eléctrico sube levemente a 140 [V/m]

en el borde de franja y el campo magnético se incrementa en mayor proporción a 1,44 [micro

Tesla], ampliando además la zona de influencia al incorporar ambas líneas.

###### 9 CONCLUSIONES

De los resultados obtenidos en las simulaciones efectuadas y en la investigación bibliográfica, se

obtiene los siguientes valores representativos en las ubicaciones que se indica:

**Tabla 9-1. Resumen de valores representativos**

|Equipo|Campo<br>eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Ubicación|
|---|---|---|---|
|Transformadores 2,5 MVA|-|<1,0|A 5m del equipo<br>|
|Centro de Transformación|-|< 1,0|A 10 m de equipo|
|Línea de transmisión 13,2kV|94,5|0,80|En borde franja|
|Cruce con línea de MT|190|1,60|Borde franja en punto de<br>Cruce|
|Paralelismo con línea de MT|140|1,44|Borde franja en zona<br>paralelismo|
|Límite Norma|5.000|200|En borde franja<br>|

Fuente: Elaboración propia

La magnitud de radio interferencia generada por la línea es -10,2 [dB/uV/m], inferior al límite de

43 [dB/uV/m] definido por la norma canadiense.

Se concluye que las instalaciones del Proyecto Fotovoltaico Chinchorro cumplen con las

restricciones impuestas por la normativa vigente respecto de emisión de campos

electromagnéticos de baja y alta frecuencia.

18

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

###### 10 REFERENCIAS

[1] Students' QuickField (TM) Finite Element Analysis System. Copyright (C) Tera Analysis

[Company,. www.quickfield.com](http://www.quickfield.com/)

[2] N. Morales, "Fenómeno corona en líneas de transmisión y sus efectos".

Publicación T(P)/9, Departamento de Ingeniería Eléctrica. Noviembre 1986.

[3] Nelson Morales O.

Informe línea de base de campos electromagnéticos Proyectos fotovoltaicos Vallenar, para

GAC, 2017

[4] ICNIRP Guidelines for limiting exposure to time varying electric and magnetic fields (1 Hz100 kHz)

Published in: Health Physics 99(6):818 - 836; 2010

International Commission on Non-Ionizing Radiation Protection

ICNIRP Publication - 2010

[5] Association canadienne de normalisation, Valeurs limites et methods de mesure du bruit

électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant alternatif. CAN3
C108.3.1 - M84. Octobre 1984.

[6] Numerical evaluation of the electric field in a compact switchgear of medium voltage

Wojciech KRAJEWSKIPh.D., D.Sc., El. Eng. Assoc. Prof.

Laboratory of Numerical Computations, Electrotechnical Institute

PROCEEDINGS OF ELECTROTECHNICAL INSTITUTE, Issue 267, 2014

[7] Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power Substations

Gerhard Bräunlich, Reinhold Bräunlich. ETH Zürich, Switzerland; FKH Fachkommission für

Hochspannungsfragen. Proceedings, 20th Int. Zurich Symposium on EMC, Zurich 2009

19

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**APÉNDICE 1 RESULTADOS DE LINEA DE BASE**

Las unidades de campo eléctrico son Volt por metro [V/m] o Kilo Volt por metro [kV/m] en alta

tensión; en el caso en estudio, 13,2 kV entre fases y 13,2/√3 KV fase a tierra. La magnitud

representativa del campo magnético es la “inducción Magnética” o “densidad de flujo
Magnético” B **,** que tiene como unidad de medida práctica el mili Gauss (1 mG = 10 [-3] Gauss) o el

micro Tesla (1T = 10 [-6] Tesla) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se caracteriza al campo eléctrico y

el campo magnético cerca de una instalación por el concepto “Campo a nivel del suelo”, que

corresponde al campo eléctrico o magnético medido o calculado a 1 metro de altura sobre el

suelo, en ausencia de otros objetos.

**Planta fotovoltaica**

Se verifica mediante Google Earth que en el lugar de instalación de la planta fotovoltaica no

existen fuentes generadoras de campo electromagnético, como se aprecia en la Figura siguiente.

**Ubicación futura planta fotovoltaica**

Fuente: Google Earth

Por lo tanto, valores de campo son nulos:

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

Campo eléctrico: 0,0 [V/m]

Inducción magnética: 0,0 [mili Gauss]

**Línea de MT existente**

En el punto de coordenadas (19 K 365700,5 mE ; 7960855,5 m S) se aprecia la presencia de una

línea de media tensión, como se muestra en la Figura siguiente.

**Cruce con línea de media tensión**

Fuente: Google Earth

La línea no se encuentra dentro de la base de datos del Coordinador Eléctrico, que incluye líneas

de transmisión de 66 kV o superior. La apreciación que se obtiene del Google Earth es que las

estructuras de soporte son postes simples, similares a los de sistemas de distribución. En atención

a estas consideraciones, se asume que la línea corresponde a una línea de 13,2kV.

Para efectuar una estimación de los campos generados por esta línea, se recurre al software

utilitario Quick Field [1], que permite modelar mediante la metodología de elementos finitos un

plano transversal a la línea y evaluar en dicho plano los campos generados por el voltaje de la

línea y la corriente que fluye por sus conductores. Una línea de transmisión típica en 13,2 kV

presenta la distribución de campos eléctrico y magnético a 1m sobre el suelo mostrada en las

figuras siguientes:

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Malla de elementos finitos**

Fuente: Elaboración propia

**Campo eléctrico a 1m sobre el suelo bajo la línea**

Fuente: Elaboración propia

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Inducción magnética a 1m sobre el suelo bajo la línea**

Fuente: Elaboración propia

El símbolo ⇩ señala la posición de la línea. Los máximos valores de campo generados por la línea

son:

Campo eléctrico: 135 [V/m]

Inducción magnética: 1,21 [micro Tesla]

**Punto de conexión**

El punto de conexión de la línea de evacuación de la planta fotovoltaica corresponde a una línea

de media tensión ubicada a un costado de la calzada poniente de la Av. Santiago Arata, próximo

a la Subestación Quiani 66/13,8 kV. La Figura siguiente indica el punto de conexión.

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Punto de conexión de línea de evacuación**

Fuente: Google Earth

La línea de media tensión existente en el punto lleva una línea de baja tensión en el mismo poste;

esta última línea provoca una depresión en el campo eléctrico generado por la línea de media

tensión y eventualmente un incremento en el campo magnético. Las figuras siguientes muestran

este efecto en una línea de referencia de 13,2 kV medida en el norte [3].

**Campo eléctrico a 1m sobre el suelo bajo línea de 13,2 kV**

Fuente: Elaboración propia

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Inducción magnética a 1m sobre el suelo bajo línea de 13,2 kV**

Fuente: Elaboración propia

Los máximos valores de campo generados por la línea son:

Campo eléctrico: 76 [V/m]

Inducción magnética: 6,71 [micro Tesla]

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**Conclusiones de Línea Base**

Se ha identificado mediante modelaciones y medidas directas en terreno de líneas similares,

valores característicos del campo eléctrico y del campo magnético de fuentes existentes en el

lugar de las instalaciones del Proyecto Fotovoltaico Chinchorro, para definir la Línea de Base de

la componente campos electromagnéticos. Los valores asumidos se presentan en la siguiente

Tabla:

**Valores representativos de Línea de base**

|Col1|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|Inducción magnética<br>[mili Gauss]|
|---|---|---|---|
|Planta fotovoltaica|0,0|0,0|0,0|
|Línea MT|135|1,21|12,1|
|Punto conexión|76|6,71|67,1|

Ninguno de los valores simulados o medidos supera los máximos tolerables para las personas,
definidos por la ICNIRP [4], que corresponden a 5.000 [Volts/m] para el campo eléctrico y 200

[micro Tesla], equivalentes a 2.000 [mili Gauss] para el campo magnético. La ICNIRP es un

organismo experto de consulta en temas de radiaciones no ionizantes reconocida por la

Organización Mundial de la Salud, OMS, la Organización Internacional del Trabajo (International

Labour Organization - ILO) y la Unión Europea.

**NORMATIVA DE REFERENCIA PARA RADIO INTERFERENCIA**

La referencia 5 indica el nivel de perturbación radio eléctrica aceptable generada por líneas de

transmisión o subestaciones, a una frecuencia de 0,5 MHz, Tabla siguiente:

**Nivel de perturbación radiofónica aceptable a 0,5 MHz**

|Tensión eléctrica<br>nominal entre fases (kV)|Radio interferencia<br>[dB /1 μV/m]|
|---|---|
|Bajo 70|43|
|70 - 200|49|
|200 - 300|53|
|300 - 400|56|
|400 - 600|60|
|Sobre 600|63|

Fuente: Referencia [5]

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

Para una línea, valores a 15 m de distancia lateral de la fase externa. Para una subestación, valores

a 15 m del borde. Para una instalación de 13,2 kV, el límite correspondiente es 43 [dB/ (1V/m)].

**NORMAS DE REFERENCIA PARA CAMPOS ELECTROMAGNÉTICOS DE 50 HZ**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de exposición

de las personas a los campos electromagnéticos de frecuencia industrial. No obstante, la

regulación ambiental que rige el tema de emisiones señala que de no existir una regulación

nacional, debe aplicarse como norma de referencia aquella que se encuentre vigente en estados

específicos. El Decreto No 40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del

Sistema de Evaluación de Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia

el 24-12-2013, indica en su Artículo 11:

_“Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos_

_de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados_

_en la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en los siguientes Estados:_

_República Federal de Alemania, República Argentina, Australia, República Federativa del Brasil,_

_Canadá, Reino de España, Estados Unidos Mexicanos, Estados Unidos de América, Nueva_

_Zelandia, Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y Confederación_

_Suiza. Para la utilización de las normas de referencia, se priorizará aquel Estado que posea_

_similitud en sus componentes ambientales, con la situación nacional y/o local, lo que será_

_justificado razonablemente por el proponente._

La recomendación de uso más frecuente para público general y exposición permanente es la

publicada por la ICNIRP [4], organismo no gubernamental reconocido por la Organización Mundial

de la Salud como referente en el tema, que establece 5.000 [V/m] para el campo eléctrico y 200

[micro Tesla], equivalente a 2.000 [mili Gauss] para la inducción magnética, valores que han sido

acogidos por la normativa de diversos países incluidos en la nómina anterior.

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

**APÉNDICE 2 ESTUDIO DE RADIO INTERFERENCIA PARA LA LÍNEA**

Se presenta a continuación el listado de salida del programa LINEAS, que calcula campo eléctrico

superficial en conductores de línea de alta tensión y radio interferencia, aplicado a la estructura

en estudio.

NOTA: El programa utiliza punto decimal (.) en lugar de coma (,). No incluye tilde de acentos.

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Número total de conductores: 3_

_Número de conductores activos: 3_

_Número de cables de guardia: 0_

|Fase|1|2|3|
|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_0.994_|_0.994_|_0.994_|
|_ubicación lateral del conductor (m)_|_-1.50_|_0.36_|_1.50_|
|_ Altura conductora sobre el suelo (m)_|_11.50_|_11.50_|_11.50_|

_Matriz de coeficientes (amplif. por (2 πƐ_ _0_ _))_

_7.7467 2.5182 2.0453_

_2.5182 7.7467 3.0057_

_2.0453 3.0057 7.7467_

_Matriz de capacitancias (amplif. por 1/(2 πƐ_ _0_ _))_

_.1480 -.0388 -.0240_

_-.0388 .1621 -.0527_

_-.0240 -.0527 .1559_

_Potenciales de conductores ( KVolts)_

_(7.9670,0.0000 ) 7.9670_

_( -3.9835, -6.8996 ) 7.9670_

##### PV Power Chile SpA Anexo 13

Estudio de Campos Electromagnéticos

DIA Parque Fotovoltaico Chinchorro

_( -3.9835,6.8996 ) 7.9670_

_Cargas en conductores (Cb)/( 2 πƐ_ _0_ _)_

_(1.4298,0.1019) 1.4334_

_(-.7452,-1.4820) 1.6588_

_(-.6026,1.4388 ) 1.5599_

_Gradientes superficiales (kVef./cm)_

_(1.4384,0.1025) 1.4420_

_(-.7497,-1.4910) 1.6688_

_(-.6062,1.4475) 1.5693_

_Radio interferencia_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|_-12,32_|_-11,53_|_-11,87_||_-10,20_|

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1.: Características técnicas transformador referencial****

| Parámetros | Valor |
| --- | --- |
| Potencia nominal del primario | 5.500 kVA |
| Frecuencia | 50 Hz |
| Tensión nominal del primario | 13,2 kV |

**Tabla 4-1.: Variación de la inducción magnética con distancia al transformador****

| Distancia D[m] | 2 | 4 | 6 | 8 | 10 |
| --- | --- | --- | --- | --- | --- |
| Inducción magnética B[micro Tesla] | 25,0 | 3,12 | 0,92 | 0,40 | 0,20 |

**Tabla 5-1.: Valores de campo en el borde de la franja y confrontación con norma****

| Col1 | Campo<br>eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Inducción<br>magnética<br>[mili Gauss] |
| --- | --- | --- | --- |
|  | 95 | 0,80 | 8,0 |
| Límite<br>ICNIRP | 5.000 | 200 | 2.000 |

**Tabla 6-1.: Magnitud de radio interferencia y confrontación con norma****

| Col1 | RI [dB/uV/m] |
| --- | --- |
| Estructura | -10,2 |
| Límite norma canadiense | 43 |

**Tabla 9-1.: Resumen de valores representativos****

| Equipo | Campo<br>eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Ubicación |
| --- | --- | --- | --- |
| Transformadores 2,5 MVA | - | <1,0 | A 5m del equipo<br> |
| Centro de Transformación | - | < 1,0 | A 10 m de equipo |
| Línea de transmisión 13,2kV | 94,5 | 0,80 | En borde franja |
| Cruce con línea de MT | 190 | 1,60 | Borde franja en punto de<br>Cruce |
| Paralelismo con línea de MT | 140 | 1,44 | Borde franja en zona<br>paralelismo |
| Límite Norma | 5.000 | 200 | En borde franja<br> |
