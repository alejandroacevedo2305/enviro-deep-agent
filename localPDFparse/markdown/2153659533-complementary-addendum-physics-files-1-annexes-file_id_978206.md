---
title: Sin título
author: Usuario de Windows
date: D:20221103145050-03'00'
language: es
type: report
pages: 300
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Evaluación del Impacto de Olor del Proyecto “Mejoramiento Tecnológico Operaciones Agricovial”
  - Índice
  - 1. Introducción
  - 2. Inventario de Emisiones
  - 3. Análisis Meteorológico de Datos Observados y Modelados
  - 4. Estimación del Impacto de las Emisiones de Olor
  - 5 Conclusiones
  - A) APENDICE 1 - Reporte de muestreo AQOM Agricovial
  - B) APENDICE 2 - Informe de APL II Chilehuevos
  - C) APENDICE 3 - Archivos de la Modelación
  ... y 1 secciones más
-->

# Evaluación del Impacto de Olor del Proyecto “Mejoramiento Tecnológico Operaciones Agricovial”

**PREPARÓ:**

**AIR QUALITY & ODOR MANAGEMENT**
**SPIN OFF DE LA PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO**

**Septiembre 2022**

|Fecha|CONTROL DE<br>REVISIÓN|Nombre|Profesión|Función|Firma|
|---|---|---|---|---|---|
|04<br>marzo<br>2022|Rev_0.1|Jorge Dumont<br>Ortiz|Ingeniero Civil<br>Bioquímico|Ingeniero<br>de<br>proyecto<br>y <br>modelador|<br>|
|04<br>marzo<br>2022|Rev_0.1|Fabio Carrera<br>Chapela|Ingeniero<br>Químico,<br>Dr.<br>Ingeniería<br>Química|Director<br>Técnico||
|02<br>de<br>septiembre<br>2022|Rev_0.1.1|Jorge Dumont<br>Ortiz|Ingeniero Civil<br>Bioquímico|Ingeniero<br>de<br>proyecto<br>y <br>modelador||
|02<br>de<br>septiembre<br>2022|Rev_0.1.1|Fabio Carrera<br>Chapela|Ingeniero<br>Químico,<br>Dr.<br>Ingeniería<br>Química|Director<br>Técnico||

2

**CONFIDENCIALIDAD**

La información contenida en este documento es de carácter confidencial y exclusivo para el

individuo o entidad a la que van dirigidas. De manera que, si usted no es el destinario

individualizado y por error recibiera este documento, le agradeceremos notificar al

remitente y borrar este documento junto con todos sus archivos digitales.

3

## Resumen Ejecutivo

El presente proyecto corresponde a la evaluación del impacto odorífico del sector

productivo de Agricovial, ubicado en la comuna de San Bernardo, Región Metropolitana de

Santiago de Chile. El sector productivo se compone por los planteles de Crianza, Postura,

las zonas de acopio de GAP y otras instalaciones de apoyo.

En el escenario base, las fuentes de emisión se corresponden con: pabellones de postura

con ventilación forzada (PPVF), pabellones de postura con ventilación natural (PPVN),

pabellones de crianza con ventilación forzada (PCVF), lombrifiltro sector planta de Riles,

sector de acopio de residuos orgánicos (Seac donde se disponen en bins las aves muertas)

y la zona de acopio de guano (ZAG) sector Lo Herrera.

Dado que el escenario proyectado incorpora modificaciones del proceso de tratamiento de

GAP y de la operación de los pabellones de postura, para este caso las fuentes de emisión

corresponden a: ductos a la salida de los PPVF, PPVN, PCVF, lombrifiltro, Seac, secadora

Kohshin y secador de guano de ave de postura. Cabe mencionar que se implementa la

aplicación de un producto que permite mitigar las emisiones odorantes (Olex o similar) y al

cual se evaluó su capacidad de mitigación, al ser aplicado durante la operación de la

secadora Kohshin, generando una reducción de la concentración de olor que es superior

81%.

No se consideraron las emisiones correspondientes al acopio de guano seco de aves de

postura ya que, en el escenario proyectado, esto se realiza en galpones cerrados (se abre

menos del 2% de las horas al año), dentro del sector El Romeral.

Para determinar las tasas de emisión de las diferentes fuentes identificadas, se emplearon

datos y antecedentes disponibles en los informes de GCA ambiental, el “Informe de

olfatometría - Planta Kohshin” de Salimax, el “Estudio de fuentes y procesos generadores

de olor para el sector productor de huevos de Chile - Acuerdo de Producción Limpia II”

(Chilehuevos 2021) y de mediciones realizadas en Empresa Avícola Zona Central.

La modelación de las emisiones de olor se realizó siguiendo las recomendaciones de la guía

del SEIA, utilizando para ello el modelo CALPUFF y empleando como base, la meteorología

generada por el modelo WRF para el año 2020. La extensión del dominio de simulación es

de 60x60 km con una resolución de 1 km, dentro del cual se incluye la estación

meteorológica El Milagro de la Dirección General de la Aeronáutica Civil para validar los

datos del modelo WRF.

La meteorología observada en la estación Milagro, indica que la dirección del viento

procede del noreste durante la mañana (03:00 a 10:00) y se dirección desde el suroeste en
horas de la tarde-noche (15:00 a 22:00), con una velocidad promedio de 1,9 m/s. La

temperatura promedio es de 14,72 °C y la humedad relativa promedio es del 68,48%.

4

La meteorología modelada en la estación Milagro, indica que la dirección de viento procede

del noreste durante la mañana y se direcciona desde el suroeste en horas de la noche, con
una velocidad promedio de 2,37 m/s. La temperatura promedio es de 14,73°C y la humedad

relativa promedio es del 80,09%.

Se identificaron en total 56 receptores discretos, con distancias desde el límite de la planta

de 84 a 1.927 m en el escenario base. Se analizó el PRMS y se identificó la clasificación de

los receptores 1 al 3, 5 al 22, 28 al 34 y 42 al 56 con el uso de suelo rural, los receptores 23

al 27 y 35 a 41 con el uso de suelo urbano, y al receptor 4 con uso de suelo urbano.

A continuación, se presentan los límites de concentración en inmisión de la ley de los países

bajos ( _Wet geurhinder en veehouderij, 2013_ ) que fue empleada para evaluar el potencial

impacto del proyecto en el escenario base y proyectado.

**Tabla 1.** Límites de concentración en inmisión - Ley de molestias de olor y ganadería de los Países bajos

(percentil 98).

|Clasificación|Límite de concentración en<br>inmisión dentro de región<br>económicamente dedicada a<br>ganadería)|Límite de concentración en<br>inmisión fuera de región<br>económicamente dedicada a<br>ganadería|
|---|---|---|
|**Núcleo urbano**|3 OUE/m3|2 OUE/m3|
|**Núcleo rural**|14 OUE/m3|8 OUE/m3|

Aun cuando en la región Metropolitana se concentra actividades agrícolas, localizándose en

la región el 43% de las instalaciones del sector de aves de postura y, el 76,8% de los

receptores se clasifica en uso de suelo rural, para ofrecer un mayor grado de protección a

los receptores, es que se considera los límites definidos “Fuera de una región

económicamente dedicada a la ganadería”, por lo que se evalúa el proyecto con un límite

de concentración en inmisión de 2 OUE/m [3] (receptores en el núcleo urbano) y de 8 OUE/m [3]

(receptores rurales).

En la fase de operación del escenario base en el sector Romeral, el percentil 98 de la
concentración horaria de las emisiones muestra una superficie de la isodora de 3 OU/m [3]
que se extiende fuera del perímetro de la planta y una isodora de 14 OU/m [3] que se

encuentra localizada sobre el perímetro del sector de postura, extendiéndose al este y oeste

del mismo (radio de alcance máximo de 489 m en dirección noroeste).

En la fase de operación del escenario base en el sector Lo Herrera, el percentil 98 de la

concentración horaria de las emisiones muestra que principalmente las isodoras se localizan
sobre la zona de acopio de GAP, con la isodora de 14 OU/m [3] que se extiende fuera de la

zona de acopio de GAP (posee un radio de alcance máximo de 1.353 m en dirección nor

noroeste).

En el escenario base (ver Tabla 2), se identificó que ninguno de los receptores clasificados
dentro del uso de suelo urbano supera el límite establecido en la normativa de 2 OU/m [3],

por su parte, de los receptores clasificados dentro del uso de suelo rural, 3 receptores

5

superan el límite definido de 8 OU/m [3], correspondientes al receptor 20, 21 y 50, que poseen
una concentración en inmisión de 14,1, 34 y 12,1 OU/m [3] respectivamente.

**Tabla 2.** Concentración ambiental de olor en receptores discretos (escenario base - Percentil 98).

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re1**|0,2|8|Sí|
|**Re2**|0,6|8|Sí|
|**Re3**|0,6|8|Sí|
|**Re4**|0,5|2|Sí|
|**Re5**|0,7|8|Sí|
|**Re6**|0,4|8|Sí|
|**Re7**|0,6|8|Sí|
|**Re8**|0,4|8|Sí|
|**Re9**|0,6|8|Sí|
|**Re10**|4,5|8|Sí|
|**Re11**|2,3|8|Sí|
|**Re12**|1,9|8|Sí|
|**Re13**|2,2|8|Sí|
|**Re14**|2,8|8|Sí|
|**Re15**|3,3|8|Sí|
|**Re16**|5|8|Sí|
|**Re17**|1,8|8|Sí|
|**Re18**|1,7|8|Sí|
|**Re19**|4,3|8|Sí|
|**Re20**|14,1|8|No|
|**Re21**|34|8|No|
|**Re22**|0,4|8|Sí|
|**Re23**|0,5|2|Sí|
|**Re24**|0,4|2|Sí|
|**Re25**|0,4|2|Sí|
|**Re26**|0,4|2|Sí|
|**Re27**|0,4|2|Sí|
|**Re28**|0,5|8|Sí|
|**Re29**|0,6|8|Sí|
|**Re30**|0,6|8|Sí|
|**Re31**|0,6|8|Sí|
|**Re32**|0,5|8|Sí|
|**Re33**|0,5|8|Sí|
|**Re34**|0,4|8|Sí|
|**Re35**|0,4|2|Sí|
|**Re36**|0,3|2|Sí|
|**Re37**|0,3|2|Sí|
|**Re38**|0,3|2|Sí|

6

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re39**|0,4|2|Sí|
|**Re40**|0,4|2|Sí|
|**Re41**|0,4|2|Sí|
|**Re42**|0,4|8|Sí|
|**Re43**|0,5|8|Sí|
|**Re44**|0,6|8|Sí|
|**Re45**|0,7|8|Sí|
|**Re46**|0,9|8|Sí|
|**Re47**|2,9|8|Sí|
|**Re48**|2,3|8|Sí|
|**Re49**|1,2|8|Sí|
|**Re50**|12,1|8|No|
|**Re51**|0,4|8|Sí|
|**Re52**|0,4|8|Sí|
|**Re53**|0,4|8|Sí|
|**Re54**|0,6|8|Sí|
|**Re55**|0,7|8|Sí|
|**Re56**|0,3|8|Sí|

Debido a que en el escenario proyectado se elimina la zona de acopio de GAP del sector Lo

Herrera, la distancia de los 56 receptores discretos al perímetro de las zonas operativas

cambia, siendo el nuevo rango de distancias de los receptores al perímetro del proyecto de

los 84 a 2.852 m.

En el escenario proyectado (ver Tabla 3), se identificó que ninguno de los receptores

clasificados dentro del uso de suelo urbano supera el límite establecido en la normativa de
2 OU/m [3] y que ninguno de los receptores clasificados dentro del uso de suelo rural supera
el límite establecido en la normativa de 8 OU/m [3] .

**Tabla 3.** Concentración ambiental de olor en receptores discretos (escenario proyectado - Percentil 98).

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re1**|0,2|8|Sí|
|**Re2**|0,6|8|Sí|
|**Re3**|0,5|8|Sí|
|**Re4**|0,5|2|Sí|
|**Re5**|0,6|8|Sí|
|**Re6**|0,4|8|Sí|
|**Re7**|0,6|8|Sí|
|**Re8**|0,3|8|Sí|
|**Re9**|0,6|8|Sí|
|**Re10**|0,3|8|Sí|
|**Re11**|0,1|8|Sí|

7

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re12**|0,1|8|Sí|
|**Re13**|0,1|8|Sí|
|**Re14**|0,1|8|Sí|
|**Re15**|0,2|8|Sí|
|**Re16**|0,1|8|Sí|
|**Re17**|0,5|8|Sí|
|**Re18**|0,5|8|Sí|
|**Re19**|0,3|8|Sí|
|**Re20**|0,6|8|Sí|
|**Re21**|0,3|8|Sí|
|**Re22**|0,1|8|Sí|
|**Re23**|0,2|2|Sí|
|**Re24**|0,2|2|Sí|
|**Re25**|0,2|2|Sí|
|**Re26**|0,2|2|Sí|
|**Re27**|0,2|2|Sí|
|**Re28**|0,2|8|Sí|
|**Re29**|0,2|8|Sí|
|**Re30**|0,2|8|Sí|
|**Re31**|0,2|8|Sí|
|**Re32**|0,2|8|Sí|
|**Re33**|0,2|8|Sí|
|**Re34**|0,2|8|Sí|
|**Re35**|0,2|2|Sí|
|**Re36**|0,2|2|Sí|
|**Re37**|0,2|2|Sí|
|**Re38**|0,2|2|Sí|
|**Re39**|0,2|2|Sí|
|**Re40**|0,2|2|Sí|
|**Re41**|0,2|2|Sí|
|**Re42**|0,2|8|Sí|
|**Re43**|0,2|8|Sí|
|**Re44**|0,2|8|Sí|
|**Re45**|0,3|8|Sí|
|**Re46**|0,3|8|Sí|
|**Re47**|1,6|8|Sí|
|**Re48**|1,3|8|Sí|
|**Re49**|0,8|8|Sí|
|**Re50**|4,9|8|Sí|
|**Re51**|0,3|8|Sí|

8

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re52**|0,3|8|Sí|
|**Re53**|0,3|8|Sí|
|**Re54**|0,4|8|Sí|
|**Re55**|0,5|8|Sí|
|**Re56**|0,2|8|Sí|

El área de influencia (AI) del escenario base del proyecto tiene una superficie de 21,5 km [2] y

abarca los sectores de postura, crianza y acopio de GAP. Desde el centroide del AI, existe

un alcance de 3,7 km al Norte, 1,61 km al Este, 3,7 km al Sur y 1,47 km al Oeste. El radio de

máximo alcance es de 5,2 km al Sur Sur-este y el radio mínimo de alcance es de 1,2 km al

Sur-oeste.

El AI del escenario proyectado se divide en dos superficies, correspondientes a la superficie
localizada en el sector Romeral y que posee una superficie de 3,27 km [2] y la superficie
localizada en el sector Lo Herrera y que posee una superficie de 0,76 km [2] .

En el escenario proyectado, desde el centroide del AI en el sector Romeral, existe un alcance

de 1,11 km norte, 0,93 km este, 1,29 km sur y 0,81 km oeste. Un radio máximo de alcance

de 1,3 km al sur sureste y un radio mínimo de alcance de 0,74 km oeste suroeste.

En el escenario proyectado, desde el centroide del AI en el sector Lo Herrera, existe un

alcance de 0,37 km norte, 0,62 km este, 0,46 km sur y 0,56 km oeste. Un radio máximo de

alcance de 0,63 km al este noreste y un radio mínimo de alcance de 0,34 km nor noreste.

Debido a la implementación de ductos a la salida de todos los PPVF, cambio de localización

del GAP desde Lo Herrera a Romeral, cambio de tratamiento de GAP de pilas a tratamiento

por secadora GAP y secadora Kohshin y la implementación de medidas de mitigación

(aplicación producto controlador de olores Olex o similar), se genera una reducción del

81,7% del área de influencia en el escenario proyectado y una reducción promedio de la

concentración en inmisión del 51,3%, con respecto al escenario base.

Considerando los antecedentes presentados, el proyecto cumple con los límites

establecidos en la ley de los países bajos en el escenario proyectado, no generando impacto

en el área colindante.

9

# Índice

1. Introducción ................................................................................................................. 16

1.1. Objetivo .................................................................................................................. 16

1.2. Dominio de Estudio ................................................................................................ 16

2. Inventario de Emisiones ............................................................................................... 20

2.1. Factores de emisión - Escenario base ................................................................... 27

2.2. Factores de emisión - Escenario proyectado ........................................................ 29

2.3. Nivel de Actividad .................................................................................................. 31

2.3.1. Fase de Operación - Escenario base .................................................................. 31

2.3.2. Fase de Operación - Escenario Proyectado ....................................................... 33

2.4. Resultados Inventario de Emisión ......................................................................... 34

2.4.1. Inventario de Emisión - Escenario base ............................................................. 34

2.4.2. Inventario de Emisión - Escenario proyectado .................................................. 36

2.5. Tipología de Proyecto ............................................................................................ 40

3. Análisis Meteorológico de Datos Observados y Modelados ........................................ 41

3.1. Estación El Milagro ................................................................................................. 42

3.1.1. Viento ................................................................................................................. 42

**3.1.1.1.** **Velocidad del Viento** .................................................................................. 45

**3.1.1.2.** **Dirección del viento** ................................................................................... 47

3.1.2. Temperatura ....................................................................................................... 50

3.1.3. Humedad Relativa .............................................................................................. 53

3.2 Análisis de la incertidumbre .................................................................................. 56

3.2.1 Incertidumbre en Estación El Milagro ................................................................ 57

4. Estimación del Impacto de las Emisiones de Olor ........................................................ 58

4.1. Receptores ............................................................................................................. 58

4.2. Selección de normativa .......................................................................................... 65

4.2.1. Norma Australiana ............................................................................................. 65

4.2.2. Norma Países bajos (Holanda) ........................................................................... 66

4.2.3. Justificación de la selección de normativa ......................................................... 66

4.3. Modelación de Impactos por Emisiones de Olor escenario actual ....................... 68

10

4.4. Modelación de Impactos por Emisiones de Olor escenario proyectado ............... 72

4.5. Área de influencia - Escenario base ...................................................................... 76

4.6. Área de influencia - Escenario proyectado ........................................................... 77

5 Conclusiones ................................................................................................................. 78

A) APENDICE 1 - Reporte de muestreo AQOM Agricovial ............................................... 79

A.1) Sector Romeral .......................................................................................................... 79

A.2) Sector Lo Herrera .................................................................................................... 106

A.3) Medición secadora Kohshin .................................................................................... 133

A.4) Empresa Avícola Zona Central ................................................................................ 186

B) APENDICE 2 - Informe de APL II Chilehuevos ............................................................ 208

C) APENDICE 3 - Archivos de la Modelación .................................................................. 298

D) APENDICE 4 - Bibliografía ........................................................................................... 299

11

## Índice de Figuras

**Figura 1.** Dominio de Estudio del proyecto Mejoramiento Tecnológico Operaciones

Agricovial. 17

**Figura 2.** Localización del perímetro productivo de Agricovial - Sector Romeral. 18

**Figura 3.** Localización del perímetro crianza y acopio de guano de Agricovial - Sector Lo

Herrera. 19

**Figura 4.** Identificación de fuentes de emisión planta de procesamiento - Escenario base.

20

**Figura 5.** Identificación de fuentes de emisión planta de tratamiento de RILes - Escenario

base. 20

**Figura 6.** Localización de fuentes de emisión de olor sector Romeral (escenario base). 22

**Figura 7.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario base). 23

**Figura 8.** Identificación de fuentes de emisión planta de procesamiento - Escenario

proyectado. 23

**Figura 9.** Identificación de fuentes de emisión planta de tratamiento de RILes - Escenario

proyectado. 24

**Figura 10.** Localización de fuentes de emisión de olor sector Romeral (escenario

proyectado) 26

**Figura 11.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario

proyectado). 27

**Figura 12.** Localización de la estación meteorológica El Milagro. 41

**Figura 13.** Rosa de viento año 2020: datos observados en estación El Milagro (izquierda) y

modelados WRF (derecha). 42

**Figura 14.** Rosa de viento año 2020: Horario 08:00 a 18:00. Datos observados en estación

El Milagro (izquierda) y modelados WRF (derecha). 43

