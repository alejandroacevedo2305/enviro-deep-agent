---
title: Informe Evaluación Impacto Olores_Agricovial_Actualizado_Rev1 WSP+Leo A_Rev2 PFR_vFC vJD_Rev0_PFR_121021
author: Jorge Dumont
date: D:20211012152039Z00'00'
language: es
type: report
pages: 220
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

**Agosto 2021**

|CONTROL DE REVISIÓN|Col2|Col3|
|---|---|---|
|Versión|Revisor|Fecha|
|Rev_0|Jorge Dumont|12/10/2021<br>31/08/2021|
|Rev_02|Jorge Dumont|25/08/2021|
|Rev_01|Jorge Dumont|13/07/2021|

2

**CONFIDENCIALIDAD**

La información contenida en este documento es de carácter confidencial y exclusivo para

el individuo o entidad a la que van dirigidas. De manera que, si usted no es el destinario

individualizado y por error recibiera este documento, le agradeceremos notificar al

remitente y borrar este documento junto con todos sus archivos digitales.

3

## Resumen Ejecutivo

El presente proyecto corresponde a la evaluación del impacto odorífico del sector

productivo de Agricovial, ubicado en la comuna de San Bernardo, Región Metropolitana

de Santiago de Chile. El sector productivo se compone por los planteles de Crianza,

Postura, las zonas de acopio de GAP y otras instalaciones de apoyo.

En el escenario base, las fuentes de emisión corresponden a: pabellones de postura con

ventilación forzada (PPVF), pabellones de postura con ventilación natural (PPVN),

pabellones de crianza con ventilación forzada (PCVF), lombrifiltro sector planta de Riles,
sector de acopio de residuos orgánicos (Seac) y la zona de acopio de guano (ZAG) sector

Lo Herrera.

Dado que el escenario proyectado incorpora modificaciones del proceso de tratamiento

de GAP y de la operación de los pabellones de postura, para este caso las fuentes de

emisión corresponden a: chimeneas a la salida de los PPVF, extractores de los PPVF, PPVN,

PCVF, lombrifiltro, Seac, secadora Kohshin y secador de guano de ave de postura. No se

consideraron las emisiones correspondientes al acopio de guano seco de aves de postura

ya que, en el escenario proyectado, esto se realiza en galpones cerrados, dentro del sector

El Romeral.

Para determinar las tasas de emisión de las diferentes fuentes identificadas, se emplearon

datos y antecedentes disponibles en los informes de GCA ambiental, del “Estudio de

fuentes y procesos generadores de olor para el sector productor de huevos de ChileAcuerdo de Producción Limpia II” (Chilehuevos 2021) y de mediciones realizadas en

Empresa Avícola Zona Central.

La modelación de las emisiones de olor se realizó siguiendo las recomendaciones de la

guía del SEIA, utilizando para ello el modelo CALPUFF y empleando como base, la

meteorología generada por el modelo WRF para el año 2020. La extensión del dominio de

simulación es de 60x60 km con una resolución de 1 km, dentro del cual se incluye la

estación meteorológica El Milagro de la Dirección General de la Aeronáutica Civil para

validar los datos del modelo WRF.

La meteorología modelada en la localización del proyecto, indica que la dirección de

viento procede del noreste durante la mañana y se direcciona desde el suroeste en horas
de la noche, con una velocidad promedio de 2,37 m/s. La temperatura promedio es de

14,73°C y la humedad relativa promedio es del 80,09%.

En la fase de operación del escenario base en el sector Romeral, el percentil 98 de la

concentración horaria de las emisiones muestra un área de influencia de la isolínea de

concentración 3 OU/m [3] que se extiende fuera del perímetro de la planta y una isolínea de

4

concentración de 14 OU/m [3] que se encuentra localizado cerca del perímetro de la planta

(sector postura con un radio de alcance máximo de 489 m en dirección noroeste).

En la fase de operación del escenario base en el sector Lo Herrera, el percentil 98 de la

concentración horaria de las emisiones muestra que principalmente las isolíneas se
localizan sobre la zona de acopio de GAP, con la isolínea de concentración de 14 OU/m [3]
que se extiende fuera de la zona de acopio de GAP (posee un radio de alcance máximo de

1.353 m en dirección nor noroeste).

Se identificaron en total 56 receptores discretos, con distancias desde el límite de la

planta de 84 a 1.927 m. De ellos, 16 receptores son capaces de percibir posibles emisiones

procedentes de los tres sectores.

**Tabla 1.** Concentración ambiental de olor en receptores discretos (escenario base).

5

|Receptores|Concentración en inmisión (OU/m3)|Localización según Sector|
|---|---|---|
|**Re1**|0,2|Romeral|
|**Re2**|0,6|Romeral|
|**Re3**|0,6|Romeral|
|**Re4**|0,5|Romeral|
|**Re5**|0,7|Romeral|
|**Re6**|0,4|Romeral|
|**Re7**|0,6|Romeral|
|**Re8**|0,4|Romeral|
|**Re9**|0,6|Romeral|
|**Re10**|4,5|Lo Herrera|
|**Re11**|2,3|Lo Herrera|
|**Re12**|1,9|Lo Herrera|
|**Re13**|2,2|Lo Herrera|
|**Re14**|2,8|Lo Herrera|
|**Re15**|3,3|Lo Herrera|
|**Re16**|5|Lo Herrera|
|**Re17**|1,8|Lo Herrera|
|**Re18**|1,7|Lo Herrera|
|**Re19**|4,3|Lo Herrera|
|**Re20**|14,1|Lo Herrera|
|**Re21**|34|Lo Herrera|
|**Re22**|0,4|Lo Herrera|
|**Re23**|0,5|Lo Herrera|
|**Re24**|0,4|Lo Herrera|
|**Re25**|0,4|Lo Herrera|
|**Re26**|0,4|Lo Herrera|
|**Re27**|0,4|Lo Herrera|
|**Re28**|0,5|Lo Herrera|

|Re29|0,6|Lo Herrera|
|---|---|---|
|**Re30**|0,6|Lo Herrera|
|**Re31**|0,6|Lo Herrera|
|**Re32**|0,5|Lo Herrera|
|**Re33**|0,5|Lo Herrera|
|**Re34**|0,4|Lo Herrera|
|**Re35**|0,4|Lo Herrera|
|**Re36**|0,3|Lo Herrera|
|**Re37**|0,3|Lo Herrera|
|**Re38**|0,3|Lo Herrera|
|**Re39**|0,4|Lo Herrera|
|**Re40**|0,4|Lo Herrera|
|**Re41**|0,4|Lo Herrera|
|**Re42**|0,4|Lo Herrera|
|**Re43**|0,5|Lo Herrera|
|**Re44**|0,6|Lo Herrera|
|**Re45**|0,7|Lo Herrera|
|**Re46**|0,9|Lo Herrera|
|**Re47**|2,9|Lo Herrera|
|**Re48**|2,3|Romeral|
|**Re49**|1,2|Romeral|
|**Re50**|12,1|Romeral|
|**Re51**|0,4|Romeral|
|**Re52**|0,4|Romeral|
|**Re53**|0,4|Romeral|
|**Re54**|0,6|Romeral|
|**Re55**|0,7|Romeral|
|**Re56**|0,3|Romeral|

De acuerdo a la ley de los países bajos ( _Wet geurhinder en veehouderij, 2013_ ) que fue

empleada para evaluar el potencial impacto del proyecto en el escenario base, en el

sector Romeral no hay receptores con concentraciones en inmisión P98 superiores a 14
OU/m [3] .

En el escenario base en el sector Lo Herrera, se identificaron dos receptores que superan

los niveles de concentración en inmisión definidos por la normativa, correspondientes a

los receptores 20 y 21, que se encuentran localizados a 369 y 300 m del perímetro de las
fuentes de emisión. El receptor 20 tiene una concentración en inmisión de 14,1 OU/m [3] y
el receptor 21 una concentración en inmisión de 34 OU/m [3] .

Debido a que en el escenario proyectado se elimina la zona de acopio de GAP del sector Lo

Herrera, la distancia de los 56 receptores discretos a la fuente de emisión cambia, siendo

6

desde los 84 a 2.852 m. De los 56 receptores discretos localizados en el dominio del

estudio, 15 receptores son capaces de detectar las emisiones procedentes del sector

postura y sector de crianza.

**Tabla 2.** Concentración ambiental de olor en receptores discretos (escenario proyectado).

7

|Receptores|Concentración en inmisión (OU/m3)|Localización según Sector|
|---|---|---|
|**Re1**|0,4|Romeral|
|**Re2**|1,5|Romeral|
|**Re3**|1,3|Romeral|
|**Re4**|1,1|Romeral|
|**Re5**|1,6|Romeral|
|**Re6**|0,9|Romeral|
|**Re7**|1,3|Romeral|
|**Re8**|0,6|Romera|
|**Re9**|1,4|Romeral|
|**Re10**|0,8|Lo Herrera|
|**Re11**|0,3|Lo Herrera|
|**Re12**|0,3|Lo Herrera|
|**Re13**|0,3|Lo Herrera|
|**Re14**|0,3|Lo Herrera|
|**Re15**|0,5|Lo Herrera|
|**Re16**|0,3|Lo Herrera|
|**Re17**|1,7|Lo Herrera|
|**Re18**|1,9|Lo Herrera|
|**Re19**|0,9|Lo Herrera|
|**Re20**|1,3|Lo Herrera|
|**Re21**|0,6|Lo Herrera|
|**Re22**|0,3|Lo Herrera|
|**Re23**|0,3|Lo Herrera|
|**Re24**|0,3|Lo Herrera|
|**Re25**|0,3|Lo Herrera|
|**Re26**|0,3|Lo Herrera|
|**Re27**|0,3|Lo Herrera|
|**Re28**|0,3|Lo Herrera|
|**Re29**|0,4|Lo Herrera|
|**Re30**|0,4|Lo Herrera|
|**Re31**|0,4|Lo Herrera|
|**Re32**|0,4|Lo Herrera|
|**Re33**|0,4|Lo Herrera|
|**Re34**|0,4|Lo Herrera|
|**Re35**|0,3|Lo Herrera|
|**Re36**|0,3|Lo Herrera|

|Re37|0,3|Lo Herrera|
|---|---|---|
|**Re38**|0,3|Lo Herrera|
|**Re39**|0,4|Lo Herrera|
|**Re40**|0,4|Lo Herrera|
|**Re41**|0,4|Lo Herrera|
|**Re42**|0,4|Lo Herrera|
|**Re43**|0,5|Lo Herrera|
|**Re44**|0,6|Lo Herrera|
|**Re45**|0,7|Lo Herrera|
|**Re46**|0,6|Lo Herrera|
|**Re47**|1,9|Lo Herrera|
|**Re48**|2,9|Romeral|
|**Re49**|1,7|Romeral|
|**Re50**|12,7|Romeral|
|**Re51**|0,6|Romeral|
|**Re52**|0,7|Romeral|
|**Re53**|0,8|Romeral|
|**Re54**|1,1|Romeral|
|**Re55**|1,4|Romeral|
|**Re56**|0,5|Romeral|

Considerando la ley de los países bajos ( _Wet geurhinder en veehouderij_, 2013), en ninguno

de los receptores localizados en el sector Romeral o el sector Lo Herrera en el escenario
proyectado se supera el límite establecido de concentración en inmisión de 14 OU/m [3], por

lo que, el proyecto de Agricovial no genera impacto en el área colindante del proyecto,

generando una disminución en concentración en inmisión en los receptores 20 y 21 del

escenario base de un 90,8 y un 98,2% respectivamente.

8

# Índice

1. Introducción 14

1.1. Objetivo 14

1.2. Dominio de Estudio 15

2. Inventario de Emisiones 17

2.1. Factores de emisión - Escenario base 20

2.2. Factores de emisión - Escenario proyectado 21

2.3. Nivel de Actividad 22

2.3.1. Fase de Operación - Escenario base 22

2.3.2. Fase de Operación - Escenario Proyectado 23

2.4. Resultados Inventario de Emisión 25