**Figura 15.** Rosa de viento año 2020: Horario 18:00 a 08:00. Datos observados en estación

El Milagro (izquierda) y modelados WRF (derecha). 43
**Figura 16.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos

observados en estación El Milagro). 44
**Figura 17.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos

modelados en estación El Milagro). 44
**Figura 18.** Ciclo diario de la velocidad del viento observada en estación El Milagro (m/s)

Hora en (UTC). 45
**Figura 19.** Ciclo diario de la velocidad del viento modelada en estación El Milagro (m/s) Hora

en (UTC). 45
**Figura 20.** Serie de tiempo de la velocidad del viento observada en estación El Milagro (m/s)

Hora en (UTC). 46
**Figura 21.** Serie de tiempo de la velocidad del viento modelada en estación El Milagro (m/s)

Hora en (UTC). 46

12

**Figura 22** . Ciclo estacional de la velocidad del viento observada en estación El Milagro (m/s)

Hora en (UTC). 47
**Figura 23.** Ciclo estacional de la velocidad del viento modelada en estación El Milagro (m/s)

Hora en (UTC). 47

**Figura 24.** Ciclo diario de la dirección del viento observada en estación El Milagro (°) Hora

en (UTC). 48

**Figura 25.** Ciclo diario de la dirección del viento modelada en estación El Milagro (°) Hora

en (UTC). 48

**Figura 26.** Serie de tiempo de la dirección del viento observada en estación El Milagro (°)

Hora en (UTC). 48

**Figura 27.** Serie de tiempo de la dirección del viento modelada en estación El Milagro (°)

Hora en (UTC). 49

**Figura 28.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°)

(Hora en UTC). 49

**Figura 29.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°)

(Hora en UTC). 50

**Figura 30.** Ciclo diario de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

50

**Figura 31.** Ciclo diario de la temperatura modelada en la estación El Milagro (°C) Hora (UTC).

51

**Figura 32.** Serie de tiempo de temperatura observada en la estación El Milagro (°C) Hora

(UTC). 51

**Figura 33.** Serie de tiempo de temperatura modelada en la estación El Milagro (°C) Hora

(UTC). 51

**Figura 34.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora

(UTC). 52

**Figura 35.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora

(UTC). 52

**Figura 36.** Ciclo diario de la humedad relativa observada en la estación El Milagro (%) Hora

(UTC). 53

**Figura 37.** Ciclo diario de la humedad relativa modelada en la estación El Milagro (%) Hora

(UTC). 53

**Figura 38.** Serie de tiempo de la humedad relativa observada en la estación El Milagro (%)

Hora (UTC). 54

**Figura 39.** Serie de tiempo de la humedad relativa modelada en la estación El Milagro (%)

Hora (UTC). 54

**Figura 40.** Ciclo estacional de la humedad relativa observada en la estación El Milagro (%)

Horas (UTC). 55

**Figura 41.** Ciclo estacional de la humedad relativa modelada en la estación El Milagro (%)

Horas (UTC). 55

**Figura 42.** Localización de receptores discretos del proyecto en el sector Romeral. 58

13

**Figura 43.** Localización de receptores discretos del proyecto en el sector Lo Herrera. 59

**Figura 44.** Uso de suelo en el sector Romeral. 64

**Figura 45.** Uso de suelo en el sector Lo Herrera. 65

**Figura 46.** Concentración ambiental horaria de olor percentil 98 en el escenario base (sector

Romeral). 69

**Figura 47.** Concentración ambiental horaria de olor percentil 98 en el escenario base (sector

Lo Herrera). 70

**Figura 48.** Concentración ambiental horaria de olor percentil 98 en el escenario proyectado

(sector Romeral). 73

**Figura 49.** Concentración ambiental horaria de olor percentil 98 en el escenario proyectado

(sector Lo Herrera). 74
**Figura 50.** Área de influencia del proyecto - Escenario base. 76
**Figura 51.** Área de influencia del proyecto - Escenario proyectado. 77

## Índice de Tablas

**Tabla 1.** Límites de concentración en inmisión - Ley de molestias de olor y ganadería de los

Países bajos (percentil 98). 5

**Tabla 2.** Concentración ambiental de olor en receptores discretos (escenario basePercentil 98). 6

**Tabla 3.** Concentración ambiental de olor en receptores discretos (escenario proyectadoPercentil 98). 7

**Tabla 4.** Coordenadas generales del perímetro del sector de postura en sector Romeral. 17

**Tabla 5.** Coordenadas generales del perímetro del sector de crianza en Lo Herrera. 18

**Tabla 6.** Coordenadas generales del perímetro del sector de acopio de GAP en Lo Herrera

(actual). 18

**Tabla 7.** Factor de emisión de fuentes de emisión de olores del escenario base. 27

**Tabla 8.** Comparación de fuentes - Zona de acopio residuos orgánicos. 29

**Tabla 9** Concentración de olor secador Kohshin operando al 10%. 30

**Tabla 10.** Factores de emisión de fuentes identificadas en el escenario proyectado. 30

**Tabla 11.** Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario

base). 31

**Tabla 12** . Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario

proyectado). 33

**Tabla 13.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario base). 35

**Tabla 14.** Porcentaje de aporte a la tasa de emisión de olor total de la planta de Agricovial

- Escenario base. 36

**Tabla 15.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).

37

**Tabla 16.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).

38

14

**Tabla 17.** Porcentaje de aporte a la tasa de emisión de olor total de la planta de Agricovial

- Escenario proyectado. 39

**Tabla 18.** Ubicación de estación meteorológica superficial El Milagro. 41

**Tabla 19.** Criterios estadísticos de aceptación de la predicción proporcionada por un modelo

meteorológico. 56

**Tabla 20.** Criterios de tolerancia de diferencia absoluta de variables modeladas. 56

**Tabla 21.** Valores de los parámetros de la predicción proporcionada por el modelo para la

Estación El Milagro. 57

**Tabla 22.** Receptores discretos. 59

**Tabla 23.** Descripción receptores discretos. 61

**Tabla 24.** Concentración ambiental de olor en receptores discretos (escenario basePercentil 98). 70

**Tabla 25.** Concentración ambiental de olor en receptores discretos (escenario proyectado

- Percentil 98). 74

15

# 1. Introducción

En el presente informe se evalúa el impacto de las emisiones de olor emitidas por el

proyecto “Mejoramiento Tecnológico Operaciones Agricovial”, ubicado en la comuna de

San Bernardo, Región Metropolitana de Santiago de Chile.

El Proyecto “Mejoramiento Tecnológico Operaciones Agricovial” consiste en evaluar las

instalaciones de producción existentes y el desarrollo de una nueva y moderna instalación

para el manejo de Guano de Ave de Postura (GAP), que buscan mejorar el desempeño

ambiental de las instalaciones que actualmente operan en la comuna, permitiendo con ello

una mejora sustentable en las operaciones, complementando la operación con medidas de

mitigación en los equipos secador GAP y secadora Kohshin, con la aplicación del producto

controlador de olores (Olex o similar).

Considerando todo lo expuesto anteriormente, los objetivos de la presentación de esta

Declaración de Impacto Ambiental son:

 - Evaluar las instalaciones actuales y que comenzaron a operar con posterioridad al

año 1997, es decir, los 3 Pabellones de Crianza y los 11 Pabellones de Postura que

actualmente superan las 60 mil gallinas (tipología de ingreso L.4.2).

 - Actualizar el manejo de gestión del Guano, lo cual contempla el traslado del sector

de acopio de guano al sector de Romeral y la implementación de nuevas tecnologías

de tratamiento, en conjunto con medidas de mitigación. Las obras constructivas

consideran: Líneas de Secado de Guano y 1 Galpón para Acopio de Guano seco.

En efecto, el escenario proyectado incorpora modificaciones del proceso de tratamiento de

GAP y de la operación de los pabellones de postura. Las modificaciones del proceso de

tratamiento de GAP consideran la eliminación del sector de acopio de GAP actual en Lo

Herrera, implementando el uso de secadores de GAP y secadora Kohshin que se localizarán

en el sector Romeral y la implementación de ductos en todos los pabellones de postura de

ventilación forzada.

## 1.1. Objetivo

Evaluar los potenciales efectos de las emisiones de Olores del Proyecto Mejoramiento

Tecnológico Operaciones Agricovial, a través de una estimación de emisiones de olores del

sector productivo de Agricovial sector Romeral y Agricovial sector Lo Herrera, en el

escenario de operación actual y el escenario proyectado.

## 1.2. Dominio de Estudio

El estudio de impacto de olores se realiza en una grilla con extensión de 60 km por 60 km y

una resolución de 1 km por 1 km.

16

**Figura 1.** Dominio de Estudio del proyecto Mejoramiento Tecnológico Operaciones Agricovial.

**Tabla 4.** Coordenadas generales del perímetro del sector de postura en sector Romeral.

|Vértice|Coordenadas UTM<br>(Datum WGS 84 Huso 19)<br>Este (m) Norte (m)|Col3|
|---|---|---|
|**A **|336644,4|6270317,3|
|**B **|336595,8|6270324,5|
|**C **|336455,3|6270151,7|
|**D **|336422,6|6270017,1|
|**E **|336286,7|6269877,7|
|**F **|336632,8|6269651,9|
|**G **|336641,7|6269631,4|
|**H **|336806,4|6269486,3|
|**I **|337191,4|6269744,9|
|**J **|337196,4|6269812,8|
|**K **|336919,4|6269731,7|
|**L **|336871,0|6269760,1|
|**M **|336880,6|6269980,3|

17

**Tabla 5.** Coordenadas generales del perímetro del sector de crianza en Lo Herrera.

|Vértice|Coordenadas UTM<br>(Datum WGS 84 Huso 19)|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|**A **|336166,2|6273729,7|
|**B **|336104,5|6273176,1|
|**C **|336668,8|6273172,5|
|**D **|336695,6|6273627,5|

**Tabla 6.** Coordenadas generales del perímetro del sector de acopio de GAP en Lo Herrera (actual).

|Vértice|Coordenadas UTM<br>(Datum WGS 84 Huso 19)|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|**A **|335503,5|6274557,0|
|**B **|335453,1|6274100,1|
|**C **|336177,9|6273870,7|
|**D **|336234,2|6274241,7|

**Figura 2.** Localización del perímetro productivo de Agricovial - Sector Romeral.

18

**Figura 3.** Localización del perímetro crianza y acopio de guano de Agricovial - Sector Lo Herrera.

19

# 2. Inventario de Emisiones

El presente proyecto corresponde a la evaluación del impacto odorífico del sector

productivo de Agricovial sector Romeral y sector Lo Herrera, en el escenario de operación

actual y el escenario proyectado. Siguiendo los lineamientos recomendados para definir los

datos de entrada que se detallan en la “Guía para el uso de modelos de calidad del aire en

el SEIA” (2012), en esta sección se procede a identificar las fuentes de emisión de olor.

Para la identificación de las fuentes de emisión del escenario base, se procedió a analizar el

diagrama de procesos de la planta de procesamiento de Agricovial y de la planta de

tratamiento de RILes (Figura 4 y Figura 5).

**Figura 4.** Identificación de fuentes de emisión planta de procesamiento - Escenario base.

**Figura 5.** Identificación de fuentes de emisión planta de tratamiento de RILes - Escenario base.

Del diagrama de proceso de la Figura 4, se identificaron las siguientes fuentes de emisión:

 - **Pabellones de postura** : están divididos en pabellones de postura con ventilación

forzada (PPVF) y pabellones de postura con ventilación natural (PPVN).

20

 - **Pabellones de crianza** : corresponden a los pabellones de crianza con ventilación

forzada (PCVF).

 - **Zona de acopio, tratamiento y almacenamiento de GAP** : identificado como zona de

acopio de GAP para efectos del proyecto (ZAG).

 - **Zona de acopio de residuos orgánicos** : corresponde al sector en el cual se produce

el acopio de los residuos de la planta, incluido el acopio de aves muertas. Se

identificó como sector de acopio de residuos orgánicos (Seac).

 - **Tratamiento de RILes** : parte del proceso se identifica como fuente emisora, lo cual

se especifica posteriormente.

No se identificaron como fuentes de emisión del proceso de producción los siguientes

procesos:

 - **Empaquetado y etiquetado, elaboración de productos** : estos procesos se realizan

en galpones cerrados, por lo que no ocurren emisiones al medio ambiente. Se realiza

su apertura menos del 2% de las horas al año, por lo que para efectos de la

modelación que considera el percentil 98, aun si se considera en la modelación su

aporte no va a ser evaluado.

Del diagrama de proceso de la Figura 5, se identificó la siguiente fuente de emisión de la

planta de tratamiento de RILes:

 - **Biofiltro** : corresponde al Lombrifiltro del proceso (considera la superficie que

actualmente está operando a la fecha del desarrollo del presente informe 120
m [3] /d).).

No se identificaron como fuentes de emisión de la planta de tratamiento de RILes los

siguientes equipos:

 - **Filtro rotatorio, desgrasador y DAF** : estos equipos se localizan en un espacio

cerrado, por lo que no ocurren emisiones al medio ambiente. Se realiza su apertura

menos del 2% de las horas al año, por lo que para efectos de la modelación que

considera el percentil 98, aun si se considera en la modelación su aporte no va a ser

evaluado.

 - **Tolva de almacenamiento y drenaje de lodos** : se encuentra cerrada. Se realiza su

apertura menos del 2% de las horas al año, por lo que para efectos de la modelación

que considera el percentil 98, aun si se considera en la modelación su aporte no va

a ser evaluado.

En el escenario base se hicieron mediciones de las fuentes en operación que se encuentran

en los anexos A.1) Sector Romeral y A.2) Sector Lo Herrera, determinando la concentración

y su factor de emisión, y se siguió el lineamiento definido en la “Guía para la predicción y

evaluación de impactos por olor en el SEIA” (2017), en el cual se define “El uso de factores

de emisión que es aconsejable solo en proyectos nuevos y siempre y cuando no se cuente

21

con emisiones de referencia, en este caso se deben utilizar preferentemente factores

publicados por agencias estatales de protección del medio ambiente, normas técnicas o

guías técnicas relacionadas”, para determinar el factor de emisión del sector de acopio de

residuos orgánicos (escenario base) y de la secadora de guano (escenario proyectado).

Cabe notar que, para las mediciones, se determinó el factor de emisión de los PPVN en la

zona superior (jaulas) y en la zona inferior (cama de guano a nivel de piso). Para las

mediciones y en consecuente, las modelaciones, la ZAG fue separada en ZAG fresco, ZAG

activo y ZAG maduro, acorde a las diferentes etapas de maduración en las cuales se

encontraban las pilas.

A continuación, se presenta la localización de las fuentes del escenario base.

**Figura 6.** Localización de fuentes de emisión de olor sector Romeral (escenario base).

22

**Figura 7.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario base).

Para la identificación de las fuentes de emisión del escenario proyectado, se procedió a

analizar el diagrama de procesos de la planta de procesamiento de Agricovial y de la planta

de tratamiento de RILes (Figura 8 y Figura 9).

**Figura 8.** Identificación de fuentes de emisión planta de procesamiento - Escenario proyectado.

23

**Figura 9.** Identificación de fuentes de emisión planta de tratamiento de RILes - Escenario proyectado.

Del diagrama de proceso de la Figura 8, se identificaron las siguientes fuentes de emisión:

 - **Pabellones de postura** : están divididos en pabellones de postura con ventilación

forzada (PPVF) y pabellones de postura con ventilación natural (PPVN). A todos los

PPVF se le implementa ductos a la salida, lo cual permite liberar la emisión odorante

a una mayor altura, favoreciendo el proceso del efecto de dispersión de la emisión.

 - **Pabellones de crianza** : corresponden a los pabellones de crianza con ventilación

forzada (PCVF).

 - **Tratamiento de GAP** : Corresponde al tratamiento que se realiza al GAP, mediante

secador de GAP y secadora Kohshin.

 - **Zona de acopio de residuos orgánicos** : corresponde al sector en el cual se produce

el acopio de los residuos de la planta, incluido el acopio de aves muertas. Se

identificó como sector de acopio de residuos orgánicos (Seac).

 - **Tratamiento de RILes** : parte del proceso se identifica como fuente emisora, tal como

se explicó previamente. Esta fuente corresponde al biofiltro (Lombrifiltro).

`o` Considera la superficie que actualmente está operando a la fecha del

desarrollo del presente informe, correspondiente a 120 (m [3] /d).

Las fuentes no identificadas como emisoras en el escenario base se mantienen como tales

en el escenario proyectado tanto para la planta procesadora como para la planta de

tratamiento de RILes (Figura 8 y Figura 9).

No se estima como fuente de emisión el almacenamiento de GAP, pues este se realiza en

galpón cerrado, por lo que para efectos de la modelación y considerando que se encuentran

cerrados, no son fuentes de emisión a modelar. La apertura del galpón se realiza menos del

2% de las horas al año, por lo que para la modelación que considera el percentil 98%, no

puede a ser evaluado. Adicionalmente, como medida de mitigación de potenciales

emisiones odorantes, se cubrirán las pilas con una manga de polietileno.

24

Para aquellas fuentes de emisión que se mantienen en el escenario proyectado, se emplean

los factores de emisión y concentraciones de olor obtenidos durante el muestreo.

Para evaluar la operación de la secadora Kohshin y el efecto de mitigación asociado a la

aplicación del producto controlador de olores, se procedió a realizar una medición con y sin
producto, tratando 120 m [3], un 10% de la capacidad del equipo. La medición se encuentra

disponible en el informe de Salimax (2022), Anexo A.3) Medición secadora Kohshin. La

aplicación del producto controlador de olores produce que se disminuya la concentración

de olor en más de un 80%. Para la estimación de la tasa de emisión de olor, se considera el

equipo operando con toda su capacidad.

Para aquellas fuentes nuevas y en consideración de que no se poseen datos de medición de

Agricovial, siguiendo la “Guía para la predicción y evaluación de impactos por olor en el

SEIA”, se empleó antecedentes levantados en el “Estudio de fuentes y procesos

generadores de olor para el sector productor de huevos de Chile - Acuerdo de Producción

Limpia II” (Chilehuevos 2021. Disponible en el APENDICE 2 - Informe de APL II Chilehuevos),

el proyecto “Ampliación Plantel Avícola Florida” (Sepulveda, 2020), y las mediciones

realizadas al secador de guano de Empresa Avícola Zona Central (presentes en el anexo A.4)

Empresa Avícola Zona Central).

Mediante los datos obtenidos de Empresa Avícola Zona Central, se procedió a estimar la

Tasa de Estimación de Olores (TEO) del secador de guano de aves de postura, determinando

a través de un balance de flujos y concentraciones de olor, la TEO que se remueve desde las

pilas de GAP tratadas por el equipo que tiene una capacidad de tratar el GAP de 200.000

aves de postura y estimando a partir de este, la TEO de 1.000.000 aves. Cabe mencionar

que dada la similitud de operación y estructura del secador de GAP con respecto al secador

Kohshin, también se implementará el producto controlador de olores como medida de

mitigación, estimando en un escenario conservador, generar una reducción de la tasa de

emisión de olor de un 50%.

25

**Figura 10.** Localización de fuentes de emisión de olor sector Romeral (escenario proyectado)

26

**Figura 11.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario proyectado).

## 2.1. Factores de emisión - Escenario base

En esta sección se presentan los factores de emisión (FE) de las fuentes de emisión de

olores, calculados a partir de la concentración de olor medida por GCA Ambiental (anexo

A.1) Sector Romeral y A.2) Sector Lo Herrera).

Las mediciones se realizaron a 1 PPVF (PPVF 1), 1 PPVN (sección jaulas y de cama),

lombrifiltro, 1 PCVF y a las pilas de guano de ave fresco, activo y maduro. Por lo que, a partir

de los datos medidos, se homologa los FE para otras fuentes del mismo tipo.

**Tabla 7.** Factor de emisión de fuentes de emisión de olores del escenario base.

|Fuente CO (OU/m3) FE (OU/(m2·s)) Tipo fuente Bibliografía|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**PPVF (medición en**<br>**extractor)**|177|--|Puntual|GCA Ambiental<br>2021|
|**PPVN sector jaulas**|148|11,3|Difusa|GCA Ambiental<br>2021|
|**PPVN sector cama**<br>**guano**|653|5,4|Difusa|GCA Ambiental<br>2021|
|**PCVF (medición en**<br>**extractor)**|241|--|Puntual|GCA Ambiental<br>2020|

27

|Fuente CO (OU/m3) FE (OU/(m2·s)) Tipo fuente Bibliografía|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Lombrifiltro**|129|1,08|Difusa|GCA Ambiental<br>2021|
|**Zona acopio residuos**<br>**orgánicos**|--|18,71|Difusa|Homologado a<br>la emisión de<br>fosa<br>de<br>aves<br>muertas cargas<br>del proyecto de<br>DIA “Ampliación<br>plantel<br>avícola<br>Florida” 2020.<br>Este estudio lo<br>homologó<br>del<br>proyecto<br>de<br>Avícola Reinero<br>SpA (2019)|
|**Pilas de guano fresco**|729|6,07|Difusa|GCA Ambiental<br>2020|
|**Pilas de guano activo**|1.202|10,02|Difusa|GCA Ambiental<br>2020|
|**Pilas de guano**<br>**maduro**|577|4,80|Difusa|GCA Ambiental<br>2020|

**Fuente** : Informe de GCA Ambiental, 2020 e Informe de GCA Ambiental, 2021.

De acuerdo a antecedentes disponibles del “Estudio de fuentes y procesos generadores de

olor para el sector productor de huevos de Chile - Acuerdo de Producción Limpia II”

(Chilehuevos 2021 disponible en APENDICE 2 - Informe de APL II Chilehuevos), durante el

volteo de las pilas activas, el factor de emisión incrementa en 4 veces. Se emplea este

antecedente para determinar la TEO de las pilas de guano activo durante su volteo.

La ecuación para la estimación de emisiones de una fuente dada es la siguiente:

E= A∙FE

Donde:

E = Tasa de emisión (OU/s).

A = Nivel de actividad.

FE = Factor de emisión.

La fuente de emisión de zona de acopio de residuos orgánicos se homologo a la del proyecto

de “Ampliación Plantel Avícola Florida”, a continuación, se muestra tabla comparativa de

las fuentes:

28

**Tabla 8.** Comparación de fuentes - Zona de acopio residuos orgánicos.

|Fuente Proyecto - Zona de acopio de Bunker de aves muertas de<br>residuos orgánicos Avícola Reinero SpA (2019)<br>(proyecto original del cual<br>homologo proyecto aprobado)|Col2|Col3|
|---|---|---|
|**Descripción de fuente**|Bins cerrados en los cuales se<br>depositan aves muertas y se les<br>aplica<br>cal<br>viva<br>(CaO),<br>se<br>encuentran localizados dentro de<br>bodega la cual contiene residuos<br>orgánicos y residuos domésticos<br>dentro de contenedor.|Contenedor bunker en el cual se<br>depositan aves muertas a las<br>cuales se les agrega cal|
|**Especificaciones de modelación**|Los bins son cerrados, y el espacio<br>en el cual se encuentran dentro<br>las fuentes es una bodega. Para<br>efectos de la modelación, se<br>consideró toda la superficie de la<br>bodega emite, sobrestimando el<br>impacto.<br>Emisión continua.|Se estima que solo el bunker<br>emite y desde un punto.<br>Emisión continua.|
|**Tipo de fuente**|Difusa|Puntual|
|**Justificación uso**|Esta fuente de emisión homologada también usa cal para mitigar las<br>emisiones. Al emplear los antecedentes de la concentración y estimar<br>el FE con su superficie, se sobrestima la emisión al considerar toda la<br>superficie de la zona de acopio de residuos orgánicos como la que<br>emite.|Esta fuente de emisión homologada también usa cal para mitigar las<br>emisiones. Al emplear los antecedentes de la concentración y estimar<br>el FE con su superficie, se sobrestima la emisión al considerar toda la<br>superficie de la zona de acopio de residuos orgánicos como la que<br>emite.|

## 2.2. Factores de emisión - Escenario proyectado

En esta sección se presentan los factores de emisión (FE) de las fuentes de emisión de

olores, calculados a partir de la concentración de olor medida por GCA Ambiental, medida

por Salimax y por datos de referencia (ver anexo APENDICE 1 - Reporte de muestreo AQOM

Agricovial y APENDICE 2 - Informe de APL II Chilehuevos). Los datos del cálculo de la tasa

de emisión del secador se presentan más adelante.

Se incluye la medición a la compostera Kohshin con uso parcial de la capacidad total (120
m [3] ) sin y con aplicación del producto controlador de olores (Ver A.3) Medición secadora

Kohshin).

29

**Tabla 9** Concentración de olor secador Kohshin operando al 10%.

|Fuente CO sin Olex CO con Olex Porcentaje Fuente<br>(OU/m3) (OU/m3) reducción de la<br>concentración|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Extractor 1 secadora**<br>**Kohshin al 10% de**<br>**capacidad**|22,2|3.2|85,4%|Informe Salimax|
|**Extractor 2 secadora**<br>**Kohshin al 10% de**<br>**capacidad**|14,8|2.7|81,7%|81,7%|

El producto genera una reducción de la concentración de olor superior al 80%. Se estima la
concentración de olor operando al 100% de la capacidad del equipo (1.200 m [3] ) y con

aplicación del producto controlador de olores (Olex o similar), multiplicando los resultados
de la medición en los extractores (en la medición se operaba con 120 m [3] de GAP), por un

factor de 10 (asociado a su capacidad total).

Para efectos de la estimación de la TEO desde los ductos del PPVF, se estima que se

mantiene la TEO del escenario base.

**Tabla 10.** Factores de emisión de fuentes identificadas en el escenario proyectado.

|Fuente CO (OU/m3) FE (OU/(m2·s)) Tipo fuente Fuente|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**PPVF (medición en**<br>**extractor)**|177|--|Puntual|GCA Ambiental<br>2021|
|**PPVN sector jaulas**|148|11,3|Difusa|GCA Ambiental<br>2021|
|**PPVN sector cama**<br>**guano**|653|5,4|Difusa|GCA Ambiental<br>2021|
|**PCVF (medición en**<br>**extractor)**|241|--|Puntual|GCA Ambiental<br>2020|
|**Lombrifiltro**|129|1,08|Difusa|GCA Ambiental<br>2021|
|**Zona acopio residuos**<br>**orgánicos**|--|18,71|Difusa|Homologado a<br>la sumatoria de<br>la emisión de<br>fosa<br>de<br>aves<br>muertas fugas y<br>cargas<br>del<br>proyecto de DIA<br>“Ampliación<br>plantel<br>avícola<br>Florida” 2020|
|**Secadora Kohshin**<br>**extractor 1**|32,58|--|Puntual|Informe<br>de<br>Salimax<br>2022,<br>multiplicado por<br>un factor de 10,|
|**Secadora Kohshin**<br>**extractor 2**|27,2|--|Puntual|Puntual|

30

|Fuente CO (OU/m3) FE (OU/(m2·s)) Tipo fuente Fuente|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|||||asociado a la<br>capacidad total<br>de operación del<br>equipo.|
|**Secador Guano ave**<br>**de postura**|--|--|Puntual|Homologado del<br>secador<br>de<br>Avícola<br>Zona<br>Central<br>y <br>escalado<br>de<br>acuerdo<br>a <br>la<br>cantidad<br>de<br>guano a tratar.|

**Fuente** : Informe del GCA Ambiental 2020, Informe de GCA Ambiental, 2021, Informe de Salimax 2022,

Agrícola Sepulveda Palou, 2020 (DIA).

## 2.3. Nivel de Actividad

La estimación de emisiones de olor, tal como se mencionó previamente, se realiza durante

la fase de operación de la planta de Agricovial (escenario base y proyectado).

## 2.3.1. Fase de Operación - Escenario base

Para determinar la tasa de emisión de las fuentes en el escenario base, se emplea las

superficies de las fuentes medidas, número de extractores y operación durante el año.

**Tabla 11.** Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario base).

|Fuente Velocidad Altura Tempera Área N° Condiciones de<br>(m/s) emisión tura (°C) emisión extracto operación<br>(m) (m2) res|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVF 1 -**<br>**extractor**|1,7|2|26,1|1,3|36|Extractores -<br>Verano y Primavera: 8<br>horas día 100% y 16<br>horas día 25%.<br>Otoño e Invierno: 6 horas<br>día 100% y 18 horas día<br>25%.|
|**PPVF 2 -**<br>**extractor**|**PPVF 2 -**<br>**extractor**|**PPVF 2 -**<br>**extractor**|**PPVF 2 -**<br>**extractor**|1,5|30|30|
|**PPVF 3 -**<br>**extractor**|**PPVF 3 -**<br>**extractor**|**PPVF 3 -**<br>**extractor**|**PPVF 3 -**<br>**extractor**|1,3|40|40|
|**PPVF 4 -**<br>**extractor**|**PPVF 4 -**<br>**extractor**|**PPVF 4 -**<br>**extractor**|**PPVF 4 -**<br>**extractor**|1,3|36|36|
|**PPVF 5 -**<br>**extractor**|**PPVF 5 -**<br>**extractor**|**PPVF 5 -**<br>**extractor**|**PPVF 5 -**<br>**extractor**|1,3|52|52|
|**PPVF 6 -**<br>**extractor**|**PPVF 6 -**<br>**extractor**|**PPVF 6 -**<br>**extractor**|**PPVF 6 -**<br>**extractor**|1,4|42|42|
|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|1,4|42|42|
|**PPVN 1 sector**<br>**jaulas**|--|2|--|222|--|Cortinas -<br>Noviembre a marzo: 50%<br>abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs.|
|**PPVN 2 sector**<br>**jaulas**|--|--|--|222|--|--|
|**PPVN 3 sector**<br>**jaulas**|--|--|--|177|--|--|

31

|Fuente Velocidad Altura Tempera Área N° Condiciones de<br>(m/s) emisión tura (°C) emisión extracto operación<br>(m) (m2) res|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVN 4 sector**<br>**jaulas**|--|||228|--||
|**PPVN 1 sector**<br>**cama guano**|--|0|--|2.368|--|Cortinas -<br>Noviembre a marzo:<br>100% abiertas 24 horas.<br>Abril a Octubre: 50% 12<br>horas y 20% 12 hrs.|
|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|2.325,1|--|--|
|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|1.642,6|--|--|
|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|1.757,1|--|--|
|**PCVF 1 -**<br>**extractor**|1,9|2|27,1|1,4|14|Extractores -<br>operación 100% durante<br>el día y 40% durante<br>noche.|
|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|1,4|14|14|
|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|1,4|15|15|
|**Lombrifiltro**|--|1,5|--|1.156|--|Emisión continua.|
|**Zona acopio**<br>**residuos**<br>**orgánicos**|--|2|--|75|--|Emisión continua.|
|**Pilas de guano**<br>**fresco**|--|1,1|--|375,8|--|Octubre a junio 8 pilas<br>semanal y julio a<br>septiembre 15 pilas por<br>semana.|
|**Pilas de guano**<br>**activo**|--|1|--|341,6|--|Octubre a junio 12 pilas<br>semanal y julio a<br>septiembre 15 pilas por<br>semana. Volteo de pilas<br>4 horas al día.|
|**Pilas de guano**<br>**maduro**|--|0,9|--|273,3|--|Octubre a junio 12 pilas<br>semanal y julio a<br>septiembre 20 pilas por<br>semana.|

Todas las fuentes definidas emiten durante el año evaluado, variando cómo se comportan

las fuentes de emisión debido a condiciones operacionales, asociadas a los requerimientos

de las aves o al proceso.

 - Pabellones de Postura Ventilación Forzada y Pabellones de Crianza Ventilación

forzada: la variación de la operación está asociada al uso de extractores, indicando

el número de extractores que están operando. Este varía de acuerdo a estaciones

del año y horas para el caso de los PPVF y de horas en el día en los PCVF, acorde a
los requerimientos de aireación de las gallinas y/o pollitas. Poseen control

computarizado que es automatizado. Los pertenecientes a los pabellones de

postura, responden a sensores de temperatura.

32

 - Pabellón de Postura Ventilación Natural: la variación de la operación está asociada

a la apertura de las cortinas, indicando el porcentaje de apertura para la sección de

las jaulas y para la sección de la cama de guano, de acuerdo a los requerimientos de

aireación de las gallinas y al secado del GAP.

 - Pilas de guano fresco, activo y maduro: el número de pilas está asociada a las

estaciones del año, tiempo que requiere de secado en las diferentes etapas y venta

del producto.

Los requerimientos de ventilación tienen por objetivo el circular la corriente de aire para

entregar aire fresco, remover compuestos gaseosos, asegurar las condiciones climáticas

dentro del pabellón (temperatura y humedad). Este es un parámetro importante, pues

afecta en la salud de las aves y por tanto, en la capacidad de producción.

## 2.3.2. Fase de Operación - Escenario Proyectado

Para determinar la tasa de emisión de las fuentes en el escenario proyectado, se emplea las

superficies de las fuentes medidas, número de extractores y operación durante el año.

Cabe destacar, tal como se mencionó previamente, que, para efectos del cálculo de la TEO

de los PPVF con ducto, se emplearon los antecedentes disponibles en el escenario base de

CO por extractor.

**Tabla 12** . Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario proyectado).

|Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extractor operación<br>(m) (m2) es|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVF 1 -**<br>**ductos**|0,9|9|26,1|42,5|36|Extractores -<br>Verano y Primavera: 8<br>horas día 100% 16 horas<br>día 25%.<br>Otoño e Invierno: 6<br>horas día 100% y 18<br>horas día 25%.|
|**PPVF 2 -**<br>**ductos**|0,9|7,6|7,6|42,5|30|30|
|**PPVF 3 - ducto**|2,7|7,2|7,2|32,5|40|40|
|**PPVF 4 -**<br>**ductos**|0,9|7,5|7,5|42,5|36|36|
|**PPVF 5 -**<br>**ductos**|1,6|8|8|35|52|52|
|**PPVF 6 -**<br>**ductos**|1,2|9,5|9,5|42,5|42|42|
|**PPVF 7 -**<br>**ductos**|1,2|7,6|7,6|42,5|42|42|
|**PPVN 1 sector**<br>**jaulas**|--|2|--|222|--|Cortinas -<br>Noviembre a marzo: 50%<br>abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs.<br>|
|**PPVN 2 sector**<br>**jaulas**|**PPVN 2 sector**<br>**jaulas**|**PPVN 2 sector**<br>**jaulas**|**PPVN 2 sector**<br>**jaulas**|222|--|--|
|**PPVN 3 sector**<br>**jaulas**|**PPVN 3 sector**<br>**jaulas**|**PPVN 3 sector**<br>**jaulas**|**PPVN 3 sector**<br>**jaulas**|177|--|--|
|**PPVN 4 sector**<br>**jaulas**|**PPVN 4 sector**<br>**jaulas**|**PPVN 4 sector**<br>**jaulas**|**PPVN 4 sector**<br>**jaulas**|228|--|--|

33

|Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extractor operación<br>(m) (m2) es|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVN 1 sector**<br>**cama guano**|--|0|--|2.368|--|Cortinas -<br>Noviembre a marzo:<br>100% abiertas 24 horas.<br>Abril a Octubre: 50% 12<br>horas y 20% 12 hrs.<br>|
|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|2.325,1|--|--|
|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|1.642,6|--|--|
|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|1.757,1|--|--|
|**PCVF 1 -**<br>**extractor**|1,9|2|27,1|1,4|14|Extractores -<br>operación 100% durante<br>el día y 40% durante<br>noche.<br>|
|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|1,4|14|14|
|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|1,4|15|15|
|**Lombrifiltro**|--|1,5|--|1.156|--|Emisión continua.|
|**Zona acopio**<br>**residuos**<br>**orgánicos**|--|2|--|75|--|Emisión continua.|
|**Secadora**<br>**Kohshin -**<br>**Extractor 1**|8,2|2|13|0,4|--|Emisión continua.|
|**Secadora**<br>**Kohshin -**<br>**Extractor 2**|8,5|2|11|0,4|--|--|
|**Secador Guano**<br>**ave de postura**|1,61|9,4|15,1|48|--|Horas operación -<br>22 h enero, febrero,<br>noviembre y diciembre.<br>21 h marzo y octubre.<br>19 h abril y septiembre.<br>17 h mayo y agosto.<br>15 h junio y julio.|

## 2.4. Resultados Inventario de Emisión

A continuación, se presenta el inventario de emisión para el corte temporal analizado para

la emisión de olores en la fase de operación de la planta de Agricovial, para ambos

escenarios (base y proyectada).

## 2.4.1. Inventario de Emisión - Escenario base

Los resultados obtenidos de la estimación de la emisión atmosférica de olor para el

escenario base del proyecto, se presenta en la siguiente tabla. A continuación, se comenta

la división de las tasas:

 - **Tasa de emisión 1** : tasa de emisión cuando los PPVF y PCVF operan con el 100% de

los extractores, los PPVN sector jaula tienen apertura del 50%, los PPVN sector cama

guano están abiertos al 100%, las pilas de acopio de guano durante los meses de

octubre a junio en la ZAG y el resto de los equipos operando normalmente.

34

- **Tasa de emisión 2** : tasa de emisión cuando los PPVF tienen el 25% de los extractores

operando, los PCVF operan con el 40% de los extractores, los PPVN sector jaula

tienen apertura del 30%, los PPVN sector cama guano están abiertos al 50%, las pilas

de acopio de guano durante los meses de julio a septiembre en la ZAG y el resto de

los equipos operando normalmente.

- **Tasa de emisión 3** : tasa de emisión cuando los PPVF y PCVF operan con el 100% de

los extractores, los PPVN sector jaula tienen apertura del 50%, los PPVN sector cama

guano están abiertos al 100%, las pilas de acopio de guano durante los meses de

octubre a junio en la ZAG (durante el volteo de las pilas) y el resto de los equipos

operando normalmente.

- **Tasa de emisión 4** : tasa de emisión cuando los PPVF tienen el 25% de los extractores

operando, los PCVF operan con el 40% de los extractores, los PPVN sector jaula

tienen apertura del 30%, los PPVN sector cama guano están abiertos al 50%, las pilas

de acopio de guano durante los meses de julio a septiembre en la ZAG (durante el

volteo de las pilas) y el resto de los equipos operando normalmente.

**Tabla 13.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario base).

|Fuente|Tasa de emisión<br>1 (OU/s)|Tasa de emisión<br>2 (OU/s)|Tasa de emisión 3<br>(OU/s)|Tasa de emisión 4<br>(OU/s)|
|---|---|---|---|---|
|**PPVF 1**|13.722|3.431|13.722|3.431|
|**PPVF 2**|13.837|3.459|13.837|3.459|
|**PPVF 3**|15.247|3.812|15.247|3.812|
|**PPVF 4**|13.722|3.431|13.722|3.431|
|**PPVF 5**|19.821|4.955|19.821|4.955|
|**PPVF 6**|17.988|4.497|17.988|4.497|
|**PPVF 7**|17.988|4.497|17.988|4.497|
|**PPVN 1 sector jaulas**|2.519|1.134|2.519|1.134|
|**PPVN 2 sector jaulas**|2.519|1.134|2.519|1.134|
|**PPVN 3 sector jaulas**|2.008|904|2.008|904|
|**PPVN 4 sector jaulas**|2.587|1.164|2.587|1.164|
|**PPVN 1 sector cama**<br>**guano**|12.884|1.933|12.884|1.933|
|**PPVN 2 sector cama**<br>**guano**|12.651|1.933|12.651|1.933|
|**PPVN 3 sector cama**<br>**guano**|8.937|1.541|8.937|1.541|
|**PPVN 4 sector cama**<br>**guano**|9.561|1.985|9.561|1.985|
|**PCVF 1**|8.783|3.513|8.783|3.513|
|**PCVF 2**|8.783|3.513|8.783|3.513|
|**PCVF 3**|9.411|3.764|9.411|3.764|
|**Lombrifiltro**|1.243|1.243|1.243|1.243|
|**Zona acopio residuos**<br>**orgánicos**|369|369|369|369|
|**Pilas de guano fresco**|18.259|34.236|18.259|34.236|
|**Pilas de guano activo**|41.063|51.329|164.252|205.316|
|**Pilas de guano**<br>**maduro**|15.757|26.262|15.757|26.262|