2.4.1. Inventario de Emisión - Escenario base 25

2.4.2. Inventario de Emisión - Escenario proyectado 26

2.5. Tipología de Proyecto 27

3. Análisis Meteorológico de Datos Observados y Modelados 28

3.1. Estación El Milagro 28

3.1.1. Viento 28

**3.1.1.1.** **Velocidad del Viento** 32

**3.1.1.2.** **Dirección del viento** 34

3.1.2. Temperatura 37

3.1.3. Humedad Relativa 40

3.2 Análisis de la incertidumbre 43

3.2.1 Incertidumbre en Estación El Milagro 44

4. Estimación del Impacto de las Emisiones de Olor 45

4.1. Receptores 45

4.2. Modelación de Impactos por Emisiones de Olor escenario actual 48

4.3. Modelación de Impactos por Emisiones de Olor escenario proyectado 50

5 Conclusiones 52

A) APENDICE 1 - Reporte de muestreo AQOM Agricovial 53

A.1) Sector Romeral 53

9

A.2) Sector Lo Herrera 80

A.3) Empresa Avícola Zona Central 107

B) APENDICE 2 - Informe de APL II Chilehuevos 129

C) APENDICE 3 - Archivos de la Modelación 219

D) APENDICE 4 - Bibliografía 220

10

## Índice de Figuras

**Figura 1.** Dominio de Estudio del proyecto Mejoramiento Tecnológico Operaciones

Agricovial. 15

**Figura 2.** Localización de los perímetros productivos de Agricovial. 16

**Figura 3.** Localización de fuentes de emisión de olor sector Romeral (escenario base). 18
**Figura 4.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario base). 18

**Figura 5.** Localización de fuentes de emisión de olor sector Romeral (escenario

proyectado) 20

**Figura 6.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario

proyectado). 20

**Figura 7.** Localización de la estación meteorológica El Milagro. 28

**Figura 8.** Rosa de viento año 2020: datos observados en estación El Milagro (izquierda) y

modelados WRF (derecha). 29

**Figura 9.** Rosa de viento año 2020: Horario 08:00 a 18:00. Datos observados en estación El

Milagro (izquierda) y modelados WRF (derecha). 30

**Figura 10.** Rosa de viento año 2020: Horario 18:00 a 08:00. Datos observados en estación

El Milagro (izquierda) y modelados WRF (derecha). 30
**Figura 11.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos

observados en estación El Milagro). 31
**Figura 12.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos

modelados en estación El Milagro). 31
**Figura 13.** Ciclo diario de la velocidad del viento observada en estación El Milagro (m/s)

Hora en (UTC). 32
**Figura 14.** Ciclo diario de la velocidad del viento modelada en estación El Milagro (m/s)

Hora en (UTC). 32

**Figura 15.** Serie de tiempo de la velocidad del viento observada en estación El Milagro
(m/s) Hora en (UTC). 33

**Figura 16.** Serie de tiempo de la velocidad del viento modelada en estación El Milagro
(m/s) Hora en (UTC). 33

**Figura 17** . Ciclo estacional de la velocidad del viento observada en estación El Milagro
(m/s) Hora en (UTC). 34

**Figura 18.** Ciclo estacional de la velocidad del viento modelada en estación El Milagro
(m/s) Hora en (UTC). 34

**Figura 19.** Ciclo diario de la dirección del viento observada en estación El Milagro (°) Hora

en (UTC). 35

**Figura 20.** Ciclo diario de la dirección del viento modelada en estación El Milagro (°) Hora
en (UTC). 35

**Figura 21.** Serie de tiempo de la dirección del viento observada en estación El Milagro (°)

Hora en (UTC). 35

11

**Figura 22.** Serie de tiempo de la dirección del viento modelada en estación El Milagro (°)

Hora en (UTC). 36

**Figura 23.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°)

(Hora en UTC). 36

**Figura 24.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°)

(Hora en UTC). 37

**Figura 25.** Ciclo diario de la temperatura observada en la estación El Milagro (°C) Hora

(UTC). 37

**Figura 26.** Ciclo diario de la temperatura modelada en la estación El Milagro (°C) Hora

(UTC). 38

**Figura 27.** Serie de tiempo de temperatura observada en la estación El Milagro (°C) Hora

(UTC). 38

**Figura 28.** Serie de tiempo de temperatura modelada en la estación El Milagro (°C) Hora
(UTC). 38

**Figura 29.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C)

Hora (UTC). 39

**Figura 30.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora

(UTC). 39

**Figura 31.** Ciclo diario de la humedad relativa observada en la estación El Milagro (%) Hora

(UTC). 40

**Figura 32.** Ciclo diario de la humedad relativa modelada en la estación El Milagro (%) Hora
(UTC). 40

**Figura 33.** Serie de tiempo de la humedad relativa observada en la estación El Milagro (%)

Hora (UTC). 41

**Figura 34.** Serie de tiempo de la humedad relativa modelada en la estación El Milagro (%)

Hora (UTC). 41

**Figura 35.** Ciclo estacional de la humedad relativa observada en la estación El Milagro (%)

Horas (UTC). 42

**Figura 36.** Ciclo estacional de la humedad relativa modelada en la estación El Milagro (%)

Horas (UTC). 42

**Figura 37.** Localización de receptores discretos del proyecto en el sector Romeral. 46

**Figura 38.** Localización de receptores discretos del proyecto en el sector Lo Herrera. 46

**Figura 39.** Concentración ambiental de olor percentil 98 en el escenario base (sector

Romeral). 49

**Figura 40.** Concentración ambiental de olor percentil 98 en el escenario base (sector Lo

Herrera). 49

**Figura 41.** Concentración ambiental de olor percentil 98 en el escenario proyectado

(sector Romeral). 51

**Figura 42.** Concentración ambiental de olor percentil 98 en el escenario proyectado

(sector Lo Herrera). 51

12

## Índice de Tablas

**Tabla 1.** Concentración ambiental de olor en receptores discretos (escenario base). 5

**Tabla 2.** Concentración ambiental de olor en receptores discretos (escenario proyectado).

7

**Tabla 3.** Coordenadas generales del perímetro del sector de postura en sector Romeral. 15

**Tabla 4.** Coordenadas generales del perímetro del sector de crianza en Lo Herrera. 16

**Tabla 5.** Coordenadas generales del perímetro del sector de acopio de GAP en Lo Herrera

(actual). 16

**Tabla 6.** Factor de emisión de fuentes de emisión de olores del escenario base. 21

**Tabla 7.** Factores de emisión de fuentes identificadas en el escenario proyectado. 22

**Tabla 8.** Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario

base). 22

**Tabla 9** . Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario

proyectado). 24

**Tabla 10.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario base). 25

**Tabla 11.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario
proyectado). 27

**Tabla 12.** Ubicación de estación meteorológica superficial El Milagro. 28

**Tabla 13.** Criterios estadísticos de aceptación de la predicción proporcionada por un

modelo meteorológico. 43

**Tabla 14.** Criterios de tolerancia de diferencia absoluta de variables modeladas. 43

**Tabla 15.** Valores de los parámetros de la predicción proporcionada por el modelo para la

Estación El Milagro. 44

**Tabla 16.** Receptores discretos. 46

13

# 1. Introducción

En el presente informe se evalúa el impacto de las emisiones de olor emitidas por el

proyecto “Mejoramiento Tecnológico Operaciones Agricovial”, ubicado en la comuna de

San Bernardo, Región Metropolitana de Santiago de Chile.

El Proyecto “Mejoramiento Tecnológico Operaciones Agricovial” consiste en evaluar las

instalaciones de producción existentes y el desarrollo de una nueva y moderna instalación

para el manejo de Guano de Ave de Postura (GAP), que buscan mejorar el desempeño

ambiental de las instalaciones que actualmente operan en la comuna, permitiendo con

ello una mejora sustentable en las operaciones.

Considerando todo lo expuesto anteriormente, los objetivos de la presentación de esta

Declaración de Impacto Ambiental son:

 - Evaluar las instalaciones actuales y que comenzaron a operar con posterioridad al

año 1997, es decir, los 3 Pabellones de Crianza y los 11 Pabellones de Postura que

actualmente superan las 60 mil gallinas (tipología de ingreso L.4.2).

 - Actualizar el manejo de gestión del Guano lo cual contempla el traslado del sector

de acopio de guano al sector de Romeral y la implementación de nuevas

tecnologías, lo que incluye nuevas obras constructivas: Líneas de Secado de Guano

y 1 Galpón para Acopio de Guano seco.

En efecto, el escenario proyectado incorpora modificaciones del proceso de tratamiento

de GAP y de la operación de los pabellones de postura. Las modificaciones del proceso de

tratamiento de GAP consideran la eliminación del sector de acopio de GAP actual en Lo

Herrera, implementando el uso de secadores de GAP y secadora Kohshin que se

localizarán en el sector Romeral y la implementación de 7 chimeneas en los pabellones de

postura de ventilación forzada, que estarán localizados en la salida de los extractores. Los

pabellones que poseerán chimeneas son:

 - Pabellón postura ventilación forzada 1 - chimeneas en ambos extremos.

 - Pabellón postura ventilación forzada 2 - chimeneas en ambos extremos.

 - Pabellón postura ventilación forzada 3 - chimenea en extremo sur.

 - Pabellón postura ventilación forzada 4 - chimenea en extremo sur.

 - Pabellón postura ventilación forzada 5 - chimenea en extremo sur

## 1.1. Objetivo

Evaluar los potenciales efectos de las emisiones de Olores del Proyecto Mejoramiento

Tecnológico Operaciones Agricovial, a través de una estimación de emisiones de olores del

sector productivo de Agricovial sector Romeral y Agricovial sector Lo Herrera, en el

escenario de operación actual y el escenario proyectado.

14

## 1.2. Dominio de Estudio

El estudio de impacto de olores se realiza en una grilla con extensión de 60 km por 60 km

y una resolución de 1 km por 1 km.

**Figura 1.** Dominio de Estudio del proyecto Mejoramiento Tecnológico Operaciones Agricovial.

**Tabla 3.** Coordenadas generales del perímetro del sector de postura en sector Romeral.

15

|Vértice|Coordenadas UTM<br>(Datum WGS 84 Huso 19)|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
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

**Tabla 4.** Coordenadas generales del perímetro del sector de crianza en Lo Herrera.

|Vértice|Coordenadas UTM<br>(Datum WGS 84 Huso 19)|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|**A **|336166,2|6273729,7|
|**B **|336104,5|6273176,1|
|**C **|336668,8|6273172,5|
|**D **|336695,6|6273627,5|

**Tabla 5.** Coordenadas generales del perímetro del sector de acopio de GAP en Lo Herrera (actual).

|Vértice|Coordenadas UTM<br>(Datum WGS 84 Huso 19)|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|**A **|335503,5|6274557,0|
|**B **|335453,1|6274100,1|
|**C **|336177,9|6273870,7|
|**D **|336234,2|6274241,7|

**Figura 2.** Localización de los perímetros productivos de Agricovial.

16

# 2. Inventario de Emisiones

El presente proyecto corresponde a la evaluación del impacto odorífico del sector

productivo de Agricovial sector Romeral y sector Lo Herrera, en el escenario de operación

actual y el escenario proyectado. Siguiendo los lineamientos recomendados para definir

los datos de entrada que se detallan en la “Guía para el uso de modelos de calidad del aire

en el SEIA” (2012), en esta sección se procede a identificar las fuentes de emisión de olor.

Cabe notar que para el escenario base, se hicieron mediciones de las fuentes en operación

que se encuentran en los anexos A.1) Sector Romeral y A.2) Sector Lo Herrera,

determinando la concentración y su factor de emisión, y se siguió el lineamiento definido

en la “Guía para la predicción y evaluación de impactos por olor en el SEIA” (2017), en el

cual se define “El uso de factores de emisión que es aconsejable solo en proyectos nuevos

y siempre y cuando no se cuente con emisiones de referencia, en este caso se deben

utilizar preferentemente factores publicados por agencias estatales de protección del

medio ambiente, normas técnicas o guías técnicas relacionadas”, para determinar el

factor de emisión del sector de acopio de residuos orgánicos (escenario base), de la

secadora de guano (escenario proyectado) y de la secadora Kohshin (escenario
proyectado).

Las principales fuentes de emisión de olor del escenario base se corresponden con:

 - Pabellones de postura con ventilación forzada (PPVF).

 - Pabellones de postura con ventilación natural (PPVN).

 - Pabellones de crianza con ventilación forzada (PCVF).

 - Lombrifiltro sector planta de Riles.

 - Sector de acopio de residuos orgánicos (Seac).

 - Zona de acopio de guano (ZAG).

Cabe notar que, para las mediciones, se determinó el factor de emisión de los PPVN en la

zona superior (jaulas) y en la zona inferior (cama de guano a nivel de piso). Para las

mediciones y en consecuente, las modelaciones, la ZAG fue separada en ZAG fresco, ZAG

activo y ZAG maduro, acorde a las diferentes etapas de maduración en las cuales se

encontraban las pilas.

A continuación, se presenta la localización de las fuentes del escenario base.

17

**Figura 3.** Localización de fuentes de emisión de olor sector Romeral (escenario base).

**Figura 4.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario base).

Para aquellas fuentes de emisión que se mantienen en el escenario proyectado, se

emplean los factores de emisión y concentraciones de olor obtenidos durante el

muestreo. Para aquellas fuentes nuevas y en consideración de que no se poseen datos de

medición de Agricovial, siguiendo la “Guía para la predicción y evaluación de impactos por

olor en el SEIA”, se empleó antecedentes levantados en el “Estudio de fuentes y procesos

18

generadores de olor para el sector productor de huevos de Chile - Acuerdo de Producción

Limpia II” (Chilehuevos 2021. Disponible en el APENDICE 2 - Informe de APL II

Chilehuevos) y las mediciones realizadas al secador de guano de Empresa Avícola Zona

Central (presentes en el anexo A.3) Empresa Avícola Zona Central).

Mediante los datos obtenidos de Empresa Avícola Zona Central, se procedió a estimar la

Tasa de Estimación de Olores (TEO) del secador de guano de aves de postura,

determinando a través de un balance de flujos y concentraciones de olor, la TEO que se

remueve desde las pilas de GAP tratadas por el equipo que tiene una capacidad de tratar

el GAP de 200.000 aves de postura y estimando a partir de este, la TEO de 1.000.000 aves.

Las fuentes de emisión de olor identificadas y modeladas para el escenario proyectado

corresponden a:

 - Chimeneas a la salida de los PPVF (N°1 ambos extremos, N°2 ambos extremos, N°3

sección sur, N°4 sección sur y N°5 sección sur).

 - Extractores de los PPVF (N°4 sección norte, N°5 sección norte, N°6 ambos

extremos y N°7 ambos extremos).

 - PPVN.

 - PCVF.

 - Lombrifiltro planta de Riles.

 - Seac.

 - Secadora Kohshin.

 - Secador de guano de ave de postura.

Cabe notar que el acopio de guano de aves de postura en el escenario proyectado se

realiza en galpones cerrados, por lo que para efectos de la modelación y considerando de

que se encuentran cerrados, no son fuentes de emisión a modelar. A continuación, se

presenta la localización de las fuentes del escenario proyectado.

19

**Figura 5.** Localización de fuentes de emisión de olor sector Romeral (escenario proyectado)

**Figura 6.** Localización de fuentes de emisión de olor sector Lo Herrera (escenario proyectado).

## 2.1. Factores de emisión - Escenario base

En esta sección se presentan los factores de emisión (FE) de las fuentes de emisión de

olores, calculados a partir de la concentración de olor medida por GCA Ambiental (anexo

A.1) Sector Romeral y A.2) Sector Lo Herrera).

20

Las mediciones se realizaron a 1 PPVF, 1 PPVN (sección jaulas y de cama), lombrifiltro, 1

PCVF y a las pilas de guano de ave fresco, activo y maduro. Por lo que, a partir de los datos

medidos, se homologa los FE para otras fuentes del mismo tipo.

**Tabla 6.** Factor de emisión de fuentes de emisión de olores del escenario base.

|Fuente|CO (OU/m3)|FE (OU/(m2·s))|Tipo fuente|
|---|---|---|---|
|**PPVF (medición en**<br>**extractor)**|177|--|Puntual|
|**PPVN sector jaulas**|148|11,3|Difusa|
|**PPVN sector cama**<br>**guano**|653|5,4|Difusa|
|**PCVF (medición en**<br>**extractor)**|241|--|Puntual|
|**Lombrifiltro**|129|1,08|Difusa|
|**Zona acopio residuos**<br>**orgánicos**|--|18,71|Difusa|
|**Pilas de guano fresco**|729|6,07|Difusa|
|**Pilas de guano activo**|1.202|10,02|Difusa|
|**Pilas de guano**<br>**maduro**|577|4,80|Difusa|

**Fuente** : Informe de GCA Ambiental, 2020 e Informe de GCA Ambiental, 2021.

De acuerdo a antecedentes disponibles del “Estudio de fuentes y procesos generadores de

olor para el sector productor de huevos de Chile - Acuerdo de Producción Limpia II”

(Chilehuevos 2021 disponible en APENDICE 2 - Informe de APL II Chilehuevos), durante el

volteo de las pilas activas, el factor de emisión incrementa en 4 veces. Se emplea este

antecedente para determinar la TEO de las pilas de guano activo durante su volteo.

La ecuación para la estimación de emisiones de una fuente dada es la siguiente:

! = # ∙%!

Donde:

!= Tasa de emisión.

#= Nivel de actividad.

%!= Factor de emisión.

## 2.2. Factores de emisión - Escenario proyectado

En esta sección se presentan los factores de emisión (FE) de las fuentes de emisión de
olores, calculados a partir de la concentración de olor medida por GCA Ambiental (anexo

A.3) Empresa Avícola Zona Central). Los datos del cálculo de la tasa de emisión del secador

se presentan más adelante.

21

Para efectos de la estimación de la TEO desde las chimeneas del PPVF, se estima que se

mantiene la TEO del escenario base.

**Tabla 7.** Factores de emisión de fuentes identificadas en el escenario proyectado.

|Fuente|CO (OU/m3)|FE (OU/(m2·s))|Tipo fuente|
|---|---|---|---|
|**PPVF (medición en**<br>**extractor)**|177|--|Puntual|
|**PPVN sector jaulas**|148|11,3|Difusa|
|**PPVN sector cama**<br>**guano**|653|5,4|Difusa|
|**PCVF (medición en**<br>**extractor)**|241|--|Puntual|
|**Lombrifiltro**|129|1,08|Difusa|
|**Zona acopio residuos**<br>**orgánicos**|--|18,71|Difusa|
|**Secadora Kohshin**|--|5,92|Difusa|

**Fuente** : Informe del GCA Ambiental 2020, e Informe de GCA Ambiental, 2021.

## 2.3. Nivel de Actividad

La estimación de emisiones de olor, tal como se mencionó previamente, se realiza durante

la fase de operación de la planta de Agricovial (escenario base y proyectado).

## 2.3.1. Fase de Operación - Escenario base

Para determinar la tasa de emisión de las fuentes en el escenario base, se emplea las

superficies de las fuentes medidas, número de extractores y operación durante el año.

**Tabla 8.** Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario base).

|Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extracto operación<br>(m) (m2) res|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVF 1 -**<br>**extractor**|1,7|2|26,1|1,3|36|Extractores -<br>Verano y Primavera: 8<br>horas día 100% y 16<br>horas día 25%.<br>Otoño e Invierno: 6 horas<br>día 100% y 18 horas día<br>25%.|
|**PPVF 2 -**<br>**extractor**|**PPVF 2 -**<br>**extractor**|**PPVF 2 -**<br>**extractor**|**PPVF 2 -**<br>**extractor**|1,5|30|30|
|**PPVF 3 -**<br>**extractor**|**PPVF 3 -**<br>**extractor**|**PPVF 3 -**<br>**extractor**|**PPVF 3 -**<br>**extractor**|1,3|40|40|
|**PPVF 4 -**<br>**extractor**|**PPVF 4 -**<br>**extractor**|**PPVF 4 -**<br>**extractor**|**PPVF 4 -**<br>**extractor**|1,3|36|36|
|**PPVF 5 -**<br>**extractor**|**PPVF 5 -**<br>**extractor**|**PPVF 5 -**<br>**extractor**|**PPVF 5 -**<br>**extractor**|1,3|52|52|
|**PPVF 6 -**<br>**extractor**|**PPVF 6 -**<br>**extractor**|**PPVF 6 -**<br>**extractor**|**PPVF 6 -**<br>**extractor**|1,4|42|42|
|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|1,4|42|42|
|**PPVN 1 sector**<br>**jaulas**|--|2|--|222|--|Cortinas -<br>Noviembre a marzo: 50%|

22

|Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extracto operación<br>(m) (m2) res|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVN 2 sector**<br>**jaulas**|--|||222|--|abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs.|
|**PPVN 3 sector**<br>**jaulas**|--|--|--|177|--|--|
|**PPVN 4 sector**<br>**jaulas**|--|--|--|228|--|--|
|**PPVN 1 sector**<br>**cama guano**|--|0|--|2.368|--|Cortinas -<br>Noviembre a marzo:<br>100% abiertas 24 horas.<br>Abril a Octubre: 50% 12<br>horas y 20% 12 hrs.|
|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|2.325,1|--|--|
|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|1.642,6|--|--|
|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|1.757,1|--|--|
|**PCVF 1 -**<br>**extractor**|1,9|2|27,1|1,4|14|Extractores -<br>operación 100% durante<br>el día y 40% durante<br>noche.|
|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|1,4|14|14|
|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|1,4|15|15|
|**Lombrifiltro**|--|1,5|--|1156|--|Emisión continua.|
|**Zona acopio**<br>**residuos**<br>**orgánicos**|--|2|--|75|--|Emisión continua.|
|**Pilas de guano**<br>**fresco**|--|1,1|--|375,8|--|Octubre a Junio 8 pilas<br>semanal y julio a<br>septiembre 15 pilas<br>semanal.|
|**Pilas de guano**<br>**activo**|--|1|--|341,6|--|Octubre a Junio 12 pilas<br>semanal y julio a<br>septiembre 15 pilas<br>semanal. Volteo de pilas<br>4 horas al día.|
|**Pilas de guano**<br>**maduro**|--|0,9|--|273,3|--|Octubre a Junio 12 pilas<br>semanal y julio a<br>septiembre 20 pilas<br>semanal.|

## 2.3.2. Fase de Operación - Escenario Proyectado

Para determinar la tasa de emisión de las fuentes en el escenario proyectado, se emplea

las superficies de las fuentes medidas, número de extractores y operación durante el año.

Cabe destacar, tal como se mencionó previamente, que, para efectos del cálculo de la TEO

de los PPVF con chimenea, se emplearon los antecedentes disponibles en el escenario

base de CO por extractor. Para efectos de la modelación, se consideró esta emisión como

fuente puntual que se localiza a la misma altura del techo de los PPVF.

23

**Tabla 9** . Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario proyectado).

|Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extractor operación<br>(m) (m2) es|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PPVF 1 -**<br>**chimeneas**|0,9|9|26,1|42,5|36|Extractores -<br>Verano y Primavera: 8<br>horas día 100% 16 horas<br>día 25%.<br>Otoño e Invierno: 6<br>horas día 100% y 18<br>horas día 25%.<br> <br> <br> <br>|
|**PPVF 2 -**<br>**chimeneas**|0,9|7,6|7,6|42,5|30|30|
|**PPVF 3 -**<br>**chimenea**|2,7|7,2|7,2|32,5|40|40|
|**PPVF 4 -**<br>**chimenea**|0,9|7,5|7,5|42,5|18|18|
|**PPVF 4 -**<br>**extractor**|1,7|2|2|1,3|18|18|
|**PPVF 5 -**<br>**chimenea**|1,6|8|8|35|26|26|
|**PPVF 5 -**<br>**extractor**|1,7|2|2|1,3|26|26|
|**PPVF 6 -**<br>**extractor**|1,7|2|2|1,4|42|42|
|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|**PPVF 7 -**<br>**extractor**|1,4|42|42|
|**PPVN 1 sector**<br>**jaulas**|--|2|--|222|--|Cortinas -<br>Noviembre a marzo: 50%<br>abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs.<br>|
|**PPVN 2 sector**<br>**jaulas**|**PPVN 2 sector**<br>**jaulas**|**PPVN 2 sector**<br>**jaulas**|**PPVN 2 sector**<br>**jaulas**|222|--|--|
|**PPVN 3 sector**<br>**jaulas**|**PPVN 3 sector**<br>**jaulas**|**PPVN 3 sector**<br>**jaulas**|**PPVN 3 sector**<br>**jaulas**|177|--|--|
|**PPVN 4 sector**<br>**jaulas**|**PPVN 4 sector**<br>**jaulas**|**PPVN 4 sector**<br>**jaulas**|**PPVN 4 sector**<br>**jaulas**|228|--|--|
|**PPVN 1 sector**<br>**cama guano**|--|0|--|2.368|--|Cortinas -<br>Noviembre a marzo:<br>100% abiertas 24 horas.<br>Abril a Octubre: 50% 12<br>horas y 20% 12 hrs.<br>|
|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|**PPVN 2 sector**<br>**cama guano**|2.325,1|--|--|
|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|**PPVN 3 sector**<br>**cama guano**|1.642,6|--|--|
|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|**PPVN 4 sector**<br>**cama guano**|1.757,1|--|--|
|**PCVF 1 -**<br>**extractor**|1,9|2|27,1|1,4|14|Extractores -<br>operación 100% durante<br>el día y 40% durante<br>noche.<br>|
|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|**PCVF 2 -**<br>**extractor**|1,4|14|14|
|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|**PCVF 3 -**<br>**extractor**|1,4|15|15|
|**Lombrifiltro**|--|1,5|--|1.156|--|Emisión continua.|
|**Zona acopio**<br>**residuos**<br>**orgánicos**|--|2|--|75|--|Emisión continua.|
|**Secadora**<br>**Kohshin**|--|1|--|2.716|--|Emisión continua.|
|**Secador Guano**<br>**ave de postura**|1,61|9,4|15,1|48|--|Horas operación -<br>22 h enero, febrero,|

24

|Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extractor operación<br>(m) (m2) es|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||noviembre y diciembre.<br>21 h marzo y octubre.<br>19 h abril y septiembre.<br>17 h mayo y agosto.<br>15 h junio y julio.|

## 2.4. Resultados Inventario de Emisión

A continuación, se presenta el inventario de emisión para el corte temporal analizado para

la emisión de olores en la fase de operación de la planta de Agricovial, para ambos

escenarios (base y proyectada).

## 2.4.1. Inventario de Emisión - Escenario base

Los resultados obtenidos de la estimación de la emisión atmosférica de olor para el

escenario base del proyecto, se presenta en la siguiente tabla.

**Tabla 10.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario base).

|Fuente|Tasa de emisión<br>1 (OU/s)|Tasa de emisión<br>2 (OU/s)|Tasa de emisión 3<br>*(OU/s)|Tasa de emisión 4<br>*(OU/s)|
|---|---|---|---|---|
|**PPVF 1**|13.722|3.431|--|--|
|**PPVF 2**|13.837|3.459|--|--|
|**PPVF 3**|15.247|3.812|--|--|
|**PPVF 4**|13.722|3.431|--|--|
|**PPVF 5**|19.821|4.955|--|--|
|**PPVF 6**|17.988|4.497|--|--|
|**PPVF 7**|17.988|4.497|--|--|
|**PPVN 1 sector jaulas**|2.519|1.134|--|--|
|**PPVN 2 sector jaulas**|2.519|1.134|--|--|
|**PPVN 3 sector jaulas**|2.008|904|--|--|
|**PPVN 4 sector jaulas**|2.587|1.164|--|--|
|**PPVN 1 sector cama**<br>**guano**|12.884|1.933|--|--|
|**PPVN 2 sector cama**<br>**guano**|12.651|1.933|--|--|
|**PPVN 3 sector cama**<br>**guano**|8.937|1.541|--|--|
|**PPVN 4 sector cama**<br>**guano**|9.561|1.985|--|--|
|**PCVF 1**|8.783|3.513|--|--|
|**PCVF 2**|8.783|3.513|--|--|
|**PCVF 3**|9.411|3.764|--|--|
|**Lombrifiltro**|1.243|1.243|--|--|
|**Zona acopio residuos**<br>**orgánicos**|369|369|--|--|
|**Pilas de guano fresco**|18.259|34.236|--|--|

25

|Fuente|Tasa de emisión<br>1 (OU/s)|Tasa de emisión<br>2 (OU/s)|Tasa de emisión 3<br>*(OU/s)|Tasa de emisión 4<br>*(OU/s)|
|---|---|---|---|---|
|**Pilas de guano activo**|41.063|51.329|164.252|205.316|
|**Pilas de guano**<br>**maduro**|15.757|26.262|--|--|
|**Total**|**269.660**|**164.037**|**--**|**--**|

**Nota:** - es la tasa de emisión durante el volteo de pilas.

## 2.4.2. Inventario de Emisión - Escenario proyectado

A continuación, se presenta la ecuación empleada para estimar la TEO que emite el

equipo secador de GAP de Empresa Avícola Zona Central, para tratar el GAP de 200.000

aves. Se empleo esta ecuación para determinar la capacidad del equipo. Cabe notar que el

equipo de Empresa Avícola Zona Central emplea la corriente de salida de los pabellones y

otra corriente contigua a la guanera, por lo que las corrientes de entrada poseen

concentración de olor. Durante la medición, se encontraban operando 8 ventiladores por

lado.

& ! ∙% ! = & "# ∙% "# + & "$ ∙% "$ + (!) %&'

Donde:

& ! = Concentración olor a la salida del secador (629 OU/m [3] ).
& "# = Concentración de olor en ventilador lado guanera (354 OU/m [3] ).
& "$ = Concentración de olor en ventilador lado pabellones (292 OU/m [3] ).
% ! = Flujo total de salida (77,3 m [3] /seg).
% "# = Flujo total entrada lado guanera (50,5 m [3] /seg).
% "$ = Flujo total entrada lado pabellones (48 m [3] /seg).

La (!) %&' para tratar el GAP de 200.000 aves es de 16.711 OU/s. Para determinar la TEO
que emitirá el equipo al tratar el GAP de 1.000.000 aves se tomaron las siguientes

consideraciones:

 - Las corrientes de aire que se alimentan al secador por los ventiladores no

provienen de los pabellones ni de la guanera. Por ello, la concentración de olor que

tienen estas corrientes se estima en 0.

 - El incremento de la TEO es proporcional al incremento del GAP a tratar.

Dadas estas consideraciones, se estima que la TEO que emite el equipo para tratar el GAP
de 1.000.000 aves es de 83.553,5 OU/s.

Los resultados obtenidos de la estimación de la emisión atmosférica de olor para el

escenario proyectado del proyecto, se presenta en la siguiente tabla.

26

**Tabla 11.** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).

|Fuente|Tasa de emisión 1 (OU/s)|Tasa de emisión 2 (OU/s)|
|---|---|---|
|**PPVF 1**|13.722|3.431|
|**PPVF 2**|13.837|3.459|
|**PPVF 3**|15.247|3.812|
|**PPVF 4**|13.722|3.431|
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
|**Secadora Kohshin**|13.313|13.313|
|**Secador de guano de ave de**<br>**postura**|83.553|83.553|
|**Total**|**291.447**|**149.079**|

## 2.5. Tipología de Proyecto

El proyecto “Mejoramiento Tecnológico Operaciones Agricovial” dada su naturaleza,

tipología y acorde al artículo 3 del RSEIA, corresponde a: “ _Agroindustrias, mataderos,_

_planteles y establos de crianza, lechería y engorda de animales, de dimensiones_

_industriales_ ”, específicamente a “ _Planteles y establos de crianza, engorda, postura y/o_

_reproducción de animales avícolas con capacidad para alojar diariamente una cantidad_

_igual o superior a..._ **”**

Considerando lo anterior, en relación con el literal g.1, cabe señalar que las partes, obras y

acciones del proyecto cuya DIA se somete a evaluación se encuentran listadas en el

artículo 3° de Reglamento del SEIA, específicamente en los literales L.4.2) y O.8). En el

caso del primer literal, se debe a que Agricovial cuenta con una cantidad superior a 60 mil

gallinas. Mientras que, con respecto al segundo literal, el ingreso se debe a la generación

de más de 30 t/día de guano, clasificado como residuo industrial sólido, producto del

funcionamiento de los pabellones.

27

# 3. Análisis Meteorológico de Datos Observados y Modelados

El estudio del impacto de olor considera la base de un año de datos meteorológicos,

correspondientes al periodo de 01-01-2020 al 31-12-2020, obtenidos de la modelación

realizada por el modelo de pronóstico WRF, contrastado frente a la estación

meteorológica El Milagro. La ubicación y localización de la estación se presenta en la

**Figura 7.** Localización de la estación meteorológica El Milagro.

**Tabla 12.** Ubicación de estación meteorológica superficial El Milagro.

|Estación|Altura<br>m.s.n.m<br>(m)|Coordenadas UTM|Col4|
|---|---|---|---|
|**Estación**|**Altura**<br>**m.s.n.m**<br>**(m)**|**Datum WGS 84 Huso 19**<br>**H **|**Datum WGS 84 Huso 19**<br>**H **|
|**Estación**|**Altura**<br>**m.s.n.m**<br>**(m)**|**Este (m)**|**Norte (m)**|
|**Estación El Milagro**|460|336.580,5|6.263.672,3|

**Fuente:** Dirección General de Aeronáutica Civil.

**Figura 7.** Localización de la estación meteorológica El Milagro.

La estación meteorológica identificada dentro del dominio cumple con el criterio de

disponibilidad de datos (al menos el 90% de los datos horarios), por lo que se utiliza la

información obtenida de la estación, para determinar los datos observados y contrastarlos

a los obtenidos por el modelo WRF.

## 3.1. Estación El Milagro 3.1.1. Viento

El análisis del viento se divide en dos secciones, que corresponden a la velocidad del

viento (magnitud) y su dirección. En la presente sección se analiza las rosas de viento y la

frecuencia de las velocidades para los datos observados y los obtenidos por el modelo

WRF. En las subsecciones siguientes, se presenta el análisis del ciclo diario de la velocidad

28

del viento, series de tiempo de la velocidad y dirección del viento y los ciclos estacionales

de la velocidad y dirección del viento.

Para el periodo 2020, los datos de la estación El Milagro, presentan una velocidad
promedio del viento de 1,98 (m/s), con una frecuencia de 12,28% de vientos calmos
(velocidad inferior a 0,5 m/s).

**Figura 8.** Rosa de viento año 2020: datos observados en estación El Milagro (izquierda) y modelados WRF

(derecha).

A partir de la rosa de viento de los datos observados, presentada en la **Figura 8** durante el

periodo 2020 se puede observar una predominancia de vientos provenientes del este, con
velocidades que fluctúan entre 0 hasta los 3,6 m/s. Los vientos de mayor intensidad, entre
3,6 a 11,1 m/s, provienen del oeste.

Para el periodo 2020, los datos modelados WRF para la estación El Milagro ( **Figura 8** ),
presentan una velocidad promedio del viento de 2,37 m/s, con una frecuencia de un

4,97% de vientos calmos. Por su parte, la rosa de viento de los datos modelados muestra

una predominancia de vientos provenientes del nor noreste, con velocidades entre los 0,5
y 3,6 m/s, y otra tendencia proveniente del oeste, con vientos que alcanzan los 8,8 m/s.

Para visualizar las diferencias horarias entre los datos observados y modelados en la