35

|Fuente|Tasa de emisión<br>1 (OU/s)|Tasa de emisión<br>2 (OU/s)|Tasa de emisión 3<br>(OU/s)|Tasa de emisión 4<br>(OU/s)|
|---|---|---|---|---|
|**Total**|**269.660**|**164.037**|**392.848**|**318.026**|

**Tabla 14.** Porcentaje de aporte a la tasa de emisión de olor total de la planta de Agricovial - Escenario base.

|Fuente % aporte total % aporte total % aporte total % aporte total<br>TEO 1 TEO 2 TEO 3 TEO 4|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Pilas de guano activo**|15,2%|31,3%|41,8%|64,6%|
|**PPVF 5**|7,4%|3,0%|5,0%|1,6%|
|**Pilas de guano fresco**|6,8%|20,9%|4,6%|10,8%|
|**PPVF 6**|6,7%|2,7%|4,6%|1,4%|
|**PPVF 7**|6,7%|2,7%|4,6%|1,4%|
|**Pilas de guano maduro**|5,8%|16,0%|4,0%|8,3%|
|**PPVF 3**|5,7%|2,3%|3,9%|1,2%|
|**PPVF 2**|5,1%|2,1%|3,5%|1,1%|
|**PPVF 1**|5,1%|2,1%|3,5%|1,1%|
|**PPVF 4**|5,1%|2,1%|3,5%|1,1%|
|**PPVN 1 sector cama guano**|4,8%|1,2%|3,3%|0,6%|
|**PPVN 2 sector cama guano**|4,7%|1,2%|3,2%|0,6%|
|**PPVN 4 sector cama guano**|3,5%|1,2%|2,4%|0,6%|
|**PCVF 3**|3,5%|2,3%|2,4%|1,2%|
|**PPVN 3 sector cama guano**|3,3%|0,9%|2,3%|0,5%|
|**PCVF 1**|3,3%|2,1%|2,2%|1,1%|
|**PCVF 2**|3,3%|2,1%|2,2%|1,1%|
|**PPVN 4 sector jaulas**|1,0%|0,7%|0,7%|0,4%|
|**PPVN 1 sector jaulas**|0,9%|0,7%|0,6%|0,4%|
|**PPVN 2 sector jaulas**|0,9%|0,7%|0,6%|0,4%|
|**PPVN 3 sector jaulas**|0,7%|0,6%|0,5%|0,3%|
|**Lombrifiltro**|0,5%|0,8%|0,3%|0,4%|
|**Zona acopio residuos orgá-**<br>**nicos**|0,1%|0,2%|0,1%|0,1%|
|**Total**|**100%**|**100%**|**100%**|**100%**|

De acuerdo al aporte a la tasa de emisión de olor para TEO 1, TEO 2, TEO 3 y TEO 4, la mayor

fuente de emisión corresponde a las pilas de guano activo con un 15,2%, 31,3%, 41,8% y un

64,6% para las TEO respectivas.

Al analizar las fuentes de emisión como un conjunto, los pabellones de postura y crianza

generan el mayor aporte para la TEO 1 y TEO 3, con un 71,6 y 49,1 %, respectivamente.

## 2.4.2. Inventario de Emisión - Escenario proyectado

En esta sección se realiza un análisis de la razón de uso de antecedentes bibliográficos para

la estimación de la TEO en el secador de GAP, su cálculo, la TEO estimada con la aplicación

de Olex (o producto controlador de olores similar) al secador de GAP y la presentación del

inventario de emisiones de todas las fuentes del escenario proyectado.

36

**Tabla 15.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).

|Característica|Secador proyecto|Secador Avícola Zona<br>central|
|---|---|---|
|**Capacidad tratamiento guano**<br>**(asociado al número de aves)**|1.000.000|200.000|
|**Alimentación corriente aire**|Proveniente del medio<br>ambiente.<br>Se estima la TEO que se<br>remueve del GAP.|Proveniente<br>de<br>la<br>guanera<br>y <br>de<br>los<br>pabellones, por lo que<br>viene<br>con<br>la<br>carga<br>odorante<br>de<br>los<br>pabellones.|
|**Descripción de la fuente**|Humedad de entrada de<br>70%-80%<br>Humedad de salida de 15<br>- 25%.<br>Temperatura de entrada<br>de 25°C.<br>Temperatura de salida de<br>20 °C.|Humedad de entrada de<br>70%<br>Humedad de salida de<br>16%.<br>Temperatura de entrada<br>de 25°C.<br>Temperatura de salida de<br>18 °C.|
|**Tipo de emisión**|Continua|Continua|
|**Tipo de fuente**|Puntual|Puntual|
|**Justificación uso**|Las condiciones de operación son similares, pero con<br>grandes diferencias en cuanto a la cantidad de GAP de<br>ave a tratar. Dado los antecedentes de estas fuentes,<br>se emplea la concentración de olor para estimar la<br>tasa de emisión de la fuente puntual homologada.<br>Se realiza un balance de las TEO en el equipo secador<br>de avícola zona central y a partir de él, se estima la TEO<br>que se emite y se escala el resultado de acuerdo a la<br>razón entre la capacidad tratamiento guano (asociado<br>al número de aves) de la fuente del proyecto con el de<br>la fuente homologada.|Las condiciones de operación son similares, pero con<br>grandes diferencias en cuanto a la cantidad de GAP de<br>ave a tratar. Dado los antecedentes de estas fuentes,<br>se emplea la concentración de olor para estimar la<br>tasa de emisión de la fuente puntual homologada.<br>Se realiza un balance de las TEO en el equipo secador<br>de avícola zona central y a partir de él, se estima la TEO<br>que se emite y se escala el resultado de acuerdo a la<br>razón entre la capacidad tratamiento guano (asociado<br>al número de aves) de la fuente del proyecto con el de<br>la fuente homologada.|

A continuación, se presenta la ecuación empleada para estimar la TEO que emite el equipo

secador de GAP de Empresa Avícola Zona Central, para tratar el GAP de 200.000 aves. Se

empleo esta ecuación para determinar la capacidad del equipo. Cabe notar que el equipo

de Empresa Avícola Zona Central emplea la corriente de salida de los pabellones y otra

corriente contigua a la guanera, por lo que las corrientes de entrada poseen concentración

de olor. Durante la medición, se encontraban operando 8 ventiladores por lado.

C s ∙F s = C e1 ∙F e1 + C e2 ∙F e2 + TEO GAP

Donde:

C s = Concentración olor a la salida del secador (629 OU/m [3] ).
C e1 = Concentración de olor en ventilador lado guanera (354 OU/m [3] ).
C e2 = Concentración de olor en ventilador lado pabellones (292 OU/m [3] ).

37

F s = Flujo total de salida (77,3 m [3] /seg, área de 48 m [2] ).
F e1 = Flujo total entrada lado guanera (50,5 m [3] /seg, área de 12,3 m [2] ).
F e2 = Flujo total entrada lado pabellones (48 m [3] /seg, área de 12,3 m [2] ).

Las corrientes laterales del secador que alimentan al equipo poseen concentración de olor,

pues provienen de los pabellones y de la guanera. Para efectos del equipo que se plantea

para este proyecto, se considera alimentación del aire del medio ambiente. Dado lo

anterior, solo a partir de la TEO GAP es que se estima el impacto del secador.

La TEO GAP para tratar el GAP de 200.000 aves es de 16.711 OU/s. Para determinar la TEO
que emitirá el equipo al tratar el GAP de 1.000.000 aves se tomaron las siguientes

consideraciones:

 - Las corrientes de aire que se alimentan al secador por los ventiladores no provienen

de los pabellones ni de la guanera. Por ello, la concentración de olor que tienen estas

corrientes se estima en 0.

 - El incremento de la TEO es proporcional al incremento del GAP a tratar.

Dadas estas consideraciones, se estima que la TEO que emite el equipo para tratar el GAP
de 1.000.000 aves es de 83.553,5 OU/s. El secador de GAP tiene una lucarna, desde la cual

se dirige la emisión con un ducto, operando como fuente puntual.

Tal como se menciona previamente, dada la similitud estructural y operacional del secador

GAP con la secadora Kohshin, se estima que se puede implementar un sistema de aplicación

del producto controlador de olores (Olex o similar). En un escenario conservador y

considerando que la reducción de la concentración generada por el producto controlador

de olores en la secadora Kohshin es superior al 80%, se estima que se puede generar una

reducción de al menos un 50% de la concentración de olor del GAP tratado por el secador
GAP. Por lo tanto, la TEO emitida por el equipo es de 41.777 OU/s.

A continuación, se comenta la división de las tasas:

 - **Tasa de emisión 1** : tasa de emisión cuando los PPVF con ductos y PCVF operan con

el 100% de los extractores, los PPVN sector jaula tienen apertura del 50%, los PPVN

sector cama guano están abiertos al 100%, y el resto de los equipos operan

normalmente.

 - **Tasa de emisión 2** : tasa de emisión cuando los PPVF con ducto tienen el 25% de los

extractores operando, los PCVF operan con el 40% de los extractores, los PPVN

sector jaula tienen apertura del 30%, los PPVN sector cama guano están abiertos al

50% y el resto de los equipos operando normalmente.

**Tabla 16.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).

38

|Fuente|Tasa de emisión 1 (OU/s)|Tasa de emisión 2 (OU/s)|
|---|---|---|
|**PPVF 1**|13.722|3.431|
|**PPVF 2**|13.837|3.459|
|**PPVF 3**|15.247|3.812|
|**PPVF 4**|13.722|3.431|

|Fuente|Tasa de emisión 1 (OU/s)|Tasa de emisión 2 (OU/s)|
|---|---|---|
|**PPVF 5**|19.821|4.955|
|**PPVF 6**|17.988|4.497|
|**PPVF 7**|17.988|4.497|
|**PPVN 1 sector jaulas**|2.519|1.134|
|**PPVN 2 sector jaulas**|2.519|1.134|
|**PPVN 3 sector jaulas**|2.008|904|
|**PPVN 4 sector jaulas**|2.587|1.164|
|**PPVN 1 sector cama guano**|12.884|1.933|
|**PPVN 2 sector cama guano**|12.651|1.933|
|**PPVN 3 sector cama guano**|8.937|1.541|
|**PPVN 4 sector cama guano**|9.561|1.985|
|**PCVF 1**|8.783|3.513|
|**PCVF 2**|8.783|3.513|
|**PCVF 3**|9.411|3.764|
|**Lombrifiltro**|1.243|1243|
|**Zona acopio residuos orgánicos**|369|369|
|**Secadora Kohshin - Extractor 1**|118|118|
|**Secadora Kohshin - Extractor 2**|102|102|
|**Secador de guano de ave de**<br>**postura**|41.777|41.777|
|**Total**|**236.577**|**94.209**|

**Tabla 17.** Porcentaje de aporte a la tasa de emisión de olor total de la planta de Agricovial - Escenario

proyectado.

|Fuente % aporte total TEO 1 % aporte total TEO 2|Col2|Col3|
|---|---|---|
|**Secador de guano de ave de postura**|17,7%|44,3%|
|**PPVF 5**|8,4%|5,3%|
|**PPVF 6**|7,6%|4,8%|
|**PPVF 7**|7,6%|4,8%|
|**PPVF 3**|6,4%|4,0%|
|**PPVF 2**|5,8%|3,7%|
|**PPVF 1**|5,8%|3,6%|
|**PPVF 4**|5,8%|3,6%|
|**PPVN 1 sector cama guano**|5,4%|2,1%|
|**PPVN 2 sector cama guano**|5,3%|2,1%|
|**PPVN 4 sector cama guano**|4,0%|2,1%|
|**PCVF 3**|4,0%|4,0%|
|**PPVN 3 sector cama guano**|3,8%|1,6%|
|**PCVF 1**|3,7%|3,7%|
|**PCVF 2**|3,7%|3,7%|
|**PPVN 4 sector jaulas**|1,1%|1,2%|
|**PPVN 1 sector jaulas**|1,1%|1,2%|
|**PPVN 2 sector jaulas**|1,1%|1,2%|
|**PPVN 3 sector jaulas**|0,8%|1,0%|
|**Lombrifiltro**|0,5%|1,3%|
|**Zona acopio residuos orgánicos**|0,2%|0,4%|
|**Secadora Kohshin - Extractor 1**|0,05%|0,1%|
|**Secadora Kohshin - Extractor 2**|0,04%|0,1%|
|**Total**|**100%**|**100%**|

39

De acuerdo al aporte a la tasa de emisión de olor para TEO 1 y TEO 2, la mayor fuente de

emisión es el secador de GAP con un 17,7% y un 44,3% respectivamente.

Al analizar las fuentes de emisión como un conjunto, los pabellones de postura y crianza

generan el mayor aporte para la TEO 1 y TEO 2, con un 81,6 y un 53,7%, respectivamente.

## 2.5. Tipología de Proyecto

El proyecto “Mejoramiento Tecnológico Operaciones Agricovial” dada su naturaleza,

tipología y acorde al artículo 3 del RSEIA, corresponde a: “ _Agroindustrias, mataderos,_

_planteles y establos de crianza, lechería y engorda de animales, de dimensiones_

_industriales_ ”, específicamente a “ _Planteles y establos de crianza, engorda, postura y/o_

_reproducción de animales avícolas con capacidad para alojar diariamente una cantidad_

_igual o superior a..._ **”**

Considerando lo anterior, en relación con el literal g.1, cabe señalar que las partes, obras y

acciones del proyecto cuya DIA se somete a evaluación se encuentran listadas en el artículo

3° de Reglamento del SEIA, específicamente en los literales L.4.2) y O.8). En el caso del

primer literal, se debe a que Agricovial cuenta con una cantidad superior a 60 mil gallinas.

Mientras que, con respecto al segundo literal, el ingreso se debe a la generación de más de

30 t/día de guano, clasificado como residuo industrial sólido, producto del funcionamiento

de los pabellones.

40

# 3. Análisis Meteorológico de Datos Observados y Modelados

El estudio del impacto de olor considera la base de un año de datos meteorológicos,

correspondientes al periodo de 01-01-2020 al 31-12-2020, obtenidos de la modelación

realizada por el modelo de pronóstico WRF, contrastado frente a la estación meteorológica

El Milagro. La ubicación y localización de la estación se presenta en la Figura 12.

**Tabla 18.** Ubicación de estación meteorológica superficial El Milagro.

|Estación|Altura<br>m.s.n.m<br>(m)|Coordenadas UTM|Col4|
|---|---|---|---|
|**Estación**|**Altura**<br>**m.s.n.m**<br>**(m)**|**Datum WGS 84 Huso 19 H**|**Datum WGS 84 Huso 19 H**|
|**Estación**|**Altura**<br>**m.s.n.m**<br>**(m)**|**Este (m)**|**Norte (m)**|
|**Estación El Milagro**|460|336.580,5|6.263.672,3|

**Fuente:** Dirección General de Aeronáutica Civil.

**Figura 12.** Localización de la estación meteorológica El Milagro.

41

## 3.1. Estación El Milagro 3.1.1. Viento

El análisis del viento se divide en dos secciones, que corresponden a la velocidad del viento

(magnitud) y su dirección. En la presente sección se analiza las rosas de viento y la

frecuencia de las velocidades para los datos observados y los obtenidos por el modelo WRF.

En las subsecciones siguientes, se presenta el análisis del ciclo diario de la velocidad del

viento, series de tiempo de la velocidad y dirección del viento y los ciclos estacionales de la

velocidad y dirección del viento.

Para el periodo 2020, los datos de la estación El Milagro, presentan una velocidad promedio
del viento de 1,98 (m/s), con una frecuencia de 12,28% de vientos calmos (velocidad inferior
a 0,5 m/s).

**Figura 13.** Rosa de viento año 2020: datos observados en estación El Milagro (izquierda) y modelados WRF

(derecha).

A partir de la rosa de viento de los datos observados, presentada en la **Figura 13** durante el

periodo 2020 se puede observar una predominancia de vientos provenientes del este, con
velocidades que fluctúan entre 0 hasta los 3,6 m/s. Los vientos de mayor intensidad, entre
3,6 a 11,1 m/s, provienen del oeste.

Para el periodo 2020, los datos modelados WRF para la estación El Milagro ( **Figura 13** ),
presentan una velocidad promedio del viento de 2,37 m/s, con una frecuencia de un 4,97%

de vientos calmos. Por su parte, la rosa de viento de los datos modelados muestra una

predominancia de vientos provenientes del nor noreste, con velocidades entre los 0,5 y 3,6
m/s, y otra tendencia proveniente del oeste, con vientos que alcanzan los 8,8 m/s.

Para visualizar las diferencias horarias entre los datos observados y modelados en la

estación meteorológica El Milagro, se presentan las rosas de viento en horario 08:00 a 18:00

y 18:00 a 08:00.

42

**Figura 14.** Rosa de viento año 2020: Horario 08:00 a 18:00. Datos observados en estación El Milagro

(izquierda) y modelados WRF (derecha).

**Figura 15.** Rosa de viento año 2020: Horario 18:00 a 08:00. Datos observados en estación El Milagro

(izquierda) y modelados WRF (derecha).

De los datos observados presentados en la **Figura 14** y **Figura 15** se aprecia que en ambos

horarios gran parte de los vientos provienen del este. Sin embargo, se observan diferencias

en la distribución de frecuencias y en las intensidades entre los intervalos horarios

seleccionados. Durante el horario de día (08:00 a 18:00) hay una mayor proporción de

vientos provenientes del sur, en relación con los vientos observados durante el horario de

noche (18:00 a 08:00).

De los datos modelados WRF presentados en la **Figura 14** y **Figura 15** se aprecia que, en el

horario de día (08:00 a 18:00) predominan vientos del nor noreste, con velocidades entre
los 0,5 hasta 5,7 m/s. Destacan también vientos provenientes del oste, que alcanzan hasta
8,8 m/s. En el horario de noche (18:00 a 08:00) predominan vientos provenientes del

43

noreste, con mismas intensidades del horario día, y otros provenientes del noroeste, en los
que aumentan las velocidades entre los 5,7 y 8,8 m/s.

**Figura 16.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos observados en

estación El Milagro).

**Figura 17.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos modelados en

estación El Milagro).

La distribución de la frecuencia de la velocidad del viento de los datos observados, que se

presentan en la **Figura 16** indica que la mayor frecuencia de la velocidad del viento se
produce en el rango 0,5 - 2,1 (m/s) con un 51,35%. Por lo tanto, de acuerdo con la escala

de Beaufort de la fuerza de los vientos, el 51,35% de las velocidades del viento se clasifican

entre ventolina y brisa muy ligera.

La distribución de la frecuencia de los datos modelados WRF, que se presentan en la **Figura**
**17.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos

modelados en estación El Milagro)., indica que la mayor frecuencia de la velocidad del
viento se produce en el rango 0,5 - 2,1 (m/s) con un 47,22%. De acuerdo a la Escala de

44

Beaufort de la fuerza de los vientos, el 47,22% de las velocidades del viento se clasifican

entre ventolina y brisa muy ligera.

### 3.1.1.1. Velocidad del Viento

En el ciclo diario de la velocidad del viento observado ( **Figura 18** ) se puede apreciar que las

menores velocidades transcurren entre las 00:00 a 12:00 horas y las mayores velocidades

entre las 19:00 a 21:00 horas. Por su parte, en el ciclo diario de la velocidad del viento

modelado WRF ( **Figura 19** ), las menores velocidades se encuentran entre las 23:00 a 12:00

horas y las mayores velocidades entre las 19:00 a 20:00 horas.

**Figura 18.** Ciclo diario de la velocidad del viento observada en estación El Milagro (m/s) Hora en (UTC).

**Figura 19.** Ciclo diario de la velocidad del viento modelada en estación El Milagro (m/s) Hora en (UTC).

Tal como en los ciclos diarios, en las series de tiempo de la velocidad del viento observada

( **Figura 20** ) en comparación con las series de tiempo de la velocidad del viento modelada

WRF ( **Figura 21** ), se puede apreciar que existe una diferencia en la amplitud de los datos.

Particularmente, las series modeladas WRF presentan una menor amplitud de los datos.

45

**Figura 20.** Serie de tiempo de la velocidad del viento observada en estación El Milagro (m/s) Hora en (UTC).