estación meteorológica El Milagro, se presentan las rosas de viento en horario 08:00 a

18:00 y 18:00 a 08:00.

29

**Figura 9.** Rosa de viento año 2020: Horario 08:00 a 18:00. Datos observados en estación El Milagro

(izquierda) y modelados WRF (derecha).

**Figura 10.** Rosa de viento año 2020: Horario 18:00 a 08:00. Datos observados en estación El Milagro

(izquierda) y modelados WRF (derecha).

De los datos observados presentados en la **Figura 9** y **Figura 10** se aprecia que en ambos

horarios gran parte de los vientos provienen del este. Sin embargo, se observan

diferencias en la distribución de frecuencias y en las intensidades entre los intervalos

horarios seleccionados. Durante el horario de día (08:00 a 18:00) hay una mayor

proporción de vientos provenientes del sur, en relación con los vientos observados

durante el horario de noche (18:00 a 08:00).

De los datos modelados WRF presentados en la **Figura 9** y **Figura 10** se aprecia que, en el

horario de día (08:00 a 18:00) predominan vientos del nor noreste, con velocidades entre
los 0,5 hasta 5,7 m/s. Destacan también vientos provenientes del oste, que alcanzan hasta
8,8 m/s. En el horario de noche (18:00 a 08:00) predominan vientos provenientes del

30

noreste, con mismas intensidades del horario día, y otros provenientes del noroeste, en
los que aumentan las velocidades entre los 5,7 y 8,8 m/s.

**Figura 11.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos observados en

estación El Milagro).

**Figura 12.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos modelados en

estación El Milagro).

La distribución de la frecuencia de la velocidad del viento de los datos observados, que se

presentan en la **Figura 11** indica que la mayor frecuencia de la velocidad del viento se
produce en el rango 0,5 - 2,1 (m/s) con un 51,35%. Por lo tanto, de acuerdo con la escala

de Beaufort de la fuerza de los vientos, el 51,35% de las velocidades del viento se

clasifican entre ventolina y brisa muy ligera.

La distribución de la frecuencia de los datos modelados WRF, que se presentan en la
**Figura 12.** Distribución de la Frecuencia de la velocidad del viento (m/s) año 2020 (Datos

modelados en estación El Milagro)., indica que la mayor frecuencia de la velocidad del
viento se produce en el rango 0,5 - 2,1 (m/s) con un 47,22%. De acuerdo a la Escala de

31

Beaufort de la fuerza de los vientos, el 47,22% de las velocidades del viento se clasifican

entre ventolina y brisa muy ligera.

### 3.1.1.1. Velocidad del Viento

En el ciclo diario de la velocidad del viento observado ( **Figura 13** ) se puede apreciar que

las menores velocidades transcurren entre las 00:00 a 12:00 horas y las mayores

velocidades entre las 19:00 a 21:00 horas. Por su parte, en el ciclo diario de la velocidad

del viento modelado WRF ( **Figura 14** ), las menores velocidades se encuentran entre las

23:00 a 12:00 horas y las mayores velocidades entre las 19:00 a 20:00 horas.

**Figura 13.** Ciclo diario de la velocidad del viento observada en estación El Milagro (m/s) Hora en (UTC).

**Figura 14.** Ciclo diario de la velocidad del viento modelada en estación El Milagro (m/s) Hora en (UTC).

Tal como en los ciclos diarios, en las series de tiempo de la velocidad del viento observada

( **Figura 15** ) en comparación con las series de tiempo de la velocidad del viento modelada
WRF ( **Figura 16** ), se puede apreciar que existe una diferencia en la amplitud de los datos.

Particularmente, las series modeladas WRF presentan una menor amplitud de los datos.

32

**Figura 15.** Serie de tiempo de la velocidad del viento observada en estación El Milagro (m/s) Hora en (UTC).

**Figura 16.** Serie de tiempo de la velocidad del viento modelada en estación El Milagro (m/s) Hora en (UTC).

En los ciclos estacionales presentados, se pueden apreciar distribuciones mensuales

horarias similares entre los datos observados ( **Figura 17** ) y los modelados ( **Figura 18** ), pero

con una menor amplitud para el caso modelado. Particularmente, el caso modelado

presenta mayores velocidades para todos los meses, entre las 00.00 a 11:00 horas, en

relación a los datos observados.

33

**Figura 17** . Ciclo estacional de la velocidad del viento observada en estación El Milagro (m/s) Hora en (UTC).

**Figura 18.** Ciclo estacional de la velocidad del viento modelada en estación El Milagro (m/s) Hora en (UTC).

### 3.1.1.2. Dirección del viento

En el ciclo diario de la dirección del viento observada ( **Figura 19** ) se puede apreciar un

ajuste que se direcciona desde el noreste en horas de la mañana (03:00 a 10:00) y que

cambia de dirección al suroeste desde las 15:00 hasta las 22:00 horas.

El ciclo diario de la dirección del viento modelada para la estación El Milagro ( **Figura 20** )

presenta una mayor amplitud de datos, llegando casi hasta los 360°. Se puede apreciar un

ajuste que se direcciona desde el noreste en horas de la mañana (04:00 a 12:00) y que

cambia de dirección al suroeste en horas de noche (14:00 a 22:00).

34

**Figura 19.** Ciclo diario de la dirección del viento observada en estación El Milagro (°) Hora en (UTC).

**Figura 20.** Ciclo diario de la dirección del viento modelada en estación El Milagro (°) Hora en (UTC).

Tal como se puede observar en los ciclos diarios, en las series de tiempo observadas y

modeladas de la estación El Milagro ( **Figura 21** y **Figura 22** ) se puede apreciar una mayor

amplitud de variación de la dirección del viento de las series modeladas.

**Figura 21.** Serie de tiempo de la dirección del viento observada en estación El Milagro (°) Hora en (UTC).

35

**Figura 22.** Serie de tiempo de la dirección del viento modelada en estación El Milagro (°) Hora en (UTC).

En los ciclos estacionales presentados se puede apreciar una diferencia entre las

distribuciones y amplitud de los datos mensuales horarios observados **Figura 23** y los

modelados **Figura 24** . Esto indica que el modelo posiblemente tenga un sesgo que

produzca una sobreestimación de la dirección del viento dentro del dominio de estudio.

**Figura 23.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°) (Hora en UTC).

36

**Figura 24.** Ciclo estacional de la dirección del viento observada en estación El Milagro (°) (Hora en UTC).

## 3.1.2. Temperatura

El análisis de la temperatura a nivel superficial (2 metros), presenta los ciclos diarios,

series de tiempo y los ciclos estacionales de los datos observados y los obtenidos por el

modelo WRF.

Los datos de temperatura observados para la estación El Milagro presentan una amplitud

entre los -1,66°C y 34,62°C y una temperatura promedio de 14,72°C ( **Figura 25** ). Las

menores temperaturas del ciclo diario se registran en el horario 08:00 a 10:00 y las

mayores temperaturas se registran en el horario de las 18:00 a 20:00.

Los datos de temperatura modelados WRF para la estación El Milagro presentan una

amplitud entre los 4,48°C y 27,43°C y una temperatura promedio de 14,73°C ( **Figura 26** ).

El ciclo diario de temperatura modelada posee una distribución similar a la observada en

la estación de El Milagro, registrando menores temperaturas en el horario 08:00 a 12:00 y

mayores en el horario 18:00 a 20:00.

**Figura 25.** Ciclo diario de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

37

**Figura 26.** Ciclo diario de la temperatura modelada en la estación El Milagro (°C) Hora (UTC).

En la serie de tiempo de la temperatura observada ( **Figura 27** ), se puede apreciar una

mayor amplitud en los valores que en la serie de tiempo de la temperatura modelada

( **Figura 28** ). La serie de tiempo modelada WRF logra capturar los patrones de

estacionalidad de la temperatura anual, pero la amplitud de los valores de la serie

modelada es más acotada que el de la serie observada.

**Figura 27.** Serie de tiempo de temperatura observada en la estación El Milagro (°C) Hora (UTC).

**Figura 28.** Serie de tiempo de temperatura modelada en la estación El Milagro (°C) Hora (UTC).

38

En los ciclos estacionales presentados ( **Figura 29** y **Figura 30** ) se puede visualizar que, para

horarios mensuales similares, los datos modelados presentan temperaturas menores que

los datos observados, por lo que posiblemente el modelo posee un sesgo que subestima

los valores de temperatura en el dominio de estudio.

**Figura 29.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

**Figura 30.** Ciclo estacional de la temperatura observada en la estación El Milagro (°C) Hora (UTC).

39

## 3.1.3. Humedad Relativa

El análisis de la humedad relativa presenta los ciclos diarios, series de tiempo y ciclos

estacionales de los datos observados y los obtenidos por el modelo WRF.

Los datos observados para la estación El Milagro presentan una amplitud de valores de

humedad relativa de 13,77% y 99,59% y una humedad relativa promedio de 68,48%
( **Figura 31** ). De acuerdo con los datos observados, los máximos horarios de humedad se

generan en horarios de mañana (07:00 a 10:00) y los mínimos se produce en horario de

tarde (18:00 a 19:00).

Los datos modelados WRF para la estación El Milagro presentan una amplitud de valores

de humedad relativa de 31,04% a 100% y una humedad relativa promedio de 80,09%

( **Figura 32** ). Los máximos horarios de humedad se producen en horario de mañana (02:00

a 11:00) y los mínimos durante la tarde (17:00 a 18:00).

**Figura 31.** Ciclo diario de la humedad relativa observada en la estación El Milagro (%) Hora (UTC).

**Figura 32.** Ciclo diario de la humedad relativa modelada en la estación El Milagro (%) Hora (UTC).

40

En la serie de tiempo de la humedad relativa observada ( **Figura 33** ) se puede apreciar una

mayor amplitud de los datos que en la serie de tiempo de la humedad relativa modelada

( **Figura 34** ).

**Figura 33.** Serie de tiempo de la humedad relativa observada en la estación El Milagro (%) Hora (UTC).

**Figura 34.** Serie de tiempo de la humedad relativa modelada en la estación El Milagro (%) Hora (UTC).

En los ciclos estacionales presentados ( **Figura 35** y **Figura 36** ), se puede visualizar que,

para horarios mensuales similares, los datos modelados presentan humedades relativas

mayores que los datos observados, por lo que posiblemente el modelo posee un sesgo

que sobreestima la humedad relativa para el dominio de estudio.

41

**Figura 35.** Ciclo estacional de la humedad relativa observada en la estación El Milagro (%) Horas (UTC).

**Figura 36.** Ciclo estacional de la humedad relativa modelada en la estación El Milagro (%) Horas (UTC).

42

## 3.2 Análisis de la incertidumbre

El análisis de la incertidumbre permite determinar la bondad de la modelación con

respecto a los datos observados. Para el presente informe, se determinaron los

parámetros estadísticos entre los datos observados en las estaciones identificadas dentro

del dominio y los datos modelados WRF.

**Tabla 13.** Criterios estadísticos de aceptación de la predicción proporcionada por un modelo meteorológico.

|Variable Meteorológica|Parámetros Estadísticos|Criterio de Validez|
|---|---|---|
|**Velocidad Viento (10 m)**|RMSE|≤ 2 m/s|
|**Velocidad Viento (10 m)**|BIAS|≤ ±0,5 m/s|
|**Dirección Viento (°)**|Error Absoluto|≤ 30°|
|**Dirección Viento (°)**|BIAS|≤ ±10°|
|**Temperatura Superficial (2 m)**|Error Absoluto|≤ 2K|
|**Temperatura Superficial (2 m)**|BIAS|≤ ±0,5K|

**Fuente** : Emery, C. _et al_ . 2017.

**Tabla 14.** Criterios de tolerancia de diferencia absoluta de variables modeladas.

|Variable Meteorológica|Criterio|
|---|---|
|**Velocidad del viento**|2,57 m/s|
|**Dirección del viento**|20°|
|**Temperatura de rocío**|1°C en superficie.|
|**Temperatura**|1°C en superficie.|

**Fuente** : Yañez-Morroni, G. _et al_ . 2018.

Donde,

,

*+#, = [1]

) −)
(

) 3

+. [/ /01] [(]

(+#

)+#

,

!5565#7869:;6 = [1]

) −)
(

) <

+. [/ /<1] [(]

(+#

)+#

=>,! =

+.

~~?~~ [1]

,

$

)

+. [/ /01] [(]

) 3

) −) )
(

(+#

)+#

Donde:

@: tiempo.

A: lugar de observación.

.: número total de observaciones temporales.

+: número total de lugares de observación.

43

): variable observada/medida.

1: variable predicha por el modelo WRF.

**Tabla 15.** Valores de los parámetros de la predicción proporcionada por el modelo para la Estación El

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
presentados ( **Tabla 13** ) y los valores de los parámetros de la predicción proporcionada por

el modelo ( **Tabla 15** ) para la estación El Milagro, se observa que según BIAS, el modelo

para la velocidad del viento no posee sesgo. Por otra parte, la raíz del error cuadrático

medio (RMSE) indica que el criterio de precisión se encuentra dentro de los criterios de

validez recomendados.

A partir del BIAS, se observa que el modelo para la dirección del viento y el modelo para la

temperatura no poseen sesgo. Sin embargo, de acuerdo con la información otorgada por

el Error absoluto medio, el criterio de precisión no cumple con el criterio de validez

recomendado en ambos casos.

Finalmente, en base al criterio BIAS y al análisis de los datos, se observa que el modelo

para la humedad relativa posee un sesgo que sobreestima el valor de esta variable.

44

# 4. Estimación del Impacto de las Emisiones de Olor

Para la estimación del impacto de las emisiones de olor, se presenta la localización de los

receptores discretos que se encuentran cercanos al sector de postura, sector de crianza y

sector de acopio de GAP y los mapas de las isolíneas de concentración correspondientes,

para permitir el análisis de los posibles impactos que pueden generarse en las cercanías.

Cabe destacar, que en Chile no existe una normativa de calidad o normas de emisión para

olores vigente. Según lo indicado en la “ _Guía para la Predicción y Evaluación de Impactos_

_por Olor_ ”, para evaluar el impacto que puede generar un proyecto, se requiere

“considerar lo establecido en normas de calidad y de emisión vigente”. A falta de una

normativa, se debe priorizar normativas de aquel estado que posea similitud en sus

componentes ambientales, con la situación nacional o local.

Debido a lo anterior, se escogió como referencia el Reino de los Países Bajos cuya

regulación en materia de olores cuenta con normativa vigente para todo el territorio

nacional. En particular, se consideró la Ley de molestias de olor y ganadería de los Países

Bajos ( _Wet geurhinder en veehouderij_, 2013), la cual - en comparación a normativas en la

materia desarrolladas por otros países- hace una distinción específica para el tipo de

actividad económica desarrollada (producción intensiva en ganadería) y el uso de suelo

(dentro o fuera de un área residencial). Por otra parte, también se consideró como criterio

de selección el hecho de que esta normativa ha sido empleada previamente para evaluar

proyectos ingresados al Servicio de Evaluación Ambiental y se ha aprobado su uso, tal

como el proyecto “ _Mejoramiento y Ajustes Operacionales Plantel de Aves Huechún (tercer_

_ingreso) Antecedentes_ ” (2021). La normativa _Wet geurhinder en veehouderij_ (2013)
establece un límite de concentración de 14 OU/m [3] en zona rural, con un percentil 98.

Finalmente, los receptores en el estudio de olores se definen como aquellos que quedan
dentro del área de influencia 1 OU/ m [3] .

## 4.1. Receptores

Las instalaciones de Agricovial están divididas en tres sectores en el escenario base,

correspondientes con sector postura, sector crianza y sector acopio de GAP, y en dos

sectores en el escenario proyectado, pues el acopio y tratamiento del GAP se realizará en

el sector de postura.

Para el presente estudio, se identificaron 56 receptores discretos, con distancias desde el

límite de las instalaciones de 84 a 1.927 m en el escenario base y de 84 a 2.852 m en el

escenario proyectado en el cual ya no existe el sector de acopio de GAP en el sector de Lo

Herrera, al encontrarse el acopio y tratamiento en el sector de postura en el Romeral.

45

**Figura 37.** Localización de receptores discretos del proyecto en el sector Romeral.

**Figura 38.** Localización de receptores discretos del proyecto en el sector Lo Herrera.

**Tabla 16.** Receptores discretos.

|Identificador|Altura<br>m.s.n.m<br>(m)|Distancia al límite<br>de la planta<br>operativa<br>Agricovial -<br>Escenario base (m)|Distancia al límite<br>de la planta<br>operativa<br>Agricovial -<br>Escenario<br>proyectado (m)|Localizaci<br>ón según<br>Sector|Coordenadas UTM|Col7|
|---|---|---|---|---|---|---|
|**Identificador**|**Altura**<br>**m.s.n.m**<br>**(m)**|**Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario base (m)**|**Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario**<br>**proyectado (m)**|**Localizaci**<br>**ón según**<br>**Sector **|**Datum WGS 84 Huso 19**|**Datum WGS 84 Huso 19**|
|**Identificador**|**Altura**<br>**m.s.n.m**<br>**(m)**|**Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario base (m)**|**Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario**<br>**proyectado (m)**|**Localizaci**<br>**ón según**<br>**Sector **|**UTMx (m)**|**UTMy (m)**|
|**Re1**|492|1.151|1.151|Romeral|334.978|6.271.787,1|
|**Re2**|497|810|810|Romeral|335.619,3|6.272.204|

46

|Re3|500|839|839|Romeral|335.707,6|6.272.250,2|
|---|---|---|---|---|---|---|
|**Re4**|486|880|880|Romeral|335.950,8|6.272.217,9|
|**Re5**|501|703|703|Romeral|336.047,3|6.272.344,2|
|**Re6**|501|1.109|1.109|Romeral|335.454,1|6.272.542,3|
|**Re7**|499|833|833|Romeral|335.294,1|6.273.225,8|
|**Re8**|503|1.521|1.521|Romeral|335.340|6.273.413,3|
|**Re9**|501|793|793|Romeral|335.374,4|6.273.622,5|
|**Re10**|490|873|873|Lo Herrera|335.781,1|6.273.544,1|
|**Re11**|494|1.789|2.698|Lo Herrera|334.689,8|6.275.195,7|
|**Re12**|492|1.927|2.852|Lo Herrera|335.284|6.274.935,1|
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

47

|Re44|506|995|995|Lo Herrera|336.967,7|6.273.808,2|
|---|---|---|---|---|---|---|
|**Re45**|504|875|875|Lo Herrera|336.276|6.269.491,9|
|**Re46**|508|428|428|Lo Herrera|336.184|6.269.403,6|
|**Re47**|508|350|350|Lo Herrera|336.567,2|6.269.591,9|
|**Re48**|478|326|326|Romeral|335.780,2|6.269.235,9|
|**Re49**|477|453|453|Romeral|335.569,3|6.269.647,3|
|**Re50**|475|84|84|Romeral|335.577,7|6.269.713,7|
|**Re51**|485|839|839|Romeral|335.699,4|6.269.805,1|
|**Re52**|485|750|750|Romeral|335.712,2|6.269.885,1|
|**Re53**|485|726|726|Romeral|335.754,8|6.268.937,1|
|**Re54**|484|588|588|Romeral|337.253|6.268.577|
|**Re55**|497|569|569|Romeral|337.653,9|6.268.897,7|
|**Re56**|471|1.090|1.090|Romeral|337.727,9|6.269.329,8|

## 4.2. Modelación de Impactos por Emisiones de Olor escenario actual

De acuerdo a la Comisión Europea, el límite de detección de la concentración de olor
percibido por el 50% de la gente, es de 1 OU/m [3] (European Commission, 2017). Como se

puede apreciar de la **Figura 39** y **Figura 40**, 16 de los 56 receptores son capaces de

detectar las emisiones procedentes del sector postura, sector crianza y sector de acopio

de GAP, con distancias de la fuente de emisión de 84 a 1.927 m.

Dada la norma de los países bajos ( _Wet geurhinder en veehouderij, 2013_ ), en el escenario

base en los sectores de Romeral y Lo Herrera, hay dos receptores que superan el límite
definido de 14 OU/m [3], correspondientes al receptor 20 y 21, que poseen una
concentración en inmisión de 14,1 y 34 OU/m [3] respectivamente. Los receptores 20 y 21 se

encuentran localizados en el sector Lo Herrera, cercanos a la zona de acopio de guano

actual.

La isolínea de concentración de 14 OU/m [3] en el sector Romeral se localiza cerca del

perímetro de la planta, y tiene una extensión de 286 m norte, 454 m oeste, 302 m sur y

403 m este desde el centro del sector de postura, con un radio de alcance máximo de 489

m en dirección noroeste.

La isolínea de concentración de 14 OU/m [3] en el sector Lo Herrera se extiende fuera del

perímetro de la zona de acopio de guano de ave de postura, y tiene una extensión de

1.091 m norte, 1.247 m oeste, 685 m sur y 622 m este desde el centro de la zona de

acopio de GAP, y posee un radio de alcance máximo de 1.353 m en dirección nor

noroeste.

De acuerdo a la normativa, el escenario base genera impacto en los receptores

colindantes del proyecto.

48

**Figura 39.** Concentración ambiental de olor percentil 98 en el escenario base (sector Romeral).

**Figura 40.** Concentración ambiental de olor percentil 98 en el escenario base (sector Lo

Herrera).

49

## 4.3. Modelación de Impactos por Emisiones de Olor escenario proyectado

De acuerdo al límite de detección de la concentración de olor, se puede apreciar de la

**Figura 41** y **Figura 42**, que 15 de los 56 receptores son capaces de detectar las emisiones

procedentes del sector postura y sector de crianza, con distancias de la fuente de emisión

de 84 a 982 m, indicando que disminuye la distancia de detección de los receptores en

comparación con el escenario base.

Dada la norma de los países bajos ( _Wet geurhinder en veehouderij_, 2013), en el escenario

proyectado en los sectores de Romeral y Lo Herrera, no hay receptores que superen el
límite definido de 14 OU/m [3] .

La isolínea de concentración de 14 OU/m [3] localizada en el sector Romeral se localiza sobre

el perímetro de la planta y se extiende hacia el norte. Tiene una extensión de 802 m norte,

511 m oeste, 296 m sur y 349 m este desde el centro de la zona de postura, y posee un

radio de alcance máximo de 911 m. El uso de chimeneas para la corriente de salida de los

pabellones de postura 1 y 2 en ambos extremos, 3, 4 y 5 en sección sur y de extractores en

los pabellones 4 y 5 (sección norte), y 6 y 7 en ambos extremos, la secadora de GAP y la
secadora Kohshin genera que la isolínea de concentración de 14 OU/m [3] incremente su

extensión en dirección norte, en comparación con el escenario base.

Por su parte, la isolínea de máxima concentración localizada en el sector Lo Herrera es de
3 OU/m [3], ubicada directamente al norte del sector de crianza de aves de postura. Se

puede apreciar que al remover el sector de acopio del sector Lo Herrera, disminuye la

concentración en los receptores aledaños.

De acuerdo a la normativa, en el escenario proyectado no se genera impacto en los

receptores colindantes del proyecto.

50

**Figura 41.** Concentración ambiental de olor percentil 98 en el escenario proyectado (sector Romeral).

**Figura 42.** Concentración ambiental de olor percentil 98 en el escenario proyectado (sector Lo Herrera).

51

# 5 Conclusiones

Del presente informe, se obtienen las siguientes conclusiones:

 - De acuerdo al análisis de incertidumbre meteorológica realizado entre las variables

modeladas y observadas, la simulación desarrollada entrega un nivel de

incertidumbre aceptable dado el nivel de resolución aplicado según las directrices

del SEIA y en base a los criterios de tolerancia definidos para la velocidad del

viento y la temperatura.

 - Según los valores de los parámetros de la predicción proporcionada por el modelo