**Figura 21.** Serie de tiempo de la velocidad del viento modelada en estación El Milagro (m/s) Hora en (UTC).

En los ciclos estacionales presentados, se pueden apreciar distribuciones mensuales

horarias similares entre los datos observados ( **Figura 22** ) y los modelados ( **Figura 23** ), pero

con una menor amplitud para el caso modelado. Particularmente, el caso modelado

presenta mayores velocidades para todos los meses, entre las 00.00 a 11:00 horas, en

relación a los datos observados.

46

**Figura 22** . Ciclo estacional de la velocidad del viento observada en estación El Milagro (m/s) Hora en (UTC).

**Figura 23.** Ciclo estacional de la velocidad del viento modelada en estación El Milagro (m/s) Hora en (UTC).

### 3.1.1.2. Dirección del viento

En el ciclo diario de la dirección del viento observada ( **Figura 24** ) se puede apreciar un ajuste

que se direcciona desde el noreste en horas de la mañana (03:00 a 10:00) y que cambia de

dirección al suroeste desde las 15:00 hasta las 22:00 horas.

El ciclo diario de la dirección del viento modelada para la estación El Milagro ( **Figura 25** )

presenta una mayor amplitud de datos, llegando casi hasta los 360°. Se puede apreciar un

ajuste que se direcciona desde el noreste en horas de la mañana (04:00 a 12:00) y que

cambia de dirección al suroeste en horas de noche (14:00 a 22:00).

47

**Figura 24.** Ciclo diario de la dirección del viento observada en estación El Milagro (°) Hora en (UTC).

**Figura 25.** Ciclo diario de la dirección del viento modelada en estación El Milagro (°) Hora en (UTC).

Tal como se puede observar en los ciclos diarios, en las series de tiempo observadas y

modeladas de la estación El Milagro ( **Figura 26** y **Figura 27** ) se puede apreciar una mayor

amplitud de variación de la dirección del viento de las series modeladas.

**Figura 26.** Serie de tiempo de la dirección del viento observada en estación El Milagro (°) Hora en (UTC).

48

**Figura 27.** Serie de tiempo de la dirección del viento modelada en estación El Milagro (°) Hora en (UTC).

En los ciclos estacionales presentados se puede apreciar una diferencia entre las

distribuciones y amplitud de los datos mensuales horarios observados **Figura 28** y los

modelados **Figura 29** . Esto indica que el modelo posiblemente tenga un sesgo que produzca

una sobreestimación de la dirección del viento dentro del dominio de estudio.

**Figura 28.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°) (Hora en UTC).

49

**Figura 29.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°) (Hora en UTC).

## 3.1.2. Temperatura

El análisis de la temperatura a nivel superficial (2 metros), presenta los ciclos diarios, series

de tiempo y los ciclos estacionales de los datos observados y los obtenidos por el modelo

WRF.

Los datos de temperatura observados para la estación El Milagro presentan una amplitud

entre los -1,66°C y 34,62°C y una temperatura promedio de 14,72°C ( **Figura 30** ). Las

menores temperaturas del ciclo diario se registran en el horario 08:00 a 10:00 y las mayores

temperaturas se registran en el horario de las 18:00 a 20:00.

Los datos de temperatura modelados WRF para la estación El Milagro presentan una

amplitud entre los 4,48°C y 27,43°C y una temperatura promedio de 14,73°C ( **Figura 31** ). El

ciclo diario de temperatura modelada posee una distribución similar a la observada en la

estación de El Milagro, registrando menores temperaturas en el horario 08:00 a 12:00 y

mayores en el horario 18:00 a 20:00.

**Figura 30.** Ciclo diario de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

50

**Figura 31.** Ciclo diario de la temperatura modelada en la estación El Milagro (°C) Hora (UTC).

En la serie de tiempo de la temperatura observada ( **Figura 32** ), se puede apreciar una mayor

amplitud en los valores que en la serie de tiempo de la temperatura modelada ( **Figura 33** ).

La serie de tiempo modelada WRF logra capturar los patrones de estacionalidad de la

temperatura anual, pero la amplitud de los valores de la serie modelada es más acotada

que el de la serie observada.

**Figura 32.** Serie de tiempo de temperatura observada en la estación El Milagro (°C) Hora (UTC).

**Figura 33.** Serie de tiempo de temperatura modelada en la estación El Milagro (°C) Hora (UTC).

51

En los ciclos estacionales presentados ( **Figura 34** y **Figura 35** ) se puede visualizar que, para

horarios mensuales similares, los datos modelados presentan temperaturas menores que

los datos observados, por lo que posiblemente el modelo posee un sesgo que subestima los

valores de temperatura en el dominio de estudio.

**Figura 34.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

**Figura 35.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

52

## 3.1.3. Humedad Relativa

El análisis de la humedad relativa presenta los ciclos diarios, series de tiempo y ciclos

estacionales de los datos observados y los obtenidos por el modelo WRF.

Los datos observados para la estación El Milagro presentan una amplitud de valores de

humedad relativa de 13,77% y 99,59% y una humedad relativa promedio de 68,48% ( **Figura**

**36** ). De acuerdo con los datos observados, los máximos horarios de humedad se generan

en horarios de mañana (07:00 a 10:00) y los mínimos se produce en horario de tarde (18:00

a 19:00).

Los datos modelados WRF para la estación El Milagro presentan una amplitud de valores de

humedad relativa de 31,04% a 100% y una humedad relativa promedio de 80,09% ( **Figura**

**37** ). Los máximos horarios de humedad se producen en horario de mañana (02:00 a 11:00)

y los mínimos durante la tarde (17:00 a 18:00).

**Figura 36.** Ciclo diario de la humedad relativa observada en la estación El Milagro (%) Hora (UTC).

**Figura 37.** Ciclo diario de la humedad relativa modelada en la estación El Milagro (%) Hora (UTC).

53

En la serie de tiempo de la humedad relativa observada ( **Figura 38** ) se puede apreciar una

mayor amplitud de los datos que en la serie de tiempo de la humedad relativa modelada

( **Figura 39** ).

**Figura 38.** Serie de tiempo de la humedad relativa observada en la estación El Milagro (%) Hora (UTC).

**Figura 39.** Serie de tiempo de la humedad relativa modelada en la estación El Milagro (%) Hora (UTC).

En los ciclos estacionales presentados ( **Figura 40** y **Figura 41** ), se puede visualizar que, para

horarios mensuales similares, los datos modelados presentan humedades relativas mayores

que los datos observados, por lo que posiblemente el modelo posee un sesgo que

sobreestima la humedad relativa para el dominio de estudio.

54

**Figura 40.** Ciclo estacional de la humedad relativa observada en la estación El Milagro (%) Horas (UTC).

**Figura 41.** Ciclo estacional de la humedad relativa modelada en la estación El Milagro (%) Horas (UTC).

55

## 3.2 Análisis de la incertidumbre

El análisis de la incertidumbre permite determinar la bondad de la modelación con respecto

a los datos observados. Para el presente informe, se determinaron los parámetros

estadísticos entre los datos observados en las estaciones identificadas dentro del dominio

y los datos modelados WRF.

**Tabla 19.** Criterios estadísticos de aceptación de la predicción proporcionada por un modelo meteorológico.

|Variable Meteorológica|Parámetros Estadísticos|Criterio de Validez|
|---|---|---|
|**Velocidad Viento (10 m)**|RMSE|≤ 2 m/s|
|**Velocidad Viento (10 m)**|BIAS|≤ ±0,5 m/s|
|**Dirección Viento (°)**|Error Absoluto|≤ 30°|
|**Dirección Viento (°)**|BIAS|≤ ±10°|
|**Temperatura Superficial (2 m)**|Error Absoluto|≤ 2K|
|**Temperatura Superficial (2 m)**|BIAS|≤ ±0,5K|

**Fuente** : Emery, C. _et al_ . 2017.

**Tabla 20.** Criterios de tolerancia de diferencia absoluta de variables modeladas.

|Variable Meteorológica|Criterio|
|---|---|
|**Velocidad del viento**|2,57 m/s|
|**Dirección del viento**|20°|
|**Temperatura de rocío**|1°C en superficie.|
|**Temperatura**|1°C en superficie.|

**Fuente** : Yañez-Morroni, G. _et al_ . 2018.

Donde,

J

I

BIAS= [1]

i −O
j

i )