para la Estación El Milagro, el modelo para la dirección del viento no cumple con el

criterio de validez ni tolerancia recomendados.

 - De acuerdo a la normativa de referencia utilizada y según las tasas de emisiones

estimadas, en el escenario base en los sectores de Romeral y Lo Herrera, hay dos
receptores que superan el límite definido para zonas rurales de 14 OU/m [3] .

 - En el escenario base el receptor que recibe la mayor concentración de inmisión es

el receptor 21 localizado en el sector Lo Herrera, cercano a la zona de acopio de
guano existente Este recibe una concentración de 34 OU/m [3] . De acuerdo a la

normativa de referencia utilizada, en el escenario base se genera un impacto en los

receptores colindantes del proyecto.

 - En el escenario proyectado, con las modificaciones incorporadas en los sectores de

Romeral y Lo Herrera, no hay receptores que superen el límite definido para zonas
rurales de 14 OU/m [3] . No generando impacto en ningún receptor de acuerdo a la

normativa de referencia utilizada.

52

# A) APENDICE 1 - Reporte de muestreo AQOM Agricovial

## A.1) Sector Romeral

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

## A.2) Sector Lo Herrera

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

106

## A.3) Empresa Avícola Zona Central

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

# B) APENDICE 2 - Informe de APL II Chilehuevos

129

130

131

132

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

# C) APENDICE 3 - Archivos de la Modelación

De acuerdo a lo señalado en la Ley 19.300 sobre Bases Generales del Medio Ambiente en

el artículo 14 bis, y en el Decreto Supremo 40 que Aprueba Reglamento del Sistema de

Evaluación de Impacto Ambiental (2012), en el artículo 21 inciso N°3 y el artículo 29 inciso

N°1, se informa que dada la naturaleza de los archivos digitales de Modelación

Meteorológica WRF y Modelaciones de Dispersión Atmosférica **CALPUFF y CALPOST**, no es

posible agregarlos al expediente electrónico, motivo por el cual dicha información se

encuentra disponible para el público en general en las oficinas de la Dirección Ejecutiva

del Servicio de Evaluación Ambiental (SEA). Los interesados en obtener acceso a dicha

documentación digital, deben comunicarse con la Oficina de Información y Atención

Ciudadana del SEA, ingresando un requerimiento a través del siguiente formulario:

https://www.portaltransparencia.cl/PortalPdT/

https://storage.googleapis.com/wrf-mmif-calpuffpublic/chilehuevos/agricovialv39/agricovialv39.met

219

# D)APENDICE 4 - Bibliografía

Dirección General de Aeronáutica Civil. Dirección Meteorológica de Chile - Servicios
Climáticos. Visitado el 06-04-2021. Disponible en: https://climatologia.meteochile.gob.cl/

Emery, C., Liu, Z., Russell, A. G., Odman, M. T., Yarwood, G., Kumar, N. (2017).

Recommendations on statistics and benchmarks to assess photochemical model

performance. Journal of the Air and Waste Management Association, 67(5), 582-598.
https://doi.org/10.1080/10962247.2016.1265027

GCA Ambiental. 2021. Reporte de muestreo AQOM Agricovial Romeral.

GCA Ambiental. 2021. Reporte de muestreo AQOM Agricovial Lo Herrera.

GCA Ambiental. 2021. Reporte de muestreo AQOM Empresa Avícola Zona Central.

Overheid. 2013. Wet geurhinder en veehouderij. Netherlands.

European Commission. 2017. Best Available Techniques (BAT) reference document for the

intensive rearing of poultry or pigs.

Estudio de fuentes y procesos generadores de olor para el sector productor de huevos de

Chile - Acuerdo de Producción Limpia II. Chilehuevos, 2021.

Servicio de Evaluación de Impacto Ambiental. 2012. Guía para el uso de modelos de

calidad del aire en el SEIA.

Servicio de Evaluación Ambiental. 2017. Guía para la predicción y evaluación de impactos

por olor en el SEIA. Ministerio del Medio Ambiente.

Yáñez-Morroni, G., Gironás, J., Caneo, M., Delgado, R., & Garreaud, R. (2018). Using the

Weather Research and Forecasting (WRF) model for precipitation forecasting in an

Andean region with complex topography. _Atmosphere_, _9_ (8).

220

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Concentración ambiental de olor en receptores discretos (escenario base).**

| Receptores | Concentración en inmisión (OU/m3) | Localización según Sector |
| --- | --- | --- |
| **Re1** | 0,2 | Romeral |
| **Re2** | 0,6 | Romeral |
| **Re3** | 0,6 | Romeral |
| **Re4** | 0,5 | Romeral |
| **Re5** | 0,7 | Romeral |
| **Re6** | 0,4 | Romeral |
| **Re7** | 0,6 | Romeral |
| **Re8** | 0,4 | Romeral |
| **Re9** | 0,6 | Romeral |
| **Re10** | 4,5 | Lo Herrera |
| **Re11** | 2,3 | Lo Herrera |
| **Re12** | 1,9 | Lo Herrera |
| **Re13** | 2,2 | Lo Herrera |
| **Re14** | 2,8 | Lo Herrera |
| **Re15** | 3,3 | Lo Herrera |
| **Re16** | 5 | Lo Herrera |
| **Re17** | 1,8 | Lo Herrera |
| **Re18** | 1,7 | Lo Herrera |
| **Re19** | 4,3 | Lo Herrera |
| **Re20** | 14,1 | Lo Herrera |
| **Re21** | 34 | Lo Herrera |
| **Re22** | 0,4 | Lo Herrera |
| **Re23** | 0,5 | Lo Herrera |
| **Re24** | 0,4 | Lo Herrera |
| **Re25** | 0,4 | Lo Herrera |
| **Re26** | 0,4 | Lo Herrera |
| **Re27** | 0,4 | Lo Herrera |
| **Re28** | 0,5 | Lo Herrera |

**Tabla 2.: ** Concentración ambiental de olor en receptores discretos (escenario proyectado).**

| Receptores | Concentración en inmisión (OU/m3) | Localización según Sector |
| --- | --- | --- |
| **Re1** | 0,4 | Romeral |
| **Re2** | 1,5 | Romeral |
| **Re3** | 1,3 | Romeral |
| **Re4** | 1,1 | Romeral |
| **Re5** | 1,6 | Romeral |
| **Re6** | 0,9 | Romeral |
| **Re7** | 1,3 | Romeral |
| **Re8** | 0,6 | Romera |
| **Re9** | 1,4 | Romeral |
| **Re10** | 0,8 | Lo Herrera |
| **Re11** | 0,3 | Lo Herrera |
| **Re12** | 0,3 | Lo Herrera |
| **Re13** | 0,3 | Lo Herrera |
| **Re14** | 0,3 | Lo Herrera |
| **Re15** | 0,5 | Lo Herrera |
| **Re16** | 0,3 | Lo Herrera |
| **Re17** | 1,7 | Lo Herrera |
| **Re18** | 1,9 | Lo Herrera |
| **Re19** | 0,9 | Lo Herrera |
| **Re20** | 1,3 | Lo Herrera |
| **Re21** | 0,6 | Lo Herrera |
| **Re22** | 0,3 | Lo Herrera |
| **Re23** | 0,3 | Lo Herrera |
| **Re24** | 0,3 | Lo Herrera |
| **Re25** | 0,3 | Lo Herrera |
| **Re26** | 0,3 | Lo Herrera |
| **Re27** | 0,3 | Lo Herrera |
| **Re28** | 0,3 | Lo Herrera |
| **Re29** | 0,4 | Lo Herrera |
| **Re30** | 0,4 | Lo Herrera |
| **Re31** | 0,4 | Lo Herrera |
| **Re32** | 0,4 | Lo Herrera |
| **Re33** | 0,4 | Lo Herrera |
| **Re34** | 0,4 | Lo Herrera |
| **Re35** | 0,3 | Lo Herrera |
| **Re36** | 0,3 | Lo Herrera |

**Tabla 3.: ** Coordenadas generales del perímetro del sector de postura en sector Romeral.**

| Vértice | Coordenadas UTM<br>(Datum WGS 84 Huso 19) | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
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

**Tabla 4.: ** Coordenadas generales del perímetro del sector de crianza en Lo Herrera.**

| Vértice | Coordenadas UTM<br>(Datum WGS 84 Huso 19) | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| **A ** | 336166,2 | 6273729,7 |
| **B ** | 336104,5 | 6273176,1 |
| **C ** | 336668,8 | 6273172,5 |
| **D ** | 336695,6 | 6273627,5 |

**Tabla 5.: ** Coordenadas generales del perímetro del sector de acopio de GAP en Lo Herrera (actual).**

| Vértice | Coordenadas UTM<br>(Datum WGS 84 Huso 19) | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| **A ** | 335503,5 | 6274557,0 |
| **B ** | 335453,1 | 6274100,1 |
| **C ** | 336177,9 | 6273870,7 |
| **D ** | 336234,2 | 6274241,7 |

**Tabla 6.: ** Factor de emisión de fuentes de emisión de olores del escenario base.**

| Fuente | CO (OU/m3) | FE (OU/(m2·s)) | Tipo fuente |
| --- | --- | --- | --- |
| **PPVF (medición en**<br>**extractor)** | 177 | -- | Puntual |
| **PPVN sector jaulas** | 148 | 11,3 | Difusa |
| **PPVN sector cama**<br>**guano** | 653 | 5,4 | Difusa |
| **PCVF (medición en**<br>**extractor)** | 241 | -- | Puntual |
| **Lombrifiltro** | 129 | 1,08 | Difusa |
| **Zona acopio residuos**<br>**orgánicos** | -- | 18,71 | Difusa |
| **Pilas de guano fresco** | 729 | 6,07 | Difusa |
| **Pilas de guano activo** | 1.202 | 10,02 | Difusa |
| **Pilas de guano**<br>**maduro** | 577 | 4,80 | Difusa |

**Tabla 7.: ** Factores de emisión de fuentes identificadas en el escenario proyectado.**

| Fuente | CO (OU/m3) | FE (OU/(m2·s)) | Tipo fuente |
| --- | --- | --- | --- |
| **PPVF (medición en**<br>**extractor)** | 177 | -- | Puntual |
| **PPVN sector jaulas** | 148 | 11,3 | Difusa |
| **PPVN sector cama**<br>**guano** | 653 | 5,4 | Difusa |
| **PCVF (medición en**<br>**extractor)** | 241 | -- | Puntual |
| **Lombrifiltro** | 129 | 1,08 | Difusa |
| **Zona acopio residuos**<br>**orgánicos** | -- | 18,71 | Difusa |
| **Secadora Kohshin** | -- | 5,92 | Difusa |

**Tabla 8.: ** Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario base).**

| Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extracto operación<br>(m) (m2) res | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **PPVF 1 -**<br>**extractor** | 1,7 | 2 | 26,1 | 1,3 | 36 | Extractores -<br>Verano y Primavera: 8<br>horas día 100% y 16<br>horas día 25%.<br>Otoño e Invierno: 6 horas<br>día 100% y 18 horas día<br>25%. |
| **PPVF 2 -**<br>**extractor** | **PPVF 2 -**<br>**extractor** | **PPVF 2 -**<br>**extractor** | **PPVF 2 -**<br>**extractor** | 1,5 | 30 | 30 |
| **PPVF 3 -**<br>**extractor** | **PPVF 3 -**<br>**extractor** | **PPVF 3 -**<br>**extractor** | **PPVF 3 -**<br>**extractor** | 1,3 | 40 | 40 |
| **PPVF 4 -**<br>**extractor** | **PPVF 4 -**<br>**extractor** | **PPVF 4 -**<br>**extractor** | **PPVF 4 -**<br>**extractor** | 1,3 | 36 | 36 |
| **PPVF 5 -**<br>**extractor** | **PPVF 5 -**<br>**extractor** | **PPVF 5 -**<br>**extractor** | **PPVF 5 -**<br>**extractor** | 1,3 | 52 | 52 |
| **PPVF 6 -**<br>**extractor** | **PPVF 6 -**<br>**extractor** | **PPVF 6 -**<br>**extractor** | **PPVF 6 -**<br>**extractor** | 1,4 | 42 | 42 |
| **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | 1,4 | 42 | 42 |
| **PPVN 1 sector**<br>**jaulas** | -- | 2 | -- | 222 | -- | Cortinas -<br>Noviembre a marzo: 50% |

**Tabla 9: ** . Nivel de actividad de las fuentes de emisión de la planta de Agricovial (escenario proyectado).**

| Fuente Velocida Altura Tempera Área N° Condiciones de<br>d (m/s) emisión tura (°C) emisión extractor operación<br>(m) (m2) es | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **PPVF 1 -**<br>**chimeneas** | 0,9 | 9 | 26,1 | 42,5 | 36 | Extractores -<br>Verano y Primavera: 8<br>horas día 100% 16 horas<br>día 25%.<br>Otoño e Invierno: 6<br>horas día 100% y 18<br>horas día 25%.<br> <br> <br> <br> |
| **PPVF 2 -**<br>**chimeneas** | 0,9 | 7,6 | 7,6 | 42,5 | 30 | 30 |
| **PPVF 3 -**<br>**chimenea** | 2,7 | 7,2 | 7,2 | 32,5 | 40 | 40 |
| **PPVF 4 -**<br>**chimenea** | 0,9 | 7,5 | 7,5 | 42,5 | 18 | 18 |
| **PPVF 4 -**<br>**extractor** | 1,7 | 2 | 2 | 1,3 | 18 | 18 |
| **PPVF 5 -**<br>**chimenea** | 1,6 | 8 | 8 | 35 | 26 | 26 |
| **PPVF 5 -**<br>**extractor** | 1,7 | 2 | 2 | 1,3 | 26 | 26 |
| **PPVF 6 -**<br>**extractor** | 1,7 | 2 | 2 | 1,4 | 42 | 42 |
| **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | **PPVF 7 -**<br>**extractor** | 1,4 | 42 | 42 |
| **PPVN 1 sector**<br>**jaulas** | -- | 2 | -- | 222 | -- | Cortinas -<br>Noviembre a marzo: 50%<br>abiertas 24 horas.<br>Abril a Octubre: 30% 12<br>horas y 15% 12 hrs.<br> |
| **PPVN 2 sector**<br>**jaulas** | **PPVN 2 sector**<br>**jaulas** | **PPVN 2 sector**<br>**jaulas** | **PPVN 2 sector**<br>**jaulas** | 222 | -- | -- |
| **PPVN 3 sector**<br>**jaulas** | **PPVN 3 sector**<br>**jaulas** | **PPVN 3 sector**<br>**jaulas** | **PPVN 3 sector**<br>**jaulas** | 177 | -- | -- |
| **PPVN 4 sector**<br>**jaulas** | **PPVN 4 sector**<br>**jaulas** | **PPVN 4 sector**<br>**jaulas** | **PPVN 4 sector**<br>**jaulas** | 228 | -- | -- |
| **PPVN 1 sector**<br>**cama guano** | -- | 0 | -- | 2.368 | -- | Cortinas -<br>Noviembre a marzo:<br>100% abiertas 24 horas.<br>Abril a Octubre: 50% 12<br>horas y 20% 12 hrs.<br> |
| **PPVN 2 sector**<br>**cama guano** | **PPVN 2 sector**<br>**cama guano** | **PPVN 2 sector**<br>**cama guano** | **PPVN 2 sector**<br>**cama guano** | 2.325,1 | -- | -- |
| **PPVN 3 sector**<br>**cama guano** | **PPVN 3 sector**<br>**cama guano** | **PPVN 3 sector**<br>**cama guano** | **PPVN 3 sector**<br>**cama guano** | 1.642,6 | -- | -- |
| **PPVN 4 sector**<br>**cama guano** | **PPVN 4 sector**<br>**cama guano** | **PPVN 4 sector**<br>**cama guano** | **PPVN 4 sector**<br>**cama guano** | 1.757,1 | -- | -- |
| **PCVF 1 -**<br>**extractor** | 1,9 | 2 | 27,1 | 1,4 | 14 | Extractores -<br>operación 100% durante<br>el día y 40% durante<br>noche.<br> |
| **PCVF 2 -**<br>**extractor** | **PCVF 2 -**<br>**extractor** | **PCVF 2 -**<br>**extractor** | **PCVF 2 -**<br>**extractor** | 1,4 | 14 | 14 |
| **PCVF 3 -**<br>**extractor** | **PCVF 3 -**<br>**extractor** | **PCVF 3 -**<br>**extractor** | **PCVF 3 -**<br>**extractor** | 1,4 | 15 | 15 |
| **Lombrifiltro** | -- | 1,5 | -- | 1.156 | -- | Emisión continua. |
| **Zona acopio**<br>**residuos**<br>**orgánicos** | -- | 2 | -- | 75 | -- | Emisión continua. |
| **Secadora**<br>**Kohshin** | -- | 1 | -- | 2.716 | -- | Emisión continua. |
| **Secador Guano**<br>**ave de postura** | 1,61 | 9,4 | 15,1 | 48 | -- | Horas operación -<br>22 h enero, febrero, |

**Tabla 10.: ** Emisiones atmosféricas de olor de la planta de Agricovial (escenario base).**

| Fuente | Tasa de emisión<br>1 (OU/s) | Tasa de emisión<br>2 (OU/s) | Tasa de emisión 3<br>*(OU/s) | Tasa de emisión 4<br>*(OU/s) |
| --- | --- | --- | --- | --- |
| **PPVF 1** | 13.722 | 3.431 | -- | -- |
| **PPVF 2** | 13.837 | 3.459 | -- | -- |
| **PPVF 3** | 15.247 | 3.812 | -- | -- |
| **PPVF 4** | 13.722 | 3.431 | -- | -- |
| **PPVF 5** | 19.821 | 4.955 | -- | -- |
| **PPVF 6** | 17.988 | 4.497 | -- | -- |
| **PPVF 7** | 17.988 | 4.497 | -- | -- |
| **PPVN 1 sector jaulas** | 2.519 | 1.134 | -- | -- |
| **PPVN 2 sector jaulas** | 2.519 | 1.134 | -- | -- |
| **PPVN 3 sector jaulas** | 2.008 | 904 | -- | -- |
| **PPVN 4 sector jaulas** | 2.587 | 1.164 | -- | -- |
| **PPVN 1 sector cama**<br>**guano** | 12.884 | 1.933 | -- | -- |
| **PPVN 2 sector cama**<br>**guano** | 12.651 | 1.933 | -- | -- |
| **PPVN 3 sector cama**<br>**guano** | 8.937 | 1.541 | -- | -- |
| **PPVN 4 sector cama**<br>**guano** | 9.561 | 1.985 | -- | -- |
| **PCVF 1** | 8.783 | 3.513 | -- | -- |
| **PCVF 2** | 8.783 | 3.513 | -- | -- |
| **PCVF 3** | 9.411 | 3.764 | -- | -- |
| **Lombrifiltro** | 1.243 | 1.243 | -- | -- |
| **Zona acopio residuos**<br>**orgánicos** | 369 | 369 | -- | -- |
| **Pilas de guano fresco** | 18.259 | 34.236 | -- | -- |

**Tabla 11.: ** Emisiones atmosféricas de olor de la planta de Agricovial (escenario proyectado).**

| Fuente | Tasa de emisión 1 (OU/s) | Tasa de emisión 2 (OU/s) |
| --- | --- | --- |
| **PPVF 1** | 13.722 | 3.431 |
| **PPVF 2** | 13.837 | 3.459 |
| **PPVF 3** | 15.247 | 3.812 |
| **PPVF 4** | 13.722 | 3.431 |
| **PPVF 5** | 19.821 | 4.955 |
| **PPVF 6** | 17.988 | 4.497 |
| **PPVF 7** | 17.988 | 4.497 |
| **PPVN 1 sector jaulas** | 2.519 | 1.134 |
| **PPVN 2 sector jaulas** | 2.519 | 1.134 |
| **PPVN 3 sector jaulas** | 2.008 | 904 |
| **PPVN 4 sector jaulas** | 2.587 | 1.164 |
| **PPVN 1 sector cama guano** | 12.884 | 1.933 |
| **PPVN 2 sector cama guano** | 12.651 | 1.933 |
| **PPVN 3 sector cama guano** | 8.937 | 1.541 |
| **PPVN 4 sector cama guano** | 9.561 | 1.985 |
| **PCVF 1** | 8.783 | 3.513 |
| **PCVF 2** | 8.783 | 3.513 |
| **PCVF 3** | 9.411 | 3.764 |
| **Lombrifiltro** | 1.243 | 1243 |
| **Zona acopio residuos orgánicos** | 369 | 369 |
| **Secadora Kohshin** | 13.313 | 13.313 |
| **Secador de guano de ave de**<br>**postura** | 83.553 | 83.553 |
| **Total** | **291.447** | **149.079** |

**Tabla 12.: ** Ubicación de estación meteorológica superficial El Milagro.**

| Estación | Altura<br>m.s.n.m<br>(m) | Coordenadas UTM | Col4 |
| --- | --- | --- | --- |
| **Estación** | **Altura**<br>**m.s.n.m**<br>**(m)** | **Datum WGS 84 Huso 19**<br>**H ** | **Datum WGS 84 Huso 19**<br>**H ** |
| **Estación** | **Altura**<br>**m.s.n.m**<br>**(m)** | **Este (m)** | **Norte (m)** |
| **Estación El Milagro** | 460 | 336.580,5 | 6.263.672,3 |

**Tabla 13.: ** Criterios estadísticos de aceptación de la predicción proporcionada por un modelo meteorológico.**

| Variable Meteorológica | Parámetros Estadísticos | Criterio de Validez |
| --- | --- | --- |
| **Velocidad Viento (10 m)** | RMSE | ≤ 2 m/s |
| **Velocidad Viento (10 m)** | BIAS | ≤ ±0,5 m/s |
| **Dirección Viento (°)** | Error Absoluto | ≤ 30° |
| **Dirección Viento (°)** | BIAS | ≤ ±10° |
| **Temperatura Superficial (2 m)** | Error Absoluto | ≤ 2K |
| **Temperatura Superficial (2 m)** | BIAS | ≤ ±0,5K |

**Tabla 14.: ** Criterios de tolerancia de diferencia absoluta de variables modeladas.**

| Variable Meteorológica | Criterio |
| --- | --- |
| **Velocidad del viento** | 2,57 m/s |
| **Dirección del viento** | 20° |
| **Temperatura de rocío** | 1°C en superficie. |
| **Temperatura** | 1°C en superficie. |

**Tabla 15.: ** Valores de los parámetros de la predicción proporcionada por el modelo para la Estación El**

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

**Tabla 16.: ** Receptores discretos.**

| Identificador | Altura<br>m.s.n.m<br>(m) | Distancia al límite<br>de la planta<br>operativa<br>Agricovial -<br>Escenario base (m) | Distancia al límite<br>de la planta<br>operativa<br>Agricovial -<br>Escenario<br>proyectado (m) | Localizaci<br>ón según<br>Sector | Coordenadas UTM | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Identificador** | **Altura**<br>**m.s.n.m**<br>**(m)** | **Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario base (m)** | **Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario**<br>**proyectado (m)** | **Localizaci**<br>**ón según**<br>**Sector ** | **Datum WGS 84 Huso 19** | **Datum WGS 84 Huso 19** |
| **Identificador** | **Altura**<br>**m.s.n.m**<br>**(m)** | **Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario base (m)** | **Distancia al límite**<br>**de**<br>**la**<br>**planta**<br>**operativa**<br>**Agricovial**<br>**- **<br>**Escenario**<br>**proyectado (m)** | **Localizaci**<br>**ón según**<br>**Sector ** | **UTMx (m)** | **UTMy (m)** |
| **Re1** | 492 | 1.151 | 1.151 | Romeral | 334.978 | 6.271.787,1 |
| **Re2** | 497 | 810 | 810 | Romeral | 335.619,3 | 6.272.204 |