IJ [∑∑(P] [j]

j=1

i=1

J

I

ErrorAbsoluto= [1]

i −O
j

i |

i

IJ [∑∑|P] [j]

j=1

i=1

IJ

RMSE= √ [1]

J

I

2

i

IJ [∑∑(P] [j]

i )

i −O i
j

j=1

i=1

Donde:

j : tiempo.

i : lugar de observación.

J : número total de observaciones temporales.

I : número total de lugares de observación.

56

O : variable observada/medida.

P : variable predicha por el modelo WRF.

**Tabla 21.** Valores de los parámetros de la predicción proporcionada por el modelo para la Estación El

Milagro.

|Variable Meteorológica|Parámetros<br>Estadísticos|Valor determinado<br>Estación El Milagro|
|---|---|---|
|**Velocidad Viento (10 m)**|BIAS|0,39 m/s|
|**Velocidad Viento (10 m)**|Error absoluto medio|1,05 m/s|
|**Velocidad Viento (10 m)**|RMSE|1,41 m/s|
|**Dirección Viento (°)**|BIAS|6,086°|
|**Dirección Viento (°)**|Error absoluto<br>medio|57,69°|
|**Dirección Viento (°)**|RMSE|83,05°|
|**Temperatura Superficial (2 m)**|BIAS|0,12 K|
|**Temperatura Superficial (2 m)**|Error absoluto<br>medio|3,26 K|
|**Temperatura Superficial (2 m)**|RMSE|3,9 K|
|**Humedad**|BIAS|11,56 %|
|**Humedad**|Error absoluto<br>medio|17,14 %|
|**Humedad**|RMSE|21,41 %|

## 3.2.1 Incertidumbre en Estación El Milagro

Considerando los criterios estadísticos de aceptación del modelo meteorológico

presentados ( **Tabla 19** ) y los valores de los parámetros de la predicción proporcionada por

el modelo ( **Tabla 21** ) para la estación El Milagro, se observa que según BIAS, el modelo para

la velocidad del viento no posee sesgo. Por otra parte, la raíz del error cuadrático medio

(RMSE) indica que el criterio de precisión se encuentra dentro de los criterios de validez

recomendados.

A partir del BIAS, se observa que el modelo para la dirección del viento y el modelo para la

temperatura no poseen sesgo. Sin embargo, de acuerdo con la información otorgada por el

Error absoluto medio, el criterio de precisión no cumple con el criterio de validez

recomendado en ambos casos.

Finalmente, en base al criterio BIAS y al análisis de los datos, se observa que el modelo para

la humedad relativa posee un sesgo que sobreestima el valor de esta variable.

57

# 4. Estimación del Impacto de las Emisiones de Olor

Para la estimación del impacto de las emisiones de olor, se presenta la localización de los

receptores discretos que se encuentran cercanos al sector de postura, sector de crianza y

sector de acopio de GAP y los mapas de las isolíneas de concentración correspondientes,

para permitir el análisis de los posibles impactos que pueden generarse en las cercanías.

## 4.1. Receptores

Las instalaciones de Agricovial están divididas en tres sectores en el escenario base,

correspondientes con sector postura, sector crianza y sector acopio de GAP, y en dos

sectores en el escenario proyectado, pues el acopio y tratamiento del GAP se realizará en

el sector de postura.

Para el presente estudio, se identificaron 56 receptores discretos, con distancias desde el

límite de las instalaciones de 84 a 1.927 m en el escenario base y de 84 a 2.852 m en el

escenario proyectado en el cual ya no existe el sector de acopio de GAP en el sector de Lo

Herrera, al encontrarse el acopio y tratamiento en el sector de postura en el Romeral.

**Figura 42.** Localización de receptores discretos del proyecto en el sector Romeral.

58

**Figura 43.** Localización de receptores discretos del proyecto en el sector Lo Herrera.

**Tabla 22.** Receptores discretos.

|Identificador|Altura<br>m.s.n.m<br>(m)|Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario base (m)|Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario<br>proyectado (m)|Localización<br>según Sector|Coordenadas UTM<br>Datum WGS 84 Huso 19<br>UTMx (m) UTMy (m)|Col7|
|---|---|---|---|---|---|---|
|**Re1**|492|1.151|1.151|Romeral|334.978|6.271.787,1|
|**Re2**|497|810|810|Romeral|335.619,3|6.272.204|
|**Re3**|500|839|839|Romeral|335.707,6|6.272.250,2|
|**Re4**|486|880|880|Romeral|335.950,8|6.272.217,9|
|**Re5**|501|703|703|Romeral|336.047,3|6.272.344,2|
|**Re6**|501|1.109|1.109|Romeral|335.454,1|6.272.542,3|
|**Re7**|499|833|833|Romeral|335.294,1|6.273.225,8|
|**Re8**|503|1.521|1.521|Romeral|335.340|6.273.413,3|
|**Re9**|501|793|793|Romeral|335.374,4|6.273.622,5|
|**Re10**|490|873|873|Lo Herrera|335.781,1|6.273.544,1|
|**Re11**|494|1.789|2.698|Lo Herrera|334.689,8|6.275.195,7|
|**Re12**|492|1.927|2.852|Lo Herrera|335.284|6.274.935,1|

59

|Identificador|Altura<br>m.s.n.m<br>(m)|Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario base (m)|Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario<br>proyectado (m)|Localización<br>según Sector|Coordenadas UTM<br>Datum WGS 84 Huso 19<br>UTMx (m) UTMy (m)|Col7|
|---|---|---|---|---|---|---|
|**Re13**|492|1.847|2.779|Lo Herrera|335.960,5|6.275.214,6|
|**Re14**|495|1.688|2.597|Lo Herrera|335.992|6.274.669,3|
|**Re15**|501|1.144|1.787|Lo Herrera|336.155,4|6.275.531,8|
|**Re16**|486|977|2.043|Lo Herrera|337.640,9|6.274.367,3|
|**Re17**|492|974|974|Lo Herrera|338.158,1|6.274.309,9|
|**Re18**|495|966|966|Lo Herrera|338.059,4|6.273.690,6|
|**Re19**|489|857|863|Lo Herrera|338.063|6.273.609,8|
|**Re20**|495|369|369|Lo Herrera|338.046,6|6.273.469,5|
|**Re21**|497|300|982|Lo Herrera|338.028,4|6.273.329,1|
|**Re22**|521|1.642|1.642|Lo Herrera|337.985,8|6.273.175,7|
|**Re23**|520|1.369|1.369|Lo Herrera|337.808,8|6.273.155,7|
|**Re24**|520|1.367|1.367|Lo Herrera|337.587,5|6.273.158,4|
|**Re25**|519|1.351|1.351|Lo Herrera|337.503,8|6.273.078,1|
|**Re26**|518|1.342|1.342|Lo Herrera|337.470,8|6.272.923,4|
|**Re27**|516|1.320|1.320|Lo Herrera|337.459,8|6.272.781,7|
|**Re28**|514|1.130|1.130|Lo Herrera|337.590,7|6.272.778,2|
|**Re29**|512|915|915|Lo Herrera|337.733,4|6.272.775,6|
|**Re30**|511|840|840|Lo Herrera|337.982,2|6.272.766,9|
|**Re31**|510|838|838|Lo Herrera|338.199,7|6.272.751,3|
|**Re32**|508|885|885|Lo Herrera|338.209|6.272.569,1|
|**Re33**|510|1.014|1.014|Lo Herrera|338.036,3|6.272.556,5|
|**Re34**|511|1.135|1.135|Lo Herrera|337.888,3|6.272.559,6|
|**Re35**|514|1.381|1.381|Lo Herrera|337.785,2|6.272.518,2|
|**Re36**|517|1.581|1.581|Lo Herrera|337.764,6|6.272.391,5|
|**Re37**|516|1.657|1.657|Lo Herrera|337.661,3|6.272.294,2|
|**Re38**|516|1.498|1.498|Lo Herrera|337.442,4|6.272.302,5|
|**Re39**|513|1.364|1.364|Lo Herrera|337.242,1|6.272.373,7|
|**Re40**|512|1.288|1.288|Lo Herrera|337.143,4|6.272.321,9|
|**Re41**|511|1.347|1.347|Lo Herrera|336.942,2|6.272.343,7|
|**Re42**|509|1.313|1.313|Lo Herrera|336.956,4|6.273.232,5|
|**Re43**|508|1.155|1.155|Lo Herrera|337.088,5|6.273.087,3|
|**Re44**|506|995|995|Lo Herrera|336.967,7|6.273.808,2|
|**Re45**|504|875|875|Lo Herrera|336.276|6.269.491,9|
|**Re46**|508|428|428|Lo Herrera|336.184|6.269.403,6|
|**Re47**|508|350|350|Lo Herrera|336.567,2|6.269.591,9|
|**Re48**|478|326|326|Romeral|335.780,2|6.269.235,9|
|**Re49**|477|453|453|Romeral|335.569,3|6.269.647,3|

60

|Identificador|Altura<br>m.s.n.m<br>(m)|Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario base (m)|Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario<br>proyectado (m)|Localización<br>según Sector|Coordenadas UTM<br>Datum WGS 84 Huso 19<br>UTMx (m) UTMy (m)|Col7|
|---|---|---|---|---|---|---|
|**Re50**|475|84|84|Romeral|335.577,7|6.269.713,7|
|**Re51**|485|839|839|Romeral|335.699,4|6.269.805,1|
|**Re52**|485|750|750|Romeral|335.712,2|6.269.885,1|
|**Re53**|485|726|726|Romeral|335.754,8|6.268.937,1|
|**Re54**|484|588|588|Romeral|337.253|6.268.577|
|**Re55**|497|569|569|Romeral|337.653,9|6.268.897,7|
|**Re56**|471|1.090|1.090|Romeral|337.727,9|6.269.329,8|

De acuerdo al PRMS (Ministerio Bienes raíces, 2022), los receptores 1 al 3, 5 al 22, 28 al 34,
42 al 51 y 56 se encuentran localizados en la tipología de suelo de Áreas de interés

agropecuario exclusivo (áreas con uso agropecuario, cuyo suelo y capacidad de uso agrícola

debe ser preservado) y los receptores 52 al 55 se encuentran localizados en áreas de

preservación ecológica (áreas mantenidas en estado natural, para asegurar y contribuir al

equilibrio y calidad del medio ambiente), tipologías pertenecientes al uso de suelo rural. El

76,8% de los receptores se encuentran localizados dentro del uso de suelo rural.

Por su parte, los receptores 23 al 27 y 35 a 41 tienen una tipología de uso de suelo para

zona habitacional mixta (permite uso para residencial, equipamiento, espacio público y

áreas verdes) y el receptor 4 se encuentra dentro del parque río Maipo. El 23,2% de los

receptores se encuentran localizados dentro del uso de suelo urbano.

A continuación, se presenta la descripción de los receptores discretos (Tabla 23), un mapa

con la geolocalización de los receptores discretos en el sector Romeral (Figura 44) y un mapa

con la geolocalización de los receptores discretos en el sector Lo Herrera (Figura 45).

**Tabla 23.** Descripción receptores discretos.

61

|Identificador|Descripción|Tipología uso suelo|
|---|---|---|
|Receptor 1|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 2|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 3|Residencia, localizada en Las brisas|Áreas de interés agropecuario exclusivo.|
|Receptor 4|Residencia localizada dentro del<br>Parque río Maipo|Parque río Maipo|
|Receptor 5|Residencia, localizada en el Camino<br>Romeral|Áreas de interés agropecuario exclusivo.|
|Receptor 6|Bodega|Áreas de interés agropecuario exclusivo.|
|Receptor 7|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 8|Residencia localizada en El Barrancón|Áreas de interés agropecuario exclusivo.|

|Identificador|Descripción|Tipología uso suelo|
|---|---|---|
|Receptor 9|Residencia localizada en las brisas|Áreas de interés agropecuario exclusivo.|
|Receptor 10|Residencia localizada en Eliodoro<br>Yañez|Áreas de interés agropecuario exclusivo.|
|Receptor 11|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 12|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 13|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 14|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 15|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 16|Residencia|Áreas de interés agropecuario exclusivo.|
|Receptor 17|Residencia localizada en El Rodeo|Áreas de interés agropecuario exclusivo.|
|Receptor 18|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 19|Residencia localizada en Eliodoro<br>Yañez|Áreas de interés agropecuario exclusivo.|
|Receptor 20|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 21|Residencia<br>localizada<br>en<br>nueva<br>independencia|Áreas de interés agropecuario exclusivo.|
|Receptor 22|Residencia localizada en Vivero|Áreas de interés agropecuario exclusivo.|
|Receptor 23|Residencia|Zona habitacional mixta|
|Receptor 24|Residencia|Zona habitacional mixta|
|Receptor 25|Residencia Localizada en Volcán Olca|Zona habitacional mixta|
|Receptor 26|Residencia Localizada en Volcán Olca|Zona habitacional mixta|
|Receptor 27|Residencia localizada en Eliodoro<br>Yañez|Zona habitacional mixta|
|Receptor 28|Residencia localizada en Eliodoro<br>Yañez|Áreas de interés agropecuario exclusivo.|
|Receptor 29|Residencia localizada en Eliodoro<br>Yañez|Áreas de interés agropecuario exclusivo.|
|Receptor 30|Residencia<br>localizada<br>en<br>C.<br>Andrómeda|Áreas de interés agropecuario exclusivo.|
|Receptor 31|Residencia<br>localizada<br>en<br>C.<br>Andrómeda|Áreas de interés agropecuario exclusivo.|
|Receptor 32|Aquavita localizada en C. Andrómeda|Áreas de interés agropecuario exclusivo.|

62

|Identificador|Descripción|Tipología uso suelo|
|---|---|---|
|Receptor 33|Reseidencia<br>localizada<br>en<br>C.<br>Andrómeda|Áreas de interés agropecuario exclusivo.|
|Receptor 34|Restaurant Familia Astudillo Lemus<br>localizado en C. Andrómeda|Áreas de interés agropecuario exclusivo.|
|Receptor 35|Residencia|Zona habitacional mixta|
|Receptor 36|Residencia|Zona habitacional mixta|
|Receptor 37|Residencia localizada en Antu Newen|Zona habitacional mixta|
|Receptor 38|Residencia localizada en Antu Newen|Zona habitacional mixta|
|Receptor 39|Residencia localizada en Antu Newen|Zona habitacional mixta|
|Receptor 40|Residencia localizada en Río Loa|Zona habitacional mixta|
|Receptor 41|Residencia localizada en Río Loa|Zona habitacional mixta|
|Receptor 42|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 43|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 44|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 45|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 46|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 47|Predio|Áreas de interés agropecuario exclusivo.|
|Receptor 48|Predio|Áreas de interés Agropecuario exclusivo.|
|Receptor 49|Predio|Áreas de interés Agropecuario exclusivo.|
|Receptor 50|Predio localizado en Cam. El Romeral|Áreas de interés Agropecuario exclusivo.|
|Receptor 51|Predio|Áreas de interés Agropecuario exclusivo.|
|Receptor 52|Predio|Áreas de preservación ecológica.|
|Receptor 53|Predio|Áreas de preservación ecológica.|
|Receptor 54|Predio|Áreas de preservación ecológica.|
|Receptor 55|Predio|Áreas de preservación ecológica.|
|Receptor 56|Predio|Áreas de interés Agropecuario exclusivo.|

63

**Figura 44.** Uso de suelo en el sector Romeral.

64

**Figura 45.** Uso de suelo en el sector Lo Herrera.

## 4.2. Selección de normativa

En Chile no existe una normativa de calidad o normas de emisión para olores vigente. Según

lo indicado en la “ _Guía para la Predicción y Evaluación de Impactos por Olor_ ” (2017), para

evaluar el impacto que puede generar un proyecto, se requiere “considerar lo establecido

en normas de calidad y de emisión vigente”.

A continuación, se presenta un análisis de la norma de 2 de los países establecidos en el

reglamento del SEIA y la justificación de la elección de la normativa:

## 4.2.1. Norma Australiana

De acuerdo a los antecedentes recabados en el estudio de la Subsecretaría del Medio

Ambiente (2013), Australia es un estado de Oceanía rodeado por los océanos índico y
pacífico; con una superficie del territorio es de 7.703.000 km [2] y una población al año 2011

fue de 21,5 millones.

65

El sector rural australiano es altamente productivo y tecnificado. Corresponde al sexto

exportador de productos agrícolas en el mundo, siendo su principal actividad la cría de

ovejas, lo cual sitúa al país como el primer productor de lana a nivel mundial, también

siendo uno de los principales exportadores de carne vacuna.

En Australia cada Estado es responsable de establecer las políticas en cuanto a calidad del

aire por olores. Tradicionalmente los Estados han adoptado regulaciones muy distintas

entre sí. [́]

## 4.2.2. Norma Países bajos (Holanda)

De acuerdo a los antecedentes recabados del estudio de la Subsecretaría del Medio

Ambiente (2013), Holanda es un país localizado en Europa, el cual posee una superficie de
territorio de 41.543 km [2] y una población de 16 millones, los cuales conviven con actividades

industriales y agrícolas.

Holanda ha sido uno de los países más avanzados en la regulación de olores molestos. Por

ser un país de superficie pequeña, con importante actividad de crianza de cerdos. Establece

los siguientes límites de acuerdo al tipo de suelo:

 - 3 OUE/m [3 ] (percentil 98) para receptores sensibles dentro del núcleo urbano, dentro de

una región económicamente dedicada a ganadería.

 - 14 OUE/m [3 ] (percentil 98) para receptores sensibles fuera del núcleo urbano, dentro de

una región económicamente dedicada a ganadería.

 - 2 OUE/m [3 ] (percentil 98) para receptores sensibles dentro del núcleo urbano, fuera de una

región económicamente dedicada a ganadería.

 - 8 OUE/m [3 ] (percentil 98) para objetos sensibles fuera del núcleo urbano, fuera de una re
gión económicamente dedicada a ganadería.

## 4.2.3. Justificación de la selección de normativa

Se analizaron las normativas de referencia de los países definidos en el reglamento del SEIA,

enfocándose en Australia y Holanda, y solo la correspondiente a la de los Países Bajos

(Holanda) cuenta con una regulación vigente que puede ser potencialmente aplicada en

Chile ( _Wet geurhinder en veehouderij_, 2013), dado que la principal actividad económica de

la zona en la cual está emplazado el proyecto es de ganadería y agricultura y que de acuerdo

al PRMS, se pueden diferenciar usos de suelo urbano y rural (ver 4.1 Receptores).

A continuación, se detalla la justificación de las consideraciones para la selección de esta

normativa:

 - Se puede detallar que las principales regiones ganaderas identificadas en Chile

corresponden a la región Metropolitana de Santiago, la región del Libertador

General Bernardo O’Higgins y la región del Maule, al respecto se puede detallar lo

siguiente:

66

`o` La producción nacional del sector porcino se concentra en un 90% entre

estas 3 regiones (Asprocer, 2022).

`o` En el sector avícola asociado a engorda (pollos y pavos), un 96,4% de la

producción nacional se enfoca en estas 3 regiones (Avinews, 2022).

 - Las instalaciones del sector de aves de postura se concentran en un

43% en la región Metropolitana (Antecedentes de Agricovial).

- El plan regulador de la región Metropolitana de Santiago permite clasificar los

receptores en aquellos localizados en un uso de suelo urbano y rural (ver 4.1

Receptores). Por lo que puede aplicarse la normativa, estableciendo diferentes

límites de concentración en inmisión.

- Se analizó el ranking de las tasas de emisión para el escenario base y proyectado del

proyecto, y el mayor aporte en las tasas de emisión corresponden a las actividades

de crianza y postura de aves, con un 71,6% del aporte de la TEO 1 en el escenario

base y de un 81,6% del aporte de la TEO 1 en el escenario proyectado. Dado lo

anterior, las principales fuentes corresponden a la actividad económica de

ganadería y agricultura.

- Esta norma fue empleada para evaluar los siguientes proyectos aprobados en el

Servicio de Evaluación Ambiental:

`o` **Sector avícola** :

 - Ampliación Plantel Avícola Florida (2020). Agrícola Sepa LTda.

Provincia de Concepción, Región del Biobío.

 - Regularización Plantel Avícola Eduardo Reinero (2020). Avícola

Reinero. Provincia de Talca, Región del Maule.

 - Mejoramiento y Ajustes Operacionales Plantel de Aves Huechún

(tercer ingreso) (2020). Agrícola Ariztía Limitada. Provincia de

Melipilla, Región Metropolitana de Santiago.

 - Ampliación Sectores de Crianza y Postura Plantel Melipilla. La Granja

S.A. (2016). Provincia de Melipilla, Región Metropolitana de Santiago.

 - Plantel Fundo Pachingo de Avícola Santa Elvira. Avícola Santa Elvira

(2021). Provincia de Limarí, Región de Coquimbo.

`o` **Sector porcino** :

 - Mejora del desempeño ambiental mediante biodigestor anaeróbico,

modernización y ampliación plantel de cerdos Santa Francisca,
AGRÍCOLA COEXCA S.A. Agrícola Coexca (2019). Provincia de

Colchagua, Región del Libertador General Bernardo O’Higgins.

`o` **Sector vacuno** :

 - Modificación del sistema de compostaje y su aplicación - Agrícola

Mollendo S.A., Agrícola Mollendo S.A (2018). Provincia del Biobío,

Región del Biobío.

 - Mejoramiento de la infraestructura y del manejo de sub-producto

agrícola guano y purines en el plantel lechero de Agrícola Panquehue

67

Limitada, Agrícola Panquehue Limitada (2018). Provincia de San

Felipe de Aconcagua, Región de Valparaíso.

Aun cuando el 76,8% de los receptores se encuentran localizado en uso de suelo Rural,

principalmente como áreas de interés agropecuario exclusivo (90,6% de los receptores

localizados en uso de suelo rural) y se puede apreciar de los estudios previamente

mencionados de que hay una concentración de actividades agrícolas en la región

Metropolitana (43% de las instalaciones del sector de ave de postura se concentran en la

región Metropolitana), con el objetivo de ofrecer un mayor grado de protección a los

receptores, es que para la evaluación del proyecto, se consideran los niveles definidos fuera

de una región económicamente dedicada a la ganadería.

Dado lo anterior, la normativa _Wet geurhinder en veehouderij_ (2013) define un límite de 8

OUE/m [3] para receptores fuera del núcleo urbano (rural) y de 2 OUE/m [3] para receptores

dentro del núcleo urbano, con un percentil 98.

## 4.3. Modelación de Impactos por Emisiones de Olor escenario actual

Dada la norma de los países bajos ( _Wet geurhinder en veehouderij, 2013_ ), en el escenario

base en los sectores de Romeral y Lo Herrera, ninguno de los receptores clasificados dentro
del uso de suelo urbano, superan el límite definido de 2 OU/m [3] ; por su parte, de los

receptores clasificados como rurales, solo tres receptores superan el límite definido de 8
OU/m [3], correspondientes al receptor 20, 21 y 50, que poseen una concentración en
inmisión de 14,1, 34 y 12,1 OU/m [3] respectivamente. Los receptores 20 y 21 se encuentran

localizados en el sector Lo Herrera, cercanos a la zona de acopio de guano actual y el

receptor 50 se encuentra en el sector Romeral, cercano a la zona de postura.

La isodora de 14 OU/m [3] en el sector Romeral se localiza cerca del perímetro de la planta, y

tiene una extensión de 286 m norte, 454 m oeste, 302 m sur y 403 m este desde el centro

del sector de postura, con un radio de alcance máximo de 489 m en dirección noroeste. La
isodora de 3 OU/m [3] se localiza rodeando el perímetro de la planta y tiene una extensión de

928 m norte, 639 m oeste, 877 m sur y 460 m este desde el centro del sector de postura,

con un radio de alcance máximo de 965 m nor noreste y un radio mínimo de alcance de 455

m este noreste.

La isodora de 14 OU/m [3] en el sector Lo Herrera se extiende fuera del perímetro de la zona

de acopio de guano de ave de postura, y tiene una extensión de 1.091 m norte, 1.247 m

oeste, 685 m sur y 622 m este desde el centro de la zona de acopio de GAP, y posee un radio
de alcance máximo de 1.353 m en dirección nor noroeste. La isodora de 3 OU/m [3] se

extiende fuera del perímetro de la zona de acopio de guano, y tiene una extensión de 1.695

m norte, 1.705 m oeste, 1.458 m sur y 1.130 m este desde el centro de la zona de acopio de

GAP, y posee un radio de alcance máximo de 2.322 m al noroeste y un radio de alcance

mínimo de 1.120 m al este noreste.

68

De acuerdo a la normativa, el escenario base genera impacto en los receptores colindantes

del proyecto.

**Figura 46.** Concentración ambiental horaria de olor percentil 98 en el escenario base (sector Romeral).

69

**Figura 47.** Concentración ambiental horaria de olor percentil 98 en el escenario base (sector Lo Herrera).

**Tabla 24.** Concentración ambiental de olor en receptores discretos (escenario base - Percentil 98).

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re1**|0,2|8|Sí|
|**Re2**|0,6|8|Sí|
|**Re3**|0,6|8|Sí|
|**Re4**|0,5|2|Sí|
|**Re5**|0,7|8|Sí|
|**Re6**|0,4|8|Sí|
|**Re7**|0,6|8|Sí|
|**Re8**|0,4|8|Sí|
|**Re9**|0,6|8|Sí|
|**Re10**|4,5|8|Sí|
|**Re11**|2,3|8|Sí|
|**Re12**|1,9|8|Sí|
|**Re13**|2,2|8|Sí|
|**Re14**|2,8|8|Sí|
|**Re15**|3,3|8|Sí|

70

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re16**|5|8|Sí|
|**Re17**|1,8|8|Sí|
|**Re18**|1,7|8|Sí|
|**Re19**|4,3|8|Sí|
|**Re20**|14,1|8|No|
|**Re21**|34|8|No|
|**Re22**|0,4|8|Sí|
|**Re23**|0,5|2|Sí|
|**Re24**|0,4|2|Sí|
|**Re25**|0,4|2|Sí|
|**Re26**|0,4|2|Sí|
|**Re27**|0,4|2|Sí|
|**Re28**|0,5|8|Sí|
|**Re29**|0,6|8|Sí|
|**Re30**|0,6|8|Sí|
|**Re31**|0,6|8|Sí|
|**Re32**|0,5|8|Sí|
|**Re33**|0,5|8|Sí|
|**Re34**|0,4|8|Sí|
|**Re35**|0,4|2|Sí|
|**Re36**|0,3|2|Sí|
|**Re37**|0,3|2|Sí|
|**Re38**|0,3|2|Sí|
|**Re39**|0,4|2|Sí|
|**Re40**|0,4|2|Sí|
|**Re41**|0,4|2|Sí|
|**Re42**|0,4|8|Sí|
|**Re43**|0,5|8|Sí|
|**Re44**|0,6|8|Sí|
|**Re45**|0,7|8|Sí|
|**Re46**|0,9|8|Sí|
|**Re47**|2,9|8|Sí|
|**Re48**|2,3|8|Sí|
|**Re49**|1,2|8|Sí|
|**Re50**|12,1|8|No|
|**Re51**|0,4|8|Sí|
|**Re52**|0,4|8|Sí|
|**Re53**|0,4|8|Sí|
|**Re54**|0,6|8|Sí|
|**Re55**|0,7|8|Sí|
|**Re56**|0,3|8|Sí|

71

## 4.4. Modelación de Impactos por Emisiones de Olor escenario proyectado

Dada la norma de los países bajos ( _Wet geurhinder en veehouderij_, 2013), en el escenario

proyectado en los sectores de Romeral y Lo Herrera, no hay receptores clasificados dentro
del uso de suelo urbano que superen el límite definido de 2 OU/m [3] y no hay receptores
clasificados dentro del uso de suelo rural que superen el límite definido de 8 OU/m [3] .

La isodora de 14 OU/m [3] se encuentra localizada en el sector Romeral sobre el perímetro de

la planta y tiene una extensión de 148,5 m al norte, 234,6 m al este, 242,4 al sur y 398,9 m

al oeste desde el centro de la zona de postura, y posee un radio de alcance máximo de 417,2

m al sur suroeste.

La isodora de 3 OU/m [3] localizada en el sector Romeral tiene una extensión de 636 m norte,

436,1 m este, 564,4 m sur y 590,5 m oeste desde el centro de la zona de postura y posee un

radio máximo de alcance de 672,2 m nor noroeste.

Por su parte, la isodora localizada en el sector Lo Herrera es tiene niveles de 1 y 3 OU/m [3], y

se encuentra ubicada directamente al norte del centro del sector de crianza de aves de

postura. Se puede apreciar que al remover el sector de acopio del sector Lo Herrera,

disminuye la concentración en los receptores aledaños y el alcance de las isodoras.

En el escenario proyectado, se puede apreciar de que debido a la implementación de ductos

en la salida de emisiones de todos los PPVF, cambio de tratamiento de GAP (tratamiento

por pilas a secadora GAP y secadora Kohshin), cambio de la localización desde el sector Lo

Herrera al sector Romeral y la implementación de medidas de mitigación (aplicación de Olex

o similar), permite que se reduzca la extensión de las isodoras.

De acuerdo a la normativa, en el escenario proyectado no se genera impacto en los

receptores colindantes del proyecto.

72

**Figura 48.** Concentración ambiental horaria de olor percentil 98 en el escenario proyectado (sector

Romeral).

73

**Figura 49.** Concentración ambiental horaria de olor percentil 98 en el escenario proyectado (sector Lo

Herrera).

**Tabla 25.** Concentración ambiental de olor en receptores discretos (escenario proyectado - Percentil 98).

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re1**|0,2|8|Sí|
|**Re2**|0,6|8|Sí|
|**Re3**|0,5|8|Sí|
|**Re4**|0,5|2|Sí|
|**Re5**|0,6|8|Sí|
|**Re6**|0,4|8|Sí|
|**Re7**|0,6|8|Sí|
|**Re8**|0,3|8|Sí|
|**Re9**|0,6|8|Sí|
|**Re10**|0,3|8|Sí|
|**Re11**|0,1|8|Sí|
|**Re12**|0,1|8|Sí|
|**Re13**|0,1|8|Sí|
|**Re14**|0,1|8|Sí|

74

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re15**|0,2|8|Sí|
|**Re16**|0,1|8|Sí|
|**Re17**|0,5|8|Sí|
|**Re18**|0,5|8|Sí|
|**Re19**|0,3|8|Sí|
|**Re20**|0,6|8|Sí|
|**Re21**|0,3|8|Sí|
|**Re22**|0,1|8|Sí|
|**Re23**|0,2|2|Sí|
|**Re24**|0,2|2|Sí|
|**Re25**|0,2|2|Sí|
|**Re26**|0,2|2|Sí|
|**Re27**|0,2|2|Sí|
|**Re28**|0,2|8|Sí|
|**Re29**|0,2|8|Sí|
|**Re30**|0,2|8|Sí|
|**Re31**|0,2|8|Sí|
|**Re32**|0,2|8|Sí|
|**Re33**|0,2|8|Sí|
|**Re34**|0,2|8|Sí|
|**Re35**|0,2|2|Sí|
|**Re36**|0,2|2|Sí|
|**Re37**|0,2|2|Sí|
|**Re38**|0,2|2|Sí|
|**Re39**|0,2|2|Sí|
|**Re40**|0,2|2|Sí|
|**Re41**|0,2|2|Sí|
|**Re42**|0,2|8|Sí|
|**Re43**|0,2|8|Sí|
|**Re44**|0,2|8|Sí|
|**Re45**|0,3|8|Sí|
|**Re46**|0,3|8|Sí|
|**Re47**|1,6|8|Sí|
|**Re48**|1,3|8|Sí|
|**Re49**|0,8|8|Sí|
|**Re50**|4,9|8|Sí|
|**Re51**|0,3|8|Sí|
|**Re52**|0,3|8|Sí|
|**Re53**|0,3|8|Sí|
|**Re54**|0,4|8|Sí|

75

|Receptores|Concentración en<br>inmisión (OU/m3)|Límite establecido por<br>normativa (OU/m3)|Cumplimiento del límite<br>establecido por normativa|
|---|---|---|---|
|**Re55**|0,5|8|Sí|
|**Re56**|0,2|8|Sí|

## 4.5. Área de influencia - Escenario base

Siguiendo los lineamientos de la “Guía para la predicción y evaluación de impactos por olor

en el SEIA” (2017), se define el área de influencia (AI) como el espacio contenido por la
isodora de 1 OU/m [3] .

Desde el centroide del AI, existe un alcance de 3,7 km al Norte, 1,61 km al Este, 3,7 km al

Sur y 1,47 km al Oeste. El radio de máximo alcance es de 5,2 km al Sur Sur-este y el radio

mínimo de alcance es de 1,2 km al Sur-oeste. El AI abarca el sector de crianza y el de postura
del proyecto, y tiene un área total de 21,5 km [2] .

**Figura 50.** Área de influencia del proyecto - Escenario base.

76

## 4.6. Área de influencia - Escenario proyectado

Desde el centroide del AI en el sector Romeral, existe un alcance de 1,11 km norte, 0,93 km

este, 1,29 km sur y 0,81 km oeste. Un radio máximo de alcance de 1,3 km al sur sureste y

un radio mínimo de alcance de 0,74 km oeste suroeste. El área de influencia tiene un área
de 3,27 km [2] .

Desde el centroide del AI en el sector Lo Herrera, existe un alcance de 0,37 km norte, 0,62

km este, 0,46 km sur y 0,56 km oeste. Un radio máximo de alcance de 0,63 km al este

noreste y un radio mínimo de alcance de 0,34 km nor noreste. El área de influencia tiene un
área de 0,76 km [2] .

El área de influencia del escenario proyectado tiene una superficie total de 3,93 km [2],

generándose una reducción de un 81,7% del área de influencia con respecto al escenario

base, debido a las medidas que se implementan en el proyecto.

**Figura 51.** Área de influencia del proyecto - Escenario proyectado.

77

# 5 Conclusiones

Del presente informe, se obtienen las siguientes conclusiones:

 - De acuerdo al análisis de incertidumbre meteorológica realizado entre las variables

modeladas y observadas, la simulación desarrollada entrega un nivel de

incertidumbre aceptable dado el nivel de resolución aplicado según las directrices

del SEIA y en base a los criterios de tolerancia definidos para la velocidad del viento

y la temperatura.

 - Según los valores de los parámetros de la predicción proporcionada por el modelo

para la Estación El Milagro, el modelo para la dirección del viento no cumple con el

criterio de validez ni tolerancia recomendados.

 - De acuerdo a la normativa de referencia utilizada, en el escenario base en los

sectores de Romeral y Lo Herrera:

`o` No hay ningún receptor localizado en zona urbana que supere una

concentración en inmisión de 2 OU/m [3] .

`o` Hay tres receptores que superan el límite definido para zonas rurales de 8

OU/m [3], correspondientes a los receptores 20, 21 y 50, con una
concentración en inmisión de 14,1, 34 y 12,1 OU/m [3] respectivamente.

`o` El escenario base genera un impacto en los receptores colindantes del

proyecto.

 - En el escenario proyectado, con las modificaciones operacionales y medidas de

mitigación incorporadas en los sectores de Romeral y Lo Herrera, no hay receptores
que superen el límite definido para zonas rurales de 8 OU/m [3] o para zonas urbanas
de 2 OU/m [3] . No generando impacto en ningún receptor de acuerdo a la normativa

de referencia utilizada.

`o` En el escenario proyectado se estima una reducción promedio de la

concentración en inmisión de un 51,3%.

 - El área de influencia proyectada tiene una reducción de un 81,7% de la superficie,

con respecto al escenario base. Esta reducción está asociada a:

`o` La implementación de ductos a la salida de todos los PPVF, favoreciendo el

proceso del efecto de dispersión de la emisión.

`o` Cambio de localización del GAP desde Lo Herrera a Romeral, cambio de

tratamiento de GAP de pilas a tratamiento por secadora GAP y secadora

Kohshin y la implementación de medidas de mitigación (aplicación de Olex o

similar).

78

# A) APENDICE 1 - Reporte de muestreo AQOM Agricovial

## A.1) Sector Romeral

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

## A.2) Sector Lo Herrera

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

## A.3) Medición secadora Kohshin

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

## A.4) Empresa Avícola Zona Central

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

# B) APENDICE 2 - Informe de APL II Chilehuevos

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

# C) APENDICE 3 - Archivos de la Modelación

De acuerdo a lo señalado en la Ley 19.300 sobre Bases Generales del Medio Ambiente en el

artículo 14 bis, y en el Decreto Supremo 40 que Aprueba Reglamento del Sistema de

Evaluación de Impacto Ambiental (2012), en el artículo 21 inciso N°3 y el artículo 29 inciso

N°1, se informa que dada la naturaleza de los archivos digitales de Modelación

Meteorológica WRF y Modelaciones de Dispersión Atmosférica **CALPUFF y CALPOST**, no es

posible agregarlos al expediente electrónico, motivo por el cual dicha información se

encuentra disponible para el público en general en las oficinas de la Dirección Ejecutiva del

Servicio de Evaluación Ambiental (SEA). Los interesados en obtener acceso a dicha

documentación digital, deben comunicarse con la Oficina de Información y Atención

Ciudadana del SEA, ingresando un requerimiento a través del siguiente formulario:

https://www.portaltransparencia.cl/PortalPdT/

https://storage.googleapis.com/wrf-mmif-calpuffpublic/chilehuevos/agricovialv39/agricovialv39.met

298

# D)APENDICE 4 - Bibliografía

Agrícola Ariztía Ltda. 2020. Mejoramiento y Ajustes Operacionales Plantel de Aves Huechún

(tercer ingreso) (DIA). SEA.

Agrícola Coexca. 2019. Mejora del desempeño ambiental mediante biodigestor anaeróbico,
modernización y ampliación plantel de cerdos Santa Francisca, AGRÍCOLA COEXCA S.A.

Agrícola Coexca (DIA). SEA.

Agrícola Mollendo. 2018. Modificación del sistema de compostaje y su aplicación (DIA). SEA.

Agrícola Panquehue Limitada. 2018. Mejoramiento de la infraestructura y del manejo de

sub-producto agrícola guano y purines en el plantel lechero de Agrícola Panquehue Limitada

(DIA). SEA.

Agrícola Sepulveda Palou. 2020. Ampliación Plantel Avícola Florida (DIA). SEA.

Asprocer. Porcicultura en Chile: situación actual y perspectivas futuras. Visitado el: 02-022022. Disponible en: https://porcino.info/porcicultura-en-chile-situacion-actual-yperspectivas-futuras/

Avinews. Chile: Producción de carne de pollo registra crecimiento de 5,7% en 2020. Visitado
el: 02-02-2022. Disponible en: https://avicultura.info/chile-produccion-pollo-crece-572020/

Avícola Reinero. 2020. Regularización Plantel Avícola Eduardo Reinero (DIA). SEA.

Avícola Santa Elvira. 2021. Plantel Fundo Pachingo de Avícola Santa Elvira (DIA). SEA.

Decreto 40. 2012. Ministerio del Medio Ambiente. Aprueba reglamento del sistema de

evaluación de impacto ambiental.

Dirección General de Aeronáutica Civil. Dirección Meteorológica de Chile - Servicios
Climáticos. Visitado el 06-04-2021. Disponible en: https://climatologia.meteochile.gob.cl/

Emery, C., Liu, Z., Russell, A. G., Odman, M. T., Yarwood, G., Kumar, N. (2017).

Recommendations on statistics and benchmarks to assess photochemical model

performance. Journal of the Air and Waste Management Association, 67(5), 582-598.
https://doi.org/10.1080/10962247.2016.1265027

Estudio de fuentes y procesos generadores de olor para el sector productor de huevos de

Chile - Acuerdo de Producción Limpia II. Chilehuevos, 2021.

European Commission. 2017. Best Available Techniques (BAT) reference document for the

intensive rearing of poultry or pigs.

GCA Ambiental. 2021. Reporte de muestreo AQOM Agricovial Romeral.

299

GCA Ambiental. 2021. Reporte de muestreo AQOM Agricovial Lo Herrera.

GCA Ambiental. 2021. Reporte de muestreo AQOM Empresa Avícola Zona Central.

La granja. 2016. Ampliación Sectores de Crianza y Postura Plantel Melipilla (DIA). SEA.

Ministerio de Bienes Nacionales. Zonificación Plan Regulador Metropolitano de Santiago

(PRMS). Visitado el: 11-01-2022. Disponible en:
https://www.ide.cl/index.php/planificacion-y-catastro/item/1878-zonificacion-plan
regulador-metropolitano-de-santiago-prms

Overheid. 2013. Wet geurhinder en veehouderij. Netherlands.

Salimax. 2022. Informe de olfatometría - Planta Kohshin.

Servicio de Evaluación de Impacto Ambiental. 2012. Guía para el uso de modelos de calidad

del aire en el SEIA.

Servicio de Evaluación Ambiental. 2017. Guía para la predicción y evaluación de impactos

por olor en el SEIA. Ministerio del Medio Ambiente.

Subsecretaría del Medio Ambiente. 2013. Estudio: antecedentes para la regulación de

olores en Chile.

Yáñez-Morroni, G., Gironás, J., Caneo, M., Delgado, R., & Garreaud, R. (2018). Using the

Weather Research and Forecasting (WRF) model for precipitation forecasting in an Andean

region with complex topography. _Atmosphere_, _9_ (8).

300

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Límites de concentración en inmisión - Ley de molestias de olor y ganadería de los Países bajos**

| Clasificación | Límite de concentración en<br>inmisión dentro de región<br>económicamente dedicada a<br>ganadería) | Límite de concentración en<br>inmisión fuera de región<br>económicamente dedicada a<br>ganadería |
| --- | --- | --- |
| **Núcleo urbano** | 3 OUE/m3 | 2 OUE/m3 |
| **Núcleo rural** | 14 OUE/m3 | 8 OUE/m3 |

**Tabla 2.: ** Concentración ambiental de olor en receptores discretos (escenario base - Percentil 98).**

| Receptores | Concentración en<br>inmisión (OU/m3) | Límite establecido por<br>normativa (OU/m3) | Cumplimiento del límite<br>establecido por normativa |
| --- | --- | --- | --- |
| **Re1** | 0,2 | 8 | Sí |
| **Re2** | 0,6 | 8 | Sí |
| **Re3** | 0,6 | 8 | Sí |
| **Re4** | 0,5 | 2 | Sí |
| **Re5** | 0,7 | 8 | Sí |
| **Re6** | 0,4 | 8 | Sí |
| **Re7** | 0,6 | 8 | Sí |
| **Re8** | 0,4 | 8 | Sí |
| **Re9** | 0,6 | 8 | Sí |
| **Re10** | 4,5 | 8 | Sí |
| **Re11** | 2,3 | 8 | Sí |
| **Re12** | 1,9 | 8 | Sí |
| **Re13** | 2,2 | 8 | Sí |
| **Re14** | 2,8 | 8 | Sí |
| **Re15** | 3,3 | 8 | Sí |
| **Re16** | 5 | 8 | Sí |
| **Re17** | 1,8 | 8 | Sí |
| **Re18** | 1,7 | 8 | Sí |
| **Re19** | 4,3 | 8 | Sí |
| **Re20** | 14,1 | 8 | No |
| **Re21** | 34 | 8 | No |
| **Re22** | 0,4 | 8 | Sí |
| **Re23** | 0,5 | 2 | Sí |
| **Re24** | 0,4 | 2 | Sí |
| **Re25** | 0,4 | 2 | Sí |
| **Re26** | 0,4 | 2 | Sí |
| **Re27** | 0,4 | 2 | Sí |
| **Re28** | 0,5 | 8 | Sí |
| **Re29** | 0,6 | 8 | Sí |
| **Re30** | 0,6 | 8 | Sí |
| **Re31** | 0,6 | 8 | Sí |
| **Re32** | 0,5 | 8 | Sí |
| **Re33** | 0,5 | 8 | Sí |
| **Re34** | 0,4 | 8 | Sí |
| **Re35** | 0,4 | 2 | Sí |
| **Re36** | 0,3 | 2 | Sí |
| **Re37** | 0,3 | 2 | Sí |
| **Re38** | 0,3 | 2 | Sí |

**Tabla 3.: ** Concentración ambiental de olor en receptores discretos (escenario proyectado - Percentil 98).**

| Receptores | Concentración en<br>inmisión (OU/m3) | Límite establecido por<br>normativa (OU/m3) | Cumplimiento del límite<br>establecido por normativa |
| --- | --- | --- | --- |
| **Re1** | 0,2 | 8 | Sí |
| **Re2** | 0,6 | 8 | Sí |
| **Re3** | 0,5 | 8 | Sí |
| **Re4** | 0,5 | 2 | Sí |
| **Re5** | 0,6 | 8 | Sí |
| **Re6** | 0,4 | 8 | Sí |
| **Re7** | 0,6 | 8 | Sí |
| **Re8** | 0,3 | 8 | Sí |
| **Re9** | 0,6 | 8 | Sí |
| **Re10** | 0,3 | 8 | Sí |
| **Re11** | 0,1 | 8 | Sí |

**Tabla 4.: ** Coordenadas generales del perímetro del sector de postura en sector Romeral.**

| Vértice | Coordenadas UTM<br>(Datum WGS 84 Huso 19)<br>Este (m) Norte (m) | Col3 |
| --- | --- | --- |
| **A ** | 336644,4 | 6270317,3 |
| **B ** | 336595,8 | 6270324,5 |
| **C ** | 336455,3 | 6270151,7 |
| **D ** | 336422,6 | 6270017,1 |
| **E ** | 336286,7 | 6269877,7 |
| **F ** | 336632,8 | 6269651,9 |
| **G ** | 336641,7 | 6269631,4 |
| **H ** | 336806,4 | 6269486,3 |
| **I ** | 337191,4 | 6269744,9 |
| **J ** | 337196,4 | 6269812,8 |
| **K ** | 336919,4 | 6269731,7 |
| **L ** | 336871,0 | 6269760,1 |
| **M ** | 336880,6 | 6269980,3 |

**Tabla 5.: ** Coordenadas generales del perímetro del sector de crianza en Lo Herrera.**

| Vértice | Coordenadas UTM<br>(Datum WGS 84 Huso 19) | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| **A ** | 336166,2 | 6273729,7 |
| **B ** | 336104,5 | 6273176,1 |
| **C ** | 336668,8 | 6273172,5 |
| **D ** | 336695,6 | 6273627,5 |

**Tabla 6.: ** Coordenadas generales del perímetro del sector de acopio de GAP en Lo Herrera (actual).**

| Vértice | Coordenadas UTM<br>(Datum WGS 84 Huso 19) | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| **A ** | 335503,5 | 6274557,0 |
| **B ** | 335453,1 | 6274100,1 |
| **C ** | 336177,9 | 6273870,7 |
| **D ** | 336234,2 | 6274241,7 |

**Tabla 7.: ** Factor de emisión de fuentes de emisión de olores del escenario base.**

| Fuente CO (OU/m3) FE (OU/(m2·s)) Tipo fuente Bibliografía | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **PPVF (medición en**<br>**extractor)** | 177 | -- | Puntual | GCA Ambiental<br>2021 |
| **PPVN sector jaulas** | 148 | 11,3 | Difusa | GCA Ambiental<br>2021 |
| **PPVN sector cama**<br>**guano** | 653 | 5,4 | Difusa | GCA Ambiental<br>2021 |
| **PCVF (medición en**<br>**extractor)** | 241 | -- | Puntual | GCA Ambiental<br>2020 |

**Tabla 8.: ** Comparación de fuentes - Zona de acopio residuos orgánicos.**

| Fuente Proyecto - Zona de acopio de Bunker de aves muertas de<br>residuos orgánicos Avícola Reinero SpA (2019)<br>(proyecto original del cual<br>homologo proyecto aprobado) | Col2 | Col3 |
| --- | --- | --- |
| **Descripción de fuente** | Bins cerrados en los cuales se<br>depositan aves muertas y se les<br>aplica<br>cal<br>viva<br>(CaO),<br>se<br>encuentran localizados dentro de<br>bodega la cual contiene residuos<br>orgánicos y residuos domésticos<br>dentro de contenedor. | Contenedor bunker en el cual se<br>depositan aves muertas a las<br>cuales se les agrega cal |
| **Especificaciones de modelación** | Los bins son cerrados, y el espacio<br>en el cual se encuentran dentro<br>las fuentes es una bodega. Para<br>efectos de la modelación, se<br>consideró toda la superficie de la<br>bodega emite, sobrestimando el<br>impacto.<br>Emisión continua. | Se estima que solo el bunker<br>emite y desde un punto.<br>Emisión continua. |
| **Tipo de fuente** | Difusa | Puntual |
| **Justificación uso** | Esta fuente de emisión homologada también usa cal para mitigar las<br>emisiones. Al emplear los antecedentes de la concentración y estimar<br>el FE con su superficie, se sobrestima la emisión al considerar toda la<br>superficie de la zona de acopio de residuos orgánicos como la que<br>emite. | Esta fuente de emisión homologada también usa cal para mitigar las<br>emisiones. Al emplear los antecedentes de la concentración y estimar<br>el FE con su superficie, se sobrestima la emisión al considerar toda la<br>superficie de la zona de acopio de residuos orgánicos como la que<br>emite. |

**Tabla 9: ** Concentración de olor secador Kohshin operando al 10%.**

| Fuente CO sin Olex CO con Olex Porcentaje Fuente<br>(OU/m3) (OU/m3) reducción de la<br>concentración | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Extractor 1 secadora**<br>**Kohshin al 10% de**<br>**capacidad** | 22,2 | 3.2 | 85,4% | Informe Salimax |
| **Extractor 2 secadora**<br>**Kohshin al 10% de**<br>**capacidad** | 14,8 | 2.7 | 81,7% | 81,7% |

**Tabla 10.: ** Factores de emisión de fuentes identificadas en el escenario proyectado.**

| Fuente CO (OU/m3) FE (OU/(m2·s)) Tipo fuente Fuente | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **PPVF (medición en**<br>**extractor)** | 177 | -- | Puntual | GCA Ambiental<br>2021 |
| **PPVN sector jaulas** | 148 | 11,3 | Difusa | GCA Ambiental<br>2021 |
| **PPVN sector cama**<br>**guano** | 653 | 5,4 | Difusa | GCA Ambiental<br>2021 |
| **PCVF (medición en**<br>**extractor)** | 241 | -- | Puntual | GCA Ambiental<br>2020 |
| **Lombrifiltro** | 129 | 1,08 | Difusa | GCA Ambiental<br>2021 |
| **Zona acopio residuos**<br>**orgánicos** | -- | 18,71 | Difusa | Homologado a<br>la sumatoria de<br>la emisión de<br>fosa<br>de<br>aves<br>muertas fugas y<br>cargas<br>del<br>proyecto de DIA<br>“Ampliación<br>plantel<br>avícola<br>Florida” 2020 |
| **Secadora Kohshin**<br>**extractor 1** | 32,58 | -- | Puntual | Informe<br>de<br>Salimax<br>2022,<br>multiplicado por<br>un factor de 10, |
| **Secadora Kohshin**<br>**extractor 2** | 27,2 | -- | Puntual | Puntual |

**Tabla 11.: ** Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario base).**

| Fuente Velocidad Altura Tempera Área N° Condiciones de<br>(m/s) emisión tura (°C) emisión extracto operación<br>(m) (m2) res | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **PPVF 1 -**<br>**extractor** | 1,7 | 2 | 26,1 | 1,3 | 36 | Extractores -<br>Verano y Primavera: 8<br>horas día 100% y 16<br>horas día 25%.<br>Otoño e Invierno: 6 horas<br>día 100% y 18 horas día<br>25%. |
| **PPVF 2 -**<br>**extractor** | **PPVF 2 -**<br>**extractor** | **PPVF 2 -**<br>**extractor** | **PPVF 2 -**<br>**extractor** | 1,5 | 30 | 30 |
| **PPVF 3 -**<br>**extractor** | **PPVF 3 -**<br>**extractor** | **PPVF 3 -**<br>**extractor** | **PPVF 3 -**<br>**extractor** | 1,3 | 40 | 40 |
| **PPVF 4 -**<br>**extractor** | **PPVF 4 -**<br>**extractor** | **PPVF 4 -**<br>**extractor** | **PPVF 4 -**<br>**extractor** | 1,3 | 36 | 36 |
| **PPVF 5 -**<br>**extractor** | **PPVF 5 -**<br>**extractor** | **PPVF 5 -**<br>**extractor** | **PPVF 5 -**<br>**extractor** | 1,3 | 52 | 52 |
| **PPVF 6 -**<br>**extractor** | **PPVF 6 -**<br>**extractor** | **PPVF 6 -**<br>**extractor** | **PPVF 6 -**<br>**extractor** | 1,4 | 42 | 42 |
| **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | 1,4 | 42 | 42 |
| **PPVN 1 sector**<br>**jaulas** | -- | 2 | -- | 222 | -- | Cortinas -<br>Noviembre a marzo: 50%<br>abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs. |
| **PPVN 2 sector**<br>**jaulas** | -- | -- | -- | 222 | -- | -- |
| **PPVN 3 sector**<br>**jaulas** | -- | -- | -- | 177 | -- | -- |

**Tabla 12: ** . Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario proyectado).**

| Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extractor operación<br>(m) (m2) es | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **PPVF 1 -**<br>**ductos** | 0,9 | 9 | 26,1 | 42,5 | 36 | Extractores -<br>Verano y Primavera: 8<br>horas día 100% 16 horas<br>día 25%.<br>Otoño e Invierno: 6<br>horas día 100% y 18<br>horas día 25%. |
| **PPVF 2 -**<br>**ductos** | 0,9 | 7,6 | 7,6 | 42,5 | 30 | 30 |
| **PPVF 3 - ducto** | 2,7 | 7,2 | 7,2 | 32,5 | 40 | 40 |
| **PPVF 4 -**<br>**ductos** | 0,9 | 7,5 | 7,5 | 42,5 | 36 | 36 |
| **PPVF 5 -**<br>**ductos** | 1,6 | 8 | 8 | 35 | 52 | 52 |
| **PPVF 6 -**<br>**ductos** | 1,2 | 9,5 | 9,5 | 42,5 | 42 | 42 |
| **PPVF 7 -**<br>**ductos** | 1,2 | 7,6 | 7,6 | 42,5 | 42 | 42 |
| **PPVN 1 sector**<br>**jaulas** | -- | 2 | -- | 222 | -- | Cortinas -<br>Noviembre a marzo: 50%<br>abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs.<br> |
| **PPVN 2 sector**<br>**jaulas** | **PPVN 2 sector**<br>**jaulas** | **PPVN 2 sector**<br>**jaulas** | **PPVN 2 sector**<br>**jaulas** | 222 | -- | -- |
| **PPVN 3 sector**<br>**jaulas** | **PPVN 3 sector**<br>**jaulas** | **PPVN 3 sector**<br>**jaulas** | **PPVN 3 sector**<br>**jaulas** | 177 | -- | -- |
| **PPVN 4 sector**<br>**jaulas** | **PPVN 4 sector**<br>**jaulas** | **PPVN 4 sector**<br>**jaulas** | **PPVN 4 sector**<br>**jaulas** | 228 | -- | -- |

**Tabla 13.: ** Emisiones atmosféricas de olor de la planta de Agricovial (escenario base).**

| Fuente | Tasa de emisión<br>1 (OU/s) | Tasa de emisión<br>2 (OU/s) | Tasa de emisión 3<br>(OU/s) | Tasa de emisión 4<br>(OU/s) |
| --- | --- | --- | --- | --- |
| **PPVF 1** | 13.722 | 3.431 | 13.722 | 3.431 |
| **PPVF 2** | 13.837 | 3.459 | 13.837 | 3.459 |
| **PPVF 3** | 15.247 | 3.812 | 15.247 | 3.812 |
| **PPVF 4** | 13.722 | 3.431 | 13.722 | 3.431 |
| **PPVF 5** | 19.821 | 4.955 | 19.821 | 4.955 |
| **PPVF 6** | 17.988 | 4.497 | 17.988 | 4.497 |
| **PPVF 7** | 17.988 | 4.497 | 17.988 | 4.497 |
| **PPVN 1 sector jaulas** | 2.519 | 1.134 | 2.519 | 1.134 |
| **PPVN 2 sector jaulas** | 2.519 | 1.134 | 2.519 | 1.134 |
| **PPVN 3 sector jaulas** | 2.008 | 904 | 2.008 | 904 |
| **PPVN 4 sector jaulas** | 2.587 | 1.164 | 2.587 | 1.164 |
| **PPVN 1 sector cama**<br>**guano** | 12.884 | 1.933 | 12.884 | 1.933 |
| **PPVN 2 sector cama**<br>**guano** | 12.651 | 1.933 | 12.651 | 1.933 |
| **PPVN 3 sector cama**<br>**guano** | 8.937 | 1.541 | 8.937 | 1.541 |
| **PPVN 4 sector cama**<br>**guano** | 9.561 | 1.985 | 9.561 | 1.985 |
| **PCVF 1** | 8.783 | 3.513 | 8.783 | 3.513 |
| **PCVF 2** | 8.783 | 3.513 | 8.783 | 3.513 |
| **PCVF 3** | 9.411 | 3.764 | 9.411 | 3.764 |
| **Lombrifiltro** | 1.243 | 1.243 | 1.243 | 1.243 |
| **Zona acopio residuos**<br>**orgánicos** | 369 | 369 | 369 | 369 |
| **Pilas de guano fresco** | 18.259 | 34.236 | 18.259 | 34.236 |
| **Pilas de guano activo** | 41.063 | 51.329 | 164.252 | 205.316 |
| **Pilas de guano**<br>**maduro** | 15.757 | 26.262 | 15.757 | 26.262 |

**Tabla 14.: ** Porcentaje de aporte a la tasa de emisión de olor total de la planta de Agricovial - Escenario base.**

| Fuente % aporte total % aporte total % aporte total % aporte total<br>TEO 1 TEO 2 TEO 3 TEO 4 | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Pilas de guano activo** | 15,2% | 31,3% | 41,8% | 64,6% |
| **PPVF 5** | 7,4% | 3,0% | 5,0% | 1,6% |
| **Pilas de guano fresco** | 6,8% | 20,9% | 4,6% | 10,8% |
| **PPVF 6** | 6,7% | 2,7% | 4,6% | 1,4% |
| **PPVF 7** | 6,7% | 2,7% | 4,6% | 1,4% |
| **Pilas de guano maduro** | 5,8% | 16,0% | 4,0% | 8,3% |
| **PPVF 3** | 5,7% | 2,3% | 3,9% | 1,2% |
| **PPVF 2** | 5,1% | 2,1% | 3,5% | 1,1% |
| **PPVF 1** | 5,1% | 2,1% | 3,5% | 1,1% |
| **PPVF 4** | 5,1% | 2,1% | 3,5% | 1,1% |
| **PPVN 1 sector cama guano** | 4,8% | 1,2% | 3,3% | 0,6% |
| **PPVN 2 sector cama guano** | 4,7% | 1,2% | 3,2% | 0,6% |
| **PPVN 4 sector cama guano** | 3,5% | 1,2% | 2,4% | 0,6% |
| **PCVF 3** | 3,5% | 2,3% | 2,4% | 1,2% |
| **PPVN 3 sector cama guano** | 3,3% | 0,9% | 2,3% | 0,5% |
| **PCVF 1** | 3,3% | 2,1% | 2,2% | 1,1% |
| **PCVF 2** | 3,3% | 2,1% | 2,2% | 1,1% |
| **PPVN 4 sector jaulas** | 1,0% | 0,7% | 0,7% | 0,4% |
| **PPVN 1 sector jaulas** | 0,9% | 0,7% | 0,6% | 0,4% |
| **PPVN 2 sector jaulas** | 0,9% | 0,7% | 0,6% | 0,4% |
| **PPVN 3 sector jaulas** | 0,7% | 0,6% | 0,5% | 0,3% |
| **Lombrifiltro** | 0,5% | 0,8% | 0,3% | 0,4% |
| **Zona acopio residuos orgá-**<br>**nicos** | 0,1% | 0,2% | 0,1% | 0,1% |
| **Total** | **100%** | **100%** | **100%** | **100%** |

**Tabla 15.: ** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).**

| Característica | Secador proyecto | Secador Avícola Zona<br>central |
| --- | --- | --- |
| **Capacidad tratamiento guano**<br>**(asociado al número de aves)** | 1.000.000 | 200.000 |
| **Alimentación corriente aire** | Proveniente del medio<br>ambiente.<br>Se estima la TEO que se<br>remueve del GAP. | Proveniente<br>de<br>la<br>guanera<br>y <br>de<br>los<br>pabellones, por lo que<br>viene<br>con<br>la<br>carga<br>odorante<br>de<br>los<br>pabellones. |
| **Descripción de la fuente** | Humedad de entrada de<br>70%-80%<br>Humedad de salida de 15<br>- 25%.<br>Temperatura de entrada<br>de 25°C.<br>Temperatura de salida de<br>20 °C. | Humedad de entrada de<br>70%<br>Humedad de salida de<br>16%.<br>Temperatura de entrada<br>de 25°C.<br>Temperatura de salida de<br>18 °C. |
| **Tipo de emisión** | Continua | Continua |
| **Tipo de fuente** | Puntual | Puntual |
| **Justificación uso** | Las condiciones de operación son similares, pero con<br>grandes diferencias en cuanto a la cantidad de GAP de<br>ave a tratar. Dado los antecedentes de estas fuentes,<br>se emplea la concentración de olor para estimar la<br>tasa de emisión de la fuente puntual homologada.<br>Se realiza un balance de las TEO en el equipo secador<br>de avícola zona central y a partir de él, se estima la TEO<br>que se emite y se escala el resultado de acuerdo a la<br>razón entre la capacidad tratamiento guano (asociado<br>al número de aves) de la fuente del proyecto con el de<br>la fuente homologada. | Las condiciones de operación son similares, pero con<br>grandes diferencias en cuanto a la cantidad de GAP de<br>ave a tratar. Dado los antecedentes de estas fuentes,<br>se emplea la concentración de olor para estimar la<br>tasa de emisión de la fuente puntual homologada.<br>Se realiza un balance de las TEO en el equipo secador<br>de avícola zona central y a partir de él, se estima la TEO<br>que se emite y se escala el resultado de acuerdo a la<br>razón entre la capacidad tratamiento guano (asociado<br>al número de aves) de la fuente del proyecto con el de<br>la fuente homologada. |

**Tabla 16.: ** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).**

| Fuente | Tasa de emisión 1 (OU/s) | Tasa de emisión 2 (OU/s) |
| --- | --- | --- |
| **PPVF 1** | 13.722 | 3.431 |
| **PPVF 2** | 13.837 | 3.459 |
| **PPVF 3** | 15.247 | 3.812 |
| **PPVF 4** | 13.722 | 3.431 |

**Tabla 17.: ** Porcentaje de aporte a la tasa de emisión de olor total de la planta de Agricovial - Escenario**

| Fuente % aporte total TEO 1 % aporte total TEO 2 | Col2 | Col3 |
| --- | --- | --- |
| **Secador de guano de ave de postura** | 17,7% | 44,3% |
| **PPVF 5** | 8,4% | 5,3% |
| **PPVF 6** | 7,6% | 4,8% |
| **PPVF 7** | 7,6% | 4,8% |
| **PPVF 3** | 6,4% | 4,0% |
| **PPVF 2** | 5,8% | 3,7% |
| **PPVF 1** | 5,8% | 3,6% |
| **PPVF 4** | 5,8% | 3,6% |
| **PPVN 1 sector cama guano** | 5,4% | 2,1% |
| **PPVN 2 sector cama guano** | 5,3% | 2,1% |
| **PPVN 4 sector cama guano** | 4,0% | 2,1% |
| **PCVF 3** | 4,0% | 4,0% |
| **PPVN 3 sector cama guano** | 3,8% | 1,6% |
| **PCVF 1** | 3,7% | 3,7% |
| **PCVF 2** | 3,7% | 3,7% |
| **PPVN 4 sector jaulas** | 1,1% | 1,2% |
| **PPVN 1 sector jaulas** | 1,1% | 1,2% |
| **PPVN 2 sector jaulas** | 1,1% | 1,2% |
| **PPVN 3 sector jaulas** | 0,8% | 1,0% |
| **Lombrifiltro** | 0,5% | 1,3% |
| **Zona acopio residuos orgánicos** | 0,2% | 0,4% |
| **Secadora Kohshin - Extractor 1** | 0,05% | 0,1% |
| **Secadora Kohshin - Extractor 2** | 0,04% | 0,1% |
| **Total** | **100%** | **100%** |

**Tabla 18.: ** Ubicación de estación meteorológica superficial El Milagro.**

| Estación | Altura<br>m.s.n.m<br>(m) | Coordenadas UTM | Col4 |
| --- | --- | --- | --- |
| **Estación** | **Altura**<br>**m.s.n.m**<br>**(m)** | **Datum WGS 84 Huso 19 H** | **Datum WGS 84 Huso 19 H** |
| **Estación** | **Altura**<br>**m.s.n.m**<br>**(m)** | **Este (m)** | **Norte (m)** |
| **Estación El Milagro** | 460 | 336.580,5 | 6.263.672,3 |

**Tabla 19.: ** Criterios estadísticos de aceptación de la predicción proporcionada por un modelo meteorológico.**

| Variable Meteorológica | Parámetros Estadísticos | Criterio de Validez |
| --- | --- | --- |
| **Velocidad Viento (10 m)** | RMSE | ≤ 2 m/s |
| **Velocidad Viento (10 m)** | BIAS | ≤ ±0,5 m/s |
| **Dirección Viento (°)** | Error Absoluto | ≤ 30° |
| **Dirección Viento (°)** | BIAS | ≤ ±10° |
| **Temperatura Superficial (2 m)** | Error Absoluto | ≤ 2K |
| **Temperatura Superficial (2 m)** | BIAS | ≤ ±0,5K |

**Tabla 20.: ** Criterios de tolerancia de diferencia absoluta de variables modeladas.**

| Variable Meteorológica | Criterio |
| --- | --- |
| **Velocidad del viento** | 2,57 m/s |
| **Dirección del viento** | 20° |
| **Temperatura de rocío** | 1°C en superficie. |
| **Temperatura** | 1°C en superficie. |

**Tabla 21.: ** Valores de los parámetros de la predicción proporcionada por el modelo para la Estación El**

| Variable Meteorológica | Parámetros<br>Estadísticos | Valor determinado<br>Estación El Milagro |
| --- | --- | --- |
| **Velocidad Viento (10 m)** | BIAS | 0,39 m/s |
| **Velocidad Viento (10 m)** | Error absoluto medio | 1,05 m/s |
| **Velocidad Viento (10 m)** | RMSE | 1,41 m/s |
| **Dirección Viento (°)** | BIAS | 6,086° |
| **Dirección Viento (°)** | Error absoluto<br>medio | 57,69° |
| **Dirección Viento (°)** | RMSE | 83,05° |
| **Temperatura Superficial (2 m)** | BIAS | 0,12 K |
| **Temperatura Superficial (2 m)** | Error absoluto<br>medio | 3,26 K |
| **Temperatura Superficial (2 m)** | RMSE | 3,9 K |
| **Humedad** | BIAS | 11,56 % |
| **Humedad** | Error absoluto<br>medio | 17,14 % |
| **Humedad** | RMSE | 21,41 % |

**Tabla 22.: ** Receptores discretos.**

| Identificador | Altura<br>m.s.n.m<br>(m) | Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario base (m) | Distancia al límite<br>de la planta<br>operativa Agricovial<br>- Escenario<br>proyectado (m) | Localización<br>según Sector | Coordenadas UTM<br>Datum WGS 84 Huso 19<br>UTMx (m) UTMy (m) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Re1** | 492 | 1.151 | 1.151 | Romeral | 334.978 | 6.271.787,1 |
| **Re2** | 497 | 810 | 810 | Romeral | 335.619,3 | 6.272.204 |
| **Re3** | 500 | 839 | 839 | Romeral | 335.707,6 | 6.272.250,2 |
| **Re4** | 486 | 880 | 880 | Romeral | 335.950,8 | 6.272.217,9 |
| **Re5** | 501 | 703 | 703 | Romeral | 336.047,3 | 6.272.344,2 |
| **Re6** | 501 | 1.109 | 1.109 | Romeral | 335.454,1 | 6.272.542,3 |
| **Re7** | 499 | 833 | 833 | Romeral | 335.294,1 | 6.273.225,8 |
| **Re8** | 503 | 1.521 | 1.521 | Romeral | 335.340 | 6.273.413,3 |
| **Re9** | 501 | 793 | 793 | Romeral | 335.374,4 | 6.273.622,5 |
| **Re10** | 490 | 873 | 873 | Lo Herrera | 335.781,1 | 6.273.544,1 |
| **Re11** | 494 | 1.789 | 2.698 | Lo Herrera | 334.689,8 | 6.275.195,7 |
| **Re12** | 492 | 1.927 | 2.852 | Lo Herrera | 335.284 | 6.274.935,1 |

**Tabla 23.: ** Descripción receptores discretos.**

| Identificador | Descripción | Tipología uso suelo |
| --- | --- | --- |
| Receptor 1 | Residencia | Áreas de interés agropecuario exclusivo. |
| Receptor 2 | Residencia | Áreas de interés agropecuario exclusivo. |
| Receptor 3 | Residencia, localizada en Las brisas | Áreas de interés agropecuario exclusivo. |
| Receptor 4 | Residencia localizada dentro del<br>Parque río Maipo | Parque río Maipo |
| Receptor 5 | Residencia, localizada en el Camino<br>Romeral | Áreas de interés agropecuario exclusivo. |
| Receptor 6 | Bodega | Áreas de interés agropecuario exclusivo. |
| Receptor 7 | Residencia | Áreas de interés agropecuario exclusivo. |
| Receptor 8 | Residencia localizada en El Barrancón | Áreas de interés agropecuario exclusivo. |

**Tabla 24.: ** Concentración ambiental de olor en receptores discretos (escenario base - Percentil 98).**

| Receptores | Concentración en<br>inmisión (OU/m3) | Límite establecido por<br>normativa (OU/m3) | Cumplimiento del límite<br>establecido por normativa |
| --- | --- | --- | --- |
| **Re1** | 0,2 | 8 | Sí |
| **Re2** | 0,6 | 8 | Sí |
| **Re3** | 0,6 | 8 | Sí |
| **Re4** | 0,5 | 2 | Sí |
| **Re5** | 0,7 | 8 | Sí |
| **Re6** | 0,4 | 8 | Sí |
| **Re7** | 0,6 | 8 | Sí |
| **Re8** | 0,4 | 8 | Sí |
| **Re9** | 0,6 | 8 | Sí |
| **Re10** | 4,5 | 8 | Sí |
| **Re11** | 2,3 | 8 | Sí |
| **Re12** | 1,9 | 8 | Sí |
| **Re13** | 2,2 | 8 | Sí |
| **Re14** | 2,8 | 8 | Sí |
| **Re15** | 3,3 | 8 | Sí |

**Tabla 25.: ** Concentración ambiental de olor en receptores discretos (escenario proyectado - Percentil 98).**

| Receptores | Concentración en<br>inmisión (OU/m3) | Límite establecido por<br>normativa (OU/m3) | Cumplimiento del límite<br>establecido por normativa |
| --- | --- | --- | --- |
| **Re1** | 0,2 | 8 | Sí |
| **Re2** | 0,6 | 8 | Sí |
| **Re3** | 0,5 | 8 | Sí |
| **Re4** | 0,5 | 2 | Sí |
| **Re5** | 0,6 | 8 | Sí |
| **Re6** | 0,4 | 8 | Sí |
| **Re7** | 0,6 | 8 | Sí |
| **Re8** | 0,3 | 8 | Sí |
| **Re9** | 0,6 | 8 | Sí |
| **Re10** | 0,3 | 8 | Sí |
| **Re11** | 0,1 | 8 | Sí |
| **Re12** | 0,1 | 8 | Sí |
| **Re13** | 0,1 | 8 | Sí |
| **Re14** | 0,1 | 8 | Sí |
